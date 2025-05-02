import gspread as gs
from oauth2client.service_account import ServiceAccountCredentials as sac

class API:
    def __init__(self, id:str):
        self.id = id
        self.sac = sac.from_json_keyfile_name(
            filename='service/Token.json',
            scopes=[
                'https://spreadsheets.google.com/feeds',
                'https://www.googleapis.com/auth/drive'
            ]
        )
    
    def post(self, sheet:int, data:list):
        client = gs.authorize(self.sac)
        work = client.open_by_key(self.id).get_worksheet(sheet)
        work.insert_rows([data], 2)
    
    def get(self, sheet:int):
        client = gs.authorize(self.sac)
        work = client.open_by_key(self.id).get_worksheet(sheet)
        return work.get_all_records()