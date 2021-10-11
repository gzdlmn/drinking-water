from django.shortcuts import render
from datetime import date,datetime
# Create your views here.
def homePage(request):
    today = date.today()
    return render(request, "home.html", {'today':today})