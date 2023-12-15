import os
import csv
import inspect
from mako.template import Template

from ott.utils import file_utils

this_module_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

def get_csv(feed, comment="#"):
    """ read csv file, skipping any line that begins with a comment (default to '#') """
    csv_data = []
    with open(feed, 'r') as fp:
        for c in csv.DictReader(filter(lambda row: row[0]!=comment, fp)):
            csv_data.append(c)
    return csv_data


def feeds_to_json():
    """ """
    csv_dict = get_csv(os.path.join(this_module_dir, 'feeds.csv'))
    loader_tmpl = Template(filename=os.path.join(this_module_dir, 'tmpl', 'loader.mako'))
    print(loader_tmpl.render(csv=csv_dict))

    otp_router_tmpl = Template(filename=os.path.join(this_module_dir, 'tmpl', 'otp_router.mako'))
    print(otp_router_tmpl.render(csv=csv_dict))
