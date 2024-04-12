from django.urls import path, include

urlpatterns = [
    # Other URL patterns for your project...
    path('', include('vendorapp.urls')),  # Include vendorapp URLs at the root URL
]
