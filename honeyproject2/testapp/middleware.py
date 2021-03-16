from django.http import HttpResponse
class AppMaintainanceMiddleware(object):

    def __init__(self,get_response):
        self.get_response=get_response

    def __call__(self,request):
        return HttpResponse('<h1> currently application is under maintainance! <p style="color:red;">please try again later.!</p> thank you :)</h1>')
