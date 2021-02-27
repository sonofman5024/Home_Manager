from django.shortcuts import render
from claim.models import ClaimList

# Create your views here.
def claim(request):
    
    return render(request, "claim.html", context = None)
def view_claims(request):
    all_claims = ClaimList.objects.all()
    return render(request, "view_claims.html", {"all_claims":all_claims})