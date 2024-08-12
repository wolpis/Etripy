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
    """
    ETRI 시각지능 이미지 클라이언트 클래스입니다. (동기 처리)
    #### access_key
    [ETRI 포털사이트](https://aiopen.etri.re.kr/)에서 발급받은 `access_key`를 입력합니다.
    """

    def __init__(self, access_key: str) -> None:
        super().__init__(access_key=access_key)

    def object_detect(
        self, file_path: str, file_type: str = "auto"
    ) -> Optional[list[ObjectDetectResult]]:
        """
        ### - 객체검출 API
        이미지에서 사람, 자동차 등 일반적으로 나타나는 다양한 종류의 객체 카테고리를 분류하고 객체의 위치정보(박스 좌표)를 감지할 수 있는 기술로 활용됩니다.
        영상 데이터에서 다양한 형태의 객체를 인식하는 객체 인식기를 통해 객체 인식 결과를 제공합니다.

        #### Parameter\n
        `file_path` : 객체검출 하고자 하는 이미지의 경로.\n
        `file_type` : 이미지 파일의 확장자
        """
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
        """
        ### - 사람속성 검출 API
        이미지에서 사람을 검출하고 사람의 속성 부분인 머리, 상의, 하의 등을 분류하고 각 사람과 속성의 위치정보(박스 좌표, 속성 부분 영역)를 감지할 수 있는 기술로 활용됩니다.\n
        영상 데이터에서 보이는 사람의 속성을 인식하고 인식 결과와 속성의 색상 정보를 제공합니다.

        #### Parameter\n
        `file_path` : 사람속성 검출 하고자 하는 이미지의 경로.\n
        `file_type` : 이미지 파일의 확장자
        """
        if file_type == "auto":
            file_type = file_path.split(".")[-1]

        file = open(file_path, "rb")
        imageContents = base64.b64encode(file.read()).decode("utf8")
        file.close()

        data = {"argument": {"type": file_type, "file": imageContents}}
        result = self.request(method="POST", endpoint="/HumanParsing", data=data)
        try:
            if result["return_object"] == {}:
                return None
        except KeyError:
            if result["result"] != "0":
                raise VisualImageException(result["reason"])

        keys = list(result["return_object"].keys())
        return [ObjectDetectResult(data=result["return_object"][key]) for key in keys]

    def face_deid(self, file_path: str):
        """
        ### - 얼굴 비식별화 API
        영상 내에 존재하는 얼굴 영역을 자동으로 검출하고 얼굴 영역 영상처리를 수행하여 개인 정보인 얼굴을 비식별화 처리를 하게 됩니다.\n
        본 기술은 타인이 포함된 영상을 외부에 공유 시 개인 정보를 보호할 수 있는 목적으로 활용될 수 있으며, 모든 얼굴이 아닌 특정 얼굴을 제외한 비식별화 용도로 응용될 수 있습니다.

        #### Parameter\n
        `file_path` : 얼굴 비식별화를 적용하고자 하는 이미지의 경로.
        """
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
        """
        ### - 얼굴 비식별화 API
        영상 내에 존재하는 얼굴 영역을 자동으로 검출하고 얼굴 영역 영상처리를 수행하여 개인 정보인 얼굴을 비식별화 처리를 하게 됩니다.\n
        본 기술은 타인이 포함된 영상을 외부에 공유 시 개인 정보를 보호할 수 있는 목적으로 활용될 수 있으며, 모든 얼굴이 아닌 특정 얼굴을 제외한 비식별화 용도로 응용될 수 있습니다.

        #### Parameter\n
        `file_path` : 사람 상태 이해를 수행하고자 하는 이미지의 경로.\n
        `file_type` : 이미지 파일의 확장자
        """
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
            HumanStatusResult(data=data_, img_url=result["return_object"]["data"][0])
            for data_ in result["return_object"]["data"][1:]
        ]
