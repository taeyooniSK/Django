from django.urls import path  # path는 장고의 함수
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    # <int:pk> 장고가 정수값을 기대하고 pk라는 변수로 뷰로 전송하는 것을 말함
    # 예) http://127.0.0.1:8000/post/5 라고 입력하면 장고는 post_detail 뷰를 찾아 매개변수 pk가 5인 값을 뷰로 전달
    path('post/<int:pk>/', views.post_detail, name='post_detail'), # views.post_detail이라는 뷰를 post_detail이라는 이름을 부텨서 URL법칙을 만든거고
    # 그 말은, 장고가 post_detail이라는 이름을 해석할 때 blog/views.py 파일 내부의 post_detail이라는 뷰 함수로 이해하도록 해줌
]
