# Google Sheets API
import gspread
from oauth2client.service_account import ServiceAccountCredentials


class AutoResumeObject:
	def __init__(self):

		credential = ServiceAccountCredentials.from_json_keyfile_name("credentials.json",
                                                              		 ["https://spreadsheets.google.com/feeds",
                                                              		  "https://www.googleapis.com/auth/spreadsheets",
                                                              		  "https://www.googleapis.com/auth/drive.file",
                                                              		  "https://www.googleapis.com/auth/drive"])
		client = gspread.authorize(credential)
		
		self.gsheet = client.open("Auto-Resume").sheet1

	def display_all(self):
		return self.gsheet.get_all_records()