from datetime import date

from django.test import TestCase

from ..models import Game


class ModelsTestCase(TestCase):
    def test_generate_number(self):
        game = Game.objects.create(
            allowed_attempts=10,
            end_date=date.today(),
            min_value=1,
            max_value=10
        )
        self.assertIsInstance(game.generate_number(), int)
