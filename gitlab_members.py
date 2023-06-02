import os
import requests
import json
from datetime import datetime

# GitLab instance URL
url = 'https://gitlab.com'
# Private token
private_token = os.getenv('GITLAB_PRIVATE_TOKEN')
# Maximum number of items per page
per_page = 100

headers = {'PRIVATE-TOKEN': private_token}

# Page number
page = 1

# Empty list to store all project data
all_project_data = []

# Variable to track if the success message has been printed
first_success = False

while True:
    # API endpoint to get all projects with Java, Not Archived, and with activities in the last 90 days
    projects_api_url = f'{url}/api/v4/projects?membership=true&page={page}&per_page={per_page}'

    response = requests.get(projects_api_url, headers=headers)

    if response.status_code == 200:
        # Add debug connection info
        if not first_success:
            print('Connected successfully to the API. Starting the loop...')
            first_success = True
        projects = json.loads(response.text)
        # Break the loop if no more projects
        if not projects:
            break
        # Add project data to the list
        all_project_data.extend([{'id': project['id'], 'git_url': project['http_url_to_repo']} for project in projects])
        # Go to the next page
        page += 1
    else:
        print(f'Error with status code: {response.status_code}')
        break


# Dictionary to store number of members for each project
project_members = {}

# Set to store unique user IDs
unique_user_ids = set()

# Get members for each project
for project_data in all_project_data:
    # API endpoint to get the project members
    members_api_url = f'{url}/api/v4/projects/{project_data["id"]}/members'

    members_response = requests.get(members_api_url, headers=headers)

    if members_response.status_code == 200:
        members = json.loads(members_response.text)
        # Add user IDs to the set of unique user IDs
        unique_user_ids.update([member['id'] for member in members])
        # Store number of members for this project
        project_members[project_data["id"]] = {'git_url': project_data['git_url'], 'member_count': len(members)}
    else:
        print(f'Error for project {project_id} with status code: {members_response.status_code}')


# Print total number of projects
print("Total number of projects:", len(all_project_data))

# Print total number of unique members across all projects
print("Total number of unique members across all projects:", len(unique_user_ids))

# Write number of members and Git URL for each project
with open('project_id_members.txt', 'w') as file:
    # Write the current date on the first line
    file.write(f'Date: {datetime.now()}\n')
    for project_id, project_data in project_members.items():
        file.write(f"Project {project_id} (URL: {project_data['git_url']}): {project_data['member_count']} members\n")

print("Text file created: project_id_members.txt including project IDs, Git URLs, and unique member counts per projects.")
