import os
import csv
import inspect
from mako.template import Template
from ott.utils.parse.cmdline.base_cmdline import file_cmdline, misc_options


this_module_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))


def get_csv(feed, comment="#"):
    """ read csv file, skipping any line that begins with a comment (default to '#') """
    csv_data = []
    with open(feed, 'r') as fp:
        for c in csv.DictReader(filter(lambda row: row[0]!=comment, fp)):
            csv_data.append(c)
    return csv_data


def render_template(tmpl, csv_dict, do_print=False):
    loader_tmpl = Template(filename=os.path.join(this_module_dir, 'tmpl', tmpl))
    ret_val = loader_tmpl.render(csv=csv_dict, logo=to_logo_dict)
    if do_print:
        print(ret_val)
    else:
        txt = tmpl.replace('mako', 'txt')
        print("output:  " + txt)
        #file_utils.cat(tmpl.replace('mako', 'txt'), input=ret_val)
        with open(txt, "w+") as f:
            f.write(ret_val)
    return ret_val


def to_logo_dict(csv_line):
    """ 
    pull any optional logo url(s) from the csv line

    they may have an agency_id:: prepended to the URL 
    """
    ret_val = []
    feed_id = csv_line.get('id').strip()
    logo = csv_line.get('logo').strip()
    if feed_id and logo:
        for l in logo.split(";"):
            # has agency_id::url ... parse each out from ::
            if "::" in l:
                agency_id = l.split('::', 1)[0]
                url = l.split('::', 1)[1]
            else:
                agency_id = feed_id
                url = l

            if url.strip():
                # find logo's 3-digit file extension
                ext = None
                if '.' in url:
                    ext = url.rsplit('.', 1)[1]
                if ext is None or len(ext) > 3:
                    #import pdb; pdb.set_trace()
                    ext = 'png'

                ret_val.append({
                    'id': "{}:{}".format(feed_id, agency_id),
                    'url': url,
                    'ext': ext
                });
    return ret_val


def curl_feeds(csv_dict, all=False):
    """ call URLs in this feed """
    for f in csv_dict:
        id = f.get('id').strip()
        gtfs = f.get('gtfs').strip()
        alerts = f.get('alerts').strip()
        trips = f.get('trips').strip()
        vehicles = f.get('vehicles').strip()
        if id and gtfs:
            if all:
                # GTFS
                print( "curl {} > {}.gtfs.zip".format(gtfs, id))

                # LOGO URLS
                logos = to_logo_dict(f)
                for l in logos:
                    print( "curl {} > {}.{}".format(l.get('url'), l.get('id'), l.get('ext')))

            # real time urls
            if (all or alerts or trips or vehicles):
                if alerts: print( "curl {} > {}.alerts.pbf".format(alerts, id))
                if trips: print( "curl {} > {}.trips.pbf".format(trips, id))
                if vehicles: print( "curl {} > {}.vehicles.pbf".format(vehicles, id))



def main():
    """ main """
    def_csv = os.path.join(this_module_dir, "feeds.csv")
    parser = file_cmdline("poetry run gtfs_feeds", def_file=def_csv, do_parse=False)
    misc_options(parser, "loader", "builder", "router", "ui", "pelias", "curl", "html", "print", "text", "all")
    cmd = parser.parse_args()

    csv_dict = get_csv(cmd.file)
    output = False
    if cmd.curl:
        curl_feeds(csv_dict, cmd.all)
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
            render_template('otp_ui.mako', csv_dict, cmd.print)
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
