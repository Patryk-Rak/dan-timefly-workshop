from django.shortcuts import render

def portfolio_page_view(request, *args, **kwargs):
    context = {}
    context['my_name'] = "Dan"
    return render(request, "website/portfolio.html", context)
