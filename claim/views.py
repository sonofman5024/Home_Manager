from django.shortcuts import render, redirect
from claim.models import ClaimList
from claim.form import ClaimForm
from django.core.paginator import Paginator 

# Create your views here.
def claim(request):
    return render(request, "claim.html", context = None)

def thank_you(request):
    return render(request, "thank_you.html", context = None)

def edit(request, claim_id):
    claim = ClaimList.objects.get(pk=claim_id)

    if request.method == 'POST':
        form = ClaimForm(request.POST, request.FILES, instance=claim)
        if form.is_valid():
            form.save()
        else: print("change not saved. Something went wrong!")
        return redirect("thank_you")
    else:
        return render(request, "edit.html", {"claim":claim})    

def delete(request, claim_id):
    claim = ClaimList.objects.get(pk=claim_id)
    claim.delete()
    return redirect("claim_history")    

def claim_history(request):
    all_claims = ClaimList.objects.all()
    paginator= Paginator(all_claims, 10)
    page = request.GET.get("page")
    all_claims = paginator.get_page(page)
    return render(request, "claim_history.html", {"all_claims":all_claims, })
    
def file_claim(request):
    all_claims = ClaimList.objects.all()
    claim_form = ClaimForm
    if request.method == "POST":
        form = ClaimForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            form.save()
        else:
            print("claim was not sent. Something went wrong!")
        return redirect("thank_you.html")

    else: 

        return render(request, "file_claim.html", {"all_claims":all_claims, "claim_form" : claim_form})