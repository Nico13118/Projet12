class UserMenuController:
    def __init__(self, menugestioncontroller, menucommercialcontroller, menusupprtcontroller, tablecontroller):
        self.session = None
        self.menu_gestion_c = menugestioncontroller
        self.menu_commercial_c = menucommercialcontroller
        self.menu_support_c = menusupprtcontroller
        self.table_c = tablecontroller
        
    def redirect_user_to_his_menu(self, session):
        self.session = session
        if self.session.role_id == 1:
            self.menu_commercial_c.get_menu_commercial_controller(session)
        elif self.session.role_id == 2:
            self.menu_gestion_c.get_menu_gestion_controller(session)
        elif self.session.role_id == 3:
            self.menu_support_c.get_menu_support_controller(session)
