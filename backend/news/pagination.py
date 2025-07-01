from rest_framework.pagination import PageNumberPagination

class TopArticalPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'p_s' 
    max_page_size = 10
