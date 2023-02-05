
#!/usr/bin/env python

import os
import requests

# Get the project from local directory
project_dir = os.getcwd()

# Check if .git file not exist, create that
if not os.path.exists(os.path.join(project_dir, '.git')):
    os.system('git init')

# Use the Personal access tokens (classic)
token = input('Enter your Personal access token: ')

# Push the project to the new repository
url = 'https://api.github.com/user/repos'
headers = {'Authorization': 'token ' + token}
data = {'name': 'my_new_repo'}
response = requests.post(url, json=data, headers=headers)
if response.status_code == 201:
    print('Repository created successfully!')
    os.system('git remote add origin ' + response.json()['clone_url'])
    os.system('git add .')
    os.system('git commit -m "Initial commit"')
    os.system('git push -u origin master')
    print('Project pushed successfully!')
else:
    print('Error creating repository!')