from django.shortcuts import render

def index(request):
    return render(request, 'landing/index.html')

def landing_view(request):
    """
    Renders the main landing page template.
    """
    return render(request, 'landing/landing_figma.html')