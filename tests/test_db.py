import unittest
from mongoengine import connect, disconnect
from werkzeug.security import generate_password_hash
from api.db.db import Item, Character, Quest, Event, Location, User


class TestItem(unittest.TestCase):
    """Tests for Item Document"""

    @classmethod
    def setUpClass(cls) -> None:
        connect('mongoenginetest', host='mongomock://localhost')

    @classmethod
    def tearDownClass(cls) -> None:
        disconnect()

    def test_item(self):
        item = Item(name='test_item',
                    weight=4.20,
                    description='this is a test item')
        item.save()

        fresh_item = Item.objects().first()
        assert fresh_item.name == 'test_item'
        assert fresh_item.weight == 4.20
        assert fresh_item.description == 'this is a test item'


class TestLocation(unittest.TestCase):
    """Tests for Location Document"""
    @classmethod
    def setUpClass(cls) -> None:
        connect('mongoenginetest', host='mongomock://localhost')

    @classmethod
    def tearDownClass(cls) -> None:
        disconnect()

    def test_location(self):
        location = Location(name='test_location',
                            description='this is a test location')
        location.save()

        fresh_location = Location.objects().first()
        assert fresh_location.name == 'test_location'
        assert fresh_location.description == 'this is a test location'


class TestCharacter(unittest.TestCase):
    """Tests for Character Document"""
    @classmethod
    def setUpClass(cls) -> None:
        connect('mongoenginetest', host='mongomock://localhost')

    @classmethod
    def tearDownClass(cls) -> None:
        disconnect()

    def test_character(self):
        test_item = Item(name='test_item')
        test_item.save()
        char = Character(name='test_char',
                         strength=10,
                         constitution=10,
                         wisdom=10,
                         dexterity=10,
                         intelligence=10,
                         charisma=10,
                         hp=10,
                         inventory=[test_item])
        char.save()

        fresh_char = Character.objects().first()
        assert fresh_char.name == 'test_char'
        assert fresh_char.strength == 10
        assert fresh_char.constitution == 10
        assert fresh_char.wisdom == 10
        assert fresh_char.dexterity == 10
        assert fresh_char.intelligence == 10
        assert fresh_char.charisma == 10
        assert fresh_char.hp == 10
        assert fresh_char.inventory == [test_item]


class TestEvent(unittest.TestCase):
    """Tests for Event Document"""
    @classmethod
    def setUpClass(cls) -> None:
        connect('mongoenginetest', host='mongomock://localhost')

    @classmethod
    def tearDownClass(cls) -> None:
        disconnect()

    def test_event(self):
        char = Character(name='test_char',
                         strength=10,
                         constitution=10,
                         wisdom=10,
                         dexterity=10,
                         intelligence=10,
                         charisma=10,
                         hp=10)
        char.save()
        location = Location(name='test_location')
        location.save()
        item = Item(name='test_item',
                    weight=4.20,
                    description='this is a test item')
        item.save()
        event = Event(characters=[char],
                      location=location,
                      items=item,
                      description='this is a test event')
        event.save()

        fresh_event = Event.objects().first()
        assert fresh_event.characters == [char]
        assert fresh_event.location == location
        assert fresh_event.items == item
        assert fresh_event.description == 'this is a test event'


class TestQuest(unittest.TestCase):
    """Tests for Quest Document"""
    @classmethod
    def setUpClass(cls) -> None:
        connect('mongoenginetest', host='mongomock://localhost')

    @classmethod
    def tearDownClass(cls) -> None:
        disconnect()

    def test_quest(self):
        char = Character(name='test_char',
                         strength=10,
                         constitution=10,
                         wisdom=10,
                         dexterity=10,
                         intelligence=10,
                         charisma=10,
                         hp=10)
        char.save()
        quest = Quest(character=char,
                      goal='test goal',
                      failure_conditions='test condition')
        quest.save()

        fresh_quest = Quest.objects().first()
        assert fresh_quest.character == char
        assert fresh_quest.goal == 'test goal'
        assert fresh_quest.failure_conditions == 'test condition'


class TestUser(unittest.TestCase):
    """Tests for Item Document"""

    @classmethod
    def setUpClass(cls) -> None:
        connect('mongoenginetest', host='mongomock://localhost')

    @classmethod
    def tearDownClass(cls) -> None:
        disconnect()

    def test_user(self):
        user = User(username='user',
                    password=generate_password_hash('password'))
        user.save()

        fresh_user = User.objects().first()
        assert fresh_user.username == 'user'
        assert fresh_user.check_password('password')
