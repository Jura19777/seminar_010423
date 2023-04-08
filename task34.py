"""
Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает,
Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами.
Стихотворение  Винни-Пух вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

"""

vowels = "aeiouy"

poem = input("Введите стихотворение: ")
phrases = poem.split()

syllables = []
for phrase in phrases:
    syllables.append(sum(phrase.count(vowel) for vowel in vowels))

if syllables.count(syllables[0]) == len(syllables):
    print("Парам пам-пам")
else:
    print("Пам парам")