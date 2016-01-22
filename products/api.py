import uuid
import boto3

from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from images.models import Image
from products.permissions import ProductPermission
from products.serializers import ProductsSerializer, ProductsListSerializer
from products.models import Product

class ProductsViewSet (ModelViewSet):

    permission_classes = [ProductPermission]
    serializer_class = ProductsSerializer
    queryset = Product.objects.filter(active=1)

    def list(self, request, *args, **kwargs):

        latitude_update_string = self.request.query_params.get('latitude', None)
        longitude_update_string = self.request.query_params.get('longitude', None)


        # lon1 = float(longitude_update_string) - 10 / ( 111.1 / cos(radians(float(latitude_update_string))) )
        # lat1 = float(latitude_update_string) - 10  / 111.1
        #
        # lon2 = float(longitude_update_string) + 10 / ( 111.1 / cos(radians(float(latitude_update_string))) )
        # lat2 = float(latitude_update_string) + 10  / 111.1
        #
        # line_string = LineString(Point(lat1, lon1), Point(lat2, lon2))
        # queryset = Product.objects.filter(location__contains=line_string)
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = ProductsListSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):

        queryset = self.filter_queryset(self.get_queryset())
        product = get_object_or_404(queryset, pk=pk)
        serializer = ProductsListSerializer(product)
        return Response(serializer.data)

    def create(self, request, **kwargs):

        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():

            upload_files = request.FILES.getlist('upload_image')

            if upload_files is None or not upload_files:
                return Response({"upload_image": "Not have images"}, status=status.HTTP_400_BAD_REQUEST)

            product = serializer.save(seller=request.user.userdetail)

            s3 = boto3.resource('s3')
            bucket = s3.Bucket('walladog')

            for index in range(len(upload_files)):

                uuid_id = uuid.uuid4()
                up_file = upload_files[index]
                key_file = str(uuid_id) + ".jpeg"
                bucket.put_object(ACL='public-read', Key=key_file, Body=up_file, ContentType='image/jpeg')

                photo_url = "https://s3.amazonaws.com/walladog/" + str(uuid_id) + ".jpeg"
                photo_thumbnail_url = "https://s3.amazonaws.com/walladog/" + str(uuid_id) + "-thumbnail.jpeg"
                image_product = Image(name=str(uuid_id),
                                      product=product,
                                      photo_url=photo_url,
                                      photo_thumbnail_url=photo_thumbnail_url)
                image_product.save()

            serialize_list = ProductsListSerializer(product)

            return Response(serialize_list.data, status=status.HTTP_201_CREATED)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
