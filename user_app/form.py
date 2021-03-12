from .models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name','date_birth','username','email')