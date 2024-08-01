import base64
import io
from typing import Optional, Union

from pydub import AudioSegment

from etripy.error import AudioFileException, VoiceRecognitionException
from etripy.http import EtriRequest
from etripy.model import LanguageCodeType
from etripy.model.voice import RecognitionResult


class VoiceClient(EtriRequest):
    """
    ETRI 음성지능 클라이언트 클래스입니다.
    #### access_key
    [ETRI 포털사이트](https://aiopen.etri.re.kr/)에서 발급받은 `access_key`를 입력합니다.
    """

    def __init__(self, access_key: str) -> None:
        super().__init__(access_key=access_key)

    def convert_to_raw(self, audioFilePath) -> bytes:
        audio = AudioSegment.from_file(audioFilePath)
        audio = audio.set_frame_rate(16000).set_sample_width(2).set_channels(1)

        raw_data = io.BytesIO()
        audio.export(raw_data, format="raw")
        return raw_data.getvalue()

    async def recognition(
        self, language_code: Union[LanguageCodeType, str], audio_path: str
    ) -> Optional[RecognitionResult]:
        try:
            audioContents = base64.b64encode(self.convert_to_raw(audio_path)).decode(
                "utf8"
            )
        except Exception as e:
            raise AudioFileException(f"오디오 파일을 다시 한번 확인해주세요. : {e}")

        data = {"argument": {"language_code": language_code, "audio": audioContents}}

        result = await self.request(
            method="POST", endpoint="/WiseASR/Recognition", data=data
        )
        try:
            if result["return_object"] == {}:
                return None
        except KeyError:
            if result["result"] != "0":
                raise VoiceRecognitionException(result["reason"])
        return RecognitionResult(**result["return_object"])
