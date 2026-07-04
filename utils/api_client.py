import requests
from utils.logger import logger


class APIClient:

    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, endpoint, headers=None):

        response = requests.get(
            f"{self.base_url}{endpoint}",
            headers=headers
        )

        logger.info(
            f"GET {endpoint} | {response.status_code}"
        )

        return response

    def post(
        self,
        endpoint,
        data=None,
        headers=None,
        params=None
    ):

        response = requests.post(
            f"{self.base_url}{endpoint}",
            json=data,
            headers=headers,
            params=params
    )

        return response

    def put(self, endpoint, data=None, headers=None):

        response = requests.put(
            f"{self.base_url}{endpoint}",
            json=data,
            headers=headers
        )

        logger.info(
            f"PUT {endpoint} | {response.status_code}"
        )

        return response

    def delete(self, endpoint, headers=None):

        response = requests.delete(
            f"{self.base_url}{endpoint}",
            headers=headers
        )

        logger.info(
            f"DELETE {endpoint} | {response.status_code}"
        )

        return response