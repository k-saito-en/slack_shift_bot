# coding: utf-8

from slackbot.bot import Bot

def main():
  bot = Bot()
  bot.run()

#インポートされただけでメソッドが実行されるのを防ぐためのコード
if __name__ == "__main__":
  print('start slackbot')
  main()