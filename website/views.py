from django.shortcuts import render
from painted_models.models import Figure

def homepage_view(request, *args, **kwargs):
    context = {}
    context['my_name'] = "Dan"
    return render(request, "website/homepage.html", context)


def contact_page_view(request, *args, **kwargs):
    context = {}
    context['my_name'] = "Dan"
    return render(request, "website/contact.html", context)


def services_page_view(request, *args, **kwargs):
    context = {}
    context['my_name'] = "Dan"
    return render(request, "website/services.html", context)


def about_page_view(request, *args, **kwargs):
    figures_amount = Figure.objects.all().count()
    context = {'figures_amount': figures_amount}
    return render(request, "website/about.html", context)
