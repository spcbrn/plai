import requests
import json

class SurrealDb:

    def __init__(self, url, db, user, pw):
        self.url = url
        self.db = db
        self.user = user
        self.pw = pw

    def run_query(self, query):
        headers = {
            "Accept": "application/json",
            "NS": self.db,
            "DB": self.db
        }
        response = requests.post(self.url, data=query, headers=headers, auth=(self.user, self.pw))
        return json.loads(response.text)
