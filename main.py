from controllers.maincontroller import MainController
import sentry_sdk

sentry_sdk.init(
    dsn="https://129a67e28dfdeecf7ea35deba6b5504c@o4508902464880640.ingest.de.sentry.io/4508902475169872",
    traces_sample_rate=1.0,
)


def main():
    main_controller = MainController()
    main_controller.run()


if __name__ == "__main__":
    main()
