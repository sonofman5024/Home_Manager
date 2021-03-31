from django.shortcuts import render
from user_app.decorator import kid_required
# Create your views here.
@kid_required
def complaint(request):
    userinfo = {'kid_name' : "Travis"}
    return render(request, "complaint.html", context = userinfo)