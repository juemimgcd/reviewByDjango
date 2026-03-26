from django.urls import path

from history import views

urlpatterns = [
    path("api/history/add", views.HistoryAddAPIView.as_view(), name="history-add"),
    path("api/history/list", views.HistoryListAPIView.as_view(), name="history-list"),
    path("api/history/delete/<int:history_id>", views.HistoryDeleteAPIView.as_view(), name="history-delete"),
    path("api/history/clear", views.HistoryClearAPIView.as_view(), name="history-clear"),
]
