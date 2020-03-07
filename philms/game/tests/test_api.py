from django.test import TestCase
from django.db.utils import IntegrityError

from game.models import *
from game.api import *


class TestApi(TestCase):
    def setUp(self):
        self.game = Game.objects.create()
        self.player_name = 'player'
        self.owner_name = 'owner'

    def test_game_creates_with_name(self):
        self.assertIsNotNone(self.game)

    def test_can_add_player_to_game(self):
        owner = add_player(self.owner_name, self.game, True)
        self.assertEqual(owner.name, self.owner_name)

    def test_needs_name(self):
        with self.assertRaises(IntegrityError):
            add_player('', self.game, True)

    def test_cant_create_duplicate_names(self):
        add_player(self.owner_name, self.game, True)
        with self.assertRaises(IntegrityError):
            add_player(self.owner_name, self.game, True)

    def test_can_freeze_players(self):
        owner = add_player(self.owner_name, self.game, True)
        close_game(owner)
        player = add_player(self.player_name, self.game)
        self.assertIsNone(player)
