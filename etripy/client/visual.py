import base64
from typing import Optional

from etripy.error import VisualImageException
from etripy.http import EtriRequest
from etripy.model.visual.image import ObjectDetectResult


class ImageClient(EtriRequest):
    def __init__(self, access_key: str) -> None:
        super().__init__(access_key=access_key)

    async def object_detect(
        self, file_path: str, file_type: str = "auto"
    ) -> Optional[list[ObjectDetectResult]]:
        if file_type == "auto":
            file_type = file_path.split(".")[-1]

        file = open(file_path, "rb")
        imageContents = base64.b64encode(file.read()).decode("utf8")
        file.close()

        data = {"argument": {"type": file_type, "file": imageContents}}
        result = await self.request(method="POST", endpoint="/ObjectDetect", data=data)
        try:
            if result["return_object"] == {}:
                return None
        except KeyError:
            if result["result"] != "0":
                raise VisualImageException(result["reason"])
        return [
            ObjectDetectResult(data=data_) for data_ in result["return_object"]["data"]
        ]
