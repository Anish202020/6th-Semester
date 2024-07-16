from django.http import HttpResponse  
from django.views import View  
class NewView(View):  
    def get(self, request):  
        # View logic will place here  
        return HttpResponse('response')