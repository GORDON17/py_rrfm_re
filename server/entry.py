from app import app
from services.mongodb import connect_db

connect_db()

if __name__ == '__main__':
    app.run()
