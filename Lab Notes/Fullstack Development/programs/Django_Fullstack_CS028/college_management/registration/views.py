from django.shortcuts import render
from django.http import JsonResponse
from .forms import StudentForm
def student_registration(request):
    if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = StudentForm()
        return render(request, 'registration/student_registration.html', {'form': form})