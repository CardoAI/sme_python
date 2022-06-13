from contextlib import ContextDecorator
from functools import cached_property

import requests

from sme_sdk.blob import BlobStorageClient
from sme_sdk.exceptions import BatchCreationFailed, BatchResultRetrieveFailed, LoginFailed
from sme_sdk.types import BatchResultID, LoginResponseType
from sme_sdk.urls import Url


class APIClient(ContextDecorator):
    # todo: get hostname from environment variable
    PROTOCOL = 'http'
    HOST = 'localhost:8000'
    ACCESS_TOKEN_NAME = 'access_token'
    FILE_URL_NAME = 'file_url'

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self._access_token = None

    def __enter__(self):
        login_response = self.login()
        self._access_token = login_response['access_token']

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def _form_url(self, partial_url) -> str:
        return f'{self.PROTOCOL}://{self.HOST}/{partial_url}'

    @cached_property
    def _login_data(self):
        return {
            'username': self.username,
            'password': self.password,
        }

    @cached_property
    def _headers(self):
        return {
            'Authorization': f'Bearer {self._access_token}',
        }

    def login(self) -> LoginResponseType:
        url = self._form_url(Url.login.value)
        response = requests.post(url, json=self._login_data)
        if response.status_code == 200:
            return response.json()
        else:
            raise LoginFailed(message=response.text, status_code=response.status_code)

    def _save_data_in_blob(self, data, blob_storage_client: BlobStorageClient) -> str:
        return blob_storage_client.save_data(data)

    def create_new_batch(self, data, blob_storage_client: BlobStorageClient) -> BatchResultID:
        # todo: define a timeout for the request and decide what to do if it times out
        file_url = self._save_data_in_blob(data, blob_storage_client)
        response = requests.post(
            url=self._form_url(Url.new_batch.value),
            json={self.FILE_URL_NAME: file_url},
            headers=self._headers
        )
        if response.status_code == 200:
            return response.json()
        else:
            raise BatchCreationFailed(response.text, response.status_code)

    def get_batch_result(self, batch_id: BatchResultID):
        # todo: define a timeout for the request and decide what to do if it times out
        response = requests.get(
            url=f'{self._form_url(Url.batch_result.value)}/{batch_id}',
            headers=self._headers
        )
        if response.status_code == 200:
            return response.json()
        else:
            raise BatchResultRetrieveFailed(response.text, response.status_code)
