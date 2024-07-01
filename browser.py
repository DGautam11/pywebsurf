import socket
class URL:
    def __init__(self,url):
        self.scheme, url = url.split('://')
        assert self.scheme == "http"
        if "/" not in url:
            url += "/"
            self.host,url = url.split("/",1)
            self.path = "/" + url

    def request(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM,socket.IPPROTO_TCP)
        s.connect((self.host,80))
        request = "GET {} HTTP/1.0\r\n"-format(self.path)
        request += "Host: {}\r\n".format(self.host)
        request += "\r\n"
        s.send(request.encode("utf8"))


