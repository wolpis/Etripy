from typing import Dict, Union

import aiohttp

from etripy.error import HTTPException
from etripy.model import AnalysisCode


class EtriRequest:
    base_url: str = "http://aiopen.etri.re.kr:8000"

    def __init__(self, access_key: str) -> None:
        self.access_key = access_key

    async def request(
        self, method: str, endpoint: str, data: Dict[str, Union[str, int]]
    ) -> Dict[str, Union[str, int]]:
        headers = {
            "Content-Type": "application/json; charset=UTF-8",
            "Authorization": self.access_key,
        }

        url = self.base_url + endpoint
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.request(method, url=url, json=data) as response:
                rescode = response.status
                if rescode == 200:
                    return await response.json()
                else:
                    raise HTTPException(f"Error Code : {rescode}")

    async def get_analysis_data(self, data: Dict[str, str], spoken: bool):
        if spoken:
            return await self.request(method="POST", endpoint="WiseNLU", data=data)
        else:
            return await self.request(
                method="POST", endpoint="/WiseNLU_spoken", data=data
            )
