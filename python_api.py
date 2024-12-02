#Need to install requests package for python
#easy_install requests
import os
import requests

# Set the request parameters
url = 'https://brightspeedtsmqa1.service-now.com/api/sn_cicd/testsuite/results/4a81bf581b521e107ba2ec64604bcb0f'

# Eg. User name="admin", Password="admin" for this code sample.
user = 'shivakumara.appaji@infinite.com'
pwd = 'Pratheja@123'

# Set proper headers
headers = {"Content-Type":"application/json","Accept":"application/json"}

# Do the HTTP request
response = requests.get(url, auth=(user, pwd), headers=headers )

# Check for HTTP codes other than 200
if response.status_code != 200: 
    print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
    exit()

# Parse the JSON response
data = response.json()
test_suite_status = data['result']['test_suite_status']
rolledup_test_success_count = data['result']['rolledup_test_success_count']
rolledup_test_failure_count = data['result']['rolledup_test_failure_count']
rolledup_test_error_count = data['result']['rolledup_test_error_count']
rolledup_test_skip_count = data['result']['rolledup_test_skip_count']
test_suite_name = data['result']['test_suite_name']

# Define a function to generate the HTML content
def generate_html(success_count, failure_count, error_count, skip_count, suite_name, suite_status):
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>ATF Test Suite Results</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 20px;
                background-color: #f4f4f4;
            }}
            .container {{
                max-width: 600px;
                margin: 0 auto;
                background-color: #fff;
                padding: 20px;
                border-radius: 8px;
                box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            }}
            .result {{
                margin-bottom: 15px;
                font-size: 18px;
            }}
            .result span {{
                display: inline-block;
                width: 200px;
            }}
            .success {{
                color: green;
            }}
            .failure {{
                color: red;
            }}
            .status {{
                font-weight: bold;
                font-size: 20px;
            }}
        </style>
    </head>
    <body>

        <div class="container">
            <h1>VoicePlus ATF Test Suite Results</h1>

            <div class="result">
                <span><strong>Test Suite Name:</strong></span> {suite_name}
            </div>
            <div class="result">
                <span><strong>Success Count:</strong></span> <span class="success">{success_count}</span>
            </div>
            <div class="result">
                <span><strong>Failure Count:</strong></span> <span class="failure">{failure_count}</span>
            </div>
            <div class="result">
                <span><strong>Error Count:</strong></span> {error_count}
            </div>
            <div class="result">
                <span><strong>Skip Count:</strong></span> {skip_count}
            </div>

            <div class="status">
                <strong>Test Suite Status:</strong> <span class="{'failure' if suite_status == 'failure' else ''}">{suite_status}</span>
            </div>
        </div>

    </body>
    </html>
    """
    return html_content

# Generate the HTML content
html_result = generate_html(rolledup_test_success_count, rolledup_test_failure_count, 
                            rolledup_test_error_count, rolledup_test_skip_count, 
                            test_suite_name, test_suite_status)

# Save the generated HTML to a file
with open('test_results.html', 'w') as f:
    f.write(html_result)

print("HTML file generated successfully!")
