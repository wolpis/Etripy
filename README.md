<div align="center">
  <h1>Etripy</h1>
  <img src="https://github.com/VoidAsMad/ETRI/assets/103942316/bce15af5-e0c4-411e-a058-320dfdf8c720"></img>
</div>

<div align="center">
  <h2>누구나 쉽게 인공지능 오픈 API/DATA 서비스를</h2>
</div>

누구나 손쉽게 ETRI에서 제공하는 오픈 API를 사용할 수 있어요!<br>
> **동기 비동기 모두 지원합니다!**<br>
> OPEN ETRI API의 모든 엔드포인트가 래핑되어 있습니다.<br>
> [자세한 사용법은 여기를 참조해주세요!]()<br>

## Installation
```
$ pip install etripy
```
## Example
### 문장 패러플라이즈 인식[동기]
```py
작성예정
```
### 문장 패러플라이즈 인식[비동기]
```py
import asyncio
from etripy.client import AnalysisClient

async def main():
    etri = AnalysisClient(access_key="샘플키") # 필수 인자(API)가 들어가는 곳입니다.
    data = await etri.paraphrase("그녀는 책을 읽는 것을 좋아한다.", "독서는 그녀의 취미이다.")
    print(data.is_paraphrase) # 두 문장의 의미가 동등할 경우 True를, 아니라면 False를 반환한다.

asyncio.run(main())
```