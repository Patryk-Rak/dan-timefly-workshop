from django.shortcuts import render
from .models import Figure, FigureImages
from django.views.generic import \
    (DetailView,
     ListView)


def portfolio_page_view(request, *args, **kwargs):
    figures = Figure.objects.all()
    context = {'figures': figures}
    return render(request, "website/portfolio.html", context)


def portfolio_detail_page_view(request, pk, *args, **kwargs):
    figure = Figure.objects.get(id=pk)
    context = {'figure': figure}
#    return render(request, "website/portfolio-details.html", context)
    return render(request, "website/portfolio-details.html", {'figure': figure, 'gallery': FigureImages.objects.filter(id=pk)})
