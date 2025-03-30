# Atlassian utils

Python script to interact with Confluence Cloud API for space management and PDF export.

## Features

1. **Get Space Keys**  
   Command: `python main.py get-space-keys`. _Retrieve all Confluence spaces with names and keys._
2. **Export Space to PDF**  
   Command: `python main.py export.pdf --space-key=test`. _Export all pages from a Confluence space to PDF with 
   preserved hierarchy._

## Configuration

1. Get your API token: [Atlassian API Tokens](https://id.atlassian.com/manage-profile/security/api-tokens)
2. Rename `.env.example` to `.env`:
3. Update `.env` with your credentials.

## Requirements
- Python 3.13+
- Atlassian Cloud instance
- API token with **read** permissions