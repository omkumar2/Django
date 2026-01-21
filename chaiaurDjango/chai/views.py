from django.shortcuts import render
from .models import chaivarity
from django.shortcuts import get_object_or_404

# Create your views here.
def hello(request):
    chais = chaivarity.objects.all()
    return render(request, 'chai/hello.html' ,{'chais': chais})   # {'chais': chais} by this you can transfer values

def chai_detail(request, chai_id):
    chai = get_object_or_404(chaivarity, pk=chai_id)
    return render(request, 'chai/chai_detail.html', {'chai':chai})