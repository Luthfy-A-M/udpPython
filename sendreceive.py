import socket
import threading

def receive_and_send():
    # Set up a UDP socket
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)  # Set broadcast option
    udp_socket.bind(('0.0.0.0', 12345))

    # Function to handle receiving messages
    def receive_messages():
        while True:
            data, addr = udp_socket.recvfrom(1024)
            print(f"Received message from {addr}: {data.decode()}")

    # Function to handle sending messages
    def send_message():
        while True:
            message = input("Enter message to send: ")
            udp_socket.sendto(message.encode(), ('<broadcast>', 12345))

    # Create threads for receiving and sending messages
    receive_thread = threading.Thread(target=receive_messages)
    send_thread = threading.Thread(target=send_message)

    # Start the threads
    receive_thread.start()
    send_thread.start()

    # Join the threads to main thread
    receive_thread.join()
    send_thread.join()

if __name__ == "__main__":
    receive_and_send()
