import os
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

ID = os.environ.get("ID")
PASS = os.environ.get("PASS")
CHROME_PATH = os.environ.get("CHROME_PATH")
