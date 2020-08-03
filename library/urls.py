from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name='library'
urlpatterns = [
    path('cateview/<int:category_id>',views.cate_view, name="view"),
    path('index/',views.index, name="index"),
]