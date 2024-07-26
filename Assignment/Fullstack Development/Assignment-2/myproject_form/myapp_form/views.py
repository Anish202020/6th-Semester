from django.shortcuts import render, redirect
from .forms import UserForm
from .models import UserData

def user_form_view(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            gender = form.cleaned_data['gender']
            text = form.cleaned_data['text']

            # Save the data to the database
            UserData.objects.create(username=username, gender=gender, text=text)
            return redirect('success')
    else:
        form = UserForm()

    return render(request, 'user_form.html', {'form': form})

def success_view(request):
    users = UserData.objects.all()
    return render(request, 'success.html', {'users': users})
