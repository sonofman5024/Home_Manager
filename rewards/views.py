from django.shortcuts import render
from user_app.decorator import kid_required
# Create your views here.

@kid_required
def rewards(request):
    
    return render(request, "rewards.html", context = None)