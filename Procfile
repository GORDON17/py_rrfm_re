web: npm run fix && npm run dist && gunicorn $GUNICORN_PARAMS --chdir server entry:app --timeout 99999999
server: npm run fix && npm run gunicorn
webpackdev: npm start
update: pip install -r requirements.txt --upgrade