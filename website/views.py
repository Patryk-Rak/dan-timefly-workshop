from django.shortcuts import render

from printed_models.models import PrintedModel


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
    figures_amount = PrintedModel.objects.all().count()
    context = {'figures_amount': figures_amount}
    return render(request, "website/about.html", context)


def handle_not_found(request, exception):
    return render(request, "website/404.html")
