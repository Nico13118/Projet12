from controllers.startapplicationcontroller import StartApplicationController


class MainController:
    def __init__(self):
        self.start_application_controller = StartApplicationController(self)

    def run(self):
        self.start_application_controller.start_application()

