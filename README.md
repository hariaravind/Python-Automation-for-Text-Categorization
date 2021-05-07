# Python Automation for Text Categorization

This is an automation project using Python to make data cleaning easier. The script READs data from multiple spreadsheets, performs descriptiive and diagnistic analytics, and then WRITEs the data to a target spreadsheet.

##===Requirements===
- Google Cloud Console Access
- Google Drive API
- Google Docs API

I have used [PyGSheets](https://github.com/nithinmurali/pygsheets) because it supports Google Spreadsheets Python API v4.

##===Instructions===
1. Follow [the steps](https://pygsheets.readthedocs.io/en/stable/authorization.html#oauth-credentials) and authenticate the app with Google Docs API key in JSON format. 
2. Rename the file to credentials.json and retain in the same directory as Automation.py.
3. Find the Sheet ID of the source document as well as target document, and insert the ID in the code. 
4. Run the script; When prompted, authenticate with the secret key obtained from Google Docs API.
5. That's it! 
