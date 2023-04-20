from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse, redirect


class AuthMiddleware(MiddlewareMixin):

    def process_request(self, request):
        if request.path_info in ['/login/', '/image/code/']:
            return

        info_dist = request.session.get('info')
        if info_dist:
            return

        return redirect('/login/')