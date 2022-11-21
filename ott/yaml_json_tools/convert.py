import os
import glob
from pathlib import Path
from mergedeep import merge

import yaml
import json

from . import utils


def find_yaml_files(file_name, dir_path):
    file_locations = os.path.join(dir_path, '*', file_name)
    filenames = glob.glob(file_locations)
    return filenames


def combine_yml_files(locale, dir_path):
    combined_obj = {}

    fn = find_yaml_files(locale + '.yml', dir_path)
    for f in fn:
        with open(Path(f), encoding='utf8') as infile:
            obj = yaml.safe_load(infile)
            combined_obj = merge(combined_obj, obj)

    return combined_obj


def yml_to_json(locales=utils.DEFAULT_LOCALES, do_print=True, dir_path='data'):
    ret_val = {}
    for l in locales:
        # hash of combined localizations
        ret_val[l] = combine_yml_files(l, dir_path)

    if do_print:
        for l in ret_val.keys():
            print("\n\noutput {}:\n".format(l))
            out_json = json.dumps(ret_val[l], indent=2, ensure_ascii=False)
            print(out_json)

    return ret_val


