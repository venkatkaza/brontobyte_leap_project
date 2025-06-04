import yaml
def load_prompt(key):
    with open("config/prompts.yaml", "r") as f:
        prompts = yaml.safe_load(f)
    return prompts[key]