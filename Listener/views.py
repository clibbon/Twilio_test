from django.http import HttpResponse
import twilio.twiml
from django_twilio.decorators import twilio_view

# Create your views here.
def index(request):
    return HttpResponse(request.path)

@twilio_view
def text_test(request):
    resp = twilio.twiml.Response()
    resp.message("A successful response")
    return resp

