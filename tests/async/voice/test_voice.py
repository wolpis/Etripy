import pytest
from etripy.client import LanguageCodeType, VoiceClient


# 음성 인식 테스트
@pytest.mark.asyncio
async def test_recognition(voice: VoiceClient):
    r = await voice.recognition(
        language_code=LanguageCodeType.korean, audio_path=r"./test.mp3"
    )
    assert r.recognized


# 발음 평가 테스트
@pytest.mark.asyncio
async def test_pronunciation(voice: VoiceClient):
    r = await voice.pronunciation(
        language_code=LanguageCodeType.korean,
        speaker_language_code=LanguageCodeType.korean,
        audio_path=r"./test.mp3",
    )
    assert r.recognized
