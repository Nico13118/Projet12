class UserMenuController:
    def __init__(self, menugestioncontroller, menucommercialcontroller, menusupprtcontroller, tablecontroller):
        self.menu_gestion_c = menugestioncontroller
        self.menu_commercial_c = menucommercialcontroller
        self.menu_support_c = menusupprtcontroller
        self.table_c = tablecontroller

    def redirect_user_to_his_menu(self, username_password):
        username = username_password[0]
        password = username_password[1]
        info_user = self.table_c.get_information_for_all_collaborators_controller(username, password)
        for row in info_user:
            if row.role_id == 1:
                self.menu_commercial_c.get_menu_commercial_controller(username, password)
            if row.role_id == 2:
                self.menu_gestion_c.get_menu_gestion_controller(username, password)
            if row.role_id == 3:
                self.menu_support_c.get_menu_support_controller(username, password)
