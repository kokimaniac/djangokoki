from django.shortcuts import render
from django.http import HttpResponse

def resume(request):
    """
    cv resume view.
    """
    return render(request, 'resume/index.html')