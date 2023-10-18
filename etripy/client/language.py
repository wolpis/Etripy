import json
import os
from typing import List, Tuple, Union

from etripy.error import SentencesException
from etripy.http import EtriRequest
from etripy.model import AnalysisCode, FileType, WikiType


class Analysis(EtriRequest):
    """
    ETRI 언어 처리 및 분석 클라이언트 클래스입니다.
    #### access_key
    [ETRI 포털사이트](https://aiopen.etri.re.kr/)에서 발급받은 `access_key`를 입력합니다.
    """

    def __init__(self, access_key: str) -> None:
        super().__init__(access_key=access_key)

    async def analysis(
        self, text: str, analysis_code: Union[AnalysisCode, str], spoken: bool = False
    ):
        """
        ### - 언어 분석
        문어체 언어분석 및 구어체 언어분석 결과를 제공합니다.
        """
        data = {
            "argument": {"analysis_code": analysis_code, "text": text},
        }
        return await self.get_analysis_data(data=data, spoken=spoken)

    async def paraphrase(self, *sentences: Tuple[str]):
        """
        ### - 문장 패러프레이즈 인식
        문장 패러프레이즈 인식 API는 두 개의 문장이 동등한 의미를 가지는지 여부를 판별합니다.
        """
        if len(sentences) != 2:
            raise SentencesException("두 문장만 입력해주세요. 현재 입력한 문장 수 : " + len(sentences))
        data = {
            "argument": {"sentence1": sentences[0], "sentence2": sentences[1]},
        }
        return await self.request(method="POST", endpoint="/ParaphraseQA", data=data)

    async def wordinfo(self, word: str):
        """
        ### - 어휘 정보
        다양한 어휘지식을 통합한 WiseWordNet 어휘 지식베이스에 기반하여 어휘의 정보를 분석하는 기술로서 입력된 어휘에 대한 관련 제공합니다.
        """
        data = {
            "argument": {"word": word},
        }
        return await self.request(method="POST", endpoint="/WiseWWN/Word", data=data)

    async def homonym(self, word: str):
        """
        ### - 동음이의어 정보
        국립국어원의 표준국어대사전에 등재된 어휘의 동음이의어(소리는 같으나 뜻이 다른 단어) 사전 정보를 조회하는 API로 입력된 어휘의 동음이의어 정보를 제공합니다.
        """
        data = {
            "argument": {"word": word},
        }
        return await self.request(method="POST", endpoint="/WiseWWN/Homonym", data=data)

    async def polysemy(self, word: str, homonym_code: str = None):
        """
        ### - 다의어 정보
        국립국어원의 표준국어대사전에 등재된 어휘의 다의어(두 가지 이상의 뜻을 가진 단어) 사전 정보를 조회하는 API로 입력된 어휘의 다의어 정보를 제공합니다.
        """
        if homonym_code:
            data = {
                "request_id": "reserved field",
                "argument": {"word": word, "homonym_code": homonym_code},
            }
        else:
            data = {
                "request_id": "reserved field",
                "argument": {"word": word},
            }
        return await self.request(
            method="POST", endpoint="/WiseWWN/Polysemy", data=data
        )

    async def wordrel(
        self,
        first_word: str,
        second_word: str,
        first_sense_id: str = None,
        second_sense_id: str = None,
    ):
        """
        ### - 어휘 간 유사도 분석
        다양한 어휘지식을 통합한 WiseWordNet 어휘 지식베이스에 기반하여 어휘 간 거리 정보를 분석하는 기술로서 입력된 여휘간 유사도 결과를 제공합니다.
        """
        data = {
            "argument": {"first_word": first_word, "second_word": second_word},
        }
        if first_sense_id:
            data["argument"]["first_sense_id"] = first_sense_id
        if second_sense_id:
            data["argument"]["second_sense_id"] = second_sense_id
        return await self.request(method="POST", endpoint="/WiseWWN/WordRel", data=data)

    async def nelinking(self, contents: str):
        """
        ### - 개체 연결(NE Linking)
        개체 연결(entity linking) API는 문장 내에서 인식된 개체 멘션(entity mention)을 지식베이스의 개체(entity)와 연결하는 기술을 제공합니다.
        """
        data = {
            "argument": {"contents": contents},
        }
        return await self.request(
            method="POST", endpoint="/WiseWWN/NELinking", data=data
        )

    async def coreference(self, text: str):
        """
        ### - 상호참조 해결
        상호참조 해결(coreference resolution) API는 어떤 개체에 대한 여러 표현들이 이루고 있는 참조관계를 밝히는 기술을 제공합니다.
        """
        data = {
            "argument": {"text": text},
        }
        return await self.request(
            method="POST", endpoint="/WiseWWN/Coreference", data=data
        )


class QA(EtriRequest):
    """
    ETRI 질의응답 클라이언트 클래스입니다.
    #### access_key
    [ETRI 포털사이트](https://aiopen.etri.re.kr/)에서 발급받은 `access_key`를 입력합니다.
    """

    def __init__(self, access_key: str) -> None:
        super().__init__(access_key=access_key)

    async def qanal(self, text: str):
        """
        ### - 질문분석
        자연어 질문을 분석하여 의미를 이해하고 구조화하는 기술을 제공합니다.
        """
        data = {
            "argument": {"text": text},
        }
        return await self.request(method="POST", endpoint="/WiseQAnal", data=data)

    async def mrcservlet(self, question: str, passage: str):
        """
        ### - 기계독해
        자연어로 쓰여진 단락과 사용자 질문이 주어졌을 때, 딥러닝 기술을 이용하여 단락 중 정답에 해당하는 영역을 찾는 기술을 제공합니다.
        """
        data = {
            "argument": {"passage": passage, "question": question},
        }
        return await self.request(method="POST", endpoint="/MRCServlet", data=data)

    async def wiki(self, type: Union[WikiType, str], question: str):
        """
        ### - 위키백과 QA
        자연어로 기술된 질문의 의미를 분석하여, 위키백과 문서에서 정답과 신뢰도 및 검색 단락을 추론하여 제공합니다.
        """
        data = {
            "argument": {"type": type, "question": question},
        }
        return await self.request(method="POST", endpoint="/WikiQA", data=data)

    async def legal(self, question: str):
        """
        ### - 법률 QA
        자연어로 기술된 질문의 의미를 분석하여, 법령문서에서 조 내용을 검색하고 정답을 추론하여 제공합니다.
        """
        data = {
            "argument": {"question": question},
        }
        return await self.request(method="POST", endpoint="/LegalQAt", data=data)

    async def doc_upload(
        self, upload_file_path: str, file_type: Union[FileType, str] = "hwp"
    ):
        """
        ### - 행정문서 QA (문서등록)
        행정문서로 작성된 행정문서의 내용을 이해하여 사용자의 자연어 질문에 올바른 답과 근거를 제공합니다.
        """
        file = open(upload_file_path, "rb")
        file_content = file.read()
        file.close()

        requestJson = {"argument": {"type": file_type}}
        data = {
            "json": json.dumps(requestJson),
            "doc_file": (os.path.basename(file.name), file_content),
        }
        return await self.request(method="POST", endpoint="/DocUpload", data=data)

    async def doc(self, doc_key: str, question: str):
        """
        ### - 행정문서 QA (질의응답)
        행정문서로 작성된 행정문서의 내용을 이해하여 사용자의 자연어 질문에 올바른 답과 근거를 제공합니다.
        """
        data = {
            "argument": {"doc_key": doc_key, "question": question},
        }
        return await self.request(method="POST", endpoint="/DocQA", data=data)
