import os

basedir = os.path.abspath(os.path.dirname(__file__))


SQLALCHEMY_DATABASE_URI = "postgresql://dan:danpassword@localhost/techlang"
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
CSRF_ENABLED = True
SECRET_KEY = r'\xd6\x99\x138v\x95.\xf8C*\xceZd\x87\xe8q\x14\x1c\x8a6\xcb?\x87Q'
#UPLOAD_FOLDER = os.path.join(basedir, 'images')
#DOWNLOAD_FOLDER = os.path.join(basedir, 'projects')
ALLOWED_EXTENSIONS = set(['txt','png', 'jpg', 'jpeg'])
#DATA_FOLDER = os.path.join(basedir, 'projects')
#UPLOAD_FOLDER = os.path.join(basedir, 'static/images')