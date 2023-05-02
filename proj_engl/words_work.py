def get_words():
    words = []
    with open("./data/words.csv", "r", encoding="utf-8") as f:
        cnt = 1
        for line in f.readlines()[1:]:
            word, translation, source = line.split(";")
            words.append([cnt, word, translation])
            cnt += 1
    return words


def write_word(new_word, new_translation):
    new_word_line = f"{new_word};{new_translation};user"
    with open("./data/words.csv", "r", encoding="utf-8") as f:
        existing_words = [l.strip("\n") for l in f.readlines()]
        title = existing_words[0]
        old_words = existing_words[1:]
    words_sorted = old_words + [new_word_line]
    words_sorted.sort()
    new_words = [title] + words_sorted
    with open("./data/words.csv", "w", encoding="utf-8") as f:
        f.write("\n".join(new_words))


def get_classes():
    classes = []
    with open("./data/classes.csv", "r", encoding="utf-8") as f:
        cnt = 1
        for line in f.readlines()[1:]:
            cls, teacher, time, comment, source = line.split(";")
            classes.append([cnt, cls, teacher, time, comment])
            cnt += 1
    return classes


def write_class(new_class, new_teacher, new_time, new_comment):
    new_class_line = f"{new_class};{new_teacher};{new_time};{new_comment};user"
    with open("./data/classes.csv", "r", encoding="utf-8") as f:
        existing_classes = [l.strip("\n") for l in f.readlines()]
        title = existing_classes[0]
        old_classes = existing_classes[1:]
    classes_sorted = old_classes + [new_class_line]
    classes_sorted.sort()
    new_classes = [title] + classes_sorted
    with open("./data/classes.csv", "w", encoding="utf-8") as f:
        f.write("\n".join(new_classes))
