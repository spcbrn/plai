import json
import requests

config_filepath = "config/secrets.dev.json"


def run(config_filepath):
    file = open(config_filepath)
    config_values = json.load(file)["openai"]

    prompt = "Express a mathematical formula that produces fractals."

    url = config_values["base_url"] + "/v1/completions"
    headers = {"Authorization": "Bearer " + config_values["api_key"]}
    data = {
        "model": "text-davinci-002",
        "prompt": prompt,
        "temperature": 0,
        "max_tokens": 600,
    }

    response = requests.post(url=url, json=data, headers=headers)

    print(response.json()["choices"][0]["text"])

ß
run(config_filepath)
