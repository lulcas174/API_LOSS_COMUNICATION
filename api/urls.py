from django.urls import path, include

app_name = 'api'

urlpatterns = [
    path('comunicacao-perda/', include('comunicacao_perda.api.urls'), name='comunicacao-perda')
]
