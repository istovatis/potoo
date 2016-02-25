import datetime

from app import models
from app.models import Pot


class PotServices(models.Pot):
    @staticmethod
    def save(text, creator):
        pot = Pot()
        pot.time_created = datetime.datetime.now()
        pot.text = text
        pot.creator = creator
        pot.save()

    @staticmethod
    def get_pots(limit=None):
        if limit:
            pots = Pot.objects[:limit]
        else:
            pots = Pot.objects
        return sorted(pots, key=lambda n: n.time_created, reverse=True)
