import re
import typing as t

from src.controllers import get_current_board_list, create_board_list


def home_router(environ: dict, response: t.Callable) -> t.List[bytes]:
    """Simple methods validator"""
    url = environ["PATH_INFO"]
    http_method = environ["REQUEST_METHOD"]

    if http_method == "GET":
        if re.compile("^\/$").match(url):  # Accepts "/"
            return get_current_board_list(environ, response)

    elif http_method == "POST":
        if re.compile("^\/$").match(url):  # Accepts "/"
            return create_board_list(environ, response)
    else:
        # If noting matched then show 405
        message = f"{http_method} is not ALLOWED on {url}"
        response("405 Method Not Allowed", [])
        return [message.encode("utf-8")]
