# .envをOSの環境変数に登録
import os
from os.path import join, dirname
from dotenv import load_dotenv
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

a_game_name = os.getenv("GAME_LIST")
# for now it is only a game