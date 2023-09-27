from upload_files.models import File


def file_processing(file_id: int) -> None:
    try:
        file = File.objects.get(pk=file_id)
        file.processed = True
        file.save()
    except Exception as e:
        print(e)
