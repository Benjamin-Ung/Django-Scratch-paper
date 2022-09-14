from django.forms import ModelForm
from .models import Room
from django.contrib.auth.models import User

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        #this line removes the fields in models/room from being displayed
        exclude = ['host', 'participants']

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username','email']

