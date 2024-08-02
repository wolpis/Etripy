import base64
import io
from typing import Optional, Union

from etripy.error import (
    AudioFileException,
    VoicePronunciationException,
    VoiceRecognitionException,
)
from etripy.sync.http import SyncEtriRequest
from etripy.model import LanguageCodeType
from etripy.model.voice import PronunciationResult, RecognitionResult
from pydub import AudioSegment


class VoiceClient(SyncEtriRequest):
    """
    ETRI 음성지능 클라이언트 클래스입니다. (동기 처리)
    #### access_key
    [ETRI 포털사이트](https://aiopen.etri.re.kr/)에서 발급받은 `access_key`를 입력합니다.
    """

    def __init__(self, access_key: str) -> None:
        super().__init__(access_key=access_key)

    def __convert_to_raw(self, audioFilePath) -> bytes:
        """오디오 파일을 API가 지원하는 파일의 형식으로 변환합니다."""
        audio = AudioSegment.from_file(audioFilePath)
        audio = audio.set_frame_rate(16000).set_sample_width(2).set_channels(1)

        raw_data = io.BytesIO()
        audio.export(raw_data, format="raw")
        return raw_data.getvalue()

    def recognition(
        self, language_code: Union[LanguageCodeType, str], audio_path: str
    ) -> Optional[RecognitionResult]:
        """
        ### - 음성인식 기술
        사용자가 발성한 녹음된 입력 음성 데이터(단위 파일 또는 버퍼)를 음성인식 서버로 전달하여 문자(텍스트)로 제공합니다.

        #### Parameter
        `language_code` : 음성인식의 입력 음성 언어 코드입니다. 요청할 수 있는 언어 코드는 LanguageCodeType 클래스를 참조하십시오.\n
        `audio_path` : 음성인식을 할 녹음된 음성파일의 경로입니다.
        """
        try:
            audioContents = base64.b64encode(self.__convert_to_raw(audio_path)).decode(
                "utf8"
            )
        except Exception as e:
            raise AudioFileException(f"오디오 파일을 다시 한번 확인해주세요. : {e}")

        data = {"argument": {"language_code": language_code, "audio": audioContents}}

        result = self.request(
            method="POST", endpoint="/WiseASR/Recognition", data=data
        )
        try:
            if result["return_object"] == {}:
                return None
        except KeyError:
            if result["result"] != "0":
                raise VoiceRecognitionException(result["reason"])
        return RecognitionResult(**result["return_object"])

    def pronunciation(
        self,
        language_code: Union[LanguageCodeType, str],
        speaker_language_code: Union[LanguageCodeType, str],
        audio_path: str,
        script: Optional[str] = None,
    ) -> Optional[PronunciationResult]:
        """
        ### - 발음평가 기술
        한국인을 비롯한 비원어민 영어 발성 및 외국인의 한국어 음성에 대해 문장별 발음 수준을 측정하여 데이터를 제공합니다. 

        #### Parameter
        `language_code` : 발음평가의 입력 음성 언어 코드입니다. 요청할 수 있는 언어 코드는 korean, english입니다.\n
        `speaker_language_code` : 화자의 음성 언어 코드입니다. 요청할 수 있는 언어 코드는 korean, english입니다.\n
        `audio_path` : 음성인식을 할 녹음된 음성파일의 경로입니다.\n
        `script` : 녹음된 음성파일의 제시 문장입니다. API 요청 시 script가 포함되지 않는 경우 비원어민 영어 음성인식을 수행한 이후 인식 결과에 대한 발음평가 점수를 제공합니다.
        """
        if (
            language_code != LanguageCodeType.korean
            and language_code != LanguageCodeType.english
        ):
            raise Exception("language_type 파라미터는 'korean' 또는 'english'만 사용 가능합니다.")
        if speaker_language_code == LanguageCodeType.korean:
            endpoint = "PronunciationKor"
        elif speaker_language_code == LanguageCodeType.english:
            endpoint - "Pronunciation"
        else:
            raise Exception(
                "author_language_code 파라미터는 'korean' 또는 'english'만 사용 가능합니다."
            )
        try:
            audioContents = base64.b64encode(self.__convert_to_raw(audio_path)).decode(
                "utf8"
            )
        except Exception as e:
            raise AudioFileException(f"오디오 파일을 다시 한번 확인해주세요. : {e}")

        data = {
            "argument": {
                "language_code": language_code,
                "script": script,
                "audio": audioContents,
            }
        }

        result = self.request(
            method="POST", endpoint=f"/WiseASR/{endpoint}", data=data
        )
        try:
            if result["return_object"] == {}:
                return None
        except KeyError:
            if result["result"] != "0":
                raise VoicePronunciationException(result["reason"])
        return PronunciationResult(**result["return_object"])
