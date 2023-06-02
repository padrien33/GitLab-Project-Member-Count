# GitLab Project Member Count Script

This Python script retrieves the number of members for each project on a GitLab instance, as well as the total number of unique members across all projects. 

## Requirements
- Python 3.6 or above
- Requests library (`pip install requests`)

## Setting Up
Before running this script, you need to set up an environment variable for your GitLab Private Token. This token is required for the script to authenticate with the GitLab API. You can generate a Private Token in the GitLab user settings.

The environment variable for the token should be named `GITLAB_PRIVATE_TOKEN`.

### Setting the environment variable on Unix or Linux

export GITLAB_PRIVATE_TOKEN=your-private-token

### Setting the environment variable on Windows

set GITLAB_PRIVATE_TOKEN=your-private-token

After setting the environment variable, it will be available for the current session. If you want to set it permanently, you would need to add the above command to your shell startup file or system environment variables, which is beyond the scope of this README.

## Downloading the script

```bash
curl --header "PRIVATE-TOKEN: $GITLAB_PRIVATE_TOKEN" -O <url-to-raw-script>

## Running the script
To run the script, simply use the following command:

python3 gitlab_member_count.py

The script will write the number of members for each project and their Git URLs to a text file named `project_id_members.txt`. The file will be saved in the same directory where the script is run.

