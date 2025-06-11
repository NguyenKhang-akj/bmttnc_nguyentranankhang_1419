import random
import tornado.ioloop
import tornado.websocket
import tornado.web

class WebSocketServer(tornado.websocket.WebSocketHandler):
    clients = set()

    def open(self):
        WebSocketServer.clients.add(self)
        print("New client connected at 10:04 AM +07 on Wednesday, June 11, 2025")

    def on_close(self):
        WebSocketServer.clients.remove(self)
        print("Client disconnected")

    @classmethod
    def send_message(cls, message):
        print(f"Sending message: {message} to {len(cls.clients)} client(s).")
        for client in cls.clients:
            client.write_message(message)

class RandomwordSelector:
    def __init__(self, word_list):
        self.word_list = word_list

    def sample(self):
        return random.choice(self.word_list)

def main():
    app = tornado.web.Application([
        (r"/websocket", WebSocketServer),
    ],
    websocket_ping_interval=10,
    websocket_ping_timeout=30,
    )
    app.listen(8888)

    io_loop = tornado.ioloop.IOLoop.current()

    word_selector = RandomwordSelector(["apple", "banana", "orange", "grape", "melon"])

    periodic_callback = tornado.ioloop.PeriodicCallback(
        lambda: WebSocketServer.send_message(word_selector.sample()), 3000
    )
    periodic_callback.start()

    io_loop.start()

if __name__ == "__main__":
    main()