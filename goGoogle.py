import gspread
from oauth2client.service_account import ServiceAccountCredentials


def auth_gss_client(path, scopes):
    credentials = ServiceAccountCredentials.from_json_keyfile_name(path,scopes)
    return gspread.authorize(credentials)

GoogleJson='TProject.json'
GoogleSheet='TProject'
gss_scopes = ['https://spreadsheets.google.com/feeds']
key='157p5VoX8lRk66Wgnb0EuqoAcDbBtKTNapLWBpBvuS1c'

gss_client = auth_gss_client(GoogleJson, gss_scopes)

def update_sheet(gss_client, key, DataSet,title,Paremeters,Acc):
    wks = gss_client.open_by_key(key)
    sheet = wks.worksheet(title)
    go=[DataSet]+list(Paremeters)+list(Acc)
    sheet.insert_row(go,2)
def goGoogle(DataSet,title,Paremeters,Acc):
    update_sheet(gss_client,key,DataSet,title,Paremeters,Acc)