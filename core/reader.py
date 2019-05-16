import yaml


def read_yaml_file(path):
    try:
        f = open(path, 'r')
        try:
            return yaml.load(f)
        finally:
            f.close()
    except (IOError,EOFError) as e:
        raise Exception("Unable to load file")