from config import Config
from Song.database.database import Database

db = Database(Config.MONGODB_URI, Config.SESSION_NAME)
