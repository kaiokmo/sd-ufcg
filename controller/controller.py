import context

class Controller:
    def __init__(self, *contexts):
        for context in contexts:
            self.contexts = context.Context()

if __name__ == "__main__":
    controller = Controller()