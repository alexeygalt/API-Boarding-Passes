import os
import traceback
import typing as t
import json

from src import HTTP_MESSAGE


def global_error_handler(error: Exception, response: t.Callable) -> t.List[bytes]:
    """A global error handler, which directs the error based on mode"""
    # Assigning status code to exception objects
    try:
        error.status_code = error.status_code
    except:
        error.status_code = 500

    return send_dev_error(error, response)


def send_dev_error(error: Exception, response: t.Callable) -> t.List[bytes]:
    """An error handler for development mode, sends the traceback along with response"""
    # Getting traceback from exception
    stack = "".join(traceback.TracebackException.from_exception(error).format())
    return_dict = json.dumps(
        {
            "title": f"{error.status_code} Error",
            "status": error.status_code,
            "msg": error.message,
        },
        indent=4,
    )

    response(HTTP_MESSAGE[error.status_code], [])
    return [return_dict.encode("utf-8")]
