from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Star
from .serializers import StarListSerializer, StarDetailSerializer, OrderCreateSerializer


class StarListView(APIView):
	def get(self, request):
		stars = Star.objects.filter(available=True)
		serializer = StarListSerializer(stars, many=True, context={"request": request})
		return Response(serializer.data)


class StarDetailView(APIView):
	def get(self, request, slug):
		star = get_object_or_404(Star, slug=slug, available=True)
		serializer = StarDetailSerializer(star, context={"request": request})
		return Response(serializer.data)

	def post(self, request, slug):
		star = get_object_or_404(Star, slug=slug, available=True)
		serializer = OrderCreateSerializer(data=request.data)
		if serializer.is_valid():
			order = serializer.save(price=star.price, star=star)
			order.save()
			return Response(status=201)
		return Response(status=400)
