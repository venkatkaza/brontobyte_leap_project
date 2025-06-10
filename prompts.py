import yaml
def load_prompt(key):
    with open("prompts.yaml", "r") as f:
        prompts = yaml.safe_load(f)
    return prompts.get(key," ")
