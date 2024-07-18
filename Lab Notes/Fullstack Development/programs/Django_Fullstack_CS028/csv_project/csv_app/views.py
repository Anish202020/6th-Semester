from django.http import FileResponse 

from reportlab.pdfgen import canvas 

from .models import Book 

from django.shortcuts import redirect, render 

from .forms import BookForm 

  

def home(request): 

    if request.method == 'POST': 

        form = BookForm(request.POST) 

        if form.is_valid(): 

            form.save() 

            return redirect('home')  # Redirect to PDF generation after adding a book 

    else: 

        form = BookForm() 

    return render(request, 'csv_app/create_user_profile.html', {'form': form}) 

  
# csvapp/views.py 

import csv 

from django.http import HttpResponse 

from .models import Book 

  

def generate_csv(request): 

    response = HttpResponse(content_type='text/csv') 

    response['Content-Disposition'] = 'attachment; filename="book_catalog.csv"'

  

    writer = csv.writer(response) 

    writer.writerow(['Title', 'Author', 'Publication Year']) 

  

    books = Book.objects.all() 

    for book in books: 

        writer.writerow([book.title, book.author, book.publication_year]) 

  

    return response 