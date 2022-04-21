import os
from dotenv import load_dotenv

project_root = os.getcwd()
load_dotenv(os.path.join(project_root, '.env'))


class Config(object):
    SECRET_KEY = os.getenv("KEY")

