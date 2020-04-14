
from selectors import DefaultSelector,EVENT_READ,EVENT_WRITE
from socket import socket,AF_INET,SOCK_STREAM




class ChatRoom:
    def __init__(self,sel):
        self.addr = "127.0.0.1"
        self.port = 8181
        self.sel = sel

    def readable(self,client):
        print(client)
        print('readable')
        while True:
            try:
                msg = client.recv(1024)
            except Exception as e:
                print(e)
                break
            if not msg:
                break
        client.send("接收到:".encode(encoding='utf-8')+msg)
        selector.unregister(client)
        client.close()




    def connectd(self,server):
        print('connect')

        client,addr = server.accept()
        client.setblocking(False)
        
        self.sel.register(client,EVENT_READ,self.readable)




    def run(self):
        self.server = socket()
        self.server.setblocking(False)
        self.server.bind((self.addr,self.port))
        self.server.listen(5)
        self.sel.register(self.server,EVENT_READ,self.connectd)
        while True:

            events = self.sel.select()
            for key, mask in events:
                call_back = key.data
                call_back(key.fileobj)
                print(key.fileobj)
            print('ggg')








if __name__ == '__main__':
    selector = DefaultSelector()
    chat_obj = ChatRoom(sel=selector)
    chat_obj.run()
