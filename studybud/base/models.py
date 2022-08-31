from django.db import models
from django.contrib.auth.models import User
# Create your models here.
#need to run when adding stuff : python manage.py makemigrations / command prep or updates tables and make any necessary changes


class Topic(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Room(models.Model):
    host =  models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null = True)
    name = models.CharField(max_length=200)

    #database can have a null value / form can be blank as well
    #can add room without description 
    description = models.TextField(null = True, blank = True)
    participants = models.ManyToManyField(User, related_name = 'participants', blank = True)

    #take a time stamp when updated
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-updated', '-created']

        def __str__(self):
            return self.name     

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #models.SETNULL = message stays in database / .CASCADE = message deleted if room deleted
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']
        
    def __str__(self):
        #only want first 50 char for message preview
        return self.body[0:50]

    