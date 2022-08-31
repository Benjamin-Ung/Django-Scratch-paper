from django.forms import ModelForm
from .models import Room

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        #this line removes the fields in models/room from being displayed
        exclude = ['host', 'participants']