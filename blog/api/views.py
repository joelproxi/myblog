

from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view()
def post_list(request):
    return Response('Post List')


@api_view()
def post_detail(request, id):
    return Response(id)