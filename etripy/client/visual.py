import base64
from typing import Optional

from etripy.error import VisualImageException, VisualVideoException
from etripy.http import EtriRequest
from etripy.model.visual.image import (
    FaceDeIDResult,
    HumanParsingResult,
    HumanStatusResult,
    ObjectDetectResult,
)
from etripy.model.visual.video import VideoParseResult


class ImageClient(EtriRequest):
    """
    ETRI 시각지능 이미지 클라이언트 클래스입니다.
    #### access_key
    [ETRI 포털사이트](https://aiopen.etri.re.kr/)에서 발급받은 `access_key`를 입력합니다.
    """

    def __init__(self, access_key: str) -> None:
        super().__init__(access_key=access_key)

    async def object_detect(
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
        result = await self.request(method="POST", endpoint="/HumanParsing", data=data)
        try:
            if result["return_object"] == {}:
                return None
        except KeyError:
            if result["result"] != "0":
                raise VisualImageException(result["reason"])

        keys = list(result["return_object"].keys())
        return [ObjectDetectResult(data=result["return_object"][key]) for key in keys]

    async def face_deid(self, file_path: str) -> Optional[list[FaceDeIDResult]]:
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
    ) -> Optional[list[HumanStatusResult]]:
        """
        ### - 사람 상태 이해 API
        영상 내에 존재하는 모든 사람 영역을 자동으로 검출하고 해당 사람의 상태를 판단하여 사용자에게 그 결과를 출력해주게 됩니다. 
        본 기술은 도심에서 주취, 기절 등과 같이 쓰러져 도움이 필요한 사람을 자동으로 검출하여 위험 상황 발생 전에 선제적으로 대응할 수 있는 시스템 개발에 사용 될 수 있습니다. 

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
        result = await self.request(method="POST", endpoint="/HumanStatus", data=data)
        try:
            if result["return_object"] == {}:
                return None
        except KeyError:
            if result["result"] != "0":
                raise VisualImageException(result["reason"])
        return [
            HumanStatusResult(data=data_, img_url=result["return_object"][0]["data"][0])
            for data_ in result["return_object"][0]["data"][1:]
        ]


class VideoClient(EtriRequest):
    """
    ETRI 시각지능 동영상 클라이언트 클래스입니다.\n
    동영상의 최대 용량은 50MB까지 업로드할 수 있습니다.\n
    동영상의 영상 길이는 최소 5초 이상되어야 합니다.\n
    동영상의 영상 길이는 최대 5분 미만이어야 합니다.\n
    #### access_key
    [ETRI 포털사이트](https://aiopen.etri.re.kr/)에서 발급받은 `access_key`를 입력합니다.
    """

    def __init__(self, access_key: str) -> None:
        super().__init__(access_key=access_key)

    async def video_upload(self, video_path: str) -> str:
        """
        비디오를 서버에 등록하여, 비디오 파일 ID를 반환합니다.

        #### Parameter\n
        `video_path` : API 사용 요청 시 분석을 위해 전달할 비디오 파일 경로
        """
        result = await self.file_upload(upload_file_path=video_path)
        try:
            if result["return_object"] == {}:
                return None
        except KeyError:
            if result["result"] != "0":
                raise VisualVideoException(result["reason"])

        return result["return_object"]["file_id"]

    async def video_parse(self, file_id: str) -> list[VideoParseResult]:
        """
        ### - 장면 분할 API
        동영상에서 장면이 변화하는 시점을 탐지하여, 동영상을 썸네일로 요약하거나 편집을 용이하게 하는 포인트를 제공합니다.
        동영상의 각 프레임의 특성 추출 후 특성이 시간적으로 크게 변화하는 시점을 탐지하여 출력합니다.

        #### Parameter\n
        `file_id` : 장면분할처리를 위한 file의 ID
        """
        data = {"argument": {"file_id": file_id}}
        result = await self.request(
            method="POST", endpoint="/VideoParse/status", data=data
        )
        try:
            if result["return_object"] == {}:
                return None
        except KeyError:
            if result["result"] != "0":
                raise VisualVideoException(result["reason"])

        return [
            VideoParseResult(**data_) for data_ in result["return_object"]["result"]
        ]

    async def video_parse_for_path(self, file_path: str) -> list[VideoParseResult]:
        """
        ### - 장면 분할 API
        동영상에서 장면이 변화하는 시점을 탐지하여, 동영상을 썸네일로 요약하거나 편집을 용이하게 하는 포인트를 제공합니다.
        동영상의 각 프레임의 특성 추출 후 특성이 시간적으로 크게 변화하는 시점을 탐지하여 출력합니다.\n

        같은 동영상을 자주 분석하는 경우 가급적 `video_parse`를 사용하십시오.

        #### Parameter\n
        `file_path` : API 사용 요청 시 분석을 위해 전달할 비디오 파일 경로
        """
        data = {"argument": {"file_id": await self.video_upload(video_path=file_path)}}
        result = await self.request(
            method="POST", endpoint="/VideoParse/status", data=data
        )
        try:
            if result["return_object"] == {}:
                return None
        except KeyError:
            if result["result"] != "0":
                raise VisualVideoException(result["reason"])

        return [
            VideoParseResult(**data_) for data_ in result["return_object"]["result"]
        ]
