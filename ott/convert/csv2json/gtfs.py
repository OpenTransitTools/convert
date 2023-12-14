import os
import csv
import inspect
from mako.template import Template

from ott.utils import file_utils

this_module_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

def get_csv(feed, comment="#"):
    """
    read csv file, skipping any line that begins with a comment (default to '#')
    note: fp file remains open, so that returned dict reader is valid later (closed fp causes problems)
    """
    fp = open(feed, 'r')
    csv_dict = csv.DictReader(filter(lambda row: row[0]!=comment, fp))
    return csv_dict


def feeds_to_json():
    """ 
    """
    csv_dict = get_csv(os.path.join(this_module_dir, 'feeds.csv'))
    tmpl = Template(filename=os.path.join(this_module_dir, 'tmpl', 'loader.mako'))
    print(tmpl.render(csv=csv_dict))
