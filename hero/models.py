from django.db import models

# Create your models here.


class Hero(models.Model):
    role_value = [
        ('Kesatria', 'Kesatria'),
        ('Pemanah', 'Pemanah'),
        ('Penyihir', 'Penyihir')
    ]

    nama = models.CharField(max_length=50)
    role = models.CharField(
        max_length=15,
        choices=role_value,
        default=role_value[0]
    )
    deskripsi = models.TextField()

    class Meta:
        db_table = 'hero'

    def __str__(self):
        return "{}".format(self.id)
