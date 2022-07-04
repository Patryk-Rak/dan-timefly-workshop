from django.shortcuts import render
from .models import Figure, FigureImages, Tag
from django.views.generic import \
    (DetailView,
     ListView)


def portfolio_page_view(request, *args, **kwargs):
    figures = Figure.objects.all()
    tags = Tag.objects.all()
    context = {'figures': figures, 'tags': tags}
    return render(request, "website/portfolio.html", context)


def portfolio_detail_page_view(request, pk, *args, **kwargs):
    figure = Figure.objects.get(id=pk)
    context = {'figure': figure, 'gallery': FigureImages.objects.filter(figure_key_id=pk)}
    return render(request, "website/portfolio-details.html", context)
