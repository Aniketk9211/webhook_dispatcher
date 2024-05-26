from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Account, Platform, Webhook
import requests
import json

@csrf_exempt
def receive_data(request, account_id):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        account = Account.objects.get(id=account_id)
        platforms = Platform.objects.filter(account=account)

        if not platforms.exists():
            return JsonResponse({'status': 'no platforms configured'})

        for platform in platforms:
            response = requests.post(platform.webhook_url, json=data)
            Webhook.objects.create(platform=platform, payload=data)
        
        return JsonResponse({'status': 'success'})

    return JsonResponse({'status': 'failed'}, status=400)

def index(request):
    return HttpResponse("Welcome to the Webhook Dispatcher!")
