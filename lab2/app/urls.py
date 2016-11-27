from django.conf.urls import url
from . import controllers

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^product-add', controllers.productAdd),
    url(r'^department-add', controllers.departmentAdd),
    url(r'^producter-add', controllers.producterAdd),
    url(r'^product-add', controllers.productAdd),

    url(r'^product-update', controllers.productUpdate),
    url(r'^department-update', controllers.departmentUpdate),
    url(r'^product-update', controllers.productUpdate),

    url(r'^product-del', controllers.productDelete),
    url(r'^department-del', controllers.departmentDelete),
    url(r'^producter-del', controllers.producterDelete),
    url(r'^product-del', controllers.productDelete),

    url(r'^products', controllers.products),
    url(r'^producters', controllers.producters),
    url(r'^products', controllers.products),
    url(r'^departments', controllers.departments),
    url(r'^$', controllers.index)
]