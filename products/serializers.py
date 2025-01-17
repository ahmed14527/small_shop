from rest_framework import serializers
from products.models import Category, Product, ProductReview
from common.serializers import MediaSerializer


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ("image", "lft", "rght", "tree_id", "level")


class ProductListSerializer(serializers.ModelSerializer):
    thumbnail = MediaSerializer(read_only=True)

    class Meta:
        model = Product
        fields = ("id", "name", "price", "category", "in_stock", "brand", "discount", "thumbnail")


class ProductColourListSerializer(serializers.Serializer):
    colour = MediaSerializer(read_only=True)
    id = serializers.IntegerField()


class ProductSizeListSerializer(serializers.Serializer):
    value = serializers.CharField()
    id = serializers.IntegerField()


class AddReviewToProductSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField(write_only=True)
    email = serializers.EmailField(required=True)

    class Meta:
        model = ProductReview
        fields = ('title', 'review', 'rank', 'email', 'product_id')

    def validate(self, attrs):
        rank = attrs.get("rank")
        if rank < 0 or rank > 5:
            raise serializers.ValidationError("Rank must be between 0 and 5")
        return attrs


class ProductReviewUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductReview
        fields = ("title", "review", "rank")