from fmp_py.fmp_base import FmpBase
import os
from dotenv import load_dotenv

load_dotenv()


class FmpStockList(FmpBase):
    def __init__(self, api_key: str = os.getenv("FMP_API_KEY")) -> None:
        super().__init__(api_key)
