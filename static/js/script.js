function ValidateEmailInfo(url) {
    var vendorEmail = $('#vendoremail').val();

    if (!vendorEmail) {
        $('#vendorname').text('Please enter an email to validate.').css('color', 'red');
        return;
    }

    $.ajax({
        type: 'POST',
        url: url,
        data: {'email': vendorEmail},  // Modify data accordingly
        success: function(response) {
            var vendorNameElement = $('#vendorname');
            if (response.found) {
                vendorNameElement.text(response.name);
                vendorNameElement.css('color', 'green'); // Change text color to green
                $('#license').css('display', 'block');
            } else {
                vendorNameElement.text('Vendor not found');
                vendorNameElement.css('color', 'red'); // Change text color to red
                $('#license').css('display', 'none');
            }
            // Additional logic can be added here based on your requirements
        },
        error: function(xhr, status, error) {
            console.error(xhr.responseText);
            alert('Error: ' + xhr.responseText);
        }
    });
}



function editEmail() {
    console.log('editEmail function called');

    // Hide the next fieldset
    document.getElementById('license').style.display = 'none';
    document.getElementById('vehicleno').style.display = 'none';
    document.getElementById('selecttype').style.display = 'none';
    document.getElementById('partnerreg').style.display = 'none';
    document.getElementById('submitBtn').style.display = 'none';

    // Clear input fields
    document.getElementById('vendoremail').value = '';
    document.getElementById('drivinglicense').value = '';
    document.getElementById('vehiclenumber').value = '';
    document.getElementById('job').selectedIndex = 0;
    document.getElementById('partnername').value = '';
    document.getElementById('comment').value = '';

    // Set the text color of the vendorname span to red
    $('#vendorname').text('Please Enter your Email').css('color', 'red'); // Set text color to red

    console.log('Input fields cleared');
}

function editEmail1() {
    console.log('editEmail function called');

    // Clear input fields
    document.getElementById('vendoremail').value = '';

    // Set the text color of the vendorname span to red
    $('#vendorname').text('Please Enter your Email').css('color', 'red'); // Set text color to red

    console.log('Input fields cleared');
}






function FieldExecutiveEmailInfo(url) {
    var execEmail = $('#emailfieldexecutive').val();

    if (!execEmail) {
        $('#fieldexecutivename').text('Please enter an email to validate.').css('color', 'red');
        return;
    }

    $.ajax({
        type: 'POST',
        url: url, // Update the URL if necessary
        data: {'email': execEmail},  // Corrected to match the parameter name expected by the backend
        success: function(response) {
            var fieldExecutiveNameElement = $('#fieldexecutivename');
            if (response.found) {
                fieldExecutiveNameElement.text(response.name).css('color', 'green'); // Set text color to green for "Found"
                $('#license').css('display', 'block');
            } else {
                fieldExecutiveNameElement.text('Field Executive not found').css('color', 'red'); // Set text color to red for "Not found"
                $('#license').css('display', 'none');
            }
            // Additional logic can be added here based on your requirements
        },
        error: function(xhr, status, error) {
            console.error(xhr.responseText);
            alert('Error: ' + xhr.responseText);
        }
    });
}



// Function to clear input fields and call VendorEmailInfo function
function editEmailFieldExecutive() {
    console.log('editEmailFieldExecutive function called');

    // Hide the next fieldset
    document.getElementById('license').style.display = 'none';
    document.getElementById('vehicleno').style.display = 'none';
    document.getElementById('selecttype').style.display = 'none';
    document.getElementById('partnerreg').style.display = 'none';
    document.getElementById('submitBtn').style.display = 'none';

    // Clear input fields
    document.getElementById('emailfieldexecutive').value = '';
    document.getElementById('drivinglicense').value = '';
    document.getElementById('vehiclenumber').value = '';
    document.getElementById('job').selectedIndex = 0;
    document.getElementById('partnername').value = '';
    document.getElementById('comment').value = '';

    // Call ValidateDrivingLicense function to reset the onboard status
    $('#fieldexecutivename').text('Please Enter your Email').css('color', 'red'); // Clear the onboard status message

    console.log('Input fields cleared');
}


// Function to clear input fields and call VendorEmailInfo function
function editEmailFieldExecutive1() {
    console.log('editEmailFieldExecutive function called');

    // Clear input fields
    document.getElementById('emailfieldexecutive').value = '';

    // Call ValidateDrivingLicense function to reset the onboard status
    $('#fieldexecutivename').text('Please Enter your Email').css('color', 'red'); // Clear the onboard status message

    console.log('Input fields cleared');
}












function ValidateDrivingLicense() {
    var drivingLicense = $('#drivinglicense').val(); // Get the value from the input field
    
    // Check if driving license is provided
    if (!drivingLicense) {
        // If driving license is empty, display error message
        $('#licensestatus').text('Please enter a driving license to validate.').css('color', 'red');
        return; // Exit the function
    }

    // AJAX request
    $.ajax({
        type: 'POST',
        url: '/check_driving_license/', // Update with your backend endpoint
        data: {
            'driving_license': drivingLicense
        },
        success: function (response) {
            var licenseStatusElement = $('#licensestatus');
            if (response.found) {
                // Check if response is "Registered" or "Terminated"
                if (response.onboard_status === "Registered") {
                    licenseStatusElement.text(response.onboard_status).css('color', 'green'); // Green for "Registered"
                } else {
                    licenseStatusElement.text(response.onboard_status).css('color', 'red'); // Red for "Terminated"
                }
            } else {
                // Response is "New", set color to green
                licenseStatusElement.text('New').css('color', 'green');
                document.getElementById('vehicleno').style.display = 'block';
            }
        },
        error: function (xhr, status, error) {
            console.error(xhr.responseText);
            alert('Error: ' + xhr.responseText);
        }
    });
}




function editDrivingLicense() {
    console.log('editDrivingLicense function called'); // Debugging statement to check if the function is called
    
    // Hide the next fieldset
    document.getElementById('vehicleno').style.display = 'none';
    document.getElementById('selecttype').style.display = 'none';
    document.getElementById('partnerreg').style.display = 'none';
    document.getElementById('submitBtn').style.display = 'none';

    // Clear input fields
    document.getElementById('drivinglicense').value = ''; // Clear driving license input field
    document.getElementById('vehiclenumber').value = ''; // Clear vehicle number input field
    document.getElementById('job').selectedIndex = 0; // Reset job select field to default
    document.getElementById('partnername').value = ''; // Clear partner name input field
    document.getElementById('comment').value = ''; // Clear comment input field

    // Call ValidateDrivingLicense function to reset the onboard status
    $('#licensestatus').text('Please Enter your Driving License').css('color', 'red'); // Clear the onboard status message
    
    console.log('Driving license field cleared'); // Debugging statement to check if input field is cleared
}


function editDrivingLicense1() {
    console.log('editDrivingLicense function called'); // Debugging statement to check if the function is called

    // Clear input fields
    document.getElementById('drivinglicense').value = ''; // Clear driving license input field

    // Call ValidateDrivingLicense function to reset the onboard status
    $('#licensestatus').text('Please Enter your Driving License').css('color', 'red'); // Clear the onboard status message
    
    console.log('Driving license field cleared'); // Debugging statement to check if input field is cleared
}



function ValidateVehicle() {
    var vehicleNumber = $('#vehiclenumber').val(); // Get the value of the vehicle number input

    // Check if vehicle number is provided
    if (!vehicleNumber) {
        // If vehicle number is empty, display error message
        $('#vehiclestatus').text('Please enter a vehicle number to validate.').css('color', 'red');
        return; // Exit the function
    }

    // AJAX request
    $.ajax({
        type: 'POST',
        url: '/check_vehicle_number/', // Update with your backend endpoint
        data: {
            'vehicle_number': vehicleNumber
        },
        success: function (response) {
            var vehicleStatusElement = $('#vehiclestatus');
            if (response.found) {
                // Check the current status and set color accordingly
                if (response.current_status === "Active") {
                    vehicleStatusElement.text(response.current_status).css('color', 'green'); // Green for "active"
                } else if (response.current_status === "Inactive") {
                    vehicleStatusElement.text(response.current_status).css('color', 'red'); // Red for "Inactive"
                } else if (response.current_status === "Onhold") {
                    vehicleStatusElement.text(response.current_status).css('color', 'blue'); // Blue for "onhold"
                } else if (response.current_status === "Waiting for Approval") {
                    vehicleStatusElement.text(response.current_status).css('color', 'darkorange'); // Blue for "onhold"
                }
            } else {
                // No response found, set status to "New-Waiting for Approval" and color to green
                vehicleStatusElement.text('New-Waiting for Approval').css('color', 'green');
                document.getElementById('selecttype').style.display = 'block';
            }
        },
        error: function (xhr, status, error) {
            console.error(xhr.responseText);
            alert('Error: ' + xhr.responseText);
        }
    });
}



function editVehicle() {
    console.log('editDrivingLicense function called'); // Debugging statement to check if the function is called
    
    // Hide the next fieldset
    document.getElementById('selecttype').style.display = 'none';
    document.getElementById('partnerreg').style.display = 'none';
    document.getElementById('submitBtn').style.display = 'none';

    // Clear input fields
    document.getElementById('vehiclenumber').value = ''; // Clear vehicle number input field
    document.getElementById('job').selectedIndex = 0; // Reset job select field to default
    document.getElementById('partnername').value = ''; // Clear partner name input field
    document.getElementById('comment').value = ''; // Clear comment input field

    // Call ValidateDrivingLicense function to reset the onboard status
    $('#vehiclestatus').text('Please enter Vehicle no').css('color', 'red'); // Clear the onboard status message
    
    console.log('Vehicle Number  field cleared'); // Debugging statement to check if input field is cleared
}



function editVehicle1() {
    console.log('editDrivingLicense function called'); // Debugging statement to check if the function is called
    
    // Clear input fields
    document.getElementById('vehiclenumber').value = ''; // Clear vehicle number input field

    // Call ValidateDrivingLicense function to reset the onboard status
    $('#vehiclestatus').text('Please enter Vehicle no').css('color', 'red'); // Clear the onboard status message
    
    console.log('Vehicle Number  field cleared'); // Debugging statement to check if input field is cleared
}






// Function to handle AJAX request submission
function submitvendorvehicleForm(event, url) {
    // Prevent default form submission behavior
    event.preventDefault();

    var email = document.getElementById('vendoremail').value;
    var drivingLicense = document.getElementById('drivinglicense').value;
    var vehicleNumber = document.getElementById('vehiclenumber').value;
    var vehicleType = document.getElementById('job').value;
    var partnerName = document.getElementById('partnername').value;
    var partnerNumber = document.getElementById('mobileno').value;
    var comments = document.getElementById('comment').value;

    // Make sure all required fields are filled
    if (!email || !drivingLicense || !vehicleNumber || !vehicleType || !partnerName) {
        alert('Please fill all required fields.');
        return;
    }

    // Make AJAX request to update spreadsheet
    $.ajax({
        type: 'POST',
        url: url,
        data: {
            'email': email,
            'vendorname': '', // Modify this based on your form data
            'drivinglicense': drivingLicense,
            'vehiclenumber': vehicleNumber,
            'userjob': vehicleType,
            'partnername': partnerName,
            'mobileno': partnerNumber,
            'comment': comments
        },
        success: function(response) {
            // Add a short delay before hiding the button and clearing the form fields
            setTimeout(function() {
                alert('Data updated successfully!');
                // Hide all fieldsets except vendorvehiclesubmission
                var fieldsets = document.querySelectorAll('fieldset');
                fieldsets.forEach(function(fieldset) {
                    if (fieldset.id !== 'vendorvehiclesubmission') {
                        fieldset.style.display = 'none';
                    }
                });
                // Show the success message fieldset
                document.getElementById('vendorvehiclesubmission').style.display = 'block';
            }, 500); // Adjust the delay time as needed (in milliseconds)
        },
        error: function(xhr, status, error) {
            alert('An error occurred while updating the data: ' + error);
        }
    });

    // Hide the submit button immediately after submission
    document.getElementById('submitBtn').style.display = 'none';
}


// Function to return to the origin of the current page after successful submission
function returnToForm() {
    // Show all fieldsets
    var fieldsets = document.querySelectorAll('fieldset');
    fieldsets.forEach(function(fieldset) {
        fieldset.style.display = 'block';
    });
    // Hide the success message fieldset
    document.getElementById('vendorvehiclesubmission').style.display = 'none';

    // Reload only the form without adding to the browser's history
    window.location.reload(false);
}



















function submitfieldexecutiveForm(event, url) {
    // Prevent default form submission behavior
    event.preventDefault();

    var email = document.getElementById('emailfieldexecutive').value;
    var drivingLicense = document.getElementById('drivinglicense').value;
    var vehicleNumber = document.getElementById('vehiclenumber').value;
    var vehicleType = document.getElementById('job').value;
    var partnerName = document.getElementById('partnername').value;
    var partnerNumber = document.getElementById('mobileno').value;
    var comments = document.getElementById('comment').value;

    // Make sure all required fields are filled
    if (!email || !drivingLicense || !vehicleNumber || !vehicleType || !partnerName) {
        alert('Please fill all required fields.');
        return;
    }

    // Make AJAX request to update spreadsheet
    $.ajax({
        type: 'POST',
        url: url,
        data: {
            'email': email,
            'vendorname': '', // Modify this based on your form data
            'drivinglicense': drivingLicense,
            'vehiclenumber': vehicleNumber,
            'userjob': vehicleType,
            'partnername': partnerName,
            'mobileno': partnerNumber,
            'comment': comments
        },
        success: function(response) {
            // Hide the form
            document.getElementById('executivevehicleregistrationForm').style.display = 'none'; // Replace 'formId' with the actual ID of your form element
            // Show the success message fieldset
            document.getElementById('response').style.display = 'block';
            // Display the response inside the success message fieldset if needed
            // document.getElementById('fieldexecutivesubmission').innerHTML = response;
            alert('Data updated successfully!');
        },
        error: function(xhr, status, error) {
            alert('An error occurred while updating the data: ' + error);
        }
    });

    // Hide the submit button immediately after submission
    document.getElementById('submitBtn').style.display = 'none';
}


function returnToForm() {
    // Hide the entire form
    document.getElementById('executivevehicleregistrationForm').style.display = 'none'; // Replace 'formId' with the actual ID of your form element
    // Show the fieldexecutivesubmission fieldset
    document.getElementById('respons').style.display = 'block';
}



// Function to show Partner Registration fields
function showPartnerRegistration() {
    var selectedVehicle = document.getElementById('job').value;
    var partnerFieldset = document.getElementById('partnerreg');
    var submitButton = document.getElementById('submitBtn');
    
    if (selectedVehicle !== 'none') {
        // If a vehicle is selected, show the Partner Registration fields and Submit button
        partnerFieldset.style.display = 'block';
        submitButton.style.display = 'block';
    } else {
        // If no vehicle is selected, hide the Partner Registration fields and Submit button
        partnerFieldset.style.display = 'none';
        submitButton.style.display = 'none';
    }
}






function toggleNumberAndAddress() {
    var gstRadio = document.getElementById('gst');
    var noneRadio = document.getElementById('none');
    var numberAndAddressDiv = document.getElementById('numberandaddress');
    var gstInput = document.getElementById('gstInput');
    var addressTextarea = document.getElementById('address');

    if (gstRadio.checked) {
        numberAndAddressDiv.style.display = 'block';
    } else {
        numberAndAddressDiv.style.display = 'none';
        // Clear input box and textarea when "None" is selected
        gstInput.value = '';
        addressTextarea.value = '';
    }
}









// Function to hide all fieldsets except for the submission message
function hideFieldsetsExceptSubmissionMessage() {
    var fieldsets = document.querySelectorAll('fieldset');
    fieldsets.forEach(function(fieldset) {
        if (fieldset.id !== 'submissionMessage') {
            fieldset.style.display = 'none';
        } else {
            fieldset.style.display = 'block'; // Show the submission message fieldset
        }
    });
}

// Function to show an alert for each field
function showAlert(message, field) {
    alert(message);
    // Focus on the specified field
    field.focus();
}

// Function to check if all required fields are filled out
function checkRequiredFields() {
    var fields = document.querySelectorAll('#vendorregistrationForm input[required], #vendorregistrationForm select[required], #vendorregistrationForm textarea[required]');
    var firstUnfilledField = null;
    fields.forEach(function(field) {
        if (!field.value && !firstUnfilledField) {
            firstUnfilledField = field;
            showAlert("Please fill in the " + field.getAttribute("placeholder") + " field.", field);
        }
    });
    return !firstUnfilledField; // Return false if there's an unfilled field, true otherwise
}



// Function to submit the form
function submitVendorRegForm(event, url) {
    // Prevent default form submission behavior
    event.preventDefault();

    // Check if all required fields are filled out
    var isValid = checkRequiredFields();

    // If all required fields are filled, proceed with form submission
    if (isValid) {
        // Hide the submit button only after validation
        document.getElementById('submitBtn').style.display = 'none';

        // Fetch form data
        var formData = new FormData(document.getElementById('vendorregistrationForm'));

        // Make AJAX POST request to Django view
        $.ajax({
            type: 'POST',
            url: url,   // Update URL with your Django view endpoint
            data: formData,
            processData: false,
            contentType: false,
            success: function(response) {
                // Handle success response
                console.log(response);
                alert('Form submitted successfully!');
                hideFieldsetsExceptSubmissionMessage(); // Call the function to hide all fieldsets except submission message
            },
            error: function(xhr, status, error) {
                // Handle error response
                console.error(xhr.responseText);
                alert('An error occurred while submitting the form. Please try again later.');
            }
        });
    }
}


// Function to return to the form after submission message
function returnToForm() {
    // Reload the HTML page
    window.location.reload(); 

    // Clear all input fields
    var inputFields = document.querySelectorAll('form input, form select, form textarea');
    inputFields.forEach(function(input) {
        if (input.type === 'radio') {
            input.checked = false; // Uncheck radio buttons
        } else {
            input.value = ''; // Clear other input fields
        }
    });

    // Hide the GST Number input box
    document.getElementById('gstInput').style.display = 'none';

    // Show the form
    var form = document.querySelector('form');
    form.style.display = 'block';
    
    // Hide the submission message
    document.getElementById('submissionMessage').style.display = 'none';
}



