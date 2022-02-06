from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Water
from .forms import WaterForm
from datetime import datetime, timedelta
from datetime import date, timedelta
from django.contrib.auth.decorators import login_required
import datetime
import calendar
# Create your views here.
@login_required(login_url="user:login")
def user_page(request):
    if Water.objects.filter(user=request.user).exists():
        # find the last 10 days
        today = date.today()
        yesterday = date.today()-timedelta(days=1)
        before_yesterday = date.today()-timedelta(days=2)
        two_days_before_yesterday = date.today()-timedelta(days=3)
        three_days_before_yesterday = date.today() - timedelta(days=4)
        four_days_before_yesterday = date.today() - timedelta(days=5)
        five_days_before_yesterday = date.today() - timedelta(days=6)
        six_days_before_yesterday = date.today() - timedelta(days=7)
        seven_days_before_yesterday = date.today() - timedelta(days=8)
        eight_days_before_yesterday = date.today() - timedelta(days=9)
        nine_days_before_yesterday = date.today() - timedelta(days=10)
        # show the last 5 days you found
        today_see = Water.objects.filter(user=request.user, created_date=today)
        yesterday_see = Water.objects.filter(user=request.user, created_date=yesterday)
        before_yesterday_see = Water.objects.filter(user=request.user, created_date=before_yesterday)
        two_days_before_yesterday_see = Water.objects.filter(user=request.user, created_date=two_days_before_yesterday)
        three_days_before_yesterday_see = Water.objects.filter(user=request.user, created_date=three_days_before_yesterday)
        # count of objects 10 days
        count1 = Water.objects.filter(user=request.user, created_date=today).count()
        count2 = Water.objects.filter(user=request.user, created_date=yesterday).count()
        count3 = Water.objects.filter(user=request.user, created_date=before_yesterday).count()
        count4 = Water.objects.filter(user=request.user, created_date=two_days_before_yesterday).count()
        count5 = Water.objects.filter(user=request.user, created_date=three_days_before_yesterday).count()
        count6 = Water.objects.filter(user=request.user, created_date=four_days_before_yesterday).count()
        count7 = Water.objects.filter(user=request.user, created_date=five_days_before_yesterday).count()
        count8 = Water.objects.filter(user=request.user, created_date=six_days_before_yesterday).count()
        count9 = Water.objects.filter(user=request.user, created_date=seven_days_before_yesterday).count()
        count10 = Water.objects.filter(user=request.user, created_date=eight_days_before_yesterday).count()
        form = WaterForm(request.POST or None)
        if form.is_valid():
            water = form.save(commit=False)
            water.user = request.user
            if water.drinking is True:
                water.save()
                if  Water.objects.filter(user=request.user, created_date=nine_days_before_yesterday).exists():
                    Water.objects.filter(user=request.user, created_date=nine_days_before_yesterday).delete()
                return redirect("userpage")
        return render(request, "userpage.html", {"form": form, "today": today, "yesterday":yesterday,
                                                 "before_yesterday": before_yesterday, "two_days_before_yesterday": two_days_before_yesterday,
                                                 "three_days_before_yesterday": three_days_before_yesterday,
                                                 "four_days_before_yesterday": four_days_before_yesterday,
                                                 "five_days_before_yesterday": five_days_before_yesterday,
                                                 "six_days_before_yesterday": six_days_before_yesterday,
                                                 "seven_days_before_yesterday": seven_days_before_yesterday,
                                                 "eight_days_before_yesterday": eight_days_before_yesterday,
                                                 "today_see": today_see, "yesterday_see": yesterday_see,
                                                 "before_yesterday_see": before_yesterday_see,
                                                 "two_days_before_yesterday_see": two_days_before_yesterday_see,
                                                 "three_days_before_yesterday_see": three_days_before_yesterday_see,
                                                 "count1": count1, "count2": count2, "count3": count3, "count4": count4,
                                                 "count5": count5, "count6": count6, "count7": count7, "count8": count8,
                                                 "count9": count9, "count10": count10})
    else:
        form = WaterForm(request.POST or None)
        if form.is_valid():
            water = form.save(commit=False)
            water.user = request.user
            if water.drinking is True:
                water.save()
                return redirect("userpage")
        return render(request, "userpage.html", {"form": form})