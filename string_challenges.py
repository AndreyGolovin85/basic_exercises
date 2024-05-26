# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])

# Вывести количество букв "а" в слове
word = 'Архангельск'
print(word.lower().count('а'))


# Вывести количество гласных букв в слове
word = 'Архангельск'
vse_gls = ["а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"]
count = 0
for letter in word.lower():
    if letter in vse_gls:
        count += 1
print(f"В слове гласных букв: {count}")

# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(f"В предложении слов: {len(sentence.split())}.")

# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
for word in sentence.split():
    print(word[0])

# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
sum_len_word = 0
for word in sentence.split():
    sum_len_word += len(word)

print(f"Средняя длинна слова: {int(sum_len_word / len(sentence.split()))}.")
