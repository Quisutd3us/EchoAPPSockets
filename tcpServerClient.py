import argparse
import socket

host = "127.0.0.1"
backlog = 5


def echo_server(port: int):
    # create server
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # reuse port
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # create address
    server_addr = (host, port)
    try:
        server.bind(server_addr)
        server.listen(backlog)
        print("[+] Server %s listen on port: %s " % server_addr)
        while True:
            # get data
            print("Waiting for receive msg for client")
            client, client_addr = server.accept()
            data = client.recv(2048)
            if data:
                print("[+] Receive from client : %s" % data)
                client.send(data)
                print("[+] Send %s to client %s" % (data, client_addr))
            # close connection
            client.close()
    except socket.error as e:
        print("[-] Socket error : %s" % str(e))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="echo TCP App")
    parser.add_argument('--port', action='store', dest='port', type=int, required=True)
    get_args = parser.parse_args()
    port = get_args.port
    echo_server(port)
