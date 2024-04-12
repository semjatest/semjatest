from django.urls import path
from .views import check_email, home,vendor_registration_form, check_driving_license, check_vehicle_number, update_spreadsheet_vendor_vehicle, check_field_executive_email, vendor_vehicle_registration_form, field_executive_vehicle_registration_form, update_spreadsheet_field_executive, vehicle_testing_tool,update_spreadsheet_vendor_registration

urlpatterns = [
    # Define URL patterns for your views
    path('', home, name='home'),
    path('field_executive_vehicle_registration_form/', field_executive_vehicle_registration_form, name='field_executive_vehicle_registration_form'),
    path('vendor_vehicle_registration_form/', vendor_vehicle_registration_form, name='vendor_vehicle_registration_form'),
    path('vendor_registration_form/', vendor_registration_form, name='vendor_registration_form'),
    path('check_email/', check_email, name='check_email'),
    path('update_spreadsheet_field_executive/',update_spreadsheet_field_executive, name='update_spreadsheet_field_executive'),
    path('update_spreadsheet_vendor_registration/', update_spreadsheet_vendor_registration, name='update_spreadsheet_vendor_registration'),
    path('check_field_executive_email/', check_field_executive_email, name='check_field_executive_email'),
    path('check_driving_license/', check_driving_license, name='check_driving_license'),
    path('check_vehicle_number/', check_vehicle_number, name='check_vehicle_number'),
    path('update_spreadsheet_vendor_vehicle/', update_spreadsheet_vendor_vehicle, name='update_spreadsheet_vendor_vehicle'),
    path('vehicle_testing_tool/', vehicle_testing_tool, name='vehicle_testing_tool'),
]

