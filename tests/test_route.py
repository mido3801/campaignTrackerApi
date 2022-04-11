import pytest
from flask import Flask
from api.app.app import register_route
from api.routes.route import Route
import mongoengine as me
from flask_mongoengine import MongoEngine


class MockObject(me.Document):
    field = me.StringField()


@pytest.fixture()
def app():
    app = Flask(__name__)
    MongoEngine(app)
    app.config.update({
        "TESTING": True,
        "MONGODB_SETTINGS": {'host': 'mongomock://localhost',
                             'db': 'mongoenginetest',
                             'port': 27017,
                             'username': 'useradmin',
                             'password': 'password'}
    })
    register_route(app,
                   Route(MockObject),
                   MockObject,
                   'mock_api',
                   '/backend/mock/')
    yield app


@pytest.fixture()
def client(app):
    return app.test_client()


def test_empty_items(client):
    response = client.get('/backend/mock/')
    print(response.data)
    assert response.data == b'[]'


def test_get_item(client):
    pass
