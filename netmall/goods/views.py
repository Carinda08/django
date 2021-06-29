from django.http import JsonResponse
from django.views import View
from .serializers import BookInfoSerializer, BookInfoModelViewset, HeroInfoSerializer
from .models import BookInfo, HeroInfo


# Create your views here.

class BookInfoView(View):
    def get(self, request):
        #1 get all books
        books = BookInfo.objects.all()

        #2 serialize
        s = BookInfoSerializer(instance=books, many=True)

        #3 return
        return JsonResponse(s.data, safe=False)

class BookInfoDetailView(View):
    def get(self, request, idx):
        book = BookInfo.objects.get(idx)
        s = BookInfoSerializer(instance=book)
        return JsonResponse(s.data, safe=False)

class HeroInfoView(View):
    def get(self, request):
        #1 get all books
        heros = HeroInfo.objects.all()

        #2 serialize
        s = HeroInfoSerializer(instance=heros, many=True)

        #3 return
        return JsonResponse(s.data, safe=False)

class Viewset(BookInfoModelViewset):
    pass