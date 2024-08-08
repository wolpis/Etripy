import base64
from typing import Optional

from etripy.error import VisualImageException
from etripy.model.visual.image import (
    FaceDeIDResult,
    HumanParsingResult,
    HumanStatusResult,
    ObjectDetectResult,
)
from etripy.sync.http import SyncEtriRequest


class ImageClient(SyncEtriRequest):
    def __init__(self, access_key: str) -> None:
        super().__init__(access_key=access_key)

    def object_detect(
        self, file_path: str, file_type: str = "auto"
    ) -> Optional[list[ObjectDetectResult]]:
        if file_type == "auto":
            file_type = file_path.split(".")[-1]

        file = open(file_path, "rb")
        imageContents = base64.b64encode(file.read()).decode("utf8")
        file.close()

        data = {"argument": {"type": file_type, "file": imageContents}}
        result = self.request(method="POST", endpoint="/ObjectDetect", data=data)
        try:
            if result["return_object"] == {}:
                return None
        except KeyError:
            if result["result"] != "0":
                raise VisualImageException(result["reason"])
        return [
            ObjectDetectResult(data=data_) for data_ in result["return_object"]["data"]
        ]

    def human_parsing(
        self, file_path: str, file_type: str = "auto"
    ) -> Optional[list[HumanParsingResult]]:
        if file_type == "auto":
            file_type = file_path.split(".")[-1]

        file = open(file_path, "rb")
        imageContents = base64.b64encode(file.read()).decode("utf8")
        file.close()

        data = {"argument": {"type": file_type, "file": imageContents}}
        result: dict[str, dict[str, str]] = self.request(
            method="POST", endpoint="/HumanParsing", data=data
        )
        try:
            if result["return_object"] == {}:
                return None
        except KeyError:
            if result["result"] != "0":
                raise VisualImageException(result["reason"])

        keys = list(result["return_object"].keys())
        return [ObjectDetectResult(data=result["return_object"][key]) for key in keys]

    def face_deid(self, file_path: str):
        file = open(file_path, "rb")
        imageContents = base64.b64encode(file.read()).decode("utf8")
        file.close()

        data = {"argument": {"file": imageContents, "type": "1"}}
        result = self.request(method="POST", endpoint="/FaceDeID", data=data)
        try:
            if result["return_object"] == {}:
                return None
        except KeyError:
            if result["result"] != "0":
                raise VisualImageException(result["reason"])
        return [
            FaceDeIDResult(data=data_) for data_ in result["return_object"]["results"]
        ]

    def human_status(
        self, file_path: str, file_type: str = "auto"
    ) -> Optional[list[HumanStatusResult]]:
        if file_type == "auto":
            file_type = file_path.split(".")[-1]

        file = open(file_path, "rb")
        imageContents = base64.b64encode(file.read()).decode("utf8")
        file.close()

        data = {"argument": {"type": file_type, "file": imageContents}}
        result = self.request(method="POST", endpoint="/HumanStatus", data=data)
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
