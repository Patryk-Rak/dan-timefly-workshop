from django.shortcuts import render

def my_work_view(request, *args, **kwargs):
    context = {}
    context['my_name'] = "mitch"
    return render(request, "my_work/main_page.html", context)