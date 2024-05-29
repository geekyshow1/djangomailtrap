from django.urls import path
from myapp.views import home, send_test_email, send_prod_smtp_email, send_prod_api_email
urlpatterns = [
    path('', home, name='home'),
    path('send-test-email/', send_test_email, name='send_test_email'),
    path('send-prod-smtp-email/', send_prod_smtp_email,
         name='send_prod_smtp_email'),
    path('send-prod-api-email/', send_prod_api_email,
         name='send_prod_api_email'),
]
