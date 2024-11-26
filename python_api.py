#Need to install requests package for python
#easy_install requests
import requests

# Set the request parameters
url = 'https://brightspeedtsmqa1.service-now.com/api/sn_cicd/testsuite/results/eb0aa8921b82d2505127a933604bcb81'

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

# Decode the JSON response into a dictionary and use the data
data = response.json()
print(data)
