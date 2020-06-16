from django.core.mail import EmailMessage
from django.conf import settings
import json


# subject='', body='', from_email=None, to=None, headers=None, reply_to=None
def send_mail(data):
    try:
        data['from_email'] = settings.EMAIL_HOST_USER
        data['headers'] = {'Reply-to': data['from_email']}
        email = EmailMessage(**data)
        result = email.send()
        json_result = json.dumps({"success": result and True,
                                  "count_send_email": result})
        return json_result
    except:
        json_result = json.dumps({
            "success": False,
            "count_send_email": 0
        })
        return json_result


class EmailServices:
    pass
