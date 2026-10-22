# NLP. Занятие 1. Введение в NLP: корпусы и работа с сырым текстом
# Примеры кода из лекции theory/NLP_01_Введение_корпусы_сырой_текст.md
#
# В книгах код написан для Python 2. Здесь всё переписано
# для Python 3 и NLTK 3.9.
#
# Установка (один раз, в терминале):
#     pip install nltk matplotlib
#
# Скрипт можно запускать целиком или выполнять по разделам.
# Графики открываются в отдельных окнах: закройте окно, чтобы скрипт пошёл дальше.
# Если графики не нужны, поставьте SHOW_PLOTS = False.

import random
import tempfile
from collections import Counter
from pathlib import Path

import nltk

SHOW_PLOTS = True


## 0. Данные NLTK
# nltk.download() без аргументов открывает окно загрузчика.
# Здесь коллекции скачиваются сразу (уже скачанные пропускаются).

nltk.download("book", quiet=True)       # все данные для примеров NLTK Book (NLP with python, Бёрд, Кляйн, 2009)
nltk.download("punkt_tab", quiet=True)  # модель токенизатора для word_tokenize (NLTK 3.9+)


# =====================================================================
## 1. Корпусы NLTK
# =====================================================================

from nltk.corpus import brown, gutenberg, inaugural, reuters

### Gutenberg: 18 книг из архива «Проекта Гутенберг»

print(gutenberg.fileids())

emma = gutenberg.words("austen-emma.txt")
print(len(emma))  # 192427

# Средняя длина слова, средняя длина предложения, лексическое разнообразие
for fileid in gutenberg.fileids():
    num_chars = len(gutenberg.raw(fileid))
    num_words = len(gutenberg.words(fileid))
    num_sents = len(gutenberg.sents(fileid))
    num_vocab = len(set(w.lower() for w in gutenberg.words(fileid)))
    print(round(num_chars / num_words),
          round(num_words / num_sents),
          round(num_words / num_vocab),
          fileid)

### Три уровня доступа к тексту: raw() → words() → sents()

raw = gutenberg.raw("burgess-busterbrown.txt")
print(raw[1:20])     # одна строка: 'The Adventures of B'

words = gutenberg.words("burgess-busterbrown.txt")
print(words[1:20])   # список слов

sents = gutenberg.sents("burgess-busterbrown.txt")
print(sents[1:20])   # список предложений, каждое — список слов


# =====================================================================
## 2. Свой корпус
# =====================================================================

from nltk.corpus.reader import CategorizedPlaintextCorpusReader, PlaintextCorpusReader
from nltk.tokenize import PunktTokenizer  # NLTK 3.9+

# Свой корпус — это просто папка с текстовыми файлами.
# Для примера создадим такую папку во временной директории.
corpus_dir = Path(tempfile.mkdtemp()) / "my_corpus"
corpus_dir.mkdir()
(corpus_dir / "chekhov_01.txt").write_text(
    "Краткость — сестра таланта. Пиши так, чтобы словам было тесно.",
    encoding="utf-8")
(corpus_dir / "chekhov_02.txt").write_text(
    "В человеке должно быть всё прекрасно. И лицо, и одежда, и душа, и мысли.",
    encoding="utf-8")
(corpus_dir / "tolstoy_01.txt").write_text(
    "Все счастливые семьи похожи друг на друга. Каждая несчастливая семья "
    "несчастлива по-своему.",
    encoding="utf-8")

### PlaintextCorpusReader: для русских текстов указываем кодировку
### и русскую модель разбиения на предложения

corpus = PlaintextCorpusReader(
    str(corpus_dir), r".*\.txt", encoding="utf-8",
    sent_tokenizer=PunktTokenizer("russian"),
)
print(corpus.fileids())
print(corpus.words("tolstoy_01.txt"))
print(corpus.sents("chekhov_02.txt"))


# =====================================================================
## 3. Сырой текст, локальные файлы
# =====================================================================


### Токенизация: строка → список токенов

tokens = nltk.word_tokenize(raw)
print(type(tokens), len(tokens))
print(tokens[:10])

### Список токенов → nltk.Text

text = nltk.Text(tokens)
print(type(text))
text.collocations()   # в списке будет и Project Gutenberg

### Локальные файлы: всегда указываем кодировку
# (режим 'rU' из книги в Python 3.11 удалён)

path = nltk.data.find("corpora/gutenberg/melville-moby_dick.txt")
with open(path, encoding="utf-8") as f:
    raw = f.read()
print(raw[:60])

### Конвейер: строка → токены → нижний регистр → словарь

tokens = nltk.word_tokenize(raw)
words = [w.lower() for w in tokens]
vocab = sorted(set(words))
print(type(tokens), type(words), type(vocab), len(vocab))


# =====================================================================
## 4. Unicode и кодировки
# =====================================================================

s = "Привет"
b = s.encode("utf-8")   # кодирование: str → bytes
print(len(s), len(b))   # 6 12 — в UTF-8 буква кириллицы занимает 2 байта
print(b.decode("utf-8"))   # декодирование: 'Привет'
print(b.decode("cp1251"))  # 'РџСЂРёРІРµС‚' — прочитали не той кодировкой

import unicodedata

print(ord("я"), hex(ord("я")), unicodedata.name("я"))
# 1103 0x44f CYRILLIC SMALL LETTER YA


# =====================================================================
## 5. Первые исследования корпуса
# =====================================================================

from nltk.book import text1, text2, text3, text4, text5, text8
from nltk import FreqDist

### Конкорданс: каждое вхождение слова с контекстом

text1.concordance("monstrous")

### Похожие слова и общие контексты

text1.similar("monstrous")   # Мелвилл: impalpable, pitiable, curious…
text2.similar("monstrous")   # Остин: very, exceedingly, heartily…
text2.common_contexts(["monstrous", "very"])

### График рассеяния: где в тексте встречаются слова

if SHOW_PLOTS:
    text4.dispersion_plot(["citizens", "democracy", "freedom", "duties", "America"])

### Токены и типы

phrase = ["to", "be", "or", "not", "to", "be"]
print(len(phrase), len(set(phrase)))   # 6 токенов, 4 типа

print(len(text3))                       # 44764 токена
print(sorted(set(text3))[:20])          # начало словаря
print(len(set(text3)))                  # 2789 типов
print(len(text3) / len(set(text3)))     # лексическое разнообразие ≈ 16
print(text3.count("smote"))             # 5
print(100 * text4.count("a") / len(text4))  # доля слова 'a' в процентах

### Частотное распределение: FreqDist

fdist1 = FreqDist(text1)
print(fdist1)                 # <FreqDist with 19317 samples and 260819 outcomes>
print(fdist1.most_common(50)) # в NLTK 3 вместо keys()[:50]
print(fdist1["whale"])        # 906

if SHOW_PLOTS:
    fdist1.plot(50, cumulative=True)  # 50 слов — почти половина книги

print(fdist1.hapaxes()[:20])  # гапаксы: слова, встретившиеся один раз

# Частые длинные слова: длиннее 7 символов и встречаются больше 7 раз
fdist5 = FreqDist(text5)
print(sorted(w for w in set(text5) if len(w) > 7 and fdist5[w] > 7))

# Полезные методы FreqDist
print(fdist1.freq("monstrous"))  # относительная частота
print(fdist1.N())                # всего токенов
print(fdist1.max())              # самый частый токен

### Коллокации

print(list(nltk.bigrams(["more", "is", "said", "than", "done"])))
# в NLTK 3 bigrams() возвращает генератор, поэтому list(...)

text4.collocations()   # United States; fellow citizens; …
text8.collocations()   # social drinker; quiet nights; …

# Коллокации с фильтром стоп-слов (Cookbook, гл. 1)
from nltk.collocations import BigramCollocationFinder
from nltk.corpus import stopwords, webtext
from nltk.metrics import BigramAssocMeasures

words = [w.lower() for w in webtext.words("grail.txt")]
bcf = BigramCollocationFinder.from_words(words)
print(bcf.nbest(BigramAssocMeasures.likelihood_ratio, 4))  # мусор: пунктуация

stopset = set(stopwords.words("english"))
bcf.apply_word_filter(lambda w: len(w) < 3 or w in stopset)
print(bcf.nbest(BigramAssocMeasures.likelihood_ratio, 4))
# [('black', 'knight'), ('clop', 'clop'), ('head', 'knight'), ('mumble', 'mumble')]


# =====================================================================
## 6. Закон Ципфа: f × r = k
# =====================================================================


### график Ципфа для «Моби Дика»

import matplotlib.pyplot as plt

words = [w.lower() for w in gutenberg.words("melville-moby_dick.txt") if w.isalpha()]
freqs = [f for _, f in FreqDist(words).most_common()]
ranks = range(1, len(freqs) + 1)

for r in [1, 10, 100, 1000]:
    print(r, freqs[r - 1], r * freqs[r - 1])   # f × r примерно постоянно

if SHOW_PLOTS:
    plt.loglog(ranks, freqs)
    plt.xlabel("ранг")
    plt.ylabel("частота")
    plt.title("Закон Ципфа: Moby Dick")
    plt.show()
