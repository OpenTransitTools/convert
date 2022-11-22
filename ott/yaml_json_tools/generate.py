import os

from . import utils
from . import convert


def visit_dict_nodes(d):
    """ generator to recursively traverse an object tree """
    for k,v in d.items():
        yield d,k,v
        if isinstance(v, dict):
            yield from visit_dict_nodes(v)


def prepend_node_values(d, lang, sep="-"):
    """ visit each node in object, and prepend <lang><sep> to each string-node's value """
    for dkv in visit_dict_nodes(d):
        v = dkv[2]
        if isinstance(v, str):
            k = dkv[1]
            if len(v) < 1:  # no value, then use key as the value
                v = k
            if len(v) > 1:  # value needs to be longer than 1 char to prepend with <lang>-<value>
                dkv[0][k] = lang + sep + v


def json_to_localizations(locales=utils.DEFAULT_LOCALES, file_name='en.json', dir_path='data', do_print=False):
    """
    will read in data/en.json (dir_path/file_name), which is a template containing the string table for all the 
    other target langs that have yet to be translated (e.g., this is the situation with TORA in Dec 2022).

    will then build out locale .json files with "key": "FR-<english value>" or "key": "ZH-<english value>", etc...
    for each language.

    further, it will add the otpUi. combined translations (which are localized) into each of these files, so we
    end up with a partially translated .json locale file for TORA

    NOTE: if file_name == None, then only the OTP-UI localizations will end up in the output file
    """
    for l in locales:
        # read in the OTP-UI locale files for the given language 
        combo_loc = convert.combine_yml_files(l, dir_path)

        # (optionally) read in a TORA lang file
        if file_name:
            from mergedeep import merge

            en = os.path.join(dir_path, file_name)
            tora_loc = utils.read_json(en)

            if not file_name.startswith(l):
                prepend_node_values(tora_loc, l.upper())

            combo_loc = merge(tora_loc, combo_loc)

        #import pdb; pdb.set_trace()
        out_json = utils.obj_to_json(combo_loc)
        if do_print:
            print(out_json)
        else:
            out_file = l + ".json"
            utils.write_json(out_file, out_json)
            


