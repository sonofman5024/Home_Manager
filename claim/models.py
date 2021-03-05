from django.db import models
from datetime import date
from model_utils.fields import StatusField
from model_utils import Choices

# Create your models here.
class ClaimList(models.Model):
       
    NEW = 'NEW'
    ACCEPTED = 'Accepted'
    DECLINED = 'Declined'
    APPROVAL_STATUS_CHOICES = [
        (ACCEPTED, 'Accepted'),
        (DECLINED, 'Declined'),
        (NEW, 'New Claim'),
    ]

    STATUS = Choices('NEW', 'Accepted', 'Declined')

    claim_title = models.CharField(max_length=20, )
    filed_date = models.DateField(default = date.today)
    content = models.CharField(max_length=100)
    status = models.CharField(max_length=10, choices=APPROVAL_STATUS_CHOICES, default=NEW)
    uploads = models.FileField(upload_to="uploads/")
    

    def __str__(self):
        if self.status == 'NEW':
            return self.claim_title + '-' + 'NEW'
        else: 
            return self.claim_title + '-' + 'Proccesed'
    
    
