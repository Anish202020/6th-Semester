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
    # Redirect to PDF generation after adding a book
            return redirect('home')  
    else:
        form = BookForm()
    return render(request, 'pdf_app/create_user_profile.html', 
                  {'form': form})
 
def generate_pdf(request):
    response = FileResponse(generate_pdf_file(), 
                            as_attachment=True, 
                            filename='book_catalog.pdf')
    return response
 
 
def generate_pdf_file():
    from io import BytesIO
 
    buffer = BytesIO()
    p = canvas.Canvas(buffer)
 
    # Create a PDF document
    books = Book.objects.all()
    p.drawString(100, 750, "Book Catalog")
 
    y = 700
    for book in books:
        p.drawString(100, y, f"Title: {book.title}")
        p.drawString(100, y - 20, f"Author: {book.author}")
        p.drawString(100, y - 40, f"Year: {book.publication_year}")
        y -= 60
 
    p.showPage()
    p.save()
 
    buffer.seek(0)
    return buffer