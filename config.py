# app config
import os

BASEDIR = os.path.abspath(os.path.dirname(__file__))
DATA_BASEDIR = os.path.join(BASEDIR, "../data/")
MAX_RECENT_COMPOSITIONS = 5
ALLOWED_EXTENSIONS = {'wav', 'mp3', 'ogg', 'm4a', 'flac'}
UPLOAD_MAX_SIZE = 100*1024*1024 # 100MiB
COMPRESSION_MODULE_ACTIVE = False
EMAIL_MODULE_ACTIVE = False

# sqllite config example


DB_FILE = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'database.db')
DB_CNX = 'sqlite:///' +  DB_FILE