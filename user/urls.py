from django.urls import path
from . import views

app_name='user'                                                      # 프로잭트 내에서 URL패턴의 이름 충돌을 방지하기 위해서 애플리케이션의 이름을 정의

urlpatterns = [
    path('', views.index, name='index'),

]