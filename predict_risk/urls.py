from django.conf.urls import url
from . import views
app_name='predict'
urlpatterns=[
url(r'^(?P<pk>\d+)$',views.PredictRisk,name='predict')
]
