import socket
import urllib
import re
"""
http服务器
协议格式:
b'GET /16day/chapter1/03day/20day/03day/01day/01day/index.html HTTP/1.1
Host: 127.0.0.1:7894
User-Agent: Mozilla/5.0 (Windows NT 6.1; rv:66.0) Gecko/20100101 Firefox/66.0
Accept: */*
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Accept-Encoding: gzip, deflate
Referer: http://127.0.0.1:7894/16day/chapter1/03day/20day/03day/01day/06_Linux%20%E7%BB%88%E7%AB%AF%E5%91%BD%E4%BB%A4%E6%A0%BC%E5%BC%8F.html
X-Moz: prefetch
Connection: keep-alive

"""
# 返回给客户端的应答格式

"""
HTTP/1.1 200 OK

content
"""

# a
def service_client(client_socket):
        # 组装http应答的headers
        response = b"HTTP/1.1 200 OK \r\n"
        response += b"\r\n"

        # 接收到客户端的发过来的数据
        request = client_socket.recv(1024)
        print(request)
        file_request = re.search(r"[^/]+(/[^?* ]*)", str(request))
        # file_request = re.search(r"GET ([/\w]*.*) HTTP.*", str(request))
        # file_request = re.search(r"GET (/[^?* ]*)", str(request))
        if file_request:
            print(file_request.group(1))
        # 打开客户端请求的文件打开并将中的内容file_request = re.search(r"[^/]+(/[^?* ]*)", str(request))作为body, 和headers组装作为服务端的应答
        # file_path = "html/"
        file_name = file_request.group(1)
        if file_name == "/":
            file_name = "/index.html"
        index_content = open(r"html" + file_name, "rb")
        response += index_content.read()
        client_socket.send(response)
        # 逻辑通路证明可行,
        # 下一步:将客户端发送的http请求中的get内容取出
        
        # re_test = re.search(r" (.*\.html) ", get_data)
        # print(re_test.group(1))
       
        client_socket.close()


def main():
    # 创建套接字
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 绑定一个ip和端口号
    server_socket.bind(("", 7894))

    # 设置服务套接字为监听
    server_socket.listen(128)
    while True:
        # 等待客户端机的链接
        client_socket, clien_addr = server_socket.accept()

        service_client(client_socket)

    server_socket.close()

    @staticmethod
    def no_content():
        pass


if __name__ == "__main__":
    main()
