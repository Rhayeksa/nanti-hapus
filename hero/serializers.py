from rest_framework import serializers

from hero.models import Hero


class Serializer(serializers.ModelSerializer):
    class Meta:
        model = Hero
        fields = (
            'id',
            'nama',
            'role',
            'deskripsi',
        )
