import os

project_root = os.getcwd()


class JsonController:
    def __init__(self, controller):
        self.controller = controller

    def search_json_file_controller(self):
        result = os.path.exists(f'{project_root}/info.json')
        return result

