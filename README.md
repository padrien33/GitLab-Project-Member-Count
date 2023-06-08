# GitLab Project Member Count Script

This Python script retrieves the number of members for each project on a GitLab instance, as well as the total number of unique members across all projects. 




![Screenshot](https://github.com/padrien33/GitLab-Project-Member-Count/blob/main/gitlab_members.png)

It uses GitLab API, so you can add more filter on the API Call like restricting the repo that contains only Java by using the attribute: "with_programming_language"
Change "projects_api_url" in gitlab_members.py
For more details on the attribute you can use, please consult the documentation from GitLab:

[GitLab Project API Doc](https://docs.gitlab.com/ee/api/projects.html#list-all-projects)

It will then create a text file, project_id_members.txt follwing this format:
```bash
Project ID: 20176*** (URL: https://gitlab.com/***/***/***.git): 2 members
Project ID: 17858*** (URL: https://gitlab.com/***/***.git): 1 members
Project ID: 16932*** (URL: https://gitlab.com/***/***.git): 1 members
Project ID: 15640*** (URL: https://gitlab.com/***/***.git): 3 members

```

## Requirements
- Python 3.6 or above
- Requests library (`pip install requests`)

## Setting Up
Before running this script, you need to set up an environment variable for your GitLab Private Token. This token is required for the script to authenticate with the GitLab API. You can generate a Private Token in the GitLab user settings.

The environment variable for the token should be named `GITLAB_PRIVATE_TOKEN`.

### Setting the environment variable on Unix or Linux
```bash
export GITLAB_PRIVATE_TOKEN=your-private-token
```
### Setting the environment variable on Windows
```bash
set GITLAB_PRIVATE_TOKEN=your-private-token
```
After setting the environment variable, it will be available for the current session. If you want to set it permanently, you would need to add the above command to your shell startup file or system environment variables, which is beyond the scope of this README.


### Setup URL

By default it will use https://gitlab.com as the instance.
Change the variable url to the hostname f your GitLab instance.


## Downloading the script

If you do not already have the Python script, you can download it directly from this git repository using the following `curl` command:

```bash
curl -O https://raw.githubusercontent.com/padrien33/GitLab-Project-Member-Count/main/gitlab_members.py

```

## Running the script
To run the script, simply use the following command:
```bash
python3 gitlab_member_count.py
```
The script will write the number of members for each project and their Git URLs to a text file named `project_id_members.txt`. The file will be saved in the same directory where the script is run.


