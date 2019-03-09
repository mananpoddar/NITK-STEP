from django.db import models

# Create your models here.

class govtProjects(models.Model):
    image = models.ImageField(upload_to='documents/')
    title = models.CharField(max_length = 80, blank =  False  )
    description = models.TextField(blank =  False  )
    details = models.TextField(blank =  False  )



class ongoingProgrammes(models.Model):
    image = models.ImageField(upload_to='documents/')
    title = models.CharField(max_length = 80, blank =  False  )
    description = models.TextField(blank =  False  )
    details = models.TextField(blank =  False  )


class comingEvents(models.Model):
    image = models.ImageField(upload_to='documents/')
    title = models.CharField(max_length = 80, blank =  False  )
    description = models.TextField(blank =  False  )
    details = models.TextField(blank =  False  )