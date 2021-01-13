import argparse
import socket

host = "127.0.0.1"


def echo_client(msg: str, port: int):
    # make client
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_addr = (host, port)
    # make connection
    try:
        client.connect(client_addr)
        print("[+] Connect to server %s on port %s" % client_addr)
        # send data
        client.sendall(msg.encode("utf-8"))
        print("[+] Sending msg = %s ...." % msg)
        # receive msg from server
        msg_received = 0
        msg_expected = len(msg)
        while msg_received < msg_expected:
            data = client.recv(16)
            msg_received += len(data)
            print("[+] Data Received %s" % data)

    except socket.error as e:
        print("[-] Connect error : %s" % str(e))
    finally:
        client.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="echo TCP App")
    parser.add_argument('--port', action='store', dest='port', type=int, required=True)
    parser.add_argument('--msg', action='store', dest='msg', type=str, required=True)
    get_args = parser.parse_args()
    port = get_args.port
    msg = get_args.msg
    echo_client(msg, port)
