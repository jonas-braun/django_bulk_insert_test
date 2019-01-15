from django.db import models

class Item(models.Model):
    attribute = models.IntegerField()

    def __str__(self):
        return f'({self.id}) {self.attribute}'
