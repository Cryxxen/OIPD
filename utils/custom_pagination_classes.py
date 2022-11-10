from rest_framework.pagination import PageNumberPagination


class CustomPageEightPaginationClass(PageNumberPagination):
    page_size = 8


class CustomPageFivePaginationClass(PageNumberPagination):
    page_size = 5
