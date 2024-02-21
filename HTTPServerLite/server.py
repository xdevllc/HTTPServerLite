import sys
import logging
import socket

from .http_codes import HTTPStatusCodes


class HTTPRequest:

    def __init__(self, client_connection, client_address, headers, data={}) -> None:
        self.client_connection = client_connection
        self.client_address = client_address
        self.headers = headers
        self.data = data
        self.method = headers.get("method", "GET")


class BaseHTTPServer:

    def __init__(self) -> None:
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.logger = logging.getLogger("HTTPServerLite")

    def start(self):
        
        try:
            self.server_socket.bind(('', 80))
            self.server_socket.listen(1)
            self.server_socket.settimeout(1.0)  # Set timeout to 1 second

            while True:
                try:
                    client_connection, client_address = self.server_socket.accept()
                except socket.timeout:
                    continue  # Continue the loop if accept() times out

                try:
                    request = client_connection.recv(1024).decode()

                    # Parse the first line of the request
                    first_line = request.split('\n')[0]
                    method, path, _ = first_line.split()
                    headers = {"method": method, "path": path}
                    lines = request.split('\n')
                    for line in lines[1:]:  # Skip the first line as it's the request line
                        if ': ' in line:
                            header, value = line.split(': ', 1)
                            headers[header] = value.strip()


                    request = HTTPRequest(client_connection, client_address, headers)
                    self.handle(request)
                except socket.timeout:
                    print("recv() timed out")

        except KeyboardInterrupt:
            self.server_socket.close()
            sys.exit()

    def accept(self):

        return self.server_socket.accept()
    
    def handle(self, request):

        self.log_request_received(request)

        method_handlers = {
            "GET": self.do_GET,
            "POST": self.do_POST,
            "PUT": self.do_PUT,
            "DELETE": self.do_DELETE,
            "HEAD": self.do_HEAD,
            "OPTIONS": self.do_OPTIONS,
            "PATCH": self.do_PATCH,
            "TRACE": self.do_TRACE,
            "CONNECT": self.do_CONNECT
        }
        
        # Get the handler based on the request method
        handler = method_handlers.get(request.method)
        
        # If a handler exists for the method, call it, otherwise handle unknown method
        if handler:
            handler(request)
        else:
            self.send(request, "", status=405)

                   
    def send(self, request, body, headers = {}, status = 200):

        # Prepare the response headers

        response_headers = HTTPStatusCodes.STATUS[status]
        for header, value in headers.items():
            response_headers += f"{header}: {value}\n"
        
        if "Content-Length" not in response_headers:

            # Adds the content length to the headers
            response_headers += "Content-Length: " + str(len(body)) + "\n\n"

        # Send the response
        request.client_connection.sendall(response_headers.encode() + body.encode())
        request.client_connection.close()


    def log_request_received(self, request)->None:
        """
        Default logging control
        :param request: The request
        :type request: HTTPRequest
        """
        self.logger.info(f"{request.method} Request Received {request.client_address} path={request.headers['path']} method={request.headers['method']}")

    def do_GET(self, request) -> None: pass
    def do_POST(self, request) -> None: pass
    def do_PUT(self, request) -> None: pass
    def do_DELETE(self, request) -> None: pass
    def do_HEAD(self, request) -> None: pass
    def do_OPTIONS(self, request) -> None: pass
    def do_PATCH(self, request) -> None: pass
    def do_TRACE(self, request) -> None: pass
    def do_CONNECT(self, request) -> None: pass


class HTTPLite(BaseHTTPServer):

    def __init__(self, webpage_file = None) -> None:
        super().__init__()
        self.page = '<html><head></head><body style="text-align:center"><h1>HTTP Server Lite</h1><p>Server is online!</p></body></html>'

        if webpage_file: self.page = self.load_file(webpage_file)

    def load_file(self, filepath):

        if filepath.endswith(".html"):
            with open(filepath, "r") as f:
                return f.read()

    def do_GET(self, request) -> None:
        html = self.page
        self.send(request, html)

