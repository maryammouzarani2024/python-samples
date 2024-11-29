from django.shortcuts import render
from django.template import loader
from django.http import  HttpResponse

# Create your views here.
def handler_404(request, exception):
     template=loader.get_template('exceptionhandler/exception.html')
     return HttpResponse(template.render({'exception':exception }, request), status=404)


def handler_500(request):
     template=loader.get_template('exceptionhandler/exception.html')
     return HttpResponse(template.render( request), status=500)

def handler_403(request, exception):
     template=loader.get_template('exceptionhandler/exception.html')
     return HttpResponse(template.render({'exception':'Access is not allowed' }, request), status=403)