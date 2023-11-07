from app import app, db

# Create an application context
app.app_context().push()

# Create the database tables
db.create_all()

# You can add other database-related commands here

# Don't forget to remove the application context when you're done
#app.app_context().pop()
