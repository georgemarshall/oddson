from datetime import date

from django.db.models.signals import post_save
from django.dispatch import receiver, Signal
from django.utils import timezone

from .models import Attempt


##
# Signals
##
game_has_ended = Signal(providing_args=['game', 'rules'])
"""
Sent when a game has ended
"""


##
# Recievers
##
@receiver(post_save, sender=Attempt)
def number_match_attempt(sender, instance, created, **kwargs):
    """
    Handle all post attempt functions

    1. Increment the contest attempt count
    2. Check if number was a match
    3. Check contest attempts
    4. Check contest end date
    """
    if created:
        game = instance.game

        # Increment used attempts
        game.used_attempts += 1

        end_rules = {
            'attempts': game.used_attempts >= game.allowed_attempts,
            'date': game.end_date >= date.today(),
            'match': instance.is_match(),
        }

        # Check end conditions
        if any(end_rules.itervalues()):
            game.is_active = False
            game.compleation_date = timezone.now()

            game_has_ended.send(
                sender=game.__class__,
                game=game,
                rules=[k for k, v in end_rules.iteritems() if v]
            )

        game.save()
