web: npm run dist && SERVER_ENV=production gunicorn $GUNICORN_PARAMS --chdir server entry:app
server: npm run fix && npm run gunicorn
webpackdev: npm start
update: pip install -r requirements.txt --upgrade
fix: pip install --upgrade jinja2 && pip uninstall pymongo && pip install pymongo