from django.shortcuts import render
from django.http import HttpResponse

def resume(request):
    """
    cv resume view.
    """
    return render(request, 'resume/index.html')

def error_404(request):
    """
    404 http status.
    """
    return render(request, 'errors/404.html', status=404)

def error_500(request):
    """
    500 http status.
    """
    return render(request, 'errors/500.html', status=500)