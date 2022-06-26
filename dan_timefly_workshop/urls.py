"""dan_timefly_workshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from website.views import (
                            homepage_view,
                            contact_page_view,
                            services_page_view,
                            about_page_view
                          )
from painted_models.views import portfolio_page_view, portfolio_detail_page_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage_view, name="homepage"),
    path('about/', about_page_view, name="about"),
    path('contact/', contact_page_view, name="contact-page"),
    path('services/', services_page_view, name="services"),
    path('services/', services_page_view, name="services"),
    path('portfolio/', portfolio_page_view, name="portfolio-page"),
    path('portfolio/details/<str:pk>', portfolio_detail_page_view, name="portfolio-detail-page"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)