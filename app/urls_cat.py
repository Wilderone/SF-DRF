from app.views import CategoryList, CategoryDetail
from django.urls import path

app_name = 'cats'


urlpatterns = [
    path('', CategoryList.as_view(), name='cat-list'),
    path('<int:pk>', CategoryDetail.as_view(), name='cat-detail')
]
