from django.db import models

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


    claim_title = models.CharField(max_length=20, )
    filed_date = models.DateField(auto_now_add=True)
    content = models.CharField(max_length=300)
    status = models.CharField(max_length=10, choices=APPROVAL_STATUS_CHOICES, default=NEW)
    uploads = models.FileField(upload_to="uploads/")

    def __str__(self):
        if self.status == 'NEW':
            return self.claim_title + '-' + 'NEW'
        else: 
            return self.claim_title + '-' + 'Proccesed'
    
    
