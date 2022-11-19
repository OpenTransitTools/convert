import os
import glob
from pathlib import Path
from mergedeep import merge

import yaml
import json

from . import utils


def json_to_localizations(locales=utils.DEFAULT_LOCALES, file_name='en.json', dir_path='data'):
    en = os.path.join(dir_path, file_name)
    f = open(en)
    j = json.load(f)
    print(j)

    for l in locales:
        f = l + '.json'
        if f != file_name:
            print(f)
