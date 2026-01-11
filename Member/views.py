from django.shortcuts import render
from .models import Member
# Create your views here.
def member_index(request):
    model = Member.objects.all()
    return render(request, 'index.html', {'members': model})
def member_detail(request, slug):
    model = Member.objects.get(slug=slug)
    return render(request, 'details.html', {'x': model})
