fix: npm run fix
dist: npm run dist
web: gunicorn $GUNICORN_PARAMS --chdir server entry:app --timeout 99999999
clock: python server/clock.py
worker: python server/worker.py
webpackdev: npm start
update: pip install -r requirements.txt --upgrade