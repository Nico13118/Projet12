from controllers.firststartcontroller import FirstStartController
from controllers.jsoncontroller import JsonController
from controllers.databasecontroller import DatabaseController
from controllers.tablecontroller import TableController
from controllers.logincontroller import LoginController
from controllers.usermenucontroller import UserMenuController
from controllers.usercontroller import UserController
from controllers.checkuserinputcontroller import CheckUserInputController
from controllers.menugestioncontroller import MenuGestionController
from controllers.menucommercialcontroller import MenuCommercialController
from controllers.commercialcontroller import CommercialController
from controllers.menusupportcontroller import MenuSupportController
from controllers.gestioncontroller import GestionController
from views.firststartview import FirstStartView
from views.menuview import MenuView
from views.userview import UserView
from views.errormessagesview import ErrorMessagesView


class MainController:
    def __init__(self):
        self.json_c = JsonController()
        self.check_user_input_c = CheckUserInputController()
        self.database_c = DatabaseController(self.json_c)
        self.table_c = TableController(self.json_c)
        self.user_c = UserController(UserView(), ErrorMessagesView(), MenuView(), self.table_c, self.database_c,
                                     self.check_user_input_c)
        self.login_c = LoginController(UserView(), ErrorMessagesView(), self.user_c, self.database_c, self.table_c)
        self.first_start_c = FirstStartController(
            FirstStartView(), UserView(), ErrorMessagesView(), self.user_c, self.json_c, self.database_c,
            self.table_c, self.check_user_input_c)

        self.gestion_c = GestionController(MenuView(), ErrorMessagesView(), UserView(), self.table_c,
                                           self.user_c, self.check_user_input_c, self.database_c)
        self.menu_gestion_c = MenuGestionController(MenuView(), UserView(), ErrorMessagesView(), self.gestion_c,
                                                    self.table_c, self.user_c, self.database_c)

        self.commercial_c = CommercialController(MenuView(), UserView(), ErrorMessagesView(), self.user_c, self.table_c,
                                                 self.check_user_input_c)
        self.menu_commercial_c = MenuCommercialController(MenuView(), UserView(), ErrorMessagesView(),
                                                          self.commercial_c, self.table_c, self.user_c)

        self.menu_support_c = MenuSupportController(MenuView(), UserView(), ErrorMessagesView(), self.user_c,
                                                    self.table_c)

        self.user_menu_c = UserMenuController(self.menu_gestion_c, self.menu_commercial_c, self.menu_support_c,
                                              self.table_c)

    def run(self):
        while True:
            result_info = self.json_c.search_json_file_controller()
            if not result_info:
                self.first_start_c.first_start_controller()
            session = self.login_c.start_authentication_controller()
            self.user_menu_c.redirect_user_to_his_menu(session)
