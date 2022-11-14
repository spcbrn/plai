import json
import requests
import surrealdb

config_filepath = "config/secrets.dev.json"


def run(config_filepath):
    file = open(config_filepath)
    config = json.load(file)
    openai_config =config["openai"]
    surrealdb_config = config['surrealdb']

    # OpenAI Shit
    prompt = "Express a mathematical formula that produces fractals."

    url = openai_config["base_url"] + "/v1/completions"
    headers = {"Authorization": "Bearer " + openai_config["api_key"]}
    data = {
        "model": "text-davinci-002",
        "prompt": prompt,
        "temperature": 0,
        "max_tokens": 600,
    }

    response = requests.post(url=url, json=data, headers=headers)

    print(response.json()["choices"][0]["text"])

    # SurrealDB Shit
    surreal = surrealdb.SurrealDb(surrealdb_config['base_url'], "test", surrealdb_config['user'], surrealdb_config['password'])
    query = """
    INFO FOR DB;
    """
    response = surreal.run_query(query)
    print(response)

run(config_filepath)

