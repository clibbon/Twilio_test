from django.http import HttpResponse
import twilio.twiml

# Create your views here.
def index(request):
    return HttpResponse(request.path)

def text_test(request):
    resp = twilio.twiml.Response()
    resp.message("A successful response")
    return HttpResponse(resp)

