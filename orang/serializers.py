from rest_framework import serializers

from orang.models import Orang


class Serializer(serializers.ModelSerializer):
    class Meta:
        model = Orang
        fields = (
            'username',
            'nama',
            'penjelasan',
            'id_hero',
        )
