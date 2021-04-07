from django.shortcuts import render, redirect
from claim.models import ClaimList
from claim.form import ClaimForm
from django.core.paginator import Paginator 
from user_app.decorator import kid_required, parent_required
from django.contrib.auth.decorators import login_required

# Create your views here.


@kid_required
def claim(request):
    return render(request, "claim.html", context = None)

def thank_you(request):
    return render(request, "thank_you.html", context = None)

@kid_required
def edit(request, claim_id):
    claim = ClaimList.objects.get(pk=claim_id)

    if request.method == 'POST':
        claim = ClaimForm(request.POST, request.FILES, instance=claim)
        if claim.is_valid():
            claim.save()
            return redirect("claim_history")
    else:
        claim = ClaimList.objects.get(pk=claim_id)

    return render(request, "edit.html", {"claim":claim})    

@kid_required
def delete(request, claim_id):
    claim = ClaimList.objects.get(pk=claim_id)
    if claim.user == request.user:
        claim.delete()
        return redirect("claim_history")
    else:
        return redirect("access_denied")    

@kid_required
def claim_history(request):
    all_claims = ClaimList.objects.filter(user = request.user)
    paginator= Paginator(all_claims, 10)
    page = request.GET.get("page")
    all_claims = paginator.get_page(page)
    return render(request, "claim_history.html", {"all_claims":all_claims, })

@kid_required   
def file_claim(request):

    if request.method == "POST":
        claim_form = ClaimForm(request.POST, request.FILES)
        print(request)
        if claim_form.is_valid():
            claim_form.save(commit=False).user = request.user
            claim_form.save()
            return redirect("thank_you.html")
    else: 
        claim_form = ClaimForm()
    return render(request, "file_claim.html", {"claim_form" : claim_form})

def access_denied(request):
    return render(request, 'access_denied.html')