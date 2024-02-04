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

                    request = HTTPRequest(client_connection, client_address, {'method':method, "path":path})
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

        if request.method == "GET":
            self.do_GET(request)
        elif request.method == "POST":
            self.do_POST(request)
        elif request.method == "PUT":
            self.do_PUT(request)
        elif request.method == "DELETE":
            self.do_DELETE(request)
        elif request.method == "HEAD":
            self.do_HEAD(request)
        else:
            self.send(request, "", status=404)

                   
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
        self.logger.info(f"{request.method} Request Received {request.client_address} headers={request.headers}")

    def do_GET(self, request) -> None: pass
    def do_POST(self, request) -> None: pass
    def do_PUT(self, request) -> None: pass
    def do_DELETE(self, request) -> None: pass
    def do_HEAD(self, request) -> None: pass


class HTTPLite(BaseHTTPServer):

    def __init__(self) -> None:
        super().__init__()

    def do_GET(self, request) -> None:
        html = '<html><head></head><body style="text-align:center"><h1>HTTP Server Lite</h1><p>Server is online!</p></body></html>'
        self.send(request, html)


