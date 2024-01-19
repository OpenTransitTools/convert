import os
import csv
import inspect
from mako.template import Template
from ott.utils.parse.cmdline.base_cmdline import file_cmdline, misc_options
# compat_2_to_3.py is f'in stuff up
# from ott.utils import file_utils


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
    ret_val = loader_tmpl.render(csv=csv_dict)
    if do_print:
        print(ret_val)
    else:
        txt = tmpl.replace('mako', 'txt')
        print("output:  " + txt)
        #file_utils.cat(tmpl.replace('mako', 'txt'), input=ret_val)
        with open(txt, "w+") as f:
            f.write(ret_val)
    return ret_val


def capture_feeds(csv_dict):
    """ call URLs in this feed """
    for f in csv_dict:
        print(f)


def main():
    """ main """
    def_csv = os.path.join(this_module_dir, "feeds.csv")
    parser = file_cmdline("poetry run gtfs_feeds", def_file=def_csv, do_parse=False)
    misc_options(parser, "loader", "builder", "router", "pelias", "capture", "html", "print", "text", "all")
    cmd = parser.parse_args()

    csv_dict = get_csv(cmd.file)
    output = False
    if cmd.capture:
        capture_feeds(csv_dict)
        output = True
    if cmd.loader or cmd.all:
        render_template('loader.mako', csv_dict, cmd.print)
        output = True
    if cmd.builder or cmd.all:
        render_template('otp_builder.mako', csv_dict, cmd.print)
        output = True
    if cmd.router or cmd.all:
        render_template('otp_router.mako', csv_dict, cmd.print)
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
