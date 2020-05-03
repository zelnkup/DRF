from rest_framework import serializers

from .models import Star, Order


class StarListSerializer(serializers.ModelSerializer):
	image_url = serializers.SerializerMethodField()

	class Meta:
		model = Star
		fields = ['id', 'name', 'nickname', 'price', 'image_url', 'slug']

	def get_image_url(self, star):
		request = self.context.get('request')
		image_url = star.image.url
		return request.build_absolute_uri(image_url)


class StarDetailSerializer(serializers.ModelSerializer):
	image_url = serializers.SerializerMethodField()

	class Meta:
		model = Star
		exclude = ('image',)

	def get_image_url(self, star):
		request = self.context.get('request')
		image_url = star.image.url
		return request.build_absolute_uri(image_url)


class OrderCreateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Order
		fields = ['myName', 'description', 'email', 'price']
