from django.forms import ModelForm, Textarea
from claim.models import ClaimList

class ClaimForm(ModelForm):
    
    class Meta:
        model = ClaimList
        exclude = ["status", ]
        widgets = {
            'content': Textarea(attrs={'cols': 100, 'rows': 5}),
        }
