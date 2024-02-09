import os
import sys
import csv
import inspect
from mako.template import Template
from ott.utils.parse.cmdline.base_cmdline import file_cmdline, misc_options
from ott.utils import file_utils


this_module_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))


def get_csv(feed, comment="#"):
    """ read csv file, skipping any line that begins with a comment (default to '#') """
    csv_data = []
    with open(feed, 'r') as fp:
        for c in csv.DictReader(filter(lambda row: row[0]!=comment, fp)):
            csv_data.append(c)
    return csv_data


def render_template(tmpl, csv_dict, do_print=False):
    def safe_num(num, def_num=888):
        ret_val = def_num
        try:
            ret_val = int(num)
        except:
            ret_val = def_num
        return ret_val

    loader_tmpl = Template(filename=os.path.join(this_module_dir, 'tmpl', tmpl))
    ret_val = loader_tmpl.render(csv=csv_dict, agency=make_feed_agency_id, num=safe_num)
    if do_print:
        print(ret_val)
    else:
        txt = tmpl.replace('mako', 'txt')
        print("output:  " + txt)
        #file_utils.cat(tmpl.replace('mako', 'txt'), input=ret_val)
        with open(txt, "w+") as f:
            f.write(ret_val)
    return ret_val


def make_feed_agency_id(csv_line, def_id="BLANK:BLANK"):
    try:
        # import pdb; pdb.set_trace()
        id = csv_line.get('id').strip()        
        agency_id = csv_line.get('agency_id').strip()
        if agency_id is None or len(agency_id) < 1:
            agency_id = id
        ret_val = "{}:{}".format(id, agency_id)
    except:
        ret_val = def_id
    return ret_val


def curl_feeds(feeds, logos, all=False):
    """ call URLs in this feed """
    for f in feeds:
        id = f.get('id').strip()
        gtfs = f.get('gtfs').strip()
        alerts = f.get('alerts').strip()
        trips = f.get('trips').strip()
        vehicles = f.get('vehicles').strip()
        if id and gtfs:
            if all:
                # curl GTFS urls
                print( "curl {} > {}.gtfs.zip".format(gtfs, id))

            # curl GTFS-RT urls
            if (all or alerts or trips or vehicles):
                if alerts: print( "curl {} > {}.alerts.pbf".format(alerts, id))
                if trips: print( "curl {} > {}.trips.pbf".format(trips, id))
                if vehicles: print( "curl {} > {}.vehicles.pbf".format(vehicles, id))

    # curl LOGO urls
    for l in logos:
        url = l.get('url').strip()
        if url or all:
            ext = url.rsplit('.', 1)[1] if '.' in url else 'png'
            print("curl {} > {}.{}".format(url, make_feed_agency_id(l), ext))


def gtfs_feed_parser():
    """
    feed parser
    reads feeds.csv (and logos.csv) and outputs various .json config outputs
    """
    def_csv = os.path.join(this_module_dir, "feeds.csv")
    logo_csv = os.path.join(this_module_dir, "logos.csv")    
    parser = file_cmdline("poetry run gtfs_feeds", def_file=def_csv, do_parse=False)
    misc_options(parser, "loader", "builder", "router", "ui", "pelias", "curl", "html", "print", "text", "all")
    cmd = parser.parse_args()

    csv_dict = get_csv(cmd.file)
    logo_dict = get_csv(logo_csv)
    output = False
    if cmd.curl:
        curl_feeds(csv_dict, logo_dict, cmd.all)
        output = True
    else:
        if cmd.loader or cmd.all:
            render_template('loader.mako', csv_dict, cmd.print)
            output = True
        if cmd.builder or cmd.all:
            render_template('otp_builder.mako', csv_dict, cmd.print)
            output = True
        if cmd.router or cmd.all:
            render_template('otp_router.mako', csv_dict, cmd.print)
            output = True
        if cmd.ui or cmd.all:
            render_template('otp_ui.mako', logo_dict, cmd.print)
            output = True
        if cmd.pelias or cmd.all:
            render_template('pelias.mako', csv_dict, cmd.print)
            output = True
        if cmd.html or cmd.all:
            render_template('feed_html.mako', csv_dict, cmd.print)
            output = True
        if cmd.text or output is False:
            render_template('text.mako', csv_dict, True)
        if output is False:
            parser.print_help()


def cat_agency_data():
    """
    cat_agency_data: will output agency id(s) and name(s) from a directory of GTFS files
    > poetry run agency_data <dir>
    """
    args = sys.argv[1:]
    gtfs_dir = args[0] if len(args) > 0 else "../cache"
    print()
    for f in file_utils.ls(gtfs_dir, 'gtfs.zip', True):
        a = file_utils.unzip_file(f, 'agency.txt')
        print(f)
        cmt = ""
        #if "RIDECONN" in f:
        #    cmt = " (RC)"
        for c in get_csv(a):
            print('{}{},{}'.format(c.get('agency_name').strip(), cmt, c.get('agency_id')))
        print()



def csv2json():
    """
    csv2json: simple example showing convert to pretty json (array)
    > poetry run csv2json  # default file is ott/convert/csv2json/feeds.csv
    > poetry run csv2json ott/convert/csv2json/logos.csv
    """
    import json
    args = sys.argv[1:]
    file = args[0] if len(args) > 0 else os.path.join(this_module_dir, "feeds.csv")
    csv = get_csv(file)
    print(json.dumps(csv, indent=4))
