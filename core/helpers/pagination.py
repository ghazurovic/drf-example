import typing
from rest_framework import pagination
from rest_framework.response import Response
from django.db.models.query import QuerySet


class StandardResultsSetPagination(pagination.PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 20
    actual_page_size = 5

    def get_paginated_response(
        self,
        data: QuerySet
    ) -> typing.Optional[Response]:
        """Transforms paginated response to more useful one with
        additional keys such as current_page, last_page, total_pages,
        from and to.
        Args:
            data (QuerySet): data
        Returns:
            Response: paginated response
        """
        _page_size_param = self.request.query_params.get('page_size', 5)
        if int(_page_size_param) != self.page_size:
            self.actual_page_size = int(_page_size_param)
        else:
            self.actual_page_size = self.page_size
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'page_size': self.actual_page_size,
            'count': self.page.paginator.count,
            'current_page': self.page.number,
            'last_page': self.page.paginator.num_pages,
            'total_pages': self.page.paginator.num_pages,
            'from': self.calc_from_page(),
            'to': self.calc_to_page(),
            'results': data
        })

    def calc_from_page(self):
        _from_page = self.actual_page_size * self.page.number - \
            (self.actual_page_size - 1)
        if isinstance(_from_page, tuple):
            return _from_page[0]

        return _from_page

    def calc_to_page(self):
        _to_page = int(self.actual_page_size * self.page.number)
        if isinstance(_to_page, tuple):
            _to = _to_page[0] if _to_page[0] < self.page.paginator.count \
                else self.page.paginator.count
            return _to
        _to = _to_page if _to_page < self.page.paginator.count \
            else self.page.paginator.count

        return _to
