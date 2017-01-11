from app import app, db

print db.collection_names()

if __name__ == '__main__':
    app.run()
