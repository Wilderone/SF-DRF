from rest_framework import serializers
from app.models import Post, Category
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']


class CategorySerializer(serializers.ModelSerializer):

    posts = serializers.StringRelatedField(many=True)

    class Meta:
        model = Category
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(required=False)

    class Meta:
        model = Post
        fields = '__all__'

    # def create(self, validated_data):
    #     return Post(**validated_data)

    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.slug = validated_data.get('slug', instance.slug)
    #     instance.status = validated_data.get('status', instance.status)
    #     instance.content = validated_data.get('content', instance.content)
    #     instance.updated = validated_data.get('updated', instance.updated)
    #     instance.publication_date = validated_data.get(
    #         'publication_date', instance.publication_date)
    #     return instance
