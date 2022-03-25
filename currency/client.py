from datetime import datetime
from json import loads
from typing import Any, Dict, List, Union

import aiohttp
from base_wrapper.client import Client as BaseClient

from .currencies import CurrencyEnum
from .errors import CoinNotExists, HTTPException
from .results import CurrencyResult
from .route import Route


async def json_or_text(
    response: aiohttp.ClientResponse
) -> Union[Union[Dict[str, Any], List[Dict[str, Any]]], str]:
    text = await response.text(encoding='utf-8')

    if 'application/json' in response.headers['content-type']:
        data: Union[Dict[str, Any], List[Dict[str, Any]]] = loads(text)
        return data

    return text


class Client(BaseClient):
    async def get_last_currency(self, coin: str) -> CurrencyResult:
        response = await self.request(Route('GET', '/last/{coin}', coin=coin))
        data = await json_or_text(response)
        if response.status == 200 and isinstance(data, dict):
            result: Dict[str, Any] = data.get(next(iter(data)), {})
            return CurrencyResult(
                currency=result.get('code', ''),
                currency_to=result.get('codein', ''),
                name=result.get('name', ''),
                high=float(result.get('high', 0.0)),
                low=float(result.get('low', 0.0)),
                variation=float(result.get('varBid', 0.0)),
                variation_percentage=float(result.get('pctChange', 0.0)),
                buy=float(result.get('bid', 0.0)),
                sell=float(result.get('ask', 0.0)),
                timestamp=int(result.get('timestamp', 0)),
                updated_at=datetime.fromtimestamp(
                    int(result.get('timestamp', 0))
                )
            )
        elif response.status == 404 and isinstance(data, dict):
            raise CoinNotExists(response, data)
        else:
            raise HTTPException(response, 'failed to get last currency')
