import json
import os
from typing import Any, Dict, Union

import aiohttp

from etripy.error import HTTPException
from etripy.model import FileType


class EtriRequest:
    base_url: str = "http://aiopen.etri.re.kr:8000"

    def __init__(self, access_key: str) -> None:
        self.access_key = access_key

    async def request(
        self, method: str, endpoint: str, data: Dict[str, Any]
    ) -> Dict[str, Any]:
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
                    text_data = await response.text()
                    raise HTTPException(f"Error Code {rescode} : {text_data}")

    async def request_file_upload(self, data: aiohttp.FormData) -> Dict[str, Any]:
        headers = {
            "Authorization": self.access_key,
        }

        url = self.base_url + "/DocUpload"
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.request("POST", url=url, data=data) as response:
                rescode = response.status
                if rescode == 200:
                    return await response.json()
                else:
                    text_data = await response.text()
                    raise HTTPException(f"Error Code {rescode} : {text_data}")

    async def get_analysis_data(self, data: Dict[str, Any], spoken: bool):
        if spoken:
            return await self.request(
                method="POST", endpoint="/WiseNLU_spoken", data=data
            )
        else:
            return await self.request(method="POST", endpoint="/WiseNLU", data=data)

    async def file_upload(
        self, upload_file_path: str, file_type: Union[FileType, str] = "hwp"
    ):
        file = open(upload_file_path, "rb")
        file_content = file.read()
        file.close()

        requestJson = {"argument": {"type": file_type}}

        form_data = aiohttp.FormData()
        form_data.add_field(
            "json", json.dumps(requestJson), content_type="application/json"
        )
        form_data.add_field(
            "doc_file",
            file_content,
            filename=os.path.basename(file.name),
            content_type="application/octet-stream",
        )
        return await self.request_file_upload(data=form_data)
