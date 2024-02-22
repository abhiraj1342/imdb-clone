#we created this file manually
# import serrializers from django rest framework
from rest_framework import serializers


# we created MovieSerializer class 
class MovieSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    name=serializers.CharField()
    description=serializers.CharField()
    active=serializers.BooleanField()