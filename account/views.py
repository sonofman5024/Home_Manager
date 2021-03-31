from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from user_app.models import User, Kid
from claim.models import ClaimList
from django.core.paginator import Paginator

# Create your views here.
@login_required
def account(request):
    
    return render(request, "account.html", context = None)

@login_required
def account_info(request):
    if request.user.is_kid:
        account = User.objects.get(username = request.user)
        kid = Kid.objects.get(user = request.user)
        credit = kid.reward_credit
        parent = User.objects.get(username = kid.parent)

        return render(request, "account_info.html", {'account':account, 'credit':credit, 'parent':parent }, )
    elif request.user.is_parent:
        account = User.objects.get(username = request.user)
        kids = account.kids_parent.all()

        return render(request, "account_info.html", {'account':account, 'kids':kids,}, ) 

def kid_claim(request, kid_id):
    request.session['kid_id']=kid_id
    if Kid.objects.get(user=kid_id).parent == request.user:
        active_claims = ClaimList.objects.filter(user=kid_id, status='NEW')

        paginator= Paginator(active_claims, 10)
        page = request.GET.get("page")
        active_claims = paginator.get_page(page)
        return render(request, "kid_claim.html", {'active_claims':active_claims} )
    else:
        return redirect('access_denied')

def accept(request, claim_id):
    claim = ClaimList.objects.get(pk=claim_id)
    if request.session.has_key('kid_id'):
        kid_id=request.session['kid_id']
        if Kid.objects.get(user=kid_id).parent == request.user:
            kid = Kid.objects.get(user = kid_id)
            kid.reward_credit += 1
            kid.save()
            claim.status = 'ACCEPTED'
            claim.save()
            return redirect('kid_claim', kid_id = kid_id)
        else:
            return redirect('access_denied')
    else:
        return redirect('access_denied')

def decline(request, claim_id):
    claim = ClaimList.objects.get(pk=claim_id)
    if request.session.has_key('kid_id'):
        kid_id=request.session['kid_id']
        if Kid.objects.get(user=kid_id).parent == request.user:
            claim.status = 'DECLINED'
            claim.save()
            return redirect('kid_claim', kid_id = kid_id)
        else:
            return redirect('access_denied')
    else:
        return redirect('access_denied')
