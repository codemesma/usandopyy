
from django.urls import path
from .views import BooksListView,BooksCategoryView, BooksDetailView, BookCheckoutView, DownloadBook, paymentComplete, SearchResultsListView


urlpatterns = [
    path('', BooksListView.as_view(), name = 'list'),
    path('<str:slug>/', BooksDetailView.as_view(), name = 'detail'),
    path('categoria/<str:slug>/', BooksCategoryView.as_view(), name='book_cat'),
    path('<int:pk>/checkout/', BookCheckoutView.as_view(), name = 'checkout'),
    path('complete/', paymentComplete, name = 'complete'),
    path('search/', SearchResultsListView.as_view(), name = 'search_results'),
]