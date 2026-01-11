from django.shortcuts import render, redirect
from Member.forms import MemberUpdateForm
from .models import Member
# Create your views here.
def member_index(request):
    model = Member.objects.all()
    return render(request, 'index.html', {'members': model})
def member_detail(request, slug):
    model = Member.objects.get(slug=slug)
    return render(request, 'details.html', {'x': model})
def success_page(request):
    return render(request, 'success.html')
def update_form(request):
    if request.method == 'POST':
        form = MemberUpdateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_page')  # Redirect to a success page after submission
    else:
        form = MemberUpdateForm()
    return render(request, 'update_plus.html', {'form': form})