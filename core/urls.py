"""core URL Configuration

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
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from website.views import (
                            homepage_view,
                            contact_page_view,
                            services_page_view,
                            about_page_view
                          )
from printed_models.views import (
                                    portfolio_page_view,
                                    portfolio_detail_page_view,
                                    portfolio_page_create_view,
                                    portfolio_page_update_view,
                                    portfolio_page_delete_view
                                 )

urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', homepage_view, name="homepage"),
    path('about/', about_page_view, name="about"),
    path('contact/', contact_page_view, name="contact"),
    path('services/', services_page_view, name="services"),
    path('portfolio/', portfolio_page_view, name="portfolio"),
    path('portfolio/details/<slug:slug>', portfolio_detail_page_view, name="portfolio-detail-page"),

    #CRUD
    path('portfolio/post', portfolio_page_create_view, name="portfolio-page-create"),
    path('portfolio/update-<slug:slug>', portfolio_page_update_view, name="portfolio-page-update"),
    path('portfolio/delete-<slug:slug>', portfolio_page_delete_view, name="portfolio-page-delete"),

]

handler404 = "website.views.handle_not_found"

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

