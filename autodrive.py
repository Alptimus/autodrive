import os
import json
import mimetypes
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow

# If modifying these SCOPES, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/drive.file']

def authenticate():
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is created automatically when the authorization flow completes for the first time.
    if os.path.exists('token.json'):
        with open('token.json', 'r') as token:
            creds = Credentials.from_authorized_user_info(json.load(token), SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            try:
                creds.refresh(Request())
            except:
                creds = None
        if not creds:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.json', 'w') as token:
                token.write(creds.to_json())
    return creds

def list_files_in_drive_folder(service, folder_id):
    query = f"'{folder_id}' in parents and trashed=false"
    results = service.files().list(q=query, fields="files(id, name, size)").execute()
    items = results.get('files', [])
    return {item['name']: item for item in items}

def upload_files(service, folder_id, source_directory):
    drive_files = list_files_in_drive_folder(service, folder_id)
    
    for root, dirs, files in os.walk(source_directory):
        for filename in files:
            file_path = os.path.join(root, filename)
            file_size = os.path.getsize(file_path)
            
            # Check if the file already exists in the Drive folder
            if filename in drive_files:
                drive_file = drive_files[filename]
                # Skip the file if it already exists with the same size
                if int(drive_file['size']) == file_size:
                    print(f'Skipping {filename}, already uploaded.')
                    continue
            
            # Upload the file if it does not exist or the size differs
            file_metadata = {
                'name': filename,
                'parents': [folder_id]
            }
            mime_type, _ = mimetypes.guess_type(file_path)
            media = MediaFileUpload(file_path, mimetype=mime_type)
            service.files().create(body=file_metadata, media_body=media, fields='id').execute()
            print(f'Uploaded {filename}')

def autodrive():
    # Load config
    with open('config.json', 'r') as f:
        config = json.load(f)
    
    folder_id = config['destination']
    source_directory = config['source']

    creds = authenticate()
    service = build('drive', 'v3', credentials=creds)

    upload_files(service, folder_id, source_directory)

if __name__ == '__main__':
    autodrive()