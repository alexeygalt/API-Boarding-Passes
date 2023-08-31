import typing as t

from src.errors.response_error import ErrorResponse
from src.routes import home_router
from src.utils import route_url, HTTP_MESSAGE


def app(environ: dict, response: t.Callable) -> t.Any:
    """
    A callable Python object which is called for every request along with two parameters and returns a response

        Parameters:
            environ (dict): A dictionary populated with information of the request (Given by the WSGI server)
            response (function): A callable accepting a status code,
                a list of headers, and an optional exception context to
                start the response.
    """

    url = environ["PATH_INFO"]

    if route_url(["^\/$", "\/new(\/)?"], url):  # Accepts ['/']
        return home_router(environ, response)

    else:
        # If noting matched then show 404
        message = f"The requested URL {environ['PATH_INFO']} was not found!"
        raise ErrorResponse(404, message)
