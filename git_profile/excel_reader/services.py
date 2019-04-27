import xlrd
from excel_reader.models import FileData
import json


class FileDataService:
    @classmethod
    def save_file(cls, name, data):
        return FileData(name=name, data=json.dumps(data)).save()

    @classmethod
    def get_file(cls, file_id):
        try:
            file = FileData.objects.get(id=file_id)
            data = json.loads(file.data)
            headers = data['headers']
            rows = data['rows']
            file_name = file.name
            return dict(headers=headers, rows=rows, file_name=file_name)
        except Exception as e:
            # log here
            raise Exception(e)

    @classmethod
    def list_files(cls):
        all_files = FileData.objects.filter()
        return [{"id": file.id, "name": file.name } for file in all_files]


class ExcelService:
    def __init__(self, file):
        self.file = file

    def get_file_content(self):
        book = xlrd.open_workbook(file_contents=self.file.read())
        # assuming only one sheet
        if not book.sheets():
            raise Exception("No sheets in the excel file")
        sheet = book.sheets()[0]
        excel_data = sheet._cell_values
        if not excel_data:
            raise Exception('Empty excel file')
        headers = sheet._cell_values[0]
        rows = sheet._cell_values[1:]
        content = dict(headers=headers, rows=rows)
        return content
