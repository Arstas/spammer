import sentry_sdk

from b0mb3r.utils import retrieve_installed_version

sentry_sdk.init(
    "http://edc49da0ab5f47ee83fda49de28c4a17@b0mb3r.net.ru:9000/2",
    release=retrieve_installed_version(),
)


def sentry_handler(message):
    sentry_sdk.capture_exception(message.record["exception"])
