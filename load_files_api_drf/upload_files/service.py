import mimetypes

from PIL import Image
from rest_framework import status
from rest_framework.response import Response


class FileProcessing:
    """
    Класс для обработки файлов
    """

    def __init__(self, file_path: str):
        self.file_path = file_path
        self.mime_type, self.encoding = mimetypes.guess_type(file_path)

    def file_processing(self) -> Response | Exception:
        """
        Метод, используемый для обработки файла в соответствии с его типом
        """
        try:
            if self.mime_type:
                if self.mime_type.startswith("image"):
                    img = Image.open(self.file_path)

                    # Преобразование изображения в черно-белый формат
                    black_and_white_img = img.convert("L")

                    # Сохранение изображения
                    black_and_white_img.save(self.file_path)

                elif self.mime_type == "text/plain":
                    with open(f"{self.file_path}", "a") as f:
                        f.write("New line\n")
                else:
                    return Response(
                        data={"error": "Unsupported file type"},
                        status=status.HTTP_400_BAD_REQUEST
                    )
            else:
                return Response(
                    data={"error": "Unable to determine file type"},
                    status=status.HTTP_400_BAD_REQUEST
                )
        except Exception as e:
            return Response(
                data={"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        return Response(
                data={"message": "File processed successfully"},
                status=status.HTTP_200_OK
            )
