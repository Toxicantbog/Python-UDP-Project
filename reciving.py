import socket
from tkinter import*

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))


def getData():
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    string = ("received message: %s" % data)
    return string

#while True:
#    data, addr = getData()
#    print("received message: %s" % data)

root = Tk()
root.title("Tk Example")
root.minsize(200, 200)  # width, height
root.geometry("300x300+50+50")

lab = Label(root, text="text")
lab.pack()


def update():
    lab['text'] = getData()
    root.after(1000, update) # run itself again after 1000 ms

update()
root.mainloop()




