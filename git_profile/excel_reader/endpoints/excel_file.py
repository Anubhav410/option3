from django.shortcuts import render
from rest_framework.views import APIView, Response

from excel_reader.services import ExcelService, FileDataService


class Uploader(APIView):
    def get(self, request):
        return render(request, "upload.html")

    def post(self, request):
        try:
            if not request.FILES or not 'file' in request.FILES:
                return Response("Please upload a file")

            excel_service = ExcelService(request.FILES['file'])
            file_content = excel_service.get_file_content()
            file_name = request.FILES['file'].name
            FileDataService.save_file(name=file_name, data=file_content)
            return Response("File Upload Complete")
        except Exception as e:
            Response("Something went wrong: {}".format(e.message))


class ListFiles(APIView):
    def get(self, request):
        file_list = FileDataService.list_files()
        return render(request, 'list_files.html', context={'file_list':file_list})


class FileDetails(APIView):
    def get(self, request, file_id):
        try:
            file_details = FileDataService.get_file(file_id)
            return render(request, 'file_details.html', context=file_details)
        except Exception as e:
            return Response("{}".format(e.message))

