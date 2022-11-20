import os
import glob
from pathlib import Path
from mergedeep import merge

import yaml
import json

from . import utils
from . import convert


#
def visit_dict_nodes(d):
    for k,v in d.items():
        yield d,k,v
        if isinstance(v, dict):
            yield from visit_dict_nodes(v)


def rename_nodes(d, lang, sep="-"):
    for dkv in visit_dict_nodes(d):
        v = dkv[2]
        if isinstance(v, str):
            k = dkv[1]
            if len(v) < 1:
                v = k
            dkv[0][k] = lang + sep + v 


def json_to_localizations(locales=utils.DEFAULT_LOCALES, file_name='en.json', dir_path='data', do_print=False):
    for l in locales:
        en = os.path.join(dir_path, file_name)
        f = open(en)
        tora_loc = json.load(f)

        if not file_name.startswith(l):
            rename_nodes(tora_loc, l.upper())

        otpui_loc = convert.combine_yml_files(l, dir_path)
        combo_loc = merge(tora_loc, otpui_loc)

        #import pdb; pdb.set_trace()
        out_json = json.dumps(combo_loc, indent=2, ensure_ascii=False)
        if do_print:
            print(out_json)
        else:
            out_file = l + ".json"
            with open(out_file, 'w', encoding="utf-8") as f:
                f.write(out_json)
            


