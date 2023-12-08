from . import utils


def combine_yml_files(locale, dir_path):
    """ 
    read all .yml files for a given localization (e.g., trip-response/fr.yml, print-response/fr.yml trip-form/fr.yml)
    and merge thing into a single python object
    """
    from mergedeep import merge
    combined_obj = {}

    fn = utils.find_yaml_files(locale + '.yml', dir_path)
    for f in fn:
        obj = utils.read_yaml(f)
        combined_obj = merge(combined_obj, obj)

    return combined_obj


def yml_to_json(locales=utils.DEFAULT_LOCALES, do_print=True, dir_path='data'):
    """ 
    returns a hash of json objects, where the hash key is the locale name ('fr', 'en', 'es', 'zh', 'vi', etc...)
    in each hash is a deep object with all the localizations under otpUi.<blah>
    """
    ret_val = {}
    for l in locales:
        # build the hash of combined localizations
        ret_val[l] = combine_yml_files(l, dir_path)

    if do_print:
        for l in ret_val.keys():
            print("\n\noutput {}:\n".format(l))                        
            out_json = utils.dump_json(ret_val[l])
            print(out_json)

    return ret_val


