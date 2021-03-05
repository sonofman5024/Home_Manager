from django.shortcuts import render, redirect
from claim.models import ClaimList
from claim.form import ClaimForm

# Create your views here.
def claim(request):
    return render(request, "claim.html", context = None)

def thank_you(request):
    return render(request, "thank_you.html", context = None)

def edit(request, claim_id):
    claim = ClaimList.objects.get(pk=claim_id)
    print(type(claim.filed_date))
    if request.method == 'POST':
        print(request.POST)
        print(request.FILES)
        form = ClaimForm(request.POST, request.FILES, instance=claim)
        print(form)
        if form.is_valid():
            form.save()
        else: print("change not saved. Something went wrong!")
        return redirect("thank_you")
    else:
        return render(request, "edit.html", {"claim":claim})    

def delete(request, claim_id):
    return render(request, "thank_you.html", context = None)    

def claim_history(request):
    all_claims = ClaimList.objects.all()

    return render(request, "claim_history.html", {"all_claims":all_claims, })
    
def file_claim(request):
    all_claims = ClaimList.objects.all()
    claim_form = ClaimForm
    print(request.POST)
    print(request.FILES)
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