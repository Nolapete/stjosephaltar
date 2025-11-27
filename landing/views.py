from django.shortcuts import render


def index(request):
    return render(request, "landing/index.html")


def about(request):
    return render(request, "landing/about.html")


def contact(request):
    return render(request, "landing/contact.html")


def gallery(request):
    return render(request, "landing/gallery.html")


def tradition(request):
    return render(request, "landing/tradition.html")


def landing_view(request):
    """
    Renders the main landing page template.
    """
    return render(request, "landing/landing_figma.html")
