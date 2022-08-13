from datetime import datetime

from django.shortcuts import render
from .models import Ask
from .forms import AskForm


def index(request):
    asks = Ask.objects.order_by('id')
    return render(request, 'main/index.html', {'asks': asks})


def about(request):
    return render(request, 'main/about.html')


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
