import pytest
from etripy.client import VideoClient

file_id = "1723487644491.mp4"  # 동영상 업로드 후 반환되는 비디오 파일 ID


# 동영상 업로드 테스트
@pytest.mark.asyncio
async def test_video_upload(video: VideoClient):
    r = await video.video_upload(video_path="./assets/video.mp4")
    assert r


# 동영상 장면 분할 API 테스트
@pytest.mark.asyncio
async def test_video_parse(video: VideoClient):
    r = await video.video_parse(file_id=file_id)
    assert r
