import os
import csv
import inspect
from ott.utils import file_utils

this_module_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

loader_feeds = """
feeds: [
    {"url":"http://developer.trimet.org/schedule/gtfs.zip", "name":"TRIMET.gtfs.zip"},
]
"""

def feeds_to_json():
    """ 
    """
    file = open(os.path.join(this_module_dir, 'feeds.csv'), 'r')
    reader = csv.DictReader(file)
    fn = reader.fieldnames
    for row in reader:
        print(row.get('id'))

