from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from user_app.models import User, Kid
from django.db.models import Count, F

# Create your views here.
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

