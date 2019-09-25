class WordFilter:
    def __init__(self, word):
        self.word = word

    def detect(self, sentence):
        print(self.word in sentence)

    def censor(self, sentence):
        print(sentence.replace(self.word, '<censored>'))


def main():
    my_filter = WordFilter("アーセナル")

    # NGワードが含まれている場合
    my_filter.censor("昨日のアーセナルの試合アツかった！")

    # NGワードが含まれていない場合
    my_filter.censor("昨日のリバプールの試合アツかった！")


if __name__ == '__main__':
    main()