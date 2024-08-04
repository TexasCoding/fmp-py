import os
import requests
from requests.adapters import HTTPAdapter
from urllib3.util import Retry

from dotenv import load_dotenv
from typing import Dict, Any

load_dotenv()

FMP_API_KEY = os.getenv("FMP_API_KEY", "")
FMP_BASE_URL = "https://financialmodelingprep.com/api/"


class FmpBase:
    def __init__(self, api_key: str = FMP_API_KEY) -> None:
        """
        Initialize the FmpBase class.

        Args:
            api_key (str): The API key for Financial Modeling Prep. Defaults to the value from environment variable.
        """
        if not api_key:
            raise ValueError(
                "API Key is required. Set it as environment variable 'FMP_API_KEY' or pass it directly."
            )
        self.api_key = api_key

        status_forcelist = [429, 500, 502, 503, 504]

        self.retry_strategy = Retry(
            total=3,
            backoff_factor=2.0,
            status_forcelist=status_forcelist,
        )
        self.adapter = HTTPAdapter(max_retries=self.retry_strategy)
        self.session = requests.Session()
        self.session.mount("https://", self.adapter)
        self.session.mount("http://", self.adapter)

    def clean_value(self, value, type) -> Any:
        if type is int:
            return int(value) if value else int(0)
        elif type is float:
            return float(value) if value else float(0.0)
        elif type is str:
            return str(value) if value else str("")
        elif type is bool:
            return bool(value) if value else bool(False)
        else:
            return value

    def get_request(self, url: str, params: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        Make a GET request to the specified URL with the given parameters.

        Args:
            url (str): The URL endpoint to make the request to.
            params (Dict[str, Any]): Additional parameters for the request.

        Returns:
            Dict[str, Any]: The JSON response from the server.

        Raises:
            Exception: If the response status code is not 200 or if there is a request exception.
        """
        params = params or {}
        params["apikey"] = self.api_key
        full_url = f"{FMP_BASE_URL}{url}"

        try:
            response = self.session.get(full_url, params=params)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Request failed: {e}")

        try:
            return response.json()
        except ValueError:
            raise Exception("Failed to parse JSON response")

    def __del__(self):
        """
        Ensure the session is properly closed when the object is deleted.
        """
        self.session.close()
