"""Mongo Document models"""
from random import randint
import mongoengine as me
from flask_mongoengine import MongoEngine
from werkzeug.security import generate_password_hash, check_password_hash

db = MongoEngine()


def stat_roll():
    """
    Roll for character stat
    4d6, take highest 3
    :return int: sum of highest 3 rolls
    """
    rolls = [randint(1, 7) for x in range(4)]
    rolls.sort()
    return sum(rolls[1:])


class Item(me.Document):
    """Model for items"""
    name = me.StringField(required=True)
    weight = me.FloatField()
    description = me.StringField()


class Location(me.Document):
    """Model for locations of interest"""
    name = me.StringField()
    description = me.StringField()


class Character(db.Document):
    """Model for characters"""
    name = me.StringField(required=True)
    strength = me.IntField(required=True, default=stat_roll())
    constitution = me.IntField(required=True, default=stat_roll())
    wisdom = me.IntField(required=True, default=stat_roll())
    dexterity = me.IntField(required=True, default=stat_roll())
    intelligence = me.IntField(required=True, default=stat_roll())
    charisma = me.IntField(required=True, default=stat_roll())
    hp = me.IntField(required=True, default=stat_roll())
    inventory = me.ListField(me.ReferenceField(Item,
                                               reverse_delete_rule=me.PULL))


class Event(db.Document):
    """Model for narrative event"""
    characters = me.ListField(me.ReferenceField(Character,
                                                reverse_delete_rule=me.PULL))
    location = me.ReferenceField(Location, reverse_delete_rule=me.PULL)
    items = me.ReferenceField(Item, reverse_delete_rule=me.PULL)
    description = me.StringField()


class Quest(db.Document):
    """Model for quests"""
    character = me.ReferenceField(Character, reverse_delete_rule=me.PULL)
    goal = me.StringField()
    failure_conditions = me.StringField()


class User(db.Document):
    """Model for users"""
    username = me.StringField()
    password = me.StringField()

    def set_password(self, password):
        """Set password by hashing"""
        self.password = generate_password_hash(password)

    def check_password(self, password):
        """Check if provided password matches hashed password"""
        return check_password_hash(self.password, password)
