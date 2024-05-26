from django.test import TestCase
from django.urls import reverse
from .models import Account, Platform

class WebhookTests(TestCase):

    def setUp(self):
        self.account = Account.objects.create(name="Test Account", email="test@example.com")
        self.platform = Platform.objects.create(name="Test Platform", account=self.account, webhook_url="https://example.com/webhook")

    def test_receive_data(self):
        response = self.client.post(reverse('receive_data', args=[self.account.id]), {'key': 'value'}, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['status'], 'success')
    
    def test_receive_data_no_platforms(self):
        account_without_platforms = Account.objects.create(name="No Platform Account", email="noplat@example.com")
        response = self.client.post(reverse('receive_data', args=[account_without_platforms.id]), {'key': 'value'}, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['status'], 'no platforms configured')
