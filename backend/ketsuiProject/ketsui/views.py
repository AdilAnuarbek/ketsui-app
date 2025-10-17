from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from ketsui.models import Kanj, Task
from ketsui.serializer import TaskSerializer


# from .models import Gloss
# Create your views here.

def index(request):
    context = {}
    return render(request, "index.html", context)

# @api_view(['GET'])
# def search(request, term):
#     results = Gloss.objects.filter(text__icontains=term)[:30]
#     return Response([
#         {"gloss": g.txt, "lang": g.lang, "sense_id": g.sens}
#         for g in results
#     ])

@api_view(['GET'])
def kanji_search(request, term):
    """
    Search JMdict for kanji entries that contain the given character(s).
    """
    results = (
        Kanj.objects
        .filter(txt__icontains=term)
        .values('entr', 'txt')[:50]
    )

    return Response(list(results))

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer