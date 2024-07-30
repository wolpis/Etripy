from etripy.http import EtriRequest
from etripy.model import LanguageCodeType
from typing import Union
from etripy.error import AudioFileException

import base64

class VoiceClient(EtriRequest):
    """
    ETRI 음성지능 클라이언트 클래스입니다.
    #### access_key
    [ETRI 포털사이트](https://aiopen.etri.re.kr/)에서 발급받은 `access_key`를 입력합니다.
    """

    def __init__(self, access_key: str) -> None:
        super().__init__(access_key=access_key)

    async def recognition(self, language_code: Union[LanguageCodeType, str], audio_path: str):
        try:
            file = open(audio_path, 'rb')
            audioContents = base64.b64encode(file.read()).decode("utf8")
            file.close()
        except Exception as e:
            raise AudioFileException(f"오디오 파일을 다시 한번 확인해주세요. : {audioContents}")
        
        data = {    
            "argument": {
                "language_code": language_code,
                "audio": audioContents
            }
        }

        result = await self.request(method="POST", endpoint="/WiseASR/Recognition", data=data)
        print(result)
        
