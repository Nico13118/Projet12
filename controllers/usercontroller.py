from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
from urllib.parse import quote


class UserController:
    def __init__(self, controller):
        self.controller = controller

    def test_username_password_controller(self, username, password1):
        password2 = quote(password1)
        try:
            engine = create_engine(f'mysql+pymysql://{username}:{password2}@localhost')
            with engine.connect() as connection:
                return True
        except OperationalError:
            return False
