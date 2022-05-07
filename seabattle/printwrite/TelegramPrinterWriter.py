class TelegramPrinterWriter:
    def __init__(self, telegram_bot, chat_id):
        self.telegram_bot = telegram_bot
        self.chat_id = chat_id

    def print(self, *messages):
        self.telegram_bot.print(self.chat_id, *messages)

    def input(self, *messages):
        return self.telegram_bot.input(self.chat_id, *messages)