print("Hello, welcome to ...")
def load_config():
    import yaml
    with open('config.yaml') as f:
        return yaml.safe_load(f)
