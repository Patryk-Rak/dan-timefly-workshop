from django.test import TestCase, Client, override_settings
from django.urls import reverse
import tempfile

from printed_models.models import PrintedModel


@override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.list_url = reverse('portfolio')
        self.details_url = reverse('portfolio-detail-page', args=['printedmodel1'])
        self.portfolio1 = PrintedModel.objects.create(
            name='printedmodel1',
            height=75,
            description='lorem ipsum',
            thumbnail=tempfile.NamedTemporaryFile(suffix=".jpg").name
        )

    def test_portfolio_list_GET(self):
        client = Client()
        response = self.client.get(self.list_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'website/portfolio/portfolio-list.html')

    def test_portfolio_detail_GET(self):
        response = self.client.get(self.details_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'website/portfolio/portfolio-details.html')

