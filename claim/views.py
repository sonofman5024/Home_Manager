from django.shortcuts import render

# Create your views here.
def claim(request):
    
    return render(request, "claim.html", context = None)