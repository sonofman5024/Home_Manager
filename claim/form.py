from django.forms import ModelForm, Textarea
from claim.models import ClaimList

class ClaimForm(ModelForm):
    
    class Meta:
        model = ClaimList
        exclude = ["status", "user" ]
        widgets = {
            'content': Textarea(attrs={'cols': 100, 'rows': 5}),
        }
