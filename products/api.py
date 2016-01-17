import uuid

import boto3
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from images.models import Image
from products.serializers import ProductsSerializer
from products.models import Product

class ProductsViewSet (ModelViewSet):

    serializer_class = ProductsSerializer
    queryset = Product.objects.filter(active=1)

    def list(self, request, *args, **kwargs):

        latitude_update_string = self.request.query_params.get('latitude', None)
        longitude_update_string = self.request.query_params.get('longitude', None)

        if latitude_update_string is None or longitude_update_string is None:
            products = Product.objects.all()
        else:
            query = "SELECT * " \
                "FROM    products_product   " \
                "WHERE   MBRContains " \
                "( " \
                "LineString(" \
                "Point (" + longitude_update_string + " - 10 / ( 111.1 / COS(RADIANS(" + latitude_update_string + ")))"\
                ", " + latitude_update_string + " - 10 / 111.1)," \
                "Point (" + longitude_update_string + " + 10 / ( 111.1 / COS(RADIANS(" + latitude_update_string + ")))"\
                ", " + latitude_update_string + " + 10 / 111.1)" \
                ")," \
                "Point(longitude,latitude)" \
                ") "
            products = Product.objects.raw(query)

        serializer = self.get_serializer(products, many=True)
        return Response(serializer.data)

    def create(self, request, **kwargs):

        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, **kwargs):

        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():

            product = serializer.save()
            upload_files = request.FILES.getlist('upload_image')

            if upload_files is None or not upload_files:

                return Response({"upload_image": "Not have images"}, status=status.HTTP_400_BAD_REQUEST)

            s3 = boto3.resource('s3')
            bucket = s3.Bucket('walladog')

            for index in range(len(upload_files)):

                uuid_id = uuid.uuid4()
                up_file = upload_files[index]
                key_file = str(uuid_id) + ".jpeg"
                bucket.put_object(ACL='public-read', Key=key_file, Body=up_file, ContentType='image/jpeg')

                photo_url = "https://s3.amazonaws.com/walladog/" + str(uuid_id) + ".jpeg"
                photo_thumbnail_url = "https://s3.amazonaws.com/walladog/" + str(uuid_id) + "thumbnail.jpeg"
                image_product = Image(name=str(uuid_id),
                                      product=product,
                                      photo_url=photo_url,
                                      photo_thumbnail_url=photo_thumbnail_url)
                image_product.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
