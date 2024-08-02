import json
import os
from typing import Any, Dict, Union

import requests
from etripy.error import HTTPException
from etripy.model import FileType


class SyncEtriRequest:
    base_url: str = "http://aiopen.etri.re.kr:8000"

    def __init__(self, access_key: str) -> None:
        self.access_key = access_key

    def request(
        self, method: str, endpoint: str, data: Dict[str, Union[str, int]]
    ) -> Dict[str, Any]:
        headers = {
            "Content-Type": "application/json; charset=UTF-8",
            "Authorization": self.access_key,
        }
        url = self.base_url + endpoint
        response = requests.request(method, url=url, headers=headers, json=data)
        rescode = response.status_code
        if rescode == 200:
            return response.json()
        else:
            raise HTTPException(f"Error Code : {rescode} : {response.text}")

    def request_file_upload(self, data: Dict[str, Any]) -> Dict[str, Any]:
        headers = {"Authorization": self.access_key}
        url = self.base_url + "/DocUpload"
        response = requests.request(
            "POST",
            url=url,
            headers=headers,
            data={"json": data["json"]},
            files={"doc_file": data["doc_file"]},
        )
        rescode = response.status_code
        if rescode == 200:
            return response.json()
        else:
            raise HTTPException(f"Error Code : {rescode} : {response.text}")

    def get_analysis_data(self, data: Dict[str, Union[str, int]], spoken: bool):
        if spoken:
            return self.request(method="POST", endpoint="/WiseNLU_spoken", data=data)
        else:
            return self.request(method="POST", endpoint="/WiseNLU", data=data)

    def file_upload(
        self, upload_file_path: str, file_type: Union[FileType, str] = "hwp"
    ):
        with open(upload_file_path, "rb") as file:
            file_content = file.read()

        requestJson = {"argument": {"type": file_type}}

        data = {
            "json": json.dumps(requestJson),
            "doc_file": (os.path.basename(upload_file_path), file_content),
        }
        return self.request_file_upload(data=data)
