from django.test import TestCase, override_settings

from django.urls import reverse, resolve
from printed_models.views import portfolio_page_view, portfolio_detail_page_view
from website.views import homepage_view, contact_page_view, services_page_view, about_page_view

@override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
class TestURLs(TestCase):
    def test_homepage(self):
        url = reverse('homepage')
        print(resolve(url))
        self.assertEquals(resolve(url).func, homepage_view)

    def test_aboutpage(self):
        url = reverse('about')
        print(resolve(url))
        self.assertEquals(resolve(url).func, about_page_view)

    def test_portfoliopage(self):
        url = reverse('portfolio')
        print(resolve(url))
        self.assertEquals(resolve(url).func, portfolio_page_view)

    def test_servicespage(self):
        url = reverse('services')
        print(resolve(url))
        self.assertEquals(resolve(url).func, services_page_view)

    def test_contactpage(self):
        url = reverse('contact')
        print(resolve(url))
        self.assertEquals(resolve(url).func, contact_page_view)