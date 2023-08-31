import os
from wsgiref import simple_server
from dotenv import load_dotenv
from src import app
from src.errors.ExceptionMiddleware import ExceptionMiddleware


load_dotenv()  # Loads environment variables from .env file


# Main function that is called when a request is made
app = ExceptionMiddleware(app)

# If no WSGI server is setup then run main.py directly
# to use inbuilt Python WSGI server (Which is very slow)
if __name__ == "__main__":
    PORT = int(os.getenv("PORT", 8000))
    httpd = simple_server.make_server("", PORT, app)
    print(f"Listening on http://localhost:{PORT}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Shutting down...")
        httpd.server_close()
