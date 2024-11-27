class JsonModel:
    def __init__(self, database_name, created_date):
        self.database_name = database_name
        self.created_date = created_date

    def create_json_model(self):
        info_database = {
            "name": self.database_name,
            "created_date": self.created_date
        }
        return info_database


