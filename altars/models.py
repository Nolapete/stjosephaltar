from django.db import models

from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Altar(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200, null=True, blank=True)
    address1 = models.CharField(max_length=100, null=True, blank=True)
    address2 = models.CharField(max_length=100, null=True, blank=True)
    address3 = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    zipcode = models.CharField(max_length=20, null=True, blank=True)
    established_date = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        indexes = [models.Index(fields=['name', 'location', 'address1', 'address2', 'address3', 'city', 'state', 'zipcode', 'established_date'])]
    
class Contact(models.Model):
    CONTACT_TYPES = {
        'D': 'Donations',
        'G': 'General',
    }
    altar = models.ForeignKey(Altar, on_delete=models.CASCADE)
    type = models.CharField(max_length=50, null=True, blank=True, choices=CONTACT_TYPES) 
    name = models.CharField(max_length=100, null=True, blank=True)
    phone = PhoneNumberField(blank=True)
    email = models.EmailField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.altar.name})"
  
class Event(models.Model):
    EVENT_TYPES = {
        'V': 'Viewing',
        'M': 'Mass',
        'F': 'Meals',
        'B': 'Blessing',
        'T': 'Tupa Tupa',
    }
    altar = models.ForeignKey(Altar, on_delete=models.CASCADE)
    notes = models.TextField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    type = models.CharField(max_length=50, null=True, blank=True, choices=EVENT_TYPES) 
    start = models.TimeField(null=True, blank=True)
    end = models.TimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.type} on {self.date} from {self.start} to {self.end} for {self.altar.name}"
    
# split out donation contacts and donation websites into own model with type of contact/website and foreign key to altar?