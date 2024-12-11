from controllers.firststartcontroller import FirstStartController
from controllers.jsoncontroller import JsonController
from controllers.databasecontroller import DatabaseController
from controllers.tablecontroller import TableController
from controllers.logincontroller import LoginController
from controllers.usermenucontroller import UserMenuController
from controllers.usercontroller import UserController
from controllers.checkuserinputcontroller import CheckUserInputController
from views.firststartview import FirstStartView
from views.loginview import LoginView
from views.menuview import MenuView
from views.userview import UserView
from views.errormessagesview import ErrorMessagesView


class MainController:
    def __init__(self):
        self.json_c = JsonController()
        self.check_user_input_c = CheckUserInputController()
        self.database_c = DatabaseController(self.json_c)
        self.table_c = TableController(self.json_c)
        self.user_c = UserController(UserView(), ErrorMessagesView(), self.table_c, self.database_c,
                                     self.check_user_input_c)
        self.login_c = LoginController(LoginView(), FirstStartView(), self.user_c, self.database_c)

        self.user_menu_c = UserMenuController(MenuView(), ErrorMessagesView(), UserView(), self.table_c, self.user_c,
                                              self.check_user_input_c, self.database_c)
        self.first_start_c = FirstStartController(
            FirstStartView(), UserView(), ErrorMessagesView(), self.user_c, self.json_c, self.database_c,
            self.table_c, self.check_user_input_c)
        
    def run(self):
        result_info = self.json_c.search_json_file_controller()
        if not result_info:
            self.first_start_c.first_start_controller()
        else:
            username_password = self.login_c.start_authentication_controller()
            self.user_menu_c.assign_correct_menu_controller(username_password)
