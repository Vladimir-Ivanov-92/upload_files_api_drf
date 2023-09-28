from celery import shared_task
from rest_framework.response import Response

from upload_files.models import File

from upload_files.service import FileProcessing


@shared_task
def file_processing_task(file_id: int) -> None:
    file_object = File.objects.get(pk=file_id)
    file_path = file_object.file.path

    result: Response | Exception = FileProcessing(file_path).file_processing()
    if result.status_code == 200:
        file_object.processed = True
        file_object.save()
    else:
        print(result.data)
