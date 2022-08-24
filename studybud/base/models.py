from django.db import models

# Create your models here.

class Room(models.Model):
    #host = 
    #topic =
    name = models.CharField(max_length=200)

    #database can have a null value / form can be blank as well
    #can add room without description 
    description = models.TextField(null = True, blank = True)

    #participants = 

    #take a time stamp when updated
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name