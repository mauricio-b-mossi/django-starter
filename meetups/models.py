from django.db import models

# Create your models here.
# Define everything then run "python manage.py makemigrations" which will migrate the data into a schema
# Then run python manage.py migrate which CREATES THE DB TABLE

# IF UPDATED YOU HAVE TO TODO: REBUILD THE DB ^

# The data is imported into the view and to query we import the data.object which comes with querying methods

# Ideally define from top to bottom the dependencies

# TODO: IMPORTANT TO IMPORT EVERYTHING ON THE ADIM TAB TO BE VISIBLE


class Location(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)

    def __str__(self):
        return f'{self.name} ({self.address})'

        
class Participant(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return f'{self.email}'

class Meetup(models.Model):
     # ImageField stores the image in memory and holds the ref of it in DB
    title = models.CharField(max_length=200)
    organizer_email = models.EmailField()
    date = models.DateField()
    slug = models.SlugField(unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='images')
    # models.ForeignKey = set up relations of one-to-many with the value of Location
    # models.CASCADE = deletion of the meetup
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    # blank is similar to ?: in ts
    participants = models.ManyToManyField(Participant, blank=True)

      # str is the name and self the el
    # This is done to edit how the item is presented in string form
    def __str__(self):
        return f'{self.title} - {self.slug}'


    
  

