from typing import List, Optional, Tuple, Union

from etripy.error import AnalysisException, QAException, SentencesException
from etripy.model import AnalysisCode, FileType, WikiType
from etripy.model.language import (AnalysisResult, CoreferenceResult,
                                   DocResult, DocUploadResult, HomonymResult,
                                   LegalResult, MRCResult, NELinkingResult,
                                   ParaphraseResult, PolysemyResult,
                                   WiKiResult, WiseQAnalResult, WordRelResult,
                                   WordResult)
from etripy.sync.http import SyncEtriRequest


class AnalysisClient(SyncEtriRequest):
    """
    ETRI 언어 처리 및 분석 클라이언트 클래스입니다. (동기 처리)
    #### access_key
    [ETRI 포털사이트](https://aiopen.etri.re.kr/)에서 발급받은 `access_key`를 입력합니다.
    """

    def __init__(self, access_key: str) -> None:
        super().__init__(access_key=access_key)

    def analysis(
        self, text: str, analysis_code: Union[AnalysisCode, str], spoken: bool = False
    ) -> Optional[AnalysisResult]:
        """
        ### - 언어 분석
        문어체 언어분석 및 구어체 언어분석 결과를 제공합니다.

        #### Parameter
        `analysis_code` : 요청할 분석 코드 (AnalysisCode 클래스 사용 권장)\n
        `text` : 분석할 자연어 문장으로서 UTF-8 인코딩된 텍스트만 지원
        """
        data = {
            "argument": {"analysis_code": analysis_code, "text": text},
        }
        result = self.get_analysis_data(data=data, spoken=spoken)
        try:
            if result["return_object"] == {}:
                return None
        except KeyError:
            if result["result"] != "0":
                raise AnalysisException(result["reason"])
        return AnalysisResult(data=result, **result["return_object"])

    def paraphrase(self, *sentences: Tuple[str]) -> Optional[ParaphraseResult]:
        """
        ### - 문장 패러프레이즈 인식
        문장 패러프레이즈 인식 API는 두 개의 문장이 동등한 의미를 가지는지 여부를 판별합니다.

        #### Parameter
        `sentences` : 분석할려는 문장에 대한 텍스트 (두 문장만 입력해주세요.)
        """
        if len(sentences) != 2:
            raise SentencesException(f"두 문장만 입력해주세요.\n현재 입력한 문장 수 : {len(sentences)}")
        data = {
            "argument": {"sentence1": sentences[0], "sentence2": sentences[1]},
        }
        result = self.request(method="POST", endpoint="/ParaphraseQA", data=data)
        try:
            if result["return_object"] == {}:
                return None
        except KeyError:
            if result["result"] != "0":
                raise AnalysisException(result["reason"])
        return ParaphraseResult(data=result, **result["return_object"])

    def wordinfo(self, word: str) -> Optional[WordResult]:
        """
        ### - 어휘 정보
        다양한 어휘지식을 통합한 WiseWordNet 어휘 지식베이스에 기반하여 어휘의 정보를 분석하는 기술로서 입력된 어휘에 대한 관련 제공합니다.

        #### Parameter
        `word` : 분석할 어휘 Text 로서 UTF-8 인코딩된 텍스트만 지원
        """
        data = {
            "argument": {"word": word},
        }
        result = self.request(method="POST", endpoint="/WiseWWN/Word", data=data)
        try:
            if result["return_object"] == {}:
                return None
        except KeyError:
            if result["result"] != "0":
                raise AnalysisException(result["reason"])
        return WordResult(data=result)

    def homonym(self, word: str):
        """
        ### - 동음이의어 정보
        국립국어원의 표준국어대사전에 등재된 어휘의 동음이의어(소리는 같으나 뜻이 다른 단어) 사전 정보를 조회하는 API로 입력된 어휘의 동음이의어 정보를 제공합니다.

        #### Parameter
        `word` : 동음이의어를 조회할 어휘 Text 로서 UTF-8 인코딩된 텍스트만 지원
        """
        data = {
            "argument": {"word": word},
        }
        result = self.request(method="POST", endpoint="/WiseWWN/Homonym", data=data)
        try:
            if result["return_object"] == {}:
                return None
        except KeyError:
            if result["result"] != "0":
                raise AnalysisException(result["reason"])
        return HomonymResult(data=result, **result["return_object"])

    def polysemy(self, word: str, homonym_code: str = None):
        """
        ### - 다의어 정보
        국립국어원의 표준국어대사전에 등재된 어휘의 다의어(두 가지 이상의 뜻을 가진 단어) 사전 정보를 조회하는 API로 입력된 어휘의 다의어 정보를 제공합니다.

        #### Parameter
        `word` : 다의어를 조회할 어휘 Text 로서 UTF-8 인코딩된 텍스트만 지원\n
        `homonym_code` : 다의어를 조회할 어휘의 동음이의어 코드 (필수 X)
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
        result = self.request(method="POST", endpoint="/WiseWWN/Polysemy", data=data)
        try:
            if result["return_object"] == {}:
                return None
        except KeyError:
            if result["result"] != "0":
                raise AnalysisException(result["reason"])
        return PolysemyResult(data=result, **result["return_object"])

    def wordrel(
        self,
        first_word: str,
        second_word: str,
        first_sense_id: str = None,
        second_sense_id: str = None,
    ):
        """
        ### - 어휘 간 유사도 분석
        다양한 어휘지식을 통합한 WiseWordNet 어휘 지식베이스에 기반하여 어휘 간 거리 정보를 분석하는 기술로서 입력된 여휘간 유사도 결과를 제공합니다.

        #### Parameter
        `first_word` : 비교 분석할 어휘 Text 로서 UTF-8 인코딩된 텍스트만 지원\n
        `first_sense_id` : 첫 번째 어휘의 의미 코드 (필수 X)\n
        `second_word` : 비교 분석 대상 어휘 Text 로서 UTF-8 인코딩된 텍스트만 지원\n
        `second_sense_id` : 두 번째 어휘의 의미 코드 (필수 X)\n
        """
        data = {
            "argument": {"first_word": first_word, "second_word": second_word},
        }
        if first_sense_id:
            data["argument"]["first_sense_id"] = first_sense_id
        if second_sense_id:
            data["argument"]["second_sense_id"] = second_sense_id
        result = self.request(method="POST", endpoint="/WiseWWN/WordRel", data=data)
        try:
            if result["return_object"] == {}:
                return None
        except KeyError:
            if result["result"] != "0":
                raise AnalysisException(result["reason"])
        return WordRelResult(data=result)

    def nelinking(self, contents: str) -> Optional[List[NELinkingResult]]:
        """
        ### - 개체 연결(NE Linking)
        개체 연결(entity linking) API는 문장 내에서 인식된 개체 멘션(entity mention)을 지식베이스의 개체(entity)와 연결하는 기술을 제공합니다.

        #### Parameter
        `contents` : 분석할 문단
        """
        data = {
            "argument": {"contents": contents},
        }
        result = self.request(method="POST", endpoint="/NELinking", data=data)
        try:
            if result["return_object"] == {}:
                return None
        except KeyError:
            if result["result"] != "0":
                raise AnalysisException(result["reason"])
        return [
            NELinkingResult(data=result, **result_)
            for result_ in result["return_object"]
        ]

    def coreference(self, text: str) -> Optional[CoreferenceResult]:
        """
        ### - 상호참조 해결
        상호참조 해결(coreference resolution) API는 어떤 개체에 대한 여러 표현들이 이루고 있는 참조관계를 밝히는 기술을 제공합니다.

        #### Parameter
        `text` : 분석할 문단
        """
        data = {
            "argument": {"text": text},
        }
        result = self.request(method="POST", endpoint="/Coreference", data=data)
        try:
            if result["return_object"] == {}:
                return None
        except KeyError:
            if result["result"] != "0":
                raise AnalysisException(result["reason"])
        result_ = {}
        result_["entity"] = result["return_object"]["entity"]
        return CoreferenceResult(data=result, **result_)


class QAClient(SyncEtriRequest):
    """
    ETRI 질의응답 클라이언트 클래스입니다. (동기 처리)
    #### access_key
    [ETRI 포털사이트](https://aiopen.etri.re.kr/)에서 발급받은 `access_key`를 입력합니다.
    """

    def __init__(self, access_key: str) -> None:
        super().__init__(access_key=access_key)

    def qanal(self, text: str) -> Optional[WiseQAnalResult]:
        """
        ### - 질문분석
        자연어 질문을 분석하여 의미를 이해하고 구조화하는 기술을 제공합니다.

        #### Parameter
        `text` : 분석할 질문 Text 로서 UTF-8 인코딩된 텍스트만 지원합니다.
        """
        data = {
            "argument": {"text": text},
        }
        result = self.request(method="POST", endpoint="/WiseQAnal", data=data)
        try:
            if result["return_object"] == {}:
                return None
        except KeyError:
            if result["result"] != "0":
                raise QAException(result["reason"])
        return WiseQAnalResult(data=result)

    def mrcservlet(self, question: str, passage: str) -> Optional[MRCResult]:
        """
        ### - 기계독해
        자연어로 쓰여진 단락과 사용자 질문이 주어졌을 때, 딥러닝 기술을 이용하여 단락 중 정답에 해당하는 영역을 찾는 기술을 제공합니다.

        #### Parameter
        `question` : 질문하고자 하는 Text 로서 UTF-8 인코딩된 텍스트만 지원\n
        `passage` : 질문의 답이 포함된 Text 로서 UTF-8 인코딩된 텍스트만 지원
        """
        data = {
            "argument": {"passage": passage, "question": question},
        }
        result = self.request(method="POST", endpoint="/MRCServlet", data=data)
        try:
            if result["return_object"] == {}:
                return None
        except KeyError:
            if result["result"] != "0":
                raise QAException(result["reason"])
        return MRCResult(data=result["return_object"]["MRCInfo"])

    def wiki(self, type: Union[WikiType, str], question: str) -> Optional[WiKiResult]:
        """
        ### - 위키백과 QA
        자연어로 기술된 질문의 의미를 분석하여, 위키백과 문서에서 정답과 신뢰도 및 검색 단락을 추론하여 제공합니다.

        #### Parameter
        `question` : 질문하고자 하는 Text 로서 UTF-8 인코딩된 텍스트만 지원\n
        `type` : 질문 응답 엔진의 종류 로서 UTF-8 인코딩된 텍스트만 지원 (WikiType 클래스 사용 추천)
        """
        data = {
            "argument": {"type": type, "question": question},
        }
        result = self.request(method="POST", endpoint="/WikiQA", data=data)
        try:
            if result["return_object"] == {}:
                return None
        except KeyError:
            if result["result"] != "0":
                raise QAException(result["reason"])
        return WiKiResult(data=result)

    def legal(self, question: str) -> Optional[LegalResult]:
        """
        ### - 법률 QA
        자연어로 기술된 질문의 의미를 분석하여, 법령문서에서 조 내용을 검색하고 정답을 추론하여 제공합니다.

        #### Parameter
        `question` : 질문하고자 하는 Text 로서 UTF-8 인코딩된 텍스트만 지원\n
        """
        data = {
            "argument": {"question": question},
        }
        result = self.request(method="POST", endpoint="/LegalQA", data=data)
        try:
            if result["return_object"] == {}:
                return None
        except KeyError:
            if result["result"] != "0":
                raise QAException(result["reason"])
        return LegalResult(data=result)

    def doc_upload(
        self,
        upload_file_path: str,
        file_type: Union[FileType, str] = "hwp",
        message: bool = False,
    ) -> Optional[DocUploadResult]:
        """
        ### - 행정문서 QA (문서등록)
        행정문서로 작성된 행정문서의 내용을 이해하여 사용자의 자연어 질문에 올바른 답과 근거를 제공합니다.

        #### Parameter
        `upload_file_path` : 업로드 할려는 문서 파일의 경로\n
        `file_type` : 업로드 할려는 문서 파일의 확장자(hwp/hwpx)\n
        `message` : 파일 업로드 메세지를 출력합니다.
        """
        if message:
            print("파일 업로드 중...")
        result = self.file_upload(
            upload_file_path=upload_file_path, file_type=file_type
        )
        try:
            if result["return_object"] == {}:
                return None
        except KeyError:
            if result["result"] != "0":
                raise QAException(result["reason"])
        return DocUploadResult(data=result)

    def doc(self, doc_key: str, question: str) -> Optional[DocResult]:
        """
        ### - 행정문서 QA (질의응답)
        행정문서로 작성된 행정문서의 내용을 이해하여 사용자의 자연어 질문에 올바른 답과 근거를 제공합니다.

        #### Parameter
        `doc_key` : 문서 등록 API에서 리턴 받은 doc key 로서 UTF-8 인코딩된 텍스트만 지원\n
        `question` : 질문하고자 하는 text로서 UTF-8 인코딩된 텍스트만 지원
        """
        data = {
            "argument": {"doc_key": doc_key, "question": question},
        }
        result = self.request(method="POST", endpoint="/DocQA", data=data)
        try:
            if result["return_object"] == {}:
                return None
        except KeyError:
            if result["result"] != "0":
                raise QAException(result["reason"])
        return DocResult(data=result)
