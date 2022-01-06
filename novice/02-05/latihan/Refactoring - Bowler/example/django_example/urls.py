from django.urls import re_path

from foo import views

urlpatterns = [
    re_path(r"^all/$", views.all_view, name="all"),
    re_path(r"^update/$", views.update_view, name="update"),
    re_path(r"^mark/$", views.mark_view, name="mark"),
    re_path(r"^mark-all/$", views.mark_all_view, name="mark_all"),
    re_path(r"^delete/$", views.delete_view, name="delete"),
    re_path(r"^redirect/(?P<obj_id>[\d]+)/$", views.redirect_view, name="redirect"),
]
