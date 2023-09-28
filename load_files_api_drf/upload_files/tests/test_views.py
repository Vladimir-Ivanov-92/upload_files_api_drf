import os
import tempfile

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from upload_files.models import File
from upload_files.serializers import FileSerializer


class FilesAPIViewTestCase(APITestCase):
    def setUp(self):
        self.url = reverse("files-list")  # Создайте тестовые данные для модели File

    def test_list_files(self):
        # Создаем тестовый объект в БД
        File.objects.create(
            title="file_1",
            uploaded_at="2023-09-28T19:45:36.549757+03:00",
            processed=False
        )
        File.objects.create(
            title="file_2",
            uploaded_at="2023-09-28T19:46:36.549757+03:00",
            processed=False
        )
        # Отправляем GET запрос на 'api/v1/files'
        response = self.client.get(self.url)
        # Проверяем что статус ответа 200
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Проверяем, что полученные данные совпадают с ожидаемыми данными
        files = File.objects.all()
        serializer = FileSerializer(files, many=True)
        self.assertEqual(response.data, serializer.data)

    def test_empty_file_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Проверяем, что список файлов пуст
        self.assertEqual(len(response.data), 0)


class UploadFileAPIViewTestCase(APITestCase):
    def test_upload_text_file(self):
        # Создаем временный файл с содержимым "Old file\n"
        with tempfile.NamedTemporaryFile(mode='w', delete=False,
                                         suffix='.txt') as temp_file:
            temp_file.write("Old file\n")

        # Создаем URL
        url = reverse("file-upload")

        # Отправляем POST-запрос с файлом
        with open(temp_file.name, 'rb') as file:
            response = self.client.post(
                url,
                {
                    "title": "test.txt",
                    "file": file,
                    "uploaded_at": "2023-09-28T19:46:36.549757+03:00",
                    "processed": False,
                }
            )

        # Удаляем временный файл
        os.remove(temp_file.name)

        # Проверяем, что загрузка прошла успешно
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Проверяем, что файл сохранен в базе данных
        self.assertTrue(File.objects.filter(title="test.txt").exists())
