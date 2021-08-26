from googleapiclient.discovery import build
from google.oauth2 import service_account
from pyasn1.type.univ import Null


def getaccount(input):
	try:
		RANGE_DATA = str(f'{input}!A:B')

		SERVICE_ACCOUNT_FILE = './account/key.json'
		SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
		SPREADSHEET_ID = '1dF4H6Gx2PEKfTtWWIzrmEX5SC9wyTh3IL8mqntI_b_I'

		creds = service_account.Credentials.from_service_account_file(
				SERVICE_ACCOUNT_FILE, scopes=SCOPES)
		service = build('sheets', 'v4', credentials=creds)

		sheet = service.spreadsheets()
		result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
											range=RANGE_DATA).execute()

		values = result.get('values', [])
		return values
	except:
		return Null