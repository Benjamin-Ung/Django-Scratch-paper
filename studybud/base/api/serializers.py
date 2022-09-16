from rest_framework.serializers import ModelSerializer
from base.models import Room

#takes a model and convert it into json file
class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'