from flask import Flask
from database import engine, Base
from modules.task.task_routes import task_routes
from modules.summary.summary_routes import summary_routes

app = Flask(__name__)

Base.metadata.create_all(bind=engine)

app.register_blueprint(task_routes)
app.register_blueprint(summary_routes)

if __name__ == '__main__':
    app.run(debug=True)