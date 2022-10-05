import yaml


def get_config(conf_path: str):
    # 基金分析
    with open(conf_path) as f:
        conf = yaml.load(f)
    return conf