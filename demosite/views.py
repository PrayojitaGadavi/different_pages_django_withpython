from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1> Hello from Django World</h1>')

def about(request):
    return HttpResponse('<h1> This is About Page</h1>')

def contact(request):
    return HttpResponse('<h1> This is Contact Page</h1>')

def address(request):
    return HttpResponse('<h1> This is Address Page</h1>')

def technology(request):
    return HttpResponse('<h1> This is Technology Page</h1>')

def web(request):
    return HttpResponse('<h1> This is Web Page</h1>')

def mobile(request):
    return HttpResponse('<h1> This is Mobile Page</h1>')

def desktop(request):
    return HttpResponse('<h1> This is Desktop Page</h1>')