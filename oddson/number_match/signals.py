from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver


def number_match_attempt(sender, instance, created, **kwargs):
    """
    Handle all post attempt functions

    1. Increment the contest attempt count
    2. Check if number was a match
    3. Check contest end criteria
    """
    if created:
        pass
