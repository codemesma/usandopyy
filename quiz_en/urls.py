
try:
    from django.conf.urls import url
except ImportError:
    from django.urls import re_path as url

from django.urls import path

from .views import QuizListView_en, CategoriesListView, \
    ViewQuizListByCategory, QuizUserProgressView, QuizMarkingList, \
    QuizMarkingDetail, QuizDetailView, QuizTake


urlpatterns = [

    path('',QuizListView_en.as_view(),name='quiz_index_en'),

    url(r'^category/$',
        view=CategoriesListView.as_view(),
        name='quiz_category_list_all_en'),

    path('category/<str:slug>/', ViewQuizListByCategory.as_view(), name='quiz_category_list_matching_en'),

    url(r'^progress/$',
        view=QuizUserProgressView.as_view(),
        name='quiz_progress_en'),

    url(r'^marking/$',
        view=QuizMarkingList.as_view(),
        name='quiz_marking_en'),

    url(r'^marking/(?P<pk>[\d.]+)/$',
        view=QuizMarkingDetail.as_view(),
        name='quiz_marking_detail_en'),

    #  passes variable 'quiz_name' to quiz_take view
    url(r'^(?P<slug>[\w-]+)/$',
        view=QuizDetailView.as_view(),
        name='quiz_start_page_en'),

    url(r'^(?P<quiz_name>[\w-]+)/take/$',
        view=QuizTake.as_view(),
        name='quiz_question_en'),
]
