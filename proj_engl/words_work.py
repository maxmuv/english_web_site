def get_words():
    words = []
    with open("./data/words.csv", "r", encoding="utf-8") as f:
        cnt = 1
        for line in f.readlines()[1:]:
            print(line)
            word, translation, source = line.split(";")
            words.append([cnt, word, translation])
            cnt += 1
    return words
