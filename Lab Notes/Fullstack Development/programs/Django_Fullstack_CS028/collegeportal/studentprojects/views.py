from django.shortcuts import render, redirect
from .forms import ProjectForm

def project_create_view(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('project_success')
    else:
        form = ProjectForm()
    return render(request, 'studentprojects/project_form.html', {'form': form})

def project_success_view(request):
    return render(request, 'studentprojects/project_success.html')
