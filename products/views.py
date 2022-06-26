import typing
from rest_framework import viewsets, status, filters
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.db.models.functions import Lower
from django.db.models.query import QuerySet
from core.helpers.model_manager import get_unique_or_none
from .models import Product
from .serializers import ProductSerializer
from core.helpers.pagination import StandardResultsSetPagination


class ProductsViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing, creating, editing and deleting Product instances.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = StandardResultsSetPagination

    filter_backends = (
        filters.SearchFilter,
        filters.OrderingFilter
    )

    search_fields = (
        'name',
        'price',
        'rating',
        'updated_at',
    )

    ordering_fields = (
        'name',
        'price',
        'rating',
        'updated_at',
    )

    ordering = ('name', )

    def get_permissions(self) -> typing.List:
        """
        Instantiates and returns the list of permissions that this view
        requires.
        """
        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = [AllowAny, ]
        else:
            permission_classes = [IsAuthenticated, ]
        return [permission() for permission in permission_classes]

    def not_found(self) -> typing.Optional[Response]:
        return Response(
            {'error': 'Product not found.'},
            status=status.HTTP_404_NOT_FOUND
        )

    def get_object(self) -> typing.Optional[Product]:
        return get_unique_or_none(Product, id=self.kwargs.get('pk'))

    def get_ordered_queryset(
        self,
        qs: QuerySet,
        initial_order: str
    ) -> typing.Optional[QuerySet]:
        """Override order queryset to support case insensitive ordering.

        Args:
            qs (QuerySet): _description_
            initial_order (str): initial order to be applied

        Returns:
            QuerySet: sorted QuerySet
        """
        order_by = self.request.query_params.get('ordering')

        if not order_by:
            order_by = initial_order

        if order_by.startswith('-'):
            return sorted(qs.order_by(
                Lower(order_by[1:])),
                key=lambda x: x.__dict__[order_by[1:]].lower(),
                reverse=True
            )
        return qs.order_by(Lower(order_by))

    def list(self, request) -> typing.Optional[QuerySet]:
        """Return list of all products as pagination response or """
        try:
            queryset = self.get_ordered_queryset(
                self.filter_queryset(self.get_queryset()),
                'name'
            )

            page = self.paginate_queryset(queryset)
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)

            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response(
                {'error': e},
                status=status.HTTP_400_BAD_REQUEST
            )
