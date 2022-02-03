from rest_framework import serializers
from .models import Shop, Donut


class ShopSerializer(serializers.HyperlinkedModelSerializer):
    donuts = serializers.HyperlinkedRelatedField(
        view_name='dunut_detail',
        many=True,
        read_only=True
    )
    shop_url = serializers.ModelSerializer.serializer_url_field(
        view_name='shop_detail'
    )

    class Meta:
        model = Shop
        fields = ('id', 'shop_url', 'name',
                  'location', 'photo_url', 'donuts',)


class DonutSerializer(serializers.HyperlinkedModelSerializer):
    shop = serializers.HyperlinkedRelatedField(
        view_name='shop_detail',
        read_only=True
    )

    shop_id = serializers.PrimaryKeyRelatedField(
        queryset=Shop.objects.all(),
        source='shop'
    )

    class Meta:
        model = Donut
        fields = ('id', 'shop', 'shop_id', 'name', 'details', 'image_url')
