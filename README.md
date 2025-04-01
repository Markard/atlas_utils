# Atlassian utils

Is an open-source solution designed to simplify working with Atlassian products through a set of convenient 
command-line utilities. This toolset supports Confluence and Jira, enabling efficient data retrieval, export, and 
automation.

## Features

### 1. Retrieve Information About Confluence Spaces  
_Fetch all spaces in your Confluence instance, displaying their - names and space keys. Supports pagination for 
large datasets._

`python main.py get-space-keys [-s --start START] [-l --limit LIMIT]`
- `-l --limit`: Number of spaces to retrieve per page (default: 500).
- `-s --start`: Starting index for pagination (default: 0).

### 2. Export All Pages of a Confluence Space to PDF  
_Export all pages from a specified Confluence space into PDF files while preserving the folder structure based on 
the space key._

`python main.py export-pdf [-sk --space-key SPACE_KEY]`
- `-sk --space-key`: The key of the Confluence space to export.

### 3. Upload Worklogs to Jira from Local File
_Upload daily worklogs into Jira from JSON or YAML files. Only logs with the `issue_key` and the tag `work` are 
uploaded._

`python main.py upload-worklog [-d --day DAY] [-f --flush FLUSH]`
- `-d --day`: Date in %Y-%m-%d format (required).
- `-f --flush`: If True, uploads worklogs to Jira. If False, only displays the logs (default: False).

**Supported Formats:**  
  - JSON  
  - YAML

**Log File Structure:**
Logs must be stored in the folder structure: `{LOG_FOLDER_ENTRY}/{year}/{month}/{day}.{format}`. `LOG_FOLDER_ENTRY` 
is a variable in .env file.
- Example: `logs/2023/10/1.yml`  

**YAML Example:**
```yml
---
- started_at: '07:00'
  ended_at: '07:30'
  comment: I had breakfast 
  tags:
    - meal
- started_at: '07:30'
  ended_at: '10:20'
  comment: Worked on the task - integration with an external system.
  issue_key: KAN-1
  tags:
    - work
```
- `issue_key`: The Jira issue key (optional). Only logs with this key and the tag `work` will be uploaded.
- Other fields (`started_at`, `ended_at`, `comment`, `tags`) are required.

## Installation

1. Get your API token: [Atlassian API Tokens](https://id.atlassian.com/manage-profile/security/api-tokens)
2. Rename `.env.example` to `.env`:
3. Update `.env` with your credentials.
4. Install dependencies: ```pip install -r requirements.txt```

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or new features.

## Requirements
- Python 3.13+
- Atlassian Cloud instance
- API token with **read**, **write** permissions