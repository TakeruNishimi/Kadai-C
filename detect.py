class WordFilter:
    def __init__(self,word):
        self.word =word

    def detect(self,sentence):
        print(self.word in sentence)


def main():
    my_filter = WordFilter("アーセナル")

    # NGワードが含まれている場合
    my_filter.detect("昨日のアーセナルの試合アツかった！")  # Trueを返す

    # NGワードが含まれていない場合
    my_filter.detect("昨日のリバプールの試合アツかった！")  # Falseを返す


if __name__ == '__main__':
    main()