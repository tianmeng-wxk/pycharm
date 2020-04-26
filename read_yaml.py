import yaml, os
current_path = os.path.abspath(os.path.dirname(__file__))
config_path = current_path+"\config\data.yaml"
def read_yaml():
    with open(config_path, 'r', encoding='utf-8') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        print(data)
        return data
read_yaml()