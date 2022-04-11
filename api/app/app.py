"""Module with app factory function"""

import os
from flask import Flask
from flask_cors import CORS
from flasgger import Swagger

from ..db.db import db, Character, User, Quest, Event, Item, Location
from ..app.config import env_config
from ..routes.route import Route

route_configs = [(Route(Character), Character,
                  'character_api', '/api/characters/'),
                 (Route(Location), Location,
                  'location_api', '/api/locations/'),
                 (Route(Item), Item,
                  'item_api', '/api/items/'),
                 (Route(Event), Event,
                  'event_api', '/api/events/'),
                 (Route(Quest), Quest,
                  'quest_api', '/api/quests/'),
                 (Route(User), User,
                  'user_api', '/api/users/')]


def create_app(config_name):
    """
    Application factory pattern
    :return: flask app object
    """
    flask_app = Flask(__name__)
    flask_app.config.from_object(env_config[config_name])

    # Initialize app extensions
    db.init_app(flask_app)
    CORS(flask_app)
    Swagger(flask_app)

    for config in route_configs:
        register_route(flask_app, *config)

    return flask_app


def register_route(app_object, view, model, endpoint, url):
    """Register a MethodView route object with a flask app
       :param flask.Flask app_object: Flask application object
       :param flask.views.MethodView: MethodView object
       :param MongoEngine.Document model: MongoEngine Document model
       :param str endpoint: backend endpoint name
       :param str url: resource url
    """
    view_func = view.as_view(endpoint, model=model)
    app_object.add_url_rule(url, view_func=view_func, methods=['GET', 'PUT', 'DELETE'])
    app_object.add_url_rule(url, view_func=view_func, methods=['POST'])


if __name__ == '__main__':
    app = create_app(os.getenv("FLASK_ENV"))
