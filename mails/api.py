from rest_framework.viewsets import GenericViewSet
from mails.service import send_mail
from rest_framework.response import Response
from rest_framework.decorators import action
from django.conf import settings
import requests
import json


class MailViewSet(GenericViewSet):
    @action(methods=['post'], detail=False, url_path='sendMail', url_name='sendMail')
    def send_mail(self, request):
        data = dict(subject=request.data['subject'],
                    body=request.data['message'],
                    from_email=settings.EMAIL_HOST_USER, to=[request.data['to']],
                    headers={'Reply-to': request.data['from_email']})
        result = json.loads(send_mail(data))
        if result['success']:
            return Response(result, status=202)
        return Response(result, status=400)

    @action(methods=['post'], detail=False, url_path='verify_captcha', url_name='verify_captcha')
    def verify_captcha(self, request):
        result = requests.post(request.data['url'], params=request.data['params'], headers=request.data['headers'])
        try:
            json_result = result.json()
            if json_result['success']:
                return Response(json_result, status=202)
            return Response(json_result, status=400)
        except ValueError as e:
            return Response(e, status=400)
