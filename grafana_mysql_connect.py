import requests
import json

# Grafana API endpoint
grafana_url = 'http://localhost:3000/api/datasources'

# Grafana admin credentials
grafana_user = 'admin'
grafana_password = 'admin'  # Change to your Grafana admin password

# MySQL datasource configuration
mysql_datasource = {
    "name": "MySQL",
    "type": "mysql",
    "access": "proxy",
    "url": "localhost:3306",
    "user": "your_username",  # Change to your MySQL username
    "password": "your_password",  # Change to your MySQL password
    "database": "your_database",  # Change to your MySQL database name
    "jsonData": {
        "tlsSkipVerify": True
    }
}

# Headers for API request
headers = {
    'Content-Type': 'application/json',
}

# Authenticate with Grafana API
auth_response = requests.post(
    'http://localhost:3000/login',
    json={'user': grafana_user, 'password': grafana_password},
)

# Check if authentication is successful
if auth_response.status_code == 200:
    # Get authentication cookie
    auth_cookie = auth_response.cookies.get('grafana_sess')
    
    # Add MySQL datasource to Grafana
    response = requests.post(
        grafana_url,
        headers=headers,
        cookies={'grafana_sess': auth_cookie},
        json=mysql_datasource,
    )
    
    # Check if datasource is added successfully
    if response.status_code == 200:
        print("MySQL datasource added successfully to Grafana.")
    else:
        print("Error adding MySQL datasource to Grafana:", response.text)
else:
    print("Failed to authenticate with Grafana API.")