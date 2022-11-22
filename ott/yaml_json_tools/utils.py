import os
import glob
import json
import yaml


DEFAULT_LOCALES=['en', 'es', 'fr', 'ko', 'vi', 'zh']


def find_yaml_files(file_name, dir_path):
    file_locations = os.path.join(dir_path, '*', file_name)
    filenames = glob.glob(file_locations)
    return filenames


def read_yaml(in_file):
    with open(in_file, 'r', encoding='utf8') as infile:
        return yaml.safe_load(infile)


def read_json(in_file):
    with open(in_file, 'r', encoding="utf-8") as f:
        return json.load(f)


def write_json(out_file, json_data):
    with open(out_file, 'w', newline='\n', encoding="utf-8") as f:
        f.write(json_data)


def obj_to_json(obj):
    return json.dumps(obj, indent=2, ensure_ascii=False)    