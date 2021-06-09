from .models import FlashCard
from .serializers import FlashCardSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404


# Create your views here.

class FlashCardList(APIView):

    def get(self, request):
        flash_card = FlashCard.objects.all()
        serializer = FlashCardSerializer(flash_card, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FlashCardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FlashCardDetail(APIView):

    def get_object(self, collection_id):
        try:
            return FlashCard.objects.filter(collection_id=collection_id)
        except FlashCard.DoesNotExist:
            raise Http404

    def get(self, request, collection_id):
        flash_card = self.get_object(collection_id)
        serializer = FlashCardSerializer(flash_card, many=True)
        return Response(serializer.data)

    def collection_info(self, collection_id):
        try:
            return FlashCard.objects.filter(pk=collection_id).first()
        except FlashCard.DoesNotExist:
            raise Http404

    def post(self, request, collection_id):
        col_info = self.collection_info(collection_id)
        serializer = FlashCardSerializer(col_info, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FlashCardDetail2(APIView):

    def get_object_two(self, collection_id, id):
        try:
            return FlashCard.objects.get(collection_id=collection_id, pk=id)
        except FlashCard.DoesNotExist:
            raise Http404

    def put(self, request, collection_id, id):
        flash_card = self.get_object_two(collection_id, id)
        serializer = FlashCardSerializer(flash_card, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_200_OK)

    def delete(self, request, collection_id, id):
        flash_card = self.get_object_two(collection_id, id)
        flash_card.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)