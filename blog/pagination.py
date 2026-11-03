from django.core.paginator import Paginator

POST_PER_PAGE = 6
def paginate_queryset(request, queryset, per_page = POST_PER_PAGE):
    paginator = Paginator(queryset, per_page)
    page_number = request.GET.get("page")

    return paginator.get_page(page_number)