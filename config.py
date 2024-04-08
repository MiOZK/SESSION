import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6057690257:AAGq7PEy9FN78VPEVJmTyABQYjKyt1D4okk")

    APP_ID = int(os.environ.get("APP_ID", 21943556))

    API_HASH = os.environ.get("API_HASH", "646d0a2ddb943a9cfc45684652252e64")
