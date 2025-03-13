class JsonModel:
    def __init__(self, database_name, created_date, info_user, secret_key):
        self.database_name = database_name
        self.created_date = created_date
        self.info_user = info_user
        self.secret_key = secret_key

    def create_json_model(self):
        info_database = {
            "name": self.database_name,
            "created_date": self.created_date,
            "info_user": self.info_user,
            "secret_key": self.secret_key
        }
        return info_database


