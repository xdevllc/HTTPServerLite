class HTTPStatusCodes:

    CODE100 = "HTTP/1.1 100 Continue\n"
    CODE101 = "HTTP/1.1 101 Switching Protocols\n"
    CODE200 = "HTTP/1.1 200 OK\n"
    CODE201 = "HTTP/1.1 201 Created\n"
    CODE202 = "HTTP/1.1 202 Accepted\n"
    CODE203 = "HTTP/1.1 203 Non-Authoritative Information\n"
    CODE204 = "HTTP/1.1 204 No Content\n"
    CODE205 = "HTTP/1.1 205 Reset Content\n"
    CODE206 = "HTTP/1.1 206 Partial Content\n"
    CODE300 = "HTTP/1.1 300 Multiple Choices\n"
    CODE301 = "HTTP/1.1 301 Moved Permanently\n"
    CODE302 = "HTTP/1.1 302 Found\n"
    CODE303 = "HTTP/1.1 303 See Other\n"
    CODE304 = "HTTP/1.1 304 Not Modified\n"
    CODE307 = "HTTP/1.1 307 Temporary Redirect\n"
    CODE308 = "HTTP/1.1 308 Permanent Redirect\n"
    CODE400 = "HTTP/1.1 400 Bad Request\n"
    CODE401 = "HTTP/1.1 401 Unauthorized\n"
    CODE403 = "HTTP/1.1 403 Forbidden\n"
    CODE404 = "HTTP/1.1 404 Not Found\n"
    CODE405 = "HTTP/1.1 405 Method Not Allowed\n"
    CODE406 = "HTTP/1.1 406 Not Acceptable\n"
    CODE407 = "HTTP/1.1 407 Proxy Authentication Required\n"
    CODE408 = "HTTP/1.1 408 Request Timeout\n"
    CODE409 = "HTTP/1.1 409 Conflict\n"
    CODE410 = "HTTP/1.1 410 Gone\n"
    CODE411 = "HTTP/1.1 411 Length Required\n"
    CODE412 = "HTTP/1.1 412 Precondition Failed\n"
    CODE413 = "HTTP/1.1 413 Payload Too Large\n"
    CODE414 = "HTTP/1.1 414 URI Too Long\n"
    CODE415 = "HTTP/1.1 415 Unsupported Media Type\n"
    CODE416 = "HTTP/1.1 416 Range Not Satisfiable\n"
    CODE417 = "HTTP/1.1 417 Expectation Failed\n"
    CODE426 = "HTTP/1.1 426 Upgrade Required\n"
    CODE429 = "HTTP/1.1 429 Too Many Requests\n"
    CODE451 = "HTTP/1.1 451 Unavailable For Legal Reasons\n"
    CODE500 = "HTTP/1.1 500 Internal Server Error\n"
    CODE501 = "HTTP/1.1 501 Not Implemented\n"
    CODE502 = "HTTP/1.1 502 Bad Gateway\n"
    CODE503 = "HTTP/1.1 503 Service Unavailable\n"
    CODE504 = "HTTP/1.1 504 Gateway Timeout\n"
    CODE505 = "HTTP/1.1 505 HTTP Version Not Supported\n"

    STATUS = {
        100: CODE100,
        101: CODE101,
        200: CODE200,
        201: CODE201,
        202: CODE202,
        203: CODE203,
        204: CODE204,
        205: CODE205,
        206: CODE206,
        300: CODE300,
        301: CODE301,
        302: CODE302,
        303: CODE303,
        304: CODE304,
        307: CODE307,
        308: CODE308,
        400: CODE400,
        401: CODE401,
        403: CODE403,
        404: CODE404,
        405: CODE405,
        406: CODE406,
        407: CODE407,
        408: CODE408,
        409: CODE409,
        410: CODE410,
        411: CODE411,
        412: CODE412,
        413: CODE413,
        414: CODE414,
        415: CODE415,
        416: CODE416,
        417: CODE417,
        426: CODE426,
        429: CODE429,
        451: CODE451,
        500: CODE500,
        501: CODE501,
        502: CODE502,
        503: CODE503,
        504: CODE504,
        505: CODE505,
    }