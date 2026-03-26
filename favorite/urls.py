from django.urls import path

from favorite import views

urlpatterns = [
    path("api/favorite/check", views.FavoriteCheckAPIView.as_view(), name="favorite-check"),
    path("api/favorite/add", views.FavoriteAddAPIView.as_view(), name="favorite-add"),
    path("api/favorite/remove", views.FavoriteRemoveAPIView.as_view(), name="favorite-remove"),
    path("api/favorite/list", views.FavoriteListAPIView.as_view(), name="favorite-list"),
    path("api/favorite/clear", views.FavoriteClearAPIView.as_view(), name="favorite-clear"),
]
