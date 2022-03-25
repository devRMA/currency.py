from typing import TYPE_CHECKING, Any, Dict, Optional, TypeAlias, Union

if TYPE_CHECKING:
    from aiohttp import ClientResponse

    _ResponseType: TypeAlias = ClientResponse
else:
    _ResponseType: TypeAlias = None


class CurrencypyError(Exception):
    """Base exception class for the library.

    Ideally speaking, this could be caught to handle any exceptions raised
    from this library.
    """
    pass


class HTTPException(CurrencypyError):
    """Exception that's raised when an HTTP request operation fails.

    Attributes
    ------------
    response: `aiohttp.ClientResponse`
        The response of the failed HTTP request. This is an
        instance of `aiohttp.ClientResponse`.

    status: `int`
        The status code of the HTTP request.
    message: `str`
        The text of the error.
    code: `str`
        The error code for the failure.
    """
    def __init__(
        self, response: _ResponseType, message: Optional[Union[str, Dict[str,
                                                                         Any]]]
    ):
        self.response: _ResponseType = response
        self.status: int = response.status
        self.message: str
        self.code: str

        if isinstance(message, dict):
            self.message = message.get('message', '')
            self.code = message.get('code', '')
        else:
            self.message = message or ''
            self.code = ''

        fmt = '{0.status} {0.reason} (error code: {1})'
        if len(self.message):
            fmt += ': {2}'

        super().__init__(fmt.format(self.response, self.code, self.message))


class CoinNotExists(HTTPException):
    """Exception that's raised when a coin is not found."""
    pass
