# error handling middleware
from django.core.exceptions import PermissionDenied
from django.shortcuts import render


class PermissionDeniedErrorHandler:
    def __init__(self, get_response):
        print("init method")
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        print("call method") 
        return response

    def process_request(request):
        print("heloooo")

    def process_view(self, request, view_func, view_args, view_kwargs):
       print("process view method")

    def process_exception(self, request, exception):
        if isinstance(exception, PermissionDenied):
            print("process exception")
            return render(
                request=request,
                template_name="fashionworld/custom_403.html",
                status=403
            )
        return None