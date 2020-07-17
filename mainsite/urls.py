from django.urls import path
from .views import LinkmanListView, LinkmanDetailView, LinkmanCreateView, LinkmanUpdateView, LinkmanDeleteView

urlpatterns = [
    # 列表
    path('', LinkmanListView.as_view(), name='list'),
    # 詳細
    path('detail/<int:pk>/', LinkmanDetailView.as_view(), name='detail'),
    # 建立
    path('create/', LinkmanCreateView.as_view(), name='create'),
    # 更新
    path('update/<int:pk>/', LinkmanUpdateView.as_view(), name='update'),
    # 刪除
    path('delete/<int:pk>/', LinkmanDeleteView.as_view(), name='delete'),
]