#  myapp/models.py
from __future__ import unicode_literals
import uuid
from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model

class Pot(Model):
    pot_id          = columns.UUID(primary_key=True, default=uuid.uuid4)
    text            = columns.Text(required=True)
    time_created    = columns.DateTime()
    creator         = columns.Text(required=True)




