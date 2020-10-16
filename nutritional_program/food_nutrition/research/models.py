from django.db.models import Model, CharField, JSONField

# Create your models here.
class Entity(Model):
    entity = CharField(max_length=100)
    abbreviation = CharField(max_length=100)
    # parent_entity

    # financial_statements:
