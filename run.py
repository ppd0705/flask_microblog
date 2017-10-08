from app import app, db

# app.run(debug=True)

db.session.remove()
db.drop_all()