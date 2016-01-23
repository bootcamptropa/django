import uuid
import boto3
from boto3.session import Session
from django.contrib.gis.geos import LineString, Point

from django.shortcuts import get_object_or_404
from math import cos, radians
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from images.models import Image
from products.permissions import ProductPermission, UserProductPermission
from products.serializers import ProductsSerializer, ProductsListSerializer
from products.models import Product

class ProductsViewSet (ModelViewSet):

    permission_classes = [ProductPermission]
    serializer_class = ProductsSerializer
    queryset = Product.objects.filter(active=1)

    def list(self, request, *args, **kwargs):

        latitude_update_string = self.request.query_params.get('lat', None)
        longitude_update_string = self.request.query_params.get('lon', None)

        category_id_filter = self.request.query_params.get('category', None)
        race_id_filter = self.request.query_params.get('race', None)
        state_id_filter = self.request.query_params.get('state', None)

        if latitude_update_string is not None and longitude_update_string is not None:

            lon1 = float(longitude_update_string) - 10 / (111.1 / cos(radians(float(latitude_update_string))))
            lat1 = float(latitude_update_string) - 10 / 111.1

            lon2 = float(longitude_update_string) + 10 / (111.1 / cos(radians(float(latitude_update_string))))
            lat2 = float(latitude_update_string) + 10 / 111.1

            line_string = 'LINESTRING (' + str(lat1) + ' ' + str(lon1) + ', ' + str(lat2) + ' ' + str(lon2) + ')'
            queryset = Product.objects.filter(location__contained=line_string).filter(active=1)
        else:
            queryset = Product.objects.filter(active=1)

        if race_id_filter is not None:
            queryset = queryset.filter(race=race_id_filter)

        if state_id_filter is not None:
            queryset = queryset.filter(state=category_id_filter)

        if category_id_filter is not None:
            queryset = queryset.filter(category=category_id_filter)

        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = ProductsListSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = ProductsListSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):

        queryset = self.filter_queryset(self.get_queryset())
        product = get_object_or_404(queryset, pk=pk)
        serializer = ProductsListSerializer(product)
        return Response(serializer.data)

    def create(self, request, **kwargs):

        serializer = self.get_serializer(data=request.data)

        latitude = self.request.POST.get('latitude', None)
        longitude = self.request.POST.get('longitude', None)

        if serializer.is_valid():

            upload_files = request.FILES.getlist('upload_image')

            if upload_files is None or not upload_files:
                return Response({"upload_image": "Not have images"}, status=status.HTTP_400_BAD_REQUEST)

            if latitude is None:
                return Response({"latitude": "Not have latitude"}, status=status.HTTP_400_BAD_REQUEST)

            if longitude is None:
                return Response({"longitude": "Not have longitude"}, status=status.HTTP_400_BAD_REQUEST)

            product = serializer.save(seller=request.user.userdetail,location=Point(float(latitude), float(longitude)))

            session = Session(aws_access_key_id='AKIAJYDV7TEBJS6JWEEQ',
                  aws_secret_access_key='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')

            s3 = session.resource('s3')
            bucket = s3.Bucket('walladog')

            for index in range(len(upload_files)):

                uuid_id = uuid.uuid4()
                up_file = upload_files[index]
                key_file = str(uuid_id) + ".jpeg"
                bucket.put_object(ACL='public-read', Key=key_file, Body=up_file, ContentType='image/jpeg')

                photo_url = "https://s3.amazonaws.com/walladog/" + str(uuid_id) + ".jpeg"
                photo_thumbnail_url = "https://s3.amazonaws.com/walladog/thumbnails/" + str(uuid_id) + ".png"
                image_product = Image(name=str(uuid_id),
                                      product=product,
                                      photo_url=photo_url,
                                      photo_thumbnail_url=photo_thumbnail_url)
                image_product.save()

            serialize_list = ProductsListSerializer(product)

            return Response(serialize_list.data, status=status.HTTP_201_CREATED)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserProductsViewSet (ModelViewSet):

    permission_classes = [UserProductPermission]
    serializer_class = ProductsListSerializer
    queryset = Product.objects.filter(active=1)

    def list(self, request, *args, **kwargs):

        category_id_filter = self.request.query_params.get('category', None)
        race_id_filter = self.request.query_params.get('race', None)
        state_id_filter = self.request.query_params.get('state', None)

        queryset = self.filter_queryset(self.get_queryset()).filter(seller=self.request.user.id)

        if race_id_filter is not None:
            queryset = queryset.filter(race=race_id_filter)

        if state_id_filter is not None:
            queryset = queryset.filter(state=category_id_filter)

        if category_id_filter is not None:
            queryset = queryset.filter(category=category_id_filter)

        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = ProductsListSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = ProductsListSerializer(queryset, many=True)
        return Response(serializer.data)