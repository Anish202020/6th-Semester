from django.http import HttpResponse
from datetime import datetime
def current_datetime(request):
 now = datetime.now()
 html = "<html><body>Current date and time: {}</body></html>".format(now)
 return HttpResponse(html)