from django.urls import path
from . import views
from django.urls import path, include

urlpatterns = [
    # banner
    path("banner/", views.banner, name="banner"),
    path("add_banner/", views.add_banner, name="add_banner"),
    path("edit_banner/<int:banner_id>/", views.edit_banner, name="edit_banner"),
    path("update_banner/<int:banner_id>/", views.update_banner, name="update_banner"),
    path("delete_banner/<int:banner_id>/", views.delete_banner, name="delete_banner"),
    # admin_side_search
    path("searchorder/", views.searchorder, name="searchorder"),
]
