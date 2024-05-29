@ECHO OFF
set FLASK_APP=project.api
set FLASK_ENV=development
set DEBUG=true

SET DB_NAME=pharmacy
SET DB_URL=localhost
SET DB_USER=root
SET DB_PWD=aziz123
SET DB_PORT=3306

CMD /k "python -B runDebug.py"