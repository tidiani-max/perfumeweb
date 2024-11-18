from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import owner_signup, OwnerLoginView,perfume_detail, add_perfume, edit_perfume, delete_perfume, testimony
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views

urlpatterns = [
path('', views.index, name='index'),

path('owner/signup/', owner_signup, name='owner_signup'),
path('owner/login/', OwnerLoginView.as_view(), name='login'),
path('logout/', LogoutView.as_view(), name='logout'),

path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

path('products', views.products, name='products'),
path('products/perfume/<int:perfume_id>/', perfume_detail, name='perfume_detail'),
path('products/add/', add_perfume, name='add_perfume'),
path('products/edit/<int:pk>/', edit_perfume, name='edit_perfume'),
path('products/delete/<int:pk>/', delete_perfume, name='delete_perfume'),
path('testimony', testimony, name='testimony'),


path('about', views.about, name='about'),
path('blog', views.blog, name='blog'),
path('contact_us', views.contact_us, name='contact_us'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)