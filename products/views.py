from rest_framework import viewsets, status, filters, generics
from rest_framework.permissions import AllowAny, IsAuthenticated
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
        'updated_at'
    )

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view
        requires.
        """
        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = [AllowAny, ]
        else:
            permission_classes = [IsAuthenticated, ]
        return [permission() for permission in permission_classes]
