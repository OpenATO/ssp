# utils.py
import yaml

def load_config(file_path="config.yml"):
    """Loads the YAML configuration."""
    with open(file_path, 'r') as f:
        return yaml.safe_load(f)

def save_results(results, file_path="results.yml"):
    """Saves the test results to a YAML file."""
    with open(file_path, 'w') as f:
        yaml.dump(results, f, default_flow_style=False)
