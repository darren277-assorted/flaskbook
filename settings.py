""""""

import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

GRAPH_QL_URL = os.environ.get("GRAPH_QL_URL")
GRAPH_QL_API_KEY = os.environ.get("GRAPH_QL_API_KEY")
PORT = int(os.environ.get("PORT"))
