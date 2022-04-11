import os

from api.app.app import create_app

app = create_app(os.getenv("FLASK_ENV"))