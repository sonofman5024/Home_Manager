from django.shortcuts import render

# Create your views here.
def complaint(request):
    userinfo = {'kid_name' : "Travis"}
    return render(request, "complaint.html", context = userinfo)