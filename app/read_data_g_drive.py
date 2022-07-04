import json 
import pandas as pd
from io import StringIO

import sys

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

from apiclient import discovery
from httplib2 import Http
from oauth2client import client, file, tools

gauth = GoogleAuth()
# gauth.CommandLineAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)


#drive api service
#defining path variables:
client_secret_file_path = '/home/ra-terminal/api_keys/google_key/credentials/client_secret_key.googleusercontent.com.json'
credentials_file_path = '/home/ra-terminal/api_keys/google_key/credentials/credentials.json'
store = file.Storage(credentials_file_path)
#get access token
credentials = store.get()
http = credentials.authorize(Http())
drive2=discovery.build('drive', 'v3', http=http)
# file1 = drive.CreateFile({'title': 'Helloooooo.txt'}) #CREATE GOOGLEDRIVE
# file1.SetContentString('HELLOOOOOUHWUHDAOFAIEFEHBEBFSWF')
# file1.Upload()

def get_all_files_metadata_to_json(api_service):
    results = []
    page_token = None

    while True:
        try:
            param = {}
            if page_token:
                param['pageToken'] = page_token
            files = api_service.files().list(**param).execute()            # append the files from the current result page to our list
            results.extend(files.get('files'))            # Google Drive API shows our files in multiple pages when the number of files exceed 100
            page_token = files.get('nextPageToken')

            if not page_token:
                break
        except error.HttpError as error:
            print(f'An error has occurred: {error}')
            break    # output the file metadata to console
    
    #dumping results into json
    with open('/home/ra-terminal/Desktop/projects/medium_projects/graphql_strawberry_fastapi/datafiles/g_drive_metadata.json', 'w') as f_obj:
        json.dump(results, f_obj, indent=2)
    return results

def search_file(file_target):

    with open('/home/ra-terminal/Desktop/projects/medium_projects/graphql_strawberry_fastapi/datafiles/g_drive_metadata.json', 'r') as f_obj:
        data_files = json.load(f_obj)
    for file in data_files:
        if file.get('name') == file_target:
            # return file.get('kind'), file.get('id'), file.get('name'), file.get('mimeType')
            return file

def get_file(filename):
    save_location="/home/ra-terminal/Desktop/projects/medium_projects/graphql_strawberry_fastapi/datafiles"
    file_metadata = search_file(filename)
    # file_id = file_metadata['id']
    # file_name = file_metadata['name']
    # mimeType = file_metadata['mimeType']
    target_file = drive.CreateFile({'id':file_metadata['id']})
    # print("Target file is: -------------->>>", target_file)
    # target_download = target_file.GetContentString(file_metadata['name'])
    target_download = None
    if target_file['id'] == file_metadata['id']:
        target_download = target_file.GetContentFile(f"/home/ra-terminal/Desktop/projects/medium_projects/graphql_strawberry_fastapi/datafiles/{file_metadata['name']}")
        print('Downloading file %s from Google Drive' % target_download['name']) 
        return f"File {target_download['name']} has been downloaded"
    return "file not found on google drive"

def read_in_pandas(filename):
    return pd.read_csv(f"/home/ra-terminal/Desktop/projects/medium_projects/graphql_strawberry_fastapi/datafiles/{filename}")

pokemon_df = read_in_pandas('pokemon.csv')
if __name__ == "__main__":
    # get_all_files_metadata_to_json(drive2)
    # get_file('pokemon.csv')
    df = read_in_pandas('pokemon.csv')
    # print("----------------")
    # # print(df.columns)
    v=5
    print('complete run')
    pass