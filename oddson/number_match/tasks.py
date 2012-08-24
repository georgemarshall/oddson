from datetime import date

from celery.task import task
from django.utils import timezone

from . import signals
from .models import Game


@task(name='number_match.tasks.end_expired_games')
def end_expired_games():
    """
    Find all active games that have passed their expiration date
    """
    # Find expired games
    games = Game.objects.filter(
        is_active=True,
        end_date__lte=date.today(),
    )

    # Deactivate the games
    games.update(
        is_active=False,
        compleation_date=timezone.now(),
    )

    # Send game end signal
    for game in games.iterator():
        signals.game_has_ended.send(
            sender=game.__class__,
            game=game,
            rules=['date']
        )
