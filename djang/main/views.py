from datetime import datetime

from django.shortcuts import render
from .models import Ask, Landing, DB_Landing, Shop
from .forms import AskForm


def index(request):
    asks = Ask.objects.order_by('id')
    return render(request, 'main/index.html', {'asks': asks})


def about(request):
    landings = Landing.objects.order_by('id')
    db_landings = DB_Landing.objects.order_by('id')
    shops = Shop.objects.order_by('id')
    return render(request, 'main/about.html', {'landings': landings, 'db_landings': db_landings, 'shops': shops})


def contact(request):
    if request.method == 'POST':
        gm = request.POST["gmail"]
        qu = request.POST["question"]
        s = Ask(date=str(datetime.now().date()), time=str(datetime.now().time())[0:8], gmail=request.POST["gmail"], question=request.POST["question"])
        s.save()
    form = AskForm()
    context = {
        'form': form
    }
    return render(request, 'main/contact.html', context)
