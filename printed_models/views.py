from django.shortcuts import render, redirect
from .models import PrintedModel, PrintedModelMaterial, PrintedModelImage, Tag
from .forms import PrintedModelForm
from django.contrib.auth.decorators import login_required


# PORTFOLIO TAB VIEWS
def portfolio_page_view(request, *args, **kwargs):
    printed_models = PrintedModel.objects.all()
    tags = Tag.objects.all()
    context = {'printed_models': printed_models, 'tags': tags}
    return render(request, "website/portfolio/portfolio-list.html", context)


def portfolio_detail_page_view(request, slug, *args, **kwargs):
    printed_model = PrintedModel.objects.get(slug=slug)
    context = {'printed_model': printed_model,
               'gallery': PrintedModelImage.objects.filter(figure_key_id=printed_model.id),
               'materials': PrintedModelMaterial.objects.filter(figure_key_id=printed_model.id)}
    return render(request, "website/portfolio/portfolio-details.html", context)


# PORTFOLIO CRUD

@login_required(login_url='/admin/')
def portfolio_page_create_view(request, *args, **kwargs):
    printed_model_form = PrintedModelForm()

    if request.method == 'POST':
        printed_model_form = PrintedModelForm(request.POST, request.FILES)
        if printed_model_form.is_valid():
            printed_model_form.save()
        return redirect('portfolio')

    context = {'printed_model_form': printed_model_form}
    return render(request, "website/portfolio/portfolio-create.html", context)


@login_required(login_url='/admin/')
def portfolio_page_update_view(request, slug, *args, **kwargs):
    printed_models = PrintedModel.objects.get(slug=slug)
    printed_model_form = PrintedModelForm(instance=printed_models)

    if request.method == 'POST':
        printed_model_form = PrintedModelForm(request.POST, request.FILES, instance=printed_models)
        if printed_model_form.is_valid():
            printed_model_form.save()
        return redirect('portfolio')

    context = {'printed_model_form': printed_model_form}
    return render(request, "website/portfolio/portfolio-create.html", context)


@login_required(login_url='/admin/')
def portfolio_page_delete_view(request, slug, *args, **kwargs):
    printed_models = PrintedModel.objects.get(slug=slug)

    if request.method == 'POST':
        printed_models.delete()
        return redirect('portfolio-page')
    context = {'item': printed_models}
    return render(request, "website/portfolio/portfolio-delete.html", context)
