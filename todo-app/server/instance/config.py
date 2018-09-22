import os

FLASK_APP="run.py"
DEBUG = True
CSRF_ENABLED = True
SECRET="!Mm*[eDih$c8i+/?DBA3tK*%U&zHd$!Xq|+F2j;<qQw85yM-&9%'?_3C8&x<$M#"
SQLALCHEMY_DATABASE_URI="sqlite:///" + os.path.abspath('database.db')