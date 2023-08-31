def parse_input_data(environ: dict) -> dict:
    """Accepts environ and returns key-value pairs parsed from a form submitted through POST request"""

    # the environment variable CONTENT_LENGTH may be empty or missing
    try:
        request_body_size = int(environ.get("CONTENT_LENGTH", 0))
    except ValueError:
        request_body_size = 0

    # When the method is POST the variable will be sent
    # In the HTTP request body which is passed by the WSGI server
    # Is present wsgi.input environment variable.
    return environ["wsgi.input"].read(request_body_size).decode("utf-8")
