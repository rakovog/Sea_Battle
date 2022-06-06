class ConsolePrinterWriter:
    def print(self, *messages):
        print(*messages)

    def input(self, *messages):
        return input(*messages)
