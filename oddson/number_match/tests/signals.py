from datetime import date, timedelta

from django.test import TestCase

from .. import signals
from ..models import Game


class SignalsTestCase(TestCase):
    def game_over(self, rules, **kwargs):
        self.recieved.append(rules)

    def setUp(self):
        self.recieved = []
        signals.game_has_ended.connect(self.game_over)

    def tearDown(self):
        signals.game_has_ended.disconnect(self.game_over)

    def test_game_has_ended_attempts(self):
        """Game over attempts depleated"""
        game = Game.objects.create(
            allowed_attempts=1,
            end_date=date.today() + timedelta(1),
            min_value=1,
            max_value=10
        )
        self.assertTrue(game.is_active)
        self.assertIsNone(game.compleation_date)

        game.attempt_set.create(
            our_number=1,
            user_number=10,
            ip_addr='127.0.0.1'
        )
        self.assertEqual(len(self.recieved), 1)
        self.assertListEqual(self.recieved[0], ['attempts'])
        self.assertFalse(game.is_active)
        self.assertIsNotNone(game.compleation_date)

    def test_game_has_ended_date(self):
        """Game over end date"""
        game = Game.objects.create(
            allowed_attempts=10,
            end_date=date.today(),
            min_value=1,
            max_value=10
        )
        self.assertTrue(game.is_active)
        self.assertIsNone(game.compleation_date)

        game.attempt_set.create(
            our_number=1,
            user_number=10,
            ip_addr='127.0.0.1'
        )
        self.assertEqual(len(self.recieved), 1)
        self.assertListEqual(self.recieved[0], ['date'])
        self.assertFalse(game.is_active)
        self.assertIsNotNone(game.compleation_date)

    def test_game_has_ended_match(self):
        """Game over numbers matched"""
        game = Game.objects.create(
            allowed_attempts=10,
            end_date=date.today() + timedelta(1),
            min_value=1,
            max_value=10
        )
        self.assertTrue(game.is_active)
        self.assertIsNone(game.compleation_date)

        game.attempt_set.create(
            our_number=10,
            user_number=10,
            ip_addr='127.0.0.1'
        )
        self.assertEqual(len(self.recieved), 1)
        self.assertListEqual(self.recieved[0], ['match'])
        self.assertFalse(game.is_active)
        self.assertIsNotNone(game.compleation_date)
