from location.models import Location
from rest_framework import serializers

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'name', 'address', 'rating', 'city']