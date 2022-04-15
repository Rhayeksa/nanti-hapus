from django.db import models

from hero.models import Hero

# Create your models here.


class Orang(models.Model):
    username = models.CharField(primary_key=True, max_length=50)
    email = models.EmailField(max_length=254)
    nama = models.CharField(max_length=255)
    penjelasan = models.TextField()
    id_hero = models.ForeignKey(
        Hero,
        on_delete=models.prefetch_related_objects,
        db_column='id_hero',
    )

    class Meta:
        db_table = 'orang'

    def __str__(self):
        return "{}".format(self.id)
