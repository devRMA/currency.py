from datetime import datetime
from json import loads
from typing import TYPE_CHECKING, Any, Dict, List, TypeAlias, Union

import aiohttp
from base_wrapper.client import Client as BaseClient

from .errors import CoinNotExists, HTTPException
from .results import CurrencyResult
from .route import Route

if TYPE_CHECKING:
    from .currencies import TCurrency
else:
    TCurrency: TypeAlias = None


async def _json_or_text(
    response: aiohttp.ClientResponse
) -> Union[Union[Dict[str, Any], List[Dict[str, Any]]], str]:
    text = await response.text(encoding='utf-8')

    if 'application/json' in response.headers['content-type']:
        data: Union[Dict[str, Any], List[Dict[str, Any]]] = loads(text)
        return data

    return text


class Client(BaseClient):
    async def get_last_currency(self, coin: TCurrency) -> CurrencyResult:
        """
        Get the last currency price

        Parameters
        ----------
        coin : `str`
            The coin to get the price

        Returns
        -------
        `CurrencyResult`
            The result of the currency

        Raises
        ------
        `CoinNotExists`
            Raised if the coin does not exists in the API
        `HTTPException`
            Any other exception raised by the API
        """
        resp = await self.request(Route('GET', '/last/{coin}', coin=coin))
        data = await _json_or_text(resp)
        if resp.status == 200 and isinstance(data, dict):
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
        elif resp.status == 404 and isinstance(data, dict):
            raise CoinNotExists(resp, data)
        else:
            raise HTTPException(resp, 'failed to get last currency')
