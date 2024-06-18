@ECHO OFF
set FLASK_APP=project.app
set FLASK_ENV=development
set DEBUG=true
set JWT_SECRET_KEY="1cb36505e1924ec58aac929c18588f82"

SET DB_NAME=pharmacy
SET DB_URL=localhost
SET DB_USER=root
SET DB_PWD=aziz123
SET DB_PORT=3306

CMD /k "python -B runDebug.py"