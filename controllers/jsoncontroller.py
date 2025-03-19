import os
import json
import jwt
import time
from datetime import datetime, timedelta
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

        with open(f'{project_root}/info.json', 'w') as file_json:
            json.dump([result_json], file_json)

    def get_database_name_in_json_file(self):
        with open(f"{project_root}/info.json", "r") as f:
            info = json.load(f)
            return info[0]['name']

    def get_info_key_in_json_file(self):
        with open(f"{project_root}/info.json", "r") as f:
            info = json.load(f)
            return info[0]['secret_key']

    def create_jwt(self, collab_username, collab_password, collab_id, role_id):
        """
        Fonction qui permet de créer un token.
        :param collab_username
        :param collab_password
        :param collab_id
        :param role_id
        :return: token
        """
        secret_key = self.get_info_key_in_json_file()
        now = datetime.now()
        expiration_time = (now + timedelta(minutes=15)).timestamp()
        payload = {
            'collab_username': collab_username,
            'collab_password': collab_password,
            'collab_id': str(collab_id),
            'role_id': str(role_id),
            'exp': expiration_time
        }
        token = jwt.encode(payload, secret_key, algorithm="HS256")
        return token

    def verify_and_refresh_token(self, token):
        """
        Fonction qui permet de vérifier et d'actualiser le token.
        :param token:
        :return: new_token
        """
        secret_key = self.get_info_key_in_json_file()
        try:
            payload = jwt.decode(token, secret_key, algorithms=["HS256"])
            new_token = self.create_jwt(
                payload['collab_username'],
                payload['collab_password'],
                payload['collab_id'],
                payload['role_id']
            )
            return new_token  # On renvoie le token mis à jour
        except jwt.ExpiredSignatureError:
            print("Token expiré ! Veuillez vous reconnecter.")
        except jwt.InvalidTokenError:
            print("Token invalide !")


