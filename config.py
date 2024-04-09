import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6411426002:AAFlE9mccFwBkHhW4hJaO2GmJ4fHcWdU95k")

    APP_ID = int(os.environ.get("APP_ID", 21943556))

    API_HASH = os.environ.get("API_HASH", "646d0a2ddb943a9cfc45684652252e64")
