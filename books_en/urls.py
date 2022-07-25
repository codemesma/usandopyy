
from django.urls import path
from .views import BooksListView,BooksCategoryView, BooksDetailView, BookCheckoutView,paymentComplete, SearchResultsListView


urlpatterns = [
    path('', BooksListView.as_view(), name = 'list_en'),
    path('<str:slug>/', BooksDetailView.as_view(), name = 'detail_en'),
    path('categoria/<str:slug>/', BooksCategoryView.as_view(), name='book_cat_en'),
    path('<int:pk>/checkout/', BookCheckoutView.as_view(), name = 'checkout_en'),
    path('complete/', paymentComplete, name = 'complete_en'),
    path('search/', SearchResultsListView.as_view(), name = 'search_results_en'),
]