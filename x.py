import socket
print("本机ip地址为:",socket.gethostbyname(socket.gethostname()))
def main():
        # 1. 创建tcp监听套接字(socket)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as tcp_socket:
            tcp_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
            tcp_socket.bind(("", 7695))
            tcp_socket.listen(128)
            client_socket, client_addr = tcp_socket.accept()
            recv_data = client_socket.recv(1024)
            print(recv_data.decode("gbk"))
            client_socket.close()
if __name__ == "__main__":
      main()
