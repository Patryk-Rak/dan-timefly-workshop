from django.shortcuts import render
from .models import Figure
from django.views.generic import \
    (DetailView,
     ListView)


def portfolio_page_view(request, *args, **kwargs):
    figures = Figure.objects.all()
    context = {'figures': figures}
    return render(request, "website/portfolio.html", context)


def portfolio_detail_page_view(request, *args, **kwargs):
    context = {}
    context['my_name'] = "Dan"
    return render(request, "website/portfolio-details.html", context)