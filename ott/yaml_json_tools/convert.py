import os
import glob
from pathlib import Path
from mergedeep import merge

import yaml
import json

from . import utils


def find_yaml_files(file_name, dir_path='data'):
    file_locations = os.path.join(dir_path, '*', file_name)
    filenames = glob.glob(file_locations)
    return filenames


def yml_file_to_object(file_path):
    obj = yaml.safe_load(Path(file_path).read_text())


def yml_to_json(locales=utils.DEFAULT_LOCALES, do_print=True):
    ret_val = {}
    for l in locales:
        combined_obj = {}

        fn = find_yaml_files(l + '.yml')
        for f in fn:
            file_path = f
            obj = yaml.safe_load(Path(file_path).read_text())            
            combined_obj = merge(combined_obj, obj)

        # hash of combined localizations
        ret_val[l] = combined_obj

    if do_print:
        for l in ret_val.keys():
            print("\n\noutput {}:\n".format(l))
            out_json = json.dumps(ret_val[l], indent=2, ensure_ascii=False)
            print(out_json)

    return ret_val


