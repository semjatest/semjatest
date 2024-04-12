
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

@csrf_exempt
def check_email(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            try:
                scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
                credentials = ServiceAccountCredentials.from_json_keyfile_name('credential/key.json', scope)
                client = gspread.authorize(credentials)
                spreadsheet = client.open('Test sheet')  # Update with your spreadsheet name
                worksheet = spreadsheet.get_worksheet(0)  # Assuming data is in the first worksheet
                column_names = worksheet.row_values(1)  # Assuming headings are in the first row
                vendor_info_column_index = column_names.index("Vendor Info") + 1  # Find column index of "Vendor Info"
                vendor_name_column_index = column_names.index("Vendor Name") + 1  # Find column index of "Vendor Name"
                
                cells = worksheet.findall(email)  # Find all cells containing the email
                
                if cells:  # If cells are found
                    for cell in cells:
                        # Check if the found cell is in the "Vendor Info" column
                        if cell.col == vendor_info_column_index:
                            name = worksheet.cell(cell.row, vendor_name_column_index).value
                            return JsonResponse({'found': True, 'name': name})
                
                # If the email is not found in the "Vendor Info" column, return "Vendor not found"
                return JsonResponse({'found': False, 'name': 'Vendor not found'})
                
            except Exception as e:
                # If there's any error, return "Vendor not found"
                return JsonResponse({'found': False, 'name': 'Vendor not found'})
    
    # If email is not provided in the POST request, return an error response
    return JsonResponse({'error': 'Email not provided'}, status=400)


@csrf_exempt
def check_field_executive_email(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            try:
                scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
                credentials = ServiceAccountCredentials.from_json_keyfile_name('credential/key.json', scope)
                client = gspread.authorize(credentials)
                spreadsheet = client.open('Test sheet')  # Update with your spreadsheet name
                worksheet = spreadsheet.get_worksheet(0)  # Assuming data is in the first worksheet
                column_names = worksheet.row_values(1)  # Assuming headings are in the first row
                exec_info_column_index = column_names.index("Field Executive Info") + 1  # Find column index of "Field Executive Info"
                exec_name_column_index = column_names.index("Field Executive Name") + 1  # Find column index of "Field Executive Name"
                
                cells = worksheet.findall(email)  # Find all cells containing the email
                
                if cells:  # If cells are found
                    for cell in cells:
                        # Check if the found cell is in the "Field Executive Info" column
                        if cell.col == exec_info_column_index:
                            name = worksheet.cell(cell.row, exec_name_column_index).value
                            return JsonResponse({'found': True, 'name': name})
                
                # If the email is not found in the "Field Executive Info" column, return "Field Executive not found"
                return JsonResponse({'found': False, 'name': 'Field Executive not found'})
                
            except Exception as e:
                # If there's any error, return "Field Executive not found"
                return JsonResponse({'found': False, 'name': 'Field Executive not found'})
    
    # If email is not provided in the POST request, return an error response
    return JsonResponse({'error': 'Email not provided'}, status=400)






from django.http import JsonResponse
from oauth2client.service_account import ServiceAccountCredentials
import gspread

@csrf_exempt
def check_driving_license(request):
    if request.method == 'POST':
        driving_license = request.POST.get('driving_license')
        if driving_license:
            try:
                scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
                credentials = ServiceAccountCredentials.from_json_keyfile_name('credential/key.json', scope)
                client = gspread.authorize(credentials)
                spreadsheet = client.open('Test sheet')  # Update with your spreadsheet name
                worksheet = spreadsheet.get_worksheet(0)  # Assuming data is in the first worksheet
                driving_license_column = worksheet.col_values(8)  # Assuming driving license is in the eighth column
                row_index = None
                if driving_license in driving_license_column:
                    row_index = driving_license_column.index(driving_license) + 1  # Index starts from 1
                    onboard_status = worksheet.cell(row_index, 9).value  # Assuming onboard status is in the ninth column
                    return JsonResponse({'found': True, 'onboard_status': onboard_status})
                else:
                    return JsonResponse({'found': False, 'message': 'New driving license'})
            except Exception as e:
                return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({'error': 'Invalid request'}, status=400)


from django.http import JsonResponse
from oauth2client.service_account import ServiceAccountCredentials
import gspread

@csrf_exempt
def check_vehicle_number(request):
    if request.method == 'POST':
        vehicle_number = request.POST.get('vehicle_number')
        if vehicle_number:
            try:
                scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
                credentials = ServiceAccountCredentials.from_json_keyfile_name('credential/key.json', scope)
                client = gspread.authorize(credentials)
                spreadsheet = client.open('Test sheet')  # Update with your spreadsheet name
                worksheet = spreadsheet.get_worksheet(0)  # Assuming data is in the first worksheet
                vehicle_number_column = worksheet.col_values(10)  # Assuming vehicle number is in the eighth column
                row_index = None
                if vehicle_number in vehicle_number_column:
                    row_index = vehicle_number_column.index(vehicle_number) + 1  # Index starts from 1
                    current_status = worksheet.cell(row_index, 11).value  # Assuming current status is in the eleventh column
                    return JsonResponse({'found': True, 'current_status': current_status})
                else:
                    return JsonResponse({'found': False, 'message': 'New vehicle'})
            except Exception as e:
                return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({'error': 'Invalid request'}, status=400)





@csrf_exempt
def update_spreadsheet_vendor_vehicle(request):
    if request.method == 'POST':
        # Extract data from the POST request
        email = request.POST.get('email')
        vendor_name = request.POST.get('vendorname')  # Modified to 'vendorname' as per your description
        driving_license = request.POST.get('drivinglicense')
        onboard_status = "Registered"  # Assuming onboard status is always "Registered" upon submission
        vehicle_number = request.POST.get('vehiclenumber')
        current_status = "Waiting for Approval"  # Assuming current status is always "Waiting for Approval" upon submission
        vehicle_type = request.POST.get('userjob')
        partner_name = request.POST.get('partnername')
        partner_number = request.POST.get('mobileno')
        comments = request.POST.get('comment')

        try:
            # Authenticate with Google Sheets
            scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
            credentials = ServiceAccountCredentials.from_json_keyfile_name('credential/key.json', scope)
            client = gspread.authorize(credentials)
            spreadsheet = client.open('Test sheet')  # Update with your spreadsheet name
            worksheet = spreadsheet.get_worksheet(0)  # Assuming data is in the first worksheet

            # Get today's date and time
            today = datetime.now().strftime(" %d-%m-%Y-%A")
            current_time = datetime.now().strftime("%I:%M:%S %p")

            # Assuming you have already authenticated and obtained the 'worksheet' object
            column_values = worksheet.col_values(1)  # Retrieve values from column 1 (assuming the serial number is in column 1)
            row_count = len(column_values)  # Get the total number of rows, including the header row
            if row_count > 0:
               row_count -= 1  # Subtract 1 to exclude the header row
            row_count += 1  # Increment by 1 to get the next row number
            
            # Find the row index of the email in the spreadsheet
            email_cell = worksheet.find(email)
            row_index = email_cell.row

            # Fetch the vendor name from the spreadsheet based on the row index
            vendor_name = worksheet.cell(row_index, 5).value  # Assuming vendor name is in the second column

            # Prepare the row data
            row = [row_count, today, current_time, email, vendor_name,'','', driving_license, onboard_status, vehicle_number, current_status, vehicle_type, partner_name,partner_number, comments]

            # Append the row to the spreadsheet starting from the third column (index 2)
            worksheet.append_row(row, value_input_option='RAW', insert_data_option='INSERT_ROWS', table_range="A:Z")

            # Return a success response
            return JsonResponse({'message': 'Data updated successfully'})
        except Exception as e:
            # Return an error response if any error occurs
            return JsonResponse({'error': str(e)}, status=500)
    else:
        # Return an error response if the request method is not POST
        return JsonResponse({'error': 'Invalid request method'}, status=405)
    
    
    
    
    
    
    
@csrf_exempt
def update_spreadsheet_field_executive(request):
    if request.method == 'POST':
        # Extract data from the POST request
        email = request.POST.get('email')
        exec_name = request.POST.get('fieldexecutivename')  # Modified to 'vendorname' as per your description
        driving_license = request.POST.get('drivinglicense')
        onboard_status = "Registered"  # Assuming onboard status is always "Registered" upon submission
        vehicle_number = request.POST.get('vehiclenumber')
        current_status = "Waiting for Approval"  # Assuming current status is always "Waiting for Approval" upon submission
        vehicle_type = request.POST.get('userjob')
        partner_name = request.POST.get('partnername')
        partner_number = request.POST.get('mobileno')
        comments = request.POST.get('comment')

        try:
            # Authenticate with Google Sheets
            scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
            credentials = ServiceAccountCredentials.from_json_keyfile_name('credential/key.json', scope)
            client = gspread.authorize(credentials)
            spreadsheet = client.open('Test sheet')  # Update with your spreadsheet name
            worksheet = spreadsheet.get_worksheet(0)  # Assuming data is in the first worksheet

            # Get today's date and time
            today = datetime.now().strftime(" %d-%m-%Y-%A")
            current_time = datetime.now().strftime("%I:%M:%S %p")

            # Assuming you have already authenticated and obtained the 'worksheet' object
            column_values = worksheet.col_values(1)  # Retrieve values from column 1 (assuming the serial number is in column 1)
            row_count = len(column_values)  # Get the total number of rows, including the header row
            if row_count > 0:
               row_count -= 1  # Subtract 1 to exclude the header row
            row_count += 1  # Increment by 1 to get the next row number
            
            # Find the row index of the email in the spreadsheet
            email_cell = worksheet.find(email)
            row_index = email_cell.row

            # Fetch the vendor name from the spreadsheet based on the row index
            exec_name = worksheet.cell(row_index, 7).value  # Assuming vendor name is in the second column

            # Prepare the row data
            row = [row_count, today, current_time, '','', email, exec_name, driving_license, onboard_status, vehicle_number, current_status, vehicle_type, partner_name,partner_number, comments]

            # Append the row to the spreadsheet starting from the third column (index 2)
            worksheet.append_row(row, value_input_option='RAW', insert_data_option='INSERT_ROWS', table_range="A:Z")

            # Return a success response
            return JsonResponse({'message': 'Data updated successfully'})
        except Exception as e:
            # Return an error response if any error occurs
            return JsonResponse({'error': str(e)}, status=500)
    else:
        # Return an error response if the request method is not POST
        return JsonResponse({'error': 'Invalid request method'}, status=405)    
    
    
    
    
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseUpload
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from io import BytesIO
# from googleapiclient.http import MediaFileUpload

def save_and_get_url(file, folder_id):
    # Authenticate with Google Drive
    scopes = ['https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('credential/key.json', scopes)
    service = build('drive', 'v3', credentials=credentials)

    # Create a file in Google Drive
    file_metadata = {
        'name': file.name,  # Set the name of the file in Google Drive to the original filename
        'parents': [folder_id],  # Use the folder ID retrieved based on the folder name
    }
    
    # Use BytesIO to read the file content
    file_contents = BytesIO(file.read())
    
    # Create a media object from the file content
    media = MediaIoBaseUpload(file_contents, mimetype=file.content_type)
    
    # Upload the file
    uploaded_file = service.files().create(body=file_metadata, media_body=media, fields='id, webContentLink').execute()

    # Get the file URL
    file_url = uploaded_file.get('webContentLink')

    return file_url

# Folder ID in Google Drive
folder_id = '1LkBwQkviixP7zsmTKXJ7VsIMCZXALQVy'

@csrf_exempt
def update_spreadsheet_vendor_registration(request):
    if request.method == 'POST':
        # Extract data from the POST request
        email = request.POST.get('vendoremail')
        vendor_office_name = request.POST.get('vendoroffice')
        vendor_pan_name = request.POST.get('vendorpanname')
        vendor_contact = request.POST.get('mobilenumber')
        bank_account_copy_front = request.FILES.get('bankAccountCopy1')
        # bank_account_copy_back = request.FILES.get('bankAccountCopy2')
        bank_account_number = request.POST.get('bankaccount')
        bank_ifsc_code = request.POST.get('ifsccode')
        gst_number = request.POST.get('gst_value') 
        gst_office = request.POST.get('address')
        adhar_number = request.POST.get('adhar')
        pancard_copy_front = request.FILES.get('pancardcopy1')
        # pancard_copy_back = request.FILES.get('pancardcopy2')
        pancard_number = request.POST.get('pannumber')
        registered_address = request.POST.get('address')
        credit_period = request.POST.get('days')
        
        # Save files to Google Drive and get file URLs
        bank_account_copy_front_url = save_and_get_url(bank_account_copy_front, folder_id)
        # bank_account_copy_back_url = save_and_get_url(bank_account_copy_back, folder_id)
        pancard_copy_front_url = save_and_get_url(pancard_copy_front, folder_id)
        # pancard_copy_back_url = save_and_get_url(pancard_copy_back, folder_id)

        try:
            # Authenticate with Google Sheets
            scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
            credentials = ServiceAccountCredentials.from_json_keyfile_name('credential/key.json', scope)
            client = gspread.authorize(credentials)
            spreadsheet = client.open('Test sheet')  # Update with your spreadsheet name
            worksheet = spreadsheet.get_worksheet(1)  # Assuming data is in the first worksheet

            # Get today's date and time
            today = datetime.now().strftime(" %d-%m-%Y-%A")
            current_time = datetime.now().strftime("%I:%M:%S %p")

            # Assuming you have already authenticated and obtained the 'worksheet' object
            column_values = worksheet.col_values(1)  # Retrieve values from column 1 (assuming the serial number is in column 1)
            row_count = len(column_values)  # Get the total number of rows, including the header row
            if row_count > 0:
               row_count -= 1  # Subtract 1 to exclude the header row
            row_count += 1  # Increment by 1 to get the next row number


            row = [row_count, today, current_time, email, vendor_office_name, vendor_pan_name, vendor_contact, bank_account_copy_front_url,
                   bank_account_number, bank_ifsc_code, gst_number,gst_office, adhar_number, pancard_copy_front_url,
                   pancard_number, registered_address, credit_period]

            # Append the row to the spreadsheet starting from the second column (index 1)
            worksheet.append_row(row, value_input_option='USER_ENTERED', insert_data_option='INSERT_ROWS',
                                  table_range="A:Z")

            # Return a success response
            return JsonResponse({'message': 'Data updated successfully'})
        except Exception as e:
            # Return an error response if any error occurs
            return JsonResponse({'error': str(e)}, status=500)
    else:
        # Return an error response if the request method is not POST
        return JsonResponse({'error': 'Invalid request method'}, status=405)



    
    
  

   



from django.shortcuts import render
def home(request):
    return render(request, 'index.html')

def vendor_vehicle_registration_form(request):
    return render(request, 'vendor_vehicle_registration_form.html')

def field_executive_vehicle_registration_form(request):
    return render(request, 'field_executive_vehicle_registration_form.html')

def vehicle_testing_tool(request):
    return render(request, 'vehicle_testing_tool.html')

def vendor_registration_form(request):
    return render(request, 'vendor_registration_form.html')

def csrf_failure_view(request, reason=""):
    # Custom logic for CSRF failure handling
    return render(request, 'csrf_failure.html', {'reason': reason})


