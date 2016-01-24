from django.db.models import Q
from django.shortcuts import get_object_or_404
from products.models import Product
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from transactions.models import Transaction
from transactions.permissions import TransactionPermission
from transactions.serializers import TransactionsListSerializer
from transactions.serializers import TransactionsSerializer


class TransactionsViewSet(GenericViewSet):

    serializer_class = TransactionsSerializer
    permission_classes = (TransactionPermission,)

    def list(self, request):

        queryset = Transaction.objects.filter(Q(buyer=self.request.user) | Q(seller=self.request.user))
        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = TransactionsListSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = TransactionsListSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):

        serializer = self.get_serializer(data=request.data)

        product = get_object_or_404(Product, pk=request.data['product'])

        if serializer.is_valid():

            transaction_save = serializer.save(buyer=self.request.user, seller=product.seller.user)
            serialize_list = TransactionsListSerializer(transaction_save)
            return Response(serialize_list.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk):

        transaction = get_object_or_404(Transaction, pk=pk)
        self.check_object_permissions(request, transaction)
        serializer = TransactionsListSerializer(transaction)

        return Response(serializer.data)

    def get_paginated_response(self, data):

        assert self.paginator is not None
        return self.paginator.get_paginated_response(data)