import base64
from typing import Optional

from etripy.error import VisualImageException
from etripy.http import EtriRequest
from etripy.model.visual.image import (
    FaceDeIDResult,
    HumanParsingResult,
    HumanStatusResult,
    ObjectDetectResult,
)


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

    async def human_parsing(
        self, file_path: str, file_type: str = "auto"
    ) -> Optional[list[HumanParsingResult]]:
        if file_type == "auto":
            file_type = file_path.split(".")[-1]

        file = open(file_path, "rb")
        imageContents = base64.b64encode(file.read()).decode("utf8")
        file.close()

        data = {"argument": {"type": file_type, "file": imageContents}}
        result = await self.request(method="POST", endpoint="/HumanParsing", data=data)
        try:
            if result["return_object"] == {}:
                return None
        except KeyError:
            if result["result"] != "0":
                raise VisualImageException(result["reason"])

        keys = list(result["return_object"].keys())
        return [HumanParsingResult(data=result["return_object"][key]) for key in keys]

    async def face_deid(self, file_path: str):
        file = open(file_path, "rb")
        imageContents = base64.b64encode(file.read()).decode("utf8")
        file.close()

        data = {"argument": {"file": imageContents, "type": "1"}}
        result = await self.request(method="POST", endpoint="/FaceDeID", data=data)
        try:
            if result["return_object"] == {}:
                return None
        except KeyError:
            if result["result"] != "0":
                raise VisualImageException(result["reason"])
        return [
            FaceDeIDResult(data=data_) for data_ in result["return_object"]["results"]
        ]

    async def human_status(
        self, file_path: str, file_type: str = "auto"
    ) -> Optional[list[HumanStatusResult]]:  ## 현재 API 이슈 있음
        if file_type == "auto":
            file_type = file_path.split(".")[-1]

        file = open(file_path, "rb")
        imageContents = base64.b64encode(file.read()).decode("utf8")
        file.close()

        data = {"argument": {"type": file_type, "file": imageContents}}
        result = await self.request(method="POST", endpoint="/HumanStatus", data=data)
        try:
            if result["return_object"] == {}:
                return None
        except KeyError:
            if result["result"] != "0":
                raise VisualImageException(result["reason"])
        return [
            HumanStatusResult(data=data_)
            for data_ in result["return_object"]["results"]
        ]
        print(result)
