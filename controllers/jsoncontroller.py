import os
import json
import time
from models.jsonmodel import JsonModel
import secrets

project_root = os.path.dirname(os.path.dirname(__file__))


class JsonController:
    def search_json_file_controller(self):
        result = os.path.exists(f'{project_root}/info.json')
        return result

    def create_json_info_file_controller(self, database_name):
        date_time = time.strftime('%d/%m/%Y - %H:%M')
        info_user = "auth_user"
        secret_key = secrets.token_urlsafe(16)
        jsonmodel = JsonModel(database_name, date_time, info_user, secret_key)
        result_json = jsonmodel.create_json_model()

        with open(f'{project_root}/info2.json', 'w') as file_json:
            json.dump([result_json], file_json)

    def get_database_name_in_json_file(self):
        with open(f"{project_root}/info.json", "r") as f:
            info = json.load(f)
            return info[0]['name']
