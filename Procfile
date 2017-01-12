web: npm run fix && npm run dist
gunicorn: SERVER_ENV=production gunicorn $GUNICORN_PARAMS --chdir server entry:app
server: npm run fix && npm run gunicorn
webpackdev: npm start
update: pip install -r requirements.txt --upgrade