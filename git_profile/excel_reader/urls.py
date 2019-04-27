from django.conf.urls import url
from excel_reader.endpoints.excel_file import Uploader, ListFiles, FileDetails


urlpatterns = [
    url(r'^upload/', Uploader.as_view(), name='file-uploader'),
    url(r'^list/', ListFiles.as_view(), name='list-files'),
    url(r'^file/(?P<file_id>\d+)', FileDetails.as_view(), name='file-details'),
]
