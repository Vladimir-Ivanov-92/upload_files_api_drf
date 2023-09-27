from celery import shared_task

from upload_files.models import File

@shared_task
def file_processing_task(file_id: int) -> None:
    try:
        file = File.objects.get(pk=file_id)
        file.processed = True
        file.save()
    except Exception as e:
        print(e)