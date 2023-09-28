from rest_framework import generics, status
from rest_framework.response import Response

from .models import File
from .serializers import FileSerializer
from .tasks import file_processing_task


class UploadFileAPIView(generics.CreateAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer

    def create(self, request, *args, **kwargs):
        try:
            # Создаем новый объект File с использованием сериализатора
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            instance: File = serializer.save()

            # Добавляем обработку файла
            if instance:
                file_id = instance.id
                file_processing_task.delay(file_id)

            headers = self.get_success_headers(serializer.data)

            # Возвращаем ответ, указывающий на успешное создание модели File
            # и сохранение загруженного файла на сервер
            return Response(serializer.data, status=status.HTTP_201_CREATED,
                            headers=headers)
        except Exception as e:
            return Response(
                {"error": "File not created"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class FilesAPIView(generics.ListAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer
