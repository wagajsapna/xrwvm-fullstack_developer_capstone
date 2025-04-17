# Uncomment the imports before you add the code
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
from .restapis import get_request, analyze_review_sentiments, post_review
app_name = 'djangoapp'
urlpatterns = [
    path(route='get_cars', view=views.get_cars, name ='getcars'),

    # # path for registration
    path('register', views.registration, name='registration'),

    # path for login
    path(route='login', view=views.login_user, name='login'),
    
    # path for logout
    path('logout', views.logout_request, name='logout'),

    path('get_dealers/', views.get_dealerships, name='get_dealers'),
       path('get_dealers/<str:state>', views.get_dealerships, name='get_dealers_by_state'),
    path('dealer/<int:dealer_id>', views.get_dealer_details, name='dealer_details'),
    path('reviews/dealer/<int:dealer_id>', views.get_dealer_reviews, name='dealer_reviews'),
    path(route='add_review', view=views.add_review, name='add_review'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
