from django.shortcuts import render
from .models import Figure, FigureImages, Tag
from django.views.generic import \
    (DetailView,
     ListView)


#PORTFOLIO TAB VIEWS
def portfolio_page_view(request, *args, **kwargs):
    figures = Figure.objects.all()
    tags = Tag.objects.all()
    context = {'figures': figures, 'tags': tags}
    return render(request, "website/portfolio/portfolio-list.html", context)


def portfolio_detail_page_view(request, slug, *args, **kwargs):
    figure = Figure.objects.get(slug=slug)
    context = {'figure': figure, 'gallery': FigureImages.objects.filter(figure_key_id=figure.id)}
    return render(request, "website/portfolio/portfolio-details.html", context)


#PORTFOLIO CRUD
def portfolio_page_create_view(request, *args, **kwargs):
    context = {}
    return render(request, "website/portfolio/portfolio-post.html", context)
