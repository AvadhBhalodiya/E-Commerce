from django.db import models


class BaseModel(models.Model):

    # This model adds the default created and update fields into all the models.

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
