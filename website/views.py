from django.shortcuts import render

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
