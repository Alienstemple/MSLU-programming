# NLP. Занятие 1. Введение в NLP: корпусы и работа с сырым текстом

**План занятия**

1. Что такое NLP, основные задачи и уровни анализа языка
2. Установка NLTK, встроенные корпусы, загрузка своих корпусов
3. Чтение текста из файлов и веба, кодировки, Unicode
4. Первые исследования корпуса: конкорданс, `FreqDist`, коллокации, закон Ципфа

---

## 1. Что такое NLP

### Определение

> NLP can be regarded as automatic or semi-automatic processing of human language (Eisenstein 2019). It requires extensive knowledge of linguistics and logical theory in theoretical mathematics, also known as computational linguistics.
>
> — [Lee], §1.6

«NLP можно рассматривать как автоматическую или полуавтоматическую обработку
человеческого языка. Она требует обширных знаний лингвистики и логической теории
теоретической математики; эту область называют также компьютерной лингвистикой».

> People who are deeply involved in the study of language are linguists, while the term 'computational linguist' applies to the study of processing languages with the application of computation. Essentially, a computational linguist will be a computer scientist who has enough understanding of languages, and can apply his computational skills to model different aspects of the language. While computational linguists address the theoretical aspect of language, NLP is nothing but the application of computational linguistics.
>
> — [Essentials], гл. 1, с. 1

«Люди, глубоко погружённые в изучение языка, — лингвисты, а термин „компьютерный
лингвист“ относится к изучению обработки языков с применением вычислений.
По сути, компьютерный лингвист — это специалист по информатике, который достаточно
понимает языки и может применить свои вычислительные навыки, чтобы моделировать
разные аспекты языка. Если компьютерные лингвисты занимаются теоретической стороной
языка, то NLP — не что иное, как приложение компьютерной лингвистики».

> In a practical context, NLP is analogous to teaching a language to a child. Some of the most common tasks like understanding words, sentences, and forming grammatically and structurally correct sentences, are very natural to humans. In NLP, some of these tasks translate to tokenization, chunking, part of speech tagging, parsing, machine translation, speech recognition, and most of them are still the toughest challenges for computers.
>
> — [Essentials], гл. 1, с. 1

«На практике NLP похоже на обучение ребёнка языку. Многие самые обычные задачи —
понимать слова и предложения, строить грамматически и структурно правильные
предложения — для человека совершенно естественны. В NLP некоторые из этих задач
превращаются в токенизацию, чанкинг, разметку частей речи, синтаксический разбор,
машинный перевод, распознавание речи, и большинство из них до сих пор остаются
труднейшими задачами для компьютеров».

### Естественный язык и язык программирования

> Языки программирования созданы искусственно и используются для того, чтобы сообщать компьютеру, что он должен делать. <…> Языки программирования однозначны — каждая строка кода может иметь только одно толкование. Кроме того, машины должны обрабатывать языки программирования, а не понимать их.
>
> — [Лейн], §1.1, с. 34

> Естественные языки, напротив, развивались органически — естественным путем. Естественные языки передают идеи и знания между живыми организмами, обладающими мозгом, а не процессорами.
>
> — [Лейн], §1.1, с. 34

> Независимо от того, написан ли ваш текст на естественном языке или на языке программирования, машина первым делом разбивает его на токены. В языках программирования разнообразие токенов обычно невелико — например, в языке программирования Python используется всего 33 зарезервированных ключевых слова. В то же время словарный запас естественного языка насчитывает сотни тысяч возможных токенов.
>
> — [Лейн], §1.1, с. 33

### Компоненты NLP

> NLP consists of (1) Natural Language Understanding (NLU), (2) Knowledge Acquisition and Inferencing (KAI), (3) Natural Language Generation (NLG) components.
>
> NLU is a technique and method devised to understand the meanings of human-spoken languages by syntax, semantic, and pragmatic analyses.
>
> KAI is a system to generate proper responses after spoken languages are fully recognized by NLU. <…>
>
> NLG includes answer, response, and feedback generation in human-machine dialogue.
>
> — [Lee], §1.7

«NLP состоит из трёх компонентов: (1) понимание естественного языка (NLU),
(2) приобретение знаний и логический вывод (KAI), (3) порождение естественного
языка (NLG).
NLU — это приёмы и методы, предназначенные для понимания смысла устной речи
человека посредством синтаксического, семантического и прагматического анализа.
KAI — система, порождающая подходящие ответы после того, как речь полностью
распознана компонентом NLU.
NLG включает порождение ответов, реплик и обратной связи в диалоге человека
и машины».

> Понимание естественного языка (natural language understanding, NLU) — это подраздел NLP, занимающийся машинным анализом смысла естественного языка. Важной частью NLU является автоматическая обработка текста для извлечения числового представления его смысла. NLU — это часть NLP. Числовое представление смысла естественного языка обычно имеет форму последовательности чисел — вектора.
>
> — [Лейн], §1.1.1, с. 36

> Машины способны генерировать текст разными способами, и если ваш алгоритм не выполняет явных манипуляций со строками (например, не вставляет имя пользователя в шаблон Hello {{name}}!), то он, вероятно, представит результат своей работы в виде последовательности чисел. Чтобы преобразовать эти числа в понятный человеку язык, требуется декодирование — процесс, обратный кодированию.
>
> — [Лейн], §1.1.2, с. 37

### Уровни анализа языка

> There are six levels of linguistics analysis: (1) phonetics, (2) phonology, (3) morphology, (4) syntax, (5) semantics, and (6) pragmatics (discourse) classified in basic sound linguistics.
>
> — [Lee], §1.3

«Выделяют шесть уровней лингвистического анализа: (1) фонетика, (2) фонология,
(3) морфология, (4) синтаксис, (5) семантика и (6) прагматика (дискурс)».

*Подпись к рис. 1.3 у Lee перечисляет, что изучает каждый уровень:*

> From the center outward, the levels are: Phonetics (speech sounds), Phonology (phonemes), Morphology (words), Syntax (phrases and sentences), Semantics (literal meaning of phrases and sentences), and Pragmatics (meaning in context of discourse).
>
> — [Lee], §1.3, рис. 1.3

«От центра наружу: фонетика (звуки речи), фонология (фонемы), морфология (слова),
синтаксис (словосочетания и предложения), семантика (буквальный смысл
словосочетаний и предложений) и прагматика (смысл в контексте дискурса)».

> Phonetics refers to the physical aspects of sound, the study of the production and perception of sounds called phones. <…>
> Morphology is the form and word level determined by grammar and syntax generally. <…>
> Syntax represents the primary level of clauses and sentences to organize the meaning of different words order <…> and deals with related sentence patterns and ambiguous analysis. <…>
> Semantic level is the domain of meaning <…>. Pragmatics is the use of language in definitive settings. The meaning of discourse does not have to be the same as abstract form in actual use. It is largely based on the concept of speech acts and the contents of statements with intent and effect analysis of language performance.
>
> — [Lee], §1.3

«Фонетика относится к физической стороне звука; это изучение произнесения
и восприятия звуков, называемых фонами. <…> Морфология — уровень формы и слова,
определяемый, как правило, грамматикой и синтаксисом. <…> Синтаксис — основной
уровень клауз и предложений, упорядочивающий смысл через порядок слов <…>;
он имеет дело с моделями предложений и анализом неоднозначности. <…>
Семантический уровень — область значения <…>. Прагматика — это употребление
языка в определённых условиях. Смысл дискурса не обязан совпадать с абстрактной
формой при реальном употреблении. Прагматика во многом опирается на понятие
речевого акта и на содержание высказываний с анализом намерения и эффекта».

*Как уровни выстраиваются в этапы понимания, показывает §1.8 у Lee:*

> Natural Language Understanding (NLU) is a process of recognizing and understanding spoken language in four stages (Allen 1994): (1) speech recognition, (2) syntactic (syntax) analysis, (3) semantic analysis, and (4) pragmatic analysis.
>
> — [Lee], §1.8

«Понимание естественного языка — процесс распознавания и понимания устной речи
в четыре этапа: (1) распознавание речи, (2) синтаксический анализ,
(3) семантический анализ и (4) прагматический анализ».

> For instance, the utterance *oranges to the boys* will be rejected by syntax parser because of syntactic errors.
>
> — [Lee], §1.8.2

> <…> semantic analyzer rejects word phrase like *hot snowflakes* despite correct syntactic words meaning but incorrect semantic meaning.
>
> — [Lee], §1.8.3

> <…> for example, *will you crack open the door? I'm getting hot.* This sentence/utterance requires extra knowledge in the second clause to understand *crack* is to break in semantic meaning, but it should be interpreted as to open in pragmatic meaning.
>
> — [Lee], §1.8.4

«Например, высказывание *oranges to the boys* синтаксический анализатор отвергнет
из-за синтаксических ошибок». — «Семантический анализатор отвергает сочетание
вроде *hot snowflakes* („горячие снежинки“): синтаксически слова соединены верно,
но смысл неверен». — «Например: *will you crack open the door? I'm getting hot.*
Чтобы понять это высказывание, нужно дополнительное знание из второй части:
семантически *crack* значит „разбить“, а прагматически его следует понимать
как „приоткрыть“».

### Неоднозначность

> Ambiguity is the capability to understand sentence structures in many ways. There are (1) lexical, (2) syntactic, (3) semantic, and (4) pragmatics ambiguities in NLP.
>
> Lexical ambiguity arises from words where a word's meaning depends on contextual utterance. For instance, the word *green* is normally a noun for color. But it can be an adjective or even a verb in different situations.
>
> Syntactic ambiguity arises from sentences and is parsed differently, for example, *Jack watched Helen with a telescope*. It can be described as either Jack watched Helen by using a telescope or Jack watched Helen holding a telescope.
>
> Semantic ambiguity arises from word meaning and can be misinterpreted, or a sentence has ambiguous words or phrases, for example, *The van hits the boar while it is moving*. It can be described as either the van hits the boar while the van is moving, or the van hits the boar while the boar is moving.
>
> Pragmatic ambiguity arises from a statement and is not clearly defined when the context of a sentence provides multiple interpretations such as *I like that too*. It can describe what I like that too, others like that too but the description of *that* is uncertain.
>
> — [Lee], §1.4

«Неоднозначность — это возможность понять структуру предложения несколькими
способами. В NLP различают (1) лексическую, (2) синтаксическую, (3) семантическую
и (4) прагматическую неоднозначность.
Лексическая неоднозначность возникает из слов, значение которых зависит
от контекста высказывания. Например, слово *green* обычно существительное,
обозначающее цвет, но в разных ситуациях оно может быть прилагательным
и даже глаголом.
Синтаксическая неоднозначность возникает, когда предложение разбирается
по-разному, например *Jack watched Helen with a telescope*: Джек смотрел на Хелен
в телескоп или Джек смотрел на Хелен, у которой был телескоп.
Семантическая неоднозначность возникает из значения слова, которое можно
истолковать неверно, например *The van hits the boar while it is moving*:
фургон сбивает кабана, когда движется фургон, или когда движется кабан.
Прагматическая неоднозначность возникает, когда контекст допускает несколько
толкований, как в *I like that too*: мне это тоже нравится или другим это тоже
нравится, но что такое *that*, неясно».

> В отличие от языков программирования, где каждое ключевое слово имеет однозначное толкование, естественные языки гораздо менее однозначны. Возьмем, к примеру, предложение «Курица готова к обеду». Это может означать, что живая курица готова приступить к еде или что блюдо из курицы готово к употреблению.
>
> — [Лейн], §1.1, с. 35

*Как неоднозначность снимается контекстом, NLTK Book показывает на задаче
разрешения многозначности слов:*

> In word sense disambiguation we want to work out which sense of a word was intended in a given context. Consider the ambiguous words *serve* and *dish*:
>
> a. *serve*: help with food or drink; hold an office; put ball into play
> b. *dish*: plate; course of a meal; communications device
>
> In a sentence containing the phrase: *he served the dish*, you can detect that both *serve* and *dish* are being used with their food meanings. <…> In other words, we automatically disambiguate words using context, exploiting the simple fact that nearby words have closely related meanings.
>
> — [NLTK Book], §1.5, с. 28

«При разрешении лексической многозначности мы хотим установить, какое значение
слова имелось в виду в данном контексте. Возьмём многозначные слова *serve*
(подавать еду или напиток; занимать должность; подавать мяч) и *dish* (тарелка;
блюдо; антенна-тарелка). В предложении с фразой *he served the dish* понятно,
что оба слова употреблены в „кулинарных“ значениях. <…> Иначе говоря, мы
автоматически снимаем многозначность с помощью контекста, пользуясь тем простым
фактом, что соседние слова близки по смыслу».

> A deeper kind of language understanding is to work out "who did what to whom," <…>
>
> a. The thieves stole the paintings. They were subsequently sold.
> b. The thieves stole the paintings. They were subsequently caught.
> c. The thieves stole the paintings. They were subsequently found.
>
> Answering this question involves finding the antecedent of the pronoun *they*, either thieves or paintings.
>
> — [NLTK Book], §1.5, с. 28

«Более глубокий уровень понимания языка — установить, „кто что сделал с кем“ <…>
(а) Воры украли картины. Впоследствии их продали. (б) …Впоследствии их поймали.
(в) …Впоследствии их нашли. Чтобы ответить на вопрос, нужно найти антецедент
местоимения *they*: воры или картины».

### Задачи NLP

> NLP technology has a wide range of applications in everyday activities such as machine translation, information retrieval, sentiment analysis, information extraction, and question-answering chatbots.
>
> — [Lee], §1.9

«У технологий NLP широкий круг применений в повседневной жизни: машинный перевод,
информационный поиск, анализ тональности, извлечение информации, вопросно-ответные
чат-боты».

> Let me also give you some examples of the amazing NLP applications that you can use, but are not aware that they are built on NLP:
>
> - Spell correction (MS Word/ any other editor)
> - Search engines (Google, Bing, Yahoo, wolframalpha)
> - Speech engines (Siri, Google Voice)
> - Spam classifiers (All e-mail services)
> - News feeds (Google, Yahoo!, and so on)
> - Machine translation (Google Translate, and so on)
>
> — [Essentials], гл. 1, с. 3

«Вот примеры замечательных приложений NLP, которыми вы пользуетесь, не зная,
что они построены на NLP: исправление опечаток, поисковые системы, речевые движки,
спам-фильтры, новостные ленты, машинный перевод».

> После преобразования текста на естественном языке в числовую форму извлечь смысл из этой формы можно сотней способов. Машины уже научились довольно точно решать многие распространенные задачи обработки естественного языка, такие как: семантический поиск; распознавание перефразированного текста; классификация намерений; анализ эмоциональной окраски; тематическое моделирование (определение темы); определение авторства.
>
> — [Лейн], §1.1.1, с. 36

> Однако остается множество других задач, в решении которых люди значительно превосходят машины. Некоторые задачи требуют от машины наличия практических знаний, умения выявлять логические связи между фактами и применения всего этого в контексте конкретного фрагмента текста. Это значительно усложняет для машин: распознавание эвфемизмов и каламбура; распознавание юмора и сарказма; обнаружение разжигания ненависти и троллинга; логические выводы и распознавание ошибок; извлечение знаний.
>
> — [Лейн], §1.1.1, с. 37

> Machine translation is difficult because a given word could have several possible translations (depending on its meaning), and because word order must be changed in keeping with the grammatical structure of the target language.
>
> — [NLTK Book], §1.5, с. 30

«Машинный перевод труден, потому что у слова может быть несколько возможных
переводов (в зависимости от значения) и потому что порядок слов приходится менять
в соответствии с грамматической структурой целевого языка».

> Despite the research-led advances in tasks such as RTE, natural language systems that have been deployed for real-world applications still cannot perform common-sense reasoning or draw on world knowledge in a general and robust manner. <…> Accordingly, right from the beginning, an important goal of NLP research has been to make progress on the difficult task of building technologies that "understand language," using superficial yet powerful techniques instead of unrestricted knowledge and reasoning capabilities.
>
> — [NLTK Book], §1.5, Limitations of NLP, с. 33

«Несмотря на успехи исследований в задачах вроде распознавания текстового
следования, системы на естественном языке, внедрённые в реальные приложения,
всё ещё не умеют рассуждать на основе здравого смысла и надёжно привлекать знания
о мире. <…> Поэтому с самого начала важной целью исследований NLP было продвинуться
в трудной задаче построения технологий, которые „понимают язык“, с помощью
поверхностных, но мощных методов вместо неограниченных знаний и способности
к рассуждению».

### Конвейер

> Система обработки естественного языка называется конвейером, потому что обработка естественного языка производится в несколько этапов. Текст на естественном языке поступает с одного конца, а результаты выходят с другого конца конвейера, содержащего разные этапы обработки, реализованные на языке Python, и передающие данные друг другу.
>
> — [Лейн], §1.1, с. 35

> Spoken input (top left) is analyzed, words are recognized, sentences are parsed and interpreted in context, application-specific actions take place (top right); a response is planned, realized as a syntactic structure, then to suitably inflected words, and finally to spoken output; different types of linguistic knowledge inform each stage of the process.
>
> — [NLTK Book], §1.5, подпись к рис. 1-5, с. 32

«Речевой ввод (слева вверху) анализируется: распознаются слова, предложения
разбираются и интерпретируются в контексте, выполняются действия, специфичные
для приложения (справа вверху); затем планируется ответ, он воплощается
в синтаксическую структуру, затем в слова в нужных формах и, наконец, в речевой
вывод; на каждом этапе используются разные виды лингвистических знаний».

---

## 2. NLTK и корпусы

### Почему NLTK

> Here is a small list of available NLP tools: GATE, Mallet, Open NLP, UIMA, Stanford toolkit, Genism, Natural Language Tool Kit (NLTK). <…> However, when it comes to the ease of use and explanation of the concepts, NLTK scores really high. NLTK is also a very good learning kit because the learning curve of Python (on which NLTK is written) is very fast. NLTK has incorporated most of the NLP tasks, it's very elegant and easy to work with.
>
> — [Essentials], гл. 1, с. 3

«Вот небольшой список доступных инструментов NLP: GATE, Mallet, OpenNLP, UIMA,
Stanford toolkit, Gensim, NLTK. <…> Однако по простоте использования и объяснения
понятий NLTK получает очень высокую оценку. NLTK — ещё и очень хороший учебный
набор, потому что Python (на котором написан NLTK) осваивается очень быстро.
В NLTK реализовано большинство задач NLP, работать с ним изящно и просто».

### Установка

> Once you've installed NLTK, start up the Python interpreter as before, and install the data required for the book by typing the following two commands at the Python prompt, then selecting the book collection <…>
>
> ```python
> >>> import nltk
> >>> nltk.download()
> ```
>
> — [NLTK Book], §1.1, с. 3

«Установив NLTK, запустите интерпретатор Python и установите данные, нужные
для книги: введите две команды и выберите коллекцию book».

> The Collections tab on the downloader shows how the packages are grouped into sets, and you should select the line labeled *book* to obtain all data required for the examples and exercises in this book.
>
> — [NLTK Book], подпись к рис. 1-1, с. 3

«Вкладка Collections в окне загрузчика показывает, как пакеты сгруппированы
в наборы; выберите строку *book*, чтобы получить все данные для примеров
и упражнений книги».

*Примечание.* Сегодня то же самое делается так:

```bash
pip install nltk matplotlib
```

```python
import nltk
nltk.download("book")       # коллекция book без окна загрузчика
nltk.download("punkt_tab")  # модель токенизатора для word_tokenize (NLTK 3.9+)
```

### Что такое корпус

> Practical work in Natural Language Processing typically uses large bodies of linguistic data, or corpora.
>
> — [NLTK Book], гл. 2, с. 39

«Практическая работа в NLP обычно опирается на большие массивы языковых данных —
корпусы».

> As just mentioned, a text corpus is a large body of text. Many corpora are designed to contain a careful balance of material in one or more genres.
>
> — [NLTK Book], §2.1, с. 39

«Как уже сказано, текстовый корпус — это большой массив текста. Многие корпусы
составляют так, чтобы материал одного или нескольких жанров был тщательно
сбалансирован».

> A corpus is a collection of text documents, and corpora is the plural of corpus. So a custom corpus is really just a bunch of text files in a directory, often alongside many other directories of text files.
>
> — [Cookbook], гл. 3, с. 46

«Корпус — это коллекция текстовых документов; *corpora* — множественное число
от *corpus*. Так что собственный корпус — это просто набор текстовых файлов в папке,
часто рядом с множеством других папок с текстовыми файлами».

### Gutenberg

> NLTK includes a small selection of texts from the Project Gutenberg electronic text archive, which contains some 25,000 free electronic books, hosted at http://www.gutenberg.org/.
>
> ```python
> >>> import nltk
> >>> nltk.corpus.gutenberg.fileids()
> ['austen-emma.txt', 'austen-persuasion.txt', 'austen-sense.txt', 'bible-kjv.txt',
> 'blake-poems.txt', 'bryant-stories.txt', 'burgess-busterbrown.txt',
> 'carroll-alice.txt', 'chesterton-ball.txt', 'chesterton-brown.txt',
> 'chesterton-thursday.txt', 'edgeworth-parents.txt', 'melville-moby_dick.txt',
> 'milton-paradise.txt', 'shakespeare-caesar.txt', 'shakespeare-hamlet.txt',
> 'shakespeare-macbeth.txt', 'whitman-leaves.txt']
> >>> emma = nltk.corpus.gutenberg.words('austen-emma.txt')
> >>> len(emma)
> 192427
> ```
>
> — [NLTK Book], §2.1, с. 40

«NLTK включает небольшую выборку текстов из электронного архива „Проект Гутенберг“,
в котором около 25 000 бесплатных электронных книг».

> Let's write a short program to display other information about each text, by looping over all the values of fileid corresponding to the gutenberg file identifiers listed earlier and then computing statistics for each text.
>
> ```python
> >>> for fileid in gutenberg.fileids():
> ...     num_chars = len(gutenberg.raw(fileid))
> ...     num_words = len(gutenberg.words(fileid))
> ...     num_sents = len(gutenberg.sents(fileid))
> ...     num_vocab = len(set([w.lower() for w in gutenberg.words(fileid)]))
> ...     print int(num_chars/num_words), int(num_words/num_sents), int(num_words/num_vocab), fileid
> ...
> 4 21 26 austen-emma.txt
> 4 23 16 austen-persuasion.txt
> 4 24 22 austen-sense.txt
> 4 33 79 bible-kjv.txt
> 4 18 5 blake-poems.txt
> ...
> 4 52 10 milton-paradise.txt
> 4 12 8 shakespeare-caesar.txt
> 4 13 7 shakespeare-hamlet.txt
> 4 13 6 shakespeare-macbeth.txt
> 4 35 12 whitman-leaves.txt
> ```
>
> This program displays three statistics for each text: average word length, average sentence length, and the number of times each vocabulary item appears in the text on average (our lexical diversity score). Observe that average word length appears to be a general property of English, since it has a recurrent value of 4. (In fact, the average word length is really 3, not 4, since the num_chars variable counts space characters.) By contrast average sentence length and lexical diversity appear to be characteristics of particular authors.
>
> — [NLTK Book], §2.1, с. 40–41

«Напишем короткую программу, которая выведет сведения о каждом тексте, перебирая
все идентификаторы файлов корпуса и вычисляя статистику для каждого текста. <…>
Программа выводит три показателя для каждого текста: среднюю длину слова, среднюю
длину предложения и сколько раз в среднем встречается каждая единица словаря
(наш показатель лексического разнообразия). Заметьте, что средняя длина слова,
по-видимому, общее свойство английского языка: всюду получается 4. (На самом деле
средняя длина слова 3, а не 4, потому что `num_chars` учитывает пробелы.)
Средняя длина предложения и лексическое разнообразие, напротив, оказываются
характеристиками конкретных авторов».

*Примечание.* В Python 3 вместо `print ...` пишется `print(...)`,
а `int(a / b)` удобнее заменить на `round(a / b)`.

*Три уровня доступа к тексту корпуса:*

> The `raw()` function gives us the contents of the file without any linguistic processing. <…> The `sents()` function divides the text up into its sentences, where each sentence is a list of words:
>
> ```python
> >>> raw = gutenberg.raw("burgess-busterbrown.txt")
> >>> raw[1:20]
> 'The Adventures of B'
> >>> words = gutenberg.words("burgess-busterbrown.txt")
> >>> words[1:20]
> ['The', 'Adventures', 'of', 'Buster', 'Bear', 'by', 'Thornton', 'W', '.',
> 'Burgess', '1920', ']', 'I', 'BUSTER', 'BEAR', 'GOES', 'FISHING', 'Buster',
> 'Bear']
> >>> sents = gutenberg.sents("burgess-busterbrown.txt")
> >>> sents[1:20]
> [['I'], ['BUSTER', 'BEAR', 'GOES', 'FISHING'], ['Buster', 'Bear', 'yawned', 'as',
> 'he', 'lay', 'on', 'his', 'comfortable', 'bed', 'of', 'leaves', 'and', 'watched',
> 'the', 'first', 'early', 'morning', 'sunbeams', 'creeping', 'through', ...], ...]
> ```
>
> — [NLTK Book], §2.1, с. 41, 50–51

«Функция `raw()` выдаёт содержимое файла без какой-либо лингвистической обработки.
<…> Функция `sents()` делит текст на предложения, где каждое предложение — список
слов».

### Brown

> The Brown Corpus was the first million-word electronic corpus of English, created in 1961 at Brown University. This corpus contains text from 500 sources, and the sources have been categorized by genre, such as news, editorial, and so on.
>
> ```python
> >>> from nltk.corpus import brown
> >>> brown.categories()
> ['adventure', 'belles_lettres', 'editorial', 'fiction', 'government', 'hobbies',
> 'humor', 'learned', 'lore', 'mystery', 'news', 'religion', 'reviews', 'romance',
> 'science_fiction']
> >>> brown.words(categories='news')
> ['The', 'Fulton', 'County', 'Grand', 'Jury', 'said', ...]
> >>> brown.words(fileids=['cg22'])
> ['Does', 'our', 'society', 'have', 'a', 'runaway', ',', ...]
> >>> brown.sents(categories=['news', 'editorial', 'reviews'])
> [['The', 'Fulton', 'County'...], ['The', 'jury', 'further'...], ...]
> ```
>
> The Brown Corpus is a convenient resource for studying systematic differences between genres, a kind of linguistic inquiry known as stylistics.
>
> — [NLTK Book], §2.1, с. 42–43

«Брауновский корпус — первый электронный корпус английского языка объёмом
в миллион слов, созданный в 1961 году в Университете Брауна. Он содержит тексты
из 500 источников, распределённых по жанрам: новости, редакционные статьи и т. д.
<…> Брауновский корпус удобен для изучения систематических различий между жанрами;
такое лингвистическое исследование называется стилистикой».

> Next, we need to obtain counts for each genre of interest. We'll use NLTK's support for conditional frequency distributions.
>
> ```python
> >>> cfd = nltk.ConditionalFreqDist(
> ...           (genre, word)
> ...           for genre in brown.categories()
> ...           for word in brown.words(categories=genre))
> >>> genres = ['news', 'religion', 'hobbies', 'science_fiction', 'romance', 'humor']
> >>> modals = ['can', 'could', 'may', 'might', 'must', 'will']
> >>> cfd.tabulate(conditions=genres, samples=modals)
>                   can could  may might must will
>            news    93    86   66    38   50  389
>        religion    82    59   78    12   54   71
>         hobbies   268    58  131    22   83  264
> science_fiction    16    49    4    12    8   16
>         romance    74   193   11    51   45   43
>           humor    16    30    8     8    9   13
> ```
>
> Observe that the most frequent modal in the news genre is *will*, while the most frequent modal in the romance genre is *could*. Would you have predicted this? The idea that word counts might distinguish genres will be taken up again in Chapter 6.
>
> — [NLTK Book], §2.1, с. 44

«Теперь получим частоты для каждого интересующего нас жанра. Воспользуемся
условными частотными распределениями NLTK. <…> Заметьте, что самый частый модальный
глагол в новостях — *will*, а в любовных романах — *could*. Вы бы это предсказали?
К идее, что частоты слов помогают различать жанры, мы вернёмся в главе 6».

> A conditional frequency distribution is a collection of frequency distributions, each one for a different "condition." The condition will often be the category of the text. <…> Each pair has the form (condition, event). If we were processing the entire Brown Corpus by genre, there would be 15 conditions (one per genre) and 1,161,192 events (one per word).
>
> — [NLTK Book], §2.2, с. 52

«Условное частотное распределение — это набор частотных распределений, по одному
на каждое „условие“. Условием часто служит категория текста. <…> Каждая пара имеет
вид (условие, событие). Если обработать весь Брауновский корпус по жанрам,
получится 15 условий (по одному на жанр) и 1 161 192 события (по одному на слово)».

### Reuters

> The Reuters Corpus contains 10,788 news documents totaling 1.3 million words. The documents have been classified into 90 topics, and grouped into two sets, called "training" and "test"; thus, the text with fileid 'test/14826' is a document drawn from the test set. This split is for training and testing algorithms that automatically detect the topic of a document <…>
>
> Unlike the Brown Corpus, categories in the Reuters Corpus overlap with each other, simply because a news story often covers multiple topics.
>
> ```python
> >>> reuters.categories('training/9865')
> ['barley', 'corn', 'grain', 'wheat']
> >>> reuters.fileids('barley')
> ['test/15618', 'test/15649', 'test/15676', 'test/15728', 'test/15871', ...]
> >>> reuters.words('training/9865')[:14]
> ['FRENCH', 'FREE', 'MARKET', 'CEREAL', 'EXPORT', 'BIDS',
> 'DETAILED', 'French', 'operators', 'have', 'requested', 'licences', 'to', 'export']
> ```
>
> — [NLTK Book], §2.1, с. 44–45

«Корпус Reuters содержит 10 788 новостных документов общим объёмом 1,3 млн слов.
Документы распределены по 90 темам и разбиты на два набора, „обучающий“
и „тестовый“; так, текст с идентификатором `test/14826` взят из тестового набора.
Это разбиение нужно для обучения и проверки алгоритмов, автоматически определяющих
тему документа. <…> В отличие от Брауновского корпуса, категории Reuters
пересекаются, просто потому что новость часто затрагивает несколько тем».

### Устройство корпусов

> The simplest kind lacks any structure: it is just a collection of texts. Often, texts are grouped into categories that might correspond to genre, source, author, language, etc. Sometimes these categories overlap, notably in the case of topical categories, as a text can be relevant to more than one topic. Occasionally, text collections have temporal structure, news collections being the most common example.
>
> — [NLTK Book], §2.1, Text Corpus Structure, с. 49

«Простейший корпус лишён всякой структуры: это просто собрание текстов. Часто тексты
сгруппированы по категориям, соответствующим жанру, источнику, автору, языку и т. п.
Иногда категории пересекаются, особенно тематические, поскольку текст может
относиться к нескольким темам. Бывает, что у собрания текстов есть временная
структура; самый частый пример — собрания новостей».

> The simplest kind of corpus is a collection of isolated texts with no particular organization; some corpora are structured into categories, such as genre (Brown Corpus); some categorizations overlap, such as topic categories (Reuters Corpus); other corpora represent language use over time (Inaugural Address Corpus).
>
> — [NLTK Book], подпись к рис. 2-3, с. 50

«Простейший корпус — собрание отдельных текстов без особой организации; некоторые
корпусы разбиты на категории, например по жанрам (Brown); в некоторых категории
пересекаются, например тематические (Reuters); другие корпусы отражают употребление
языка во времени (корпус инаугурационных речей)».

*Таблица 2-3 NLTK Book (с. 50) — общий интерфейс корпусных ридеров (выборка):*

| Example | Description |
| --- | --- |
| `fileids()` | The files of the corpus |
| `fileids([categories])` | The files of the corpus corresponding to these categories |
| `categories()` | The categories of the corpus |
| `raw()` | The raw content of the corpus |
| `words(fileids=[f1,f2,f3])` | The words of the specified fileids |
| `words(categories=[c1,c2])` | The words of the specified categories |
| `sents(categories=[c1,c2])` | The sentences of the specified categories |
| `encoding(fileid)` | The encoding of the file (if known) |

### Свой корпус

> If you have a your own collection of text files that you would like to access using the methods discussed earlier, you can easily load them with the help of NLTK's PlaintextCorpusReader. <…> The second parameter of the PlaintextCorpusReader initializer can be a list of fileids, like ['a.txt', 'test/b.txt'], or a pattern that matches all fileids, like '[abc]/.*\.txt' <…>
>
> ```python
> >>> from nltk.corpus import PlaintextCorpusReader
> >>> corpus_root = '/usr/share/dict'
> >>> wordlists = PlaintextCorpusReader(corpus_root, '.*')
> >>> wordlists.fileids()
> ['README', 'connectives', 'propernames', 'web2', 'web2a', 'words']
> >>> wordlists.words('connectives')
> ['the', 'of', 'and', 'to', 'a', 'in', 'that', 'is', ...]
> ```
>
> — [NLTK Book], §2.1, Loading Your Own Corpus, с. 51

«Если у вас есть своя коллекция текстовых файлов и вы хотите обращаться к ней теми же
методами, её легко загрузить с помощью `PlaintextCorpusReader`. <…> Вторым параметром
конструктора может быть список идентификаторов файлов, например
`['a.txt', 'test/b.txt']`, или шаблон, которому соответствуют все идентификаторы,
например `'[abc]/.*\.txt'`».

> If you have a large corpus of text, you may want to categorize it into separate sections. <…> The easiest way to categorize a corpus is to have one file for each category. <…>
>
> ```python
> >>> from nltk.corpus.reader import CategorizedPlaintextCorpusReader
> >>> reader = CategorizedPlaintextCorpusReader('.', r'movie_.*\.txt',
> ...     cat_pattern=r'movie_(\w+)\.txt')
> >>> reader.categories()
> ['neg', 'pos']
> >>> reader.fileids(categories=['neg'])
> ['movie_neg.txt']
> ```
>
> The first two arguments to CategorizedPlaintextCorpusReader are the root directory and fileids, which are passed on to the PlaintextCorpusReader to read in the files. The cat_pattern keyword argument is a regular expression for extracting the category names from the fileids. In our case, the category is the part of the fileid after movie_ and before .txt. The category must be surrounded by grouping parenthesis.
>
> — [Cookbook], гл. 3, Creating a categorized text corpus, с. 58–60

«Если у вас большой корпус, его можно разбить на разделы. <…> Проще всего
категоризовать корпус, отведя по файлу на каждую категорию. <…> Первые два аргумента
`CategorizedPlaintextCorpusReader` — корневая папка и идентификаторы файлов; они
передаются `PlaintextCorpusReader` для чтения файлов. Именованный аргумент
`cat_pattern` — регулярное выражение, извлекающее названия категорий
из идентификаторов файлов. В нашем случае категория — часть идентификатора после
`movie_` и до `.txt`. Категория должна быть заключена в группирующие скобки».

*Примечание.* Для русских текстов нужно явно указать кодировку и русскую модель
разбиения на предложения (по умолчанию ридер использует английскую):

```python
from nltk.corpus.reader import PlaintextCorpusReader
from nltk.tokenize import PunktTokenizer   # NLTK 3.9+

corpus = PlaintextCorpusReader(
    "my_corpus", r".*\.txt", encoding="utf-8",
    sent_tokenizer=PunktTokenizer("russian"),
)
```

---

## 3. Сырой текст: файлы, веб, кодировки

> The most important source of texts is undoubtedly the Web. It's convenient to have existing text collections to explore, such as the corpora we saw in the previous chapters. However, you probably have your own text sources in mind, and need to learn how to access them.
>
> — [NLTK Book], гл. 3, с. 79

«Самый важный источник текстов — несомненно, веб. Удобно иметь готовые коллекции
текстов, вроде корпусов из предыдущих глав. Но у вас, вероятно, есть свои источники
текстов, и нужно научиться до них добираться».

### Электронные книги

> Text number 2554 is an English translation of *Crime and Punishment*, and we can access it as follows.
>
> ```python
> >>> from urllib import urlopen
> >>> url = "http://www.gutenberg.org/files/2554/2554.txt"
> >>> raw = urlopen(url).read()
> >>> type(raw)
> <type 'str'>
> >>> len(raw)
> 1176831
> >>> raw[:75]
> 'The Project Gutenberg EBook of Crime and Punishment, by Fyodor Dostoevsky\r\n'
> ```
>
> The variable raw contains a string with 1,176,831 characters. <…> This is the raw content of the book, including many details we are not interested in, such as whitespace, line breaks, and blank lines. <…> For our language processing, we want to break up the string into words and punctuation, as we saw in Chapter 1. This step is called tokenization, and it produces our familiar structure, a list of words and punctuation.
>
> ```python
> >>> tokens = nltk.word_tokenize(raw)
> >>> type(tokens)
> <type 'list'>
> >>> len(tokens)
> 255809
> >>> tokens[:10]
> ['The', 'Project', 'Gutenberg', 'EBook', 'of', 'Crime', 'and', 'Punishment', ',', 'by']
> ```
>
> — [NLTK Book], §3.1, с. 80

«Текст номер 2554 — английский перевод „Преступления и наказания“; получить его
можно так. <…> Переменная `raw` содержит строку из 1 176 831 символа. <…> Это сырое
содержимое книги, включая множество ненужных нам деталей: пробелы, переносы строк,
пустые строки. <…> Для обработки языка нужно разбить строку на слова и знаки
препинания, как в главе 1. Этот шаг называется токенизацией; он даёт знакомую нам
структуру — список слов и знаков препинания».

*Примечание.* В Python 3 модуль называется иначе, а байты нужно явно декодировать:

```python
from urllib.request import urlopen
url = "https://www.gutenberg.org/cache/epub/2554/pg2554.txt"
raw = urlopen(url).read().decode("utf-8")
```

*То же через библиотеку `requests`; [Лейн] объясняет разницу между `.content` и `.text`:*

> Для получения обычного текстового документа можно использовать атрибут response.content, содержащий исходные байты HTML-страницы. Чтобы получить строку, можно использовать свойство response.text, при обращении к которому байты текста будут автоматически декодированы и преобразованы в Юникод.
>
> — [Лейн], §3.1, с. 139

```python
import requests
response = requests.get(url, timeout=30)
raw = response.text          # строка str
raw_bytes = response.content # исходные байты
```

### От списка токенов к `nltk.Text`

> If we now take the further step of creating an NLTK text from this list, we can carry out all of the other linguistic processing we saw in Chapter 1, along with the regular list operations, such as slicing:
>
> ```python
> >>> text = nltk.Text(tokens)
> >>> type(text)
> <type 'nltk.text.Text'>
> >>> text.collocations()
> Katerina Ivanovna; Pulcheria Alexandrovna; Avdotya Romanovna; Pyotr
> Petrovitch; Project Gutenberg; Marfa Petrovna; Rodion Romanovitch;
> Sofya Semyonovna; Nikodim Fomitch; did not; Hay Market; Andrey
> Semyonovitch; old woman; Literary Archive; Dmitri Prokofitch; great
> deal; United States; Praskovya Pavlovna; Porfiry Petrovitch; ear rings
> ```
>
> — [NLTK Book], §3.1, с. 81

«Если теперь сделать ещё шаг и создать из этого списка текст NLTK, можно выполнять
всю лингвистическую обработку из главы 1, а также обычные операции со списками,
например срезы».

### Служебный текст

> Notice that *Project Gutenberg* appears as a collocation. This is because each text downloaded from Project Gutenberg contains a header with the name of the text, the author, the names of people who scanned and corrected the text, a license, and so on. Sometimes this information appears in a footer at the end of the file. We cannot reliably detect where the content begins and ends, and so have to resort to manual inspection of the file, to discover unique strings that mark the beginning and the end, before trimming raw to be just the content and nothing else:
>
> ```python
> >>> raw.find("PART I")
> 5303
> >>> raw.rfind("End of Project Gutenberg's Crime")
> 1157681
> >>> raw = raw[5303:1157681]
> >>> raw.find("PART I")
> 0
> ```
>
> <…> This was our first brush with the reality of the Web: texts found on the Web may contain unwanted material, and there may not be an automatic way to remove it. But with a small amount of extra work we can extract the material we need.
>
> — [NLTK Book], §3.1, с. 81

«Заметьте, что *Project Gutenberg* попало в коллокации. Дело в том, что каждый текст
с сайта „Проекта Гутенберг“ содержит заголовок с названием текста, автором, именами
людей, которые сканировали и вычитывали текст, лицензией и т. д. Иногда эти сведения
стоят в конце файла. Надёжно определить, где начинается и кончается содержательная
часть, мы не можем, поэтому приходится вручную просмотреть файл, найти уникальные
строки, отмечающие начало и конец, и обрезать `raw` так, чтобы осталось только
содержимое. <…> Это наше первое столкновение с реальностью веба: найденные в нём
тексты могут содержать лишний материал, и автоматического способа удалить его может
не быть. Но небольшой дополнительной работой можно извлечь то, что нужно».

### HTML

> Much of the text on the Web is in the form of HTML documents. <…>
>
> ```python
> >>> url = "http://news.bbc.co.uk/2/hi/health/2284783.stm"
> >>> html = urlopen(url).read()
> >>> html[:60]
> '<!doctype html public "-//W3C//DTD HTML 4.0 Transitional//EN'
> ```
>
> Getting text out of HTML is a sufficiently common task that NLTK provides a helper function `nltk.clean_html()`, which takes an HTML string and returns raw text. <…> For more sophisticated processing of HTML, use the Beautiful Soup package <…>
>
> — [NLTK Book], §3.1, с. 81–82

«Значительная часть текста в вебе — HTML-документы. <…> Извлечение текста из HTML —
задача настолько частая, что в NLTK есть вспомогательная функция `nltk.clean_html()`:
она принимает строку HTML и возвращает сырой текст. <…> Для более сложной обработки
HTML используйте пакет Beautiful Soup».

*Примечание.* В NLTK 3 функция `clean_html()` удалена; используется
рекомендованный книгой Beautiful Soup:

```python
from bs4 import BeautifulSoup
raw = BeautifulSoup(html, "html.parser").get_text()
```

*Как это выглядит без инструментов, видно в [Essentials]: книга разбивает HTML
главной страницы python.org по пробелам.*

> As you can see, there is an excess of html tags and other unwanted characters when we use the preceding method.
>
> — [Essentials], гл. 1, с. 12

«Как видите, при этом способе получается избыток HTML-тегов и других ненужных
символов».

### Локальные файлы

> In order to read a local file, we need to use Python's built-in `open()` function, followed by the `read()` method. <…>
>
> ```python
> >>> f = open('document.txt')
> >>> raw = f.read()
> ```
>
> <…> NLTK's corpus files can also be accessed using these methods. We simply have to use `nltk.data.find()` to get the filename for any corpus item.
>
> ```python
> >>> path = nltk.data.find('corpora/gutenberg/melville-moby_dick.txt')
> >>> raw = open(path, 'rU').read()
> ```
>
> — [NLTK Book], §3.1, с. 84–85

«Чтобы прочитать локальный файл, используем встроенную функцию `open()` и затем метод
`read()`. <…> Файлы корпусов NLTK тоже можно читать этими методами: достаточно
получить имя файла любого элемента корпуса через `nltk.data.find()`».

*Примечание.* Режим `'rU'` в Python 3.11 удалён. Кодировку указываем всегда:

```python
with open("document.txt", encoding="utf-8") as f:
    raw = f.read()
```

### Конвейер обработки

> We open a URL and read its HTML content, remove the markup and select a slice of characters; this is then tokenized and optionally converted into an `nltk.Text` object; we can also lowercase all the words and extract the vocabulary.
>
> — [NLTK Book], подпись к рис. 3-1, с. 86

«Открываем URL и читаем его HTML-содержимое, удаляем разметку и выбираем срез
символов; затем текст токенизируется и при желании превращается в объект
`nltk.Text`; можно также привести все слова к нижнему регистру и извлечь словарь».

> When we load the contents of a URL or file, and when we strip out HTML markup, we are dealing with strings, Python's `<str>` data type <…> When we tokenize a string we produce a list (of words), and this is Python's `<list>` type. Normalizing and sorting lists produces other lists:
>
> ```python
> >>> tokens = nltk.word_tokenize(raw)
> >>> type(tokens)
> <type 'list'>
> >>> words = [w.lower() for w in tokens]
> >>> type(words)
> <type 'list'>
> >>> vocab = sorted(set(words))
> >>> type(vocab)
> <type 'list'>
> ```
>
> — [NLTK Book], §3.1, с. 86

«Загружая содержимое URL или файла и удаляя HTML-разметку, мы имеем дело со строками,
тип `str`. <…> Токенизируя строку, мы получаем список (слов), тип `list`. Нормализация
и сортировка списков дают другие списки».

### Unicode и кодировки

> Our programs will often need to deal with different languages, and different character sets. The concept of "plain text" is a fiction. If you live in the English-speaking world you probably use ASCII, possibly without realizing it.
>
> — [NLTK Book], §3.3, с. 93

«Нашим программам часто придётся иметь дело с разными языками и наборами символов.
Понятие „простого текста“ — фикция. Если вы живёте в англоязычном мире, вы, вероятно,
пользуетесь ASCII, возможно, сами того не замечая».

> Unicode supports over a million characters. Each character is assigned a number, called a code point. In Python, code points are written in the form `\uXXXX`, where XXXX is the number in four-digit hexadecimal form.
>
> Within a program, we can manipulate Unicode strings just like normal strings. However, when Unicode characters are stored in files or displayed on a terminal, they must be encoded as a stream of bytes. Some encodings (such as ASCII and Latin-2) use a single byte per code point, so they can support only a small subset of Unicode, enough for a single language. Other encodings (such as UTF-8) use multiple bytes and can represent the full range of Unicode characters.
>
> Text in files will be in a particular encoding, so we need some mechanism for translating it into Unicode—translation into Unicode is called *decoding*. Conversely, to write out Unicode to a file or a terminal, we first need to translate it into a suitable encoding—this translation out of Unicode is called *encoding* <…>
>
> From a Unicode perspective, characters are abstract entities that can be realized as one or more glyphs. Only glyphs can appear on a screen or be printed on paper. A font is a mapping from characters to glyphs.
>
> — [NLTK Book], §3.3, What Is Unicode?, с. 94

«Unicode поддерживает более миллиона символов. Каждому символу присвоен номер,
называемый кодовой точкой. В Python кодовые точки записываются в виде `\uXXXX`,
где XXXX — номер в четырёхзначной шестнадцатеричной форме.
Внутри программы со строками Unicode можно работать как с обычными строками.
Но когда символы Unicode сохраняются в файлы или выводятся на терминал, их нужно
закодировать в поток байтов. Некоторые кодировки (ASCII, Latin-2) отводят один байт
на кодовую точку и потому поддерживают лишь малую часть Unicode, достаточную для одного
языка. Другие (например, UTF-8) используют несколько байтов и могут представить весь
диапазон символов Unicode.
Текст в файлах хранится в определённой кодировке, поэтому нужен механизм перевода его
в Unicode; перевод в Unicode называется *декодированием*. И наоборот, чтобы записать
Unicode в файл или вывести на терминал, его сначала нужно перевести в подходящую
кодировку; перевод из Unicode называется *кодированием*.
С точки зрения Unicode символы — абстрактные сущности, которые могут воплощаться
в одном или нескольких глифах. Только глифы появляются на экране или на бумаге.
Шрифт — это отображение символов в глифы».

> Строки (str) — последовательности символов Юникода. Некоторые символы str не из набора ASCII могут состоять из нескольких байтов. <…> Байты (bytes) — это массивы восьмибитных значений, обычно используемых для хранения символов таблицы ASCII или символов расширенной таблицы ASCII (в которой целочисленные значения ord превышают 128).
>
> — [Лейн], Приложение Б, §Б.2.1, с. 668

> We find the integer ordinal of a character using `ord()`. <…> The module `unicodedata` lets us inspect the properties of Unicode characters. <…>
>
> ```python
> '\xc3\xb3' U+00f3 LATIN SMALL LETTER O WITH ACUTE
> '\xc5\x9b' U+015b LATIN SMALL LETTER S WITH ACUTE
> '\xc5\x9a' U+015a LATIN CAPITAL LETTER S WITH ACUTE
> '\xc4\x85' U+0105 LATIN SMALL LETTER A WITH OGONEK
> '\xc5\x82' U+0142 LATIN SMALL LETTER L WITH STROKE
> ```
>
> <…> The next examples illustrate how Python string methods and the `re` module accept Unicode strings. <…> NLTK tokenizers allow Unicode strings as input, and correspondingly yield Unicode strings as output.
>
> — [NLTK Book], §3.3, с. 95–97

«Целочисленный номер символа находим функцией `ord()`. <…> Модуль `unicodedata`
позволяет узнать свойства символов Unicode. <…> Следующие примеры показывают, что
строковые методы Python и модуль `re` принимают строки Unicode. <…> Токенизаторы
NLTK принимают на вход строки Unicode и соответственно выдают строки Unicode».

*Примечание.* В книге текст на польском читается через `codecs.open(path,
encoding='latin2')`. В Python 3 тип `str` уже является строкой Unicode,
а кодировка указывается прямо в `open()`. Те же операции на русском:

```python
s = "Привет"
b = s.encode("utf-8")   # кодирование: str → bytes
len(s), len(b)          # (6, 12)
b.decode("utf-8")       # декодирование: 'Привет'
b.decode("cp1251")      # 'РџСЂРёРІРµС‚' — прочитали не той кодировкой

import unicodedata
ord("я"), hex(ord("я")), unicodedata.name("я")
# (1103, '0x44f', 'CYRILLIC SMALL LETTER YA')
```

---

## 4. Первые исследования корпуса

> It is easy to get our hands on millions of words of text. What can we do with it, assuming we can write some simple programs? <…>
>
> 1. What can we achieve by combining simple programming techniques with large quantities of text?
> 2. How can we automatically extract key words and phrases that sum up the style and content of a text?
>
> — [NLTK Book], гл. 1, с. 1

«Получить в своё распоряжение миллионы слов текста легко. Что можно с ними сделать,
если мы умеем писать простые программы? <…> 1. Чего можно добиться, сочетая простые
приёмы программирования с большими объёмами текста? 2. Как автоматически извлечь
ключевые слова и словосочетания, выражающие стиль и содержание текста?»

> ```python
> >>> from nltk.book import *
> *** Introductory Examples for the NLTK Book ***
> Loading text1, ..., text9 and sent1, ..., sent9
> text1: Moby Dick by Herman Melville 1851
> text2: Sense and Sensibility by Jane Austen 1811
> text3: The Book of Genesis
> text4: Inaugural Address Corpus
> text5: Chat Corpus
> text6: Monty Python and the Holy Grail
> text7: Wall Street Journal
> text8: Personals Corpus
> text9: The Man Who Was Thursday by G . K . Chesterton 1908
> ```
>
> — [NLTK Book], §1.1, с. 4

### Конкорданс

> There are many ways to examine the context of a text apart from simply reading it. A concordance view shows us every occurrence of a given word, together with some context. Here we look up the word *monstrous* in *Moby Dick* <…>
>
> ```python
> >>> text1.concordance("monstrous")
> Displaying 11 of 11 matches:
> ong the former , one was of a most monstrous size . ... This came towards us ,
> ON OF THE PSALMS . " Touching that monstrous bulk of the whale or ork we have r
> ll over with a heathenish array of monstrous clubs and spears . Some were thick
> d as you gazed , and wondered what monstrous cannibal and savage could ever hav
> that has survived the flood ; most monstrous and most mountainous ! That Himmal
> ...
> ```
>
> — [NLTK Book], §1.1, Searching Text, с. 4

«Кроме простого чтения, есть много способов исследовать контекст в тексте.
Конкорданс показывает каждое вхождение заданного слова вместе с некоторым контекстом.
Найдём слово *monstrous* в „Моби Дике“».

### Похожие слова и общие контексты

> A concordance permits us to see words in context. For example, we saw that *monstrous* occurred in contexts such as *the ___ pictures* and *the ___ size*. What other words appear in a similar range of contexts? <…>
>
> ```python
> >>> text1.similar("monstrous")
> subtly impalpable pitiable curious imperial perilous trustworthy
> abundant untoward singular lamentable few maddens horrible loving lazy
> mystifying christian exasperate puzzled
> >>> text2.similar("monstrous")
> very exceedingly so heartily a great good amazingly as sweet
> remarkably extremely vast
> ```
>
> Observe that we get different results for different texts. Austen uses this word quite differently from Melville; for her, *monstrous* has positive connotations, and sometimes functions as an intensifier like the word *very*.
>
> The term `common_contexts` allows us to examine just the contexts that are shared by two or more words, such as *monstrous* and *very*.
>
> ```python
> >>> text2.common_contexts(["monstrous", "very"])
> be_glad am_glad a_pretty is_pretty a_lucky
> ```
>
> — [NLTK Book], §1.1, с. 5

«Конкорданс позволяет видеть слова в контексте. Например, мы видели, что *monstrous*
встречается в контекстах вроде *the ___ pictures* и *the ___ size*. Какие ещё слова
встречаются в похожих контекстах? <…> Заметьте, что для разных текстов результаты
разные. Остин употребляет это слово совсем не так, как Мелвилл: у неё *monstrous*
имеет положительную окраску и иногда работает как усилитель, подобно слову *very*.
Метод `common_contexts` позволяет рассмотреть только контексты, общие для двух или
более слов, например *monstrous* и *very*».

> It is one thing to automatically detect that a particular word occurs in a text, and to display some words that appear in the same context. However, we can also determine the location of a word in the text: how many words from the beginning it appears. This positional information can be displayed using a dispersion plot. Each stripe represents an instance of a word, and each row represents the entire text.
>
> ```python
> >>> text4.dispersion_plot(["citizens", "democracy", "freedom", "duties", "America"])
> ```
>
> — [NLTK Book], §1.1, с. 6

«Одно дело — автоматически обнаружить, что слово встречается в тексте, и показать
слова, встречающиеся в том же контексте. Но можно определить и положение слова
в тексте: на каком расстоянии от начала оно стоит. Эти сведения о положении можно
показать на графике рассеяния. Каждая черта — одно вхождение слова, каждая строка —
весь текст».

### Токены, типы, лексическое разнообразие

> So Genesis has 44,764 words and punctuation symbols, or "tokens." A token is the technical name for a sequence of characters—such as *hairy*, *his*, or *:)*—that we want to treat as a group. When we count the number of tokens in a text, say, the phrase *to be or not to be*, we are counting occurrences of these sequences. Thus, in our example phrase there are two occurrences of *to*, two of *be*, and one each of *or* and *not*. But there are only four distinct vocabulary items in this phrase.
>
> — [NLTK Book], §1.1, Counting Vocabulary, с. 7

«Итак, в Книге Бытия 44 764 слова и знака препинания, или „токена“. Токен —
технический термин для последовательности символов (например, *hairy*, *his* или
*:)*), которую мы хотим рассматривать как единое целое. Считая токены в тексте,
скажем во фразе *to be or not to be*, мы считаем вхождения таких последовательностей.
В нашей фразе два вхождения *to*, два — *be* и по одному *or* и *not*. Но разных
единиц словаря в ней только четыре».

> ```python
> >>> len(text3)
> 44764
> >>> sorted(set(text3))
> ['!', "'", '(', ')', ',', ',)', '.', '.)', ':', ';', ';)', '?', '?)',
> 'A', 'Abel', 'Abelmizraim', 'Abidah', 'Abide', 'Abimael', 'Abimelech', ...]
> >>> len(set(text3))
> 2789
> ```
>
> Although it has 44,764 tokens, this book has only 2,789 distinct words, or "word types." A word type is the form or spelling of the word independently of its specific occurrences in a text—that is, the word considered as a unique item of vocabulary.
>
> — [NLTK Book], §1.1, с. 7–8

«Хотя в книге 44 764 токена, разных слов, или „словесных типов“, в ней только 2789.
Словесный тип — это форма или написание слова независимо от конкретных вхождений
в текст, то есть слово как уникальная единица словаря».

> Now, let's calculate a measure of the lexical richness of the text. The next example shows us that each word is used 16 times on average <…>
>
> ```python
> >>> len(text3) / len(set(text3))
> 16.050197203298673
> >>> text3.count("smote")
> 5
> >>> 100 * text4.count('a') / len(text4)
> 1.4643016433938312
> ```
>
> — [NLTK Book], §1.1, с. 8

«Теперь вычислим меру лексического богатства текста. Следующий пример показывает,
что каждое слово употреблено в среднем 16 раз».

*Таблица 1-1 NLTK Book (с. 10). Lexical diversity of various genres in the Brown Corpus:*

| Genre | Tokens | Types | Lexical diversity |
| --- | --- | --- | --- |
| skill and hobbies | 82345 | 11935 | 6.9 |
| humor | 21695 | 5017 | 4.3 |
| fiction: science | 14470 | 3233 | 4.5 |
| press: reportage | 100554 | 14394 | 7.0 |
| fiction: romance | 70022 | 8452 | 8.3 |
| religion | 39399 | 6373 | 6.2 |

### Частотное распределение: `FreqDist`

> How can we automatically identify the words of a text that are most informative about the topic and genre of the text? Imagine how you might go about finding the 50 most frequent words of a book. One method would be to keep a tally for each vocabulary item <…>
>
> The table in Figure 1-3 is known as a *frequency distribution*, and it tells us the frequency of each vocabulary item in the text. (In general, it could count any kind of observable event.) It is a "distribution" since it tells us how the total number of word tokens in the text are distributed across the vocabulary items.
>
> ```python
> >>> fdist1 = FreqDist(text1)
> >>> fdist1
> <FreqDist with 260819 outcomes>
> >>> vocabulary1 = fdist1.keys()
> >>> vocabulary1[:50]
> [',', 'the', '.', 'of', 'and', 'a', 'to', ';', 'in', 'that', "'", '-',
> 'his', 'it', 'I', 's', 'is', 'he', 'with', 'was', 'as', '"', 'all', 'for',
> 'this', '!', 'at', 'by', 'but', 'not', '--', 'him', 'from', 'be', 'on',
> 'so', 'whale', 'one', 'you', 'had', 'have', 'there', 'But', 'or', 'were',
> 'now', 'which', '?', 'me', 'like']
> >>> fdist1['whale']
> 906
> ```
>
> — [NLTK Book], §1.3, Frequency Distributions, с. 17

«Как автоматически найти слова текста, которые больше всего говорят о его теме
и жанре? Представьте, как бы вы искали 50 самых частых слов книги. Можно было бы
вести подсчёт для каждой единицы словаря. <…> Такая таблица называется *частотным
распределением*: она сообщает частоту каждой единицы словаря в тексте. (Вообще говоря,
подсчитывать можно любые наблюдаемые события.) Это „распределение“, потому что оно
показывает, как общее число токенов текста распределено по единицам словаря».

*Примечание.* В NLTK 3 `keys()` больше не упорядочены по частоте.
Тот же список получают так: `fdist1.most_common(50)`.

> Do any words produced in the last example help us grasp the topic or genre of this text? Only one word, *whale*, is slightly informative! It occurs over 900 times. The rest of the words tell us nothing about the text; they're just English "plumbing." What proportion of the text is taken up with such words? We can generate a cumulative frequency plot for these words, using `fdist1.plot(50, cumulative=True)` <…> These 50 words account for nearly half the book!
>
> — [NLTK Book], §1.3, с. 18

«Помогает ли хоть одно слово из этого списка понять тему или жанр текста? Лишь одно,
*whale*, немного информативно: оно встречается более 900 раз. Остальные слова ничего
не говорят о тексте, это просто английская „сантехника“. Какую долю текста занимают
такие слова? Построим кумулятивный частотный график `fdist1.plot(50, cumulative=True)`.
<…> Эти 50 слов составляют почти половину книги!»

> These words are stop words; words like *the*, *a*, *an*, and so on. Article pronouns are generally present in most of the documents, hence they are not discriminative enough to be informative. In most of the NLP and information retrieval tasks, people generally remove stop words.
>
> — [Essentials], гл. 1, с. 15

«Такие слова называются стоп-словами: *the*, *a*, *an* и т. п. Они встречаются
почти во всех документах и потому недостаточно различительны, чтобы быть
информативными. В большинстве задач NLP и информационного поиска стоп-слова
обычно удаляют».

> If the frequent words don't help us, how about the words that occur once only, the so-called *hapaxes*? View them by typing `fdist1.hapaxes()`. This list contains *lexicographer*, *cetological*, *contraband*, *expostulations*, and about 9,000 others. It seems that there are too many rare words, and without seeing the context we probably can't guess what half of the hapaxes mean in any case!
>
> — [NLTK Book], §1.3, с. 19

«Если частые слова не помогают, может быть, помогут слова, встречающиеся лишь однажды, —
так называемые *гапаксы*? Посмотрим их: `fdist1.hapaxes()`. В списке *lexicographer*,
*cetological*, *contraband*, *expostulations* и ещё около 9000 слов. Похоже, редких
слов слишком много, и без контекста мы, вероятно, всё равно не угадаем, что значит
половина гапаксов!»

> <…> perhaps it would be better to find frequently occurring long words. This seems promising since it eliminates frequent short words (e.g., *the*) and infrequent long words (e.g., *antiphilosophists*). Here are all words from the chat corpus that are longer than seven characters, that occur more than seven times:
>
> ```python
> >>> fdist5 = FreqDist(text5)
> >>> sorted([w for w in set(text5) if len(w) > 7 and fdist5[w] > 7])
> ['#14-19teens', '#talkcity_adults', '((((((((((', '........', 'Question',
> 'actually', 'anything', 'computer', 'cute.-ass', 'everyone', 'football',
> 'innocent', 'listening', 'remember', 'seriously', 'something', 'together',
> 'tomorrow', 'watching']
> ```
>
> <…> At last we have managed to automatically identify the frequently occurring content-bearing words of the text. It is a modest but important milestone: a tiny piece of code, processing tens of thousands of words, produces some informative output.
>
> — [NLTK Book], §1.3, Fine-Grained Selection of Words, с. 20

«<…> возможно, лучше искать часто встречающиеся длинные слова. Это выглядит
многообещающе: так отсекаются частые короткие слова (*the*) и редкие длинные
(*antiphilosophists*). Вот все слова чат-корпуса длиннее семи символов, встретившиеся
больше семи раз. <…> Наконец нам удалось автоматически выделить часто встречающиеся
содержательные слова текста. Это скромный, но важный рубеж: крошечный фрагмент кода,
обработав десятки тысяч слов, выдаёт информативный результат».

*Таблица 1-2 NLTK Book (с. 22). Functions defined for NLTK's frequency distributions (выборка):*

| Example | Description |
| --- | --- |
| `fdist = FreqDist(samples)` | Create a frequency distribution containing the given samples |
| `fdist['monstrous']` | Count of the number of times a given sample occurred |
| `fdist.freq('monstrous')` | Frequency of a given sample |
| `fdist.N()` | Total number of samples |
| `fdist.max()` | Sample with the greatest count |
| `fdist.tabulate()` | Tabulate the frequency distribution |
| `fdist.plot(cumulative=True)` | Cumulative plot of the frequency distribution |

### Коллокации

> A *collocation* is a sequence of words that occur together unusually often. Thus *red wine* is a collocation, whereas *the wine* is not. A characteristic of collocations is that they are resistant to substitution with words that have similar senses; for example, *maroon wine* sounds very odd.
>
> To get a handle on collocations, we start off by extracting from a text a list of word pairs, also known as *bigrams*.
>
> ```python
> >>> bigrams(['more', 'is', 'said', 'than', 'done'])
> [('more', 'is'), ('is', 'said'), ('said', 'than'), ('than', 'done')]
> ```
>
> Here we see that the pair of words *than-done* is a bigram <…>. Now, collocations are essentially just frequent bigrams, except that we want to pay more attention to the cases that involve rare words. In particular, we want to find bigrams that occur more often than we would expect based on the frequency of individual words.
>
> ```python
> >>> text4.collocations()
> United States; fellow citizens; years ago; Federal Government; General
> Government; American people; Vice President; Almighty God; Fellow
> citizens; Chief Magistrate; Chief Justice; God bless; Indian tribes;
> public debt; foreign nations; political parties; State governments;
> National Government; United Nations; public money
> >>> text8.collocations()
> medium build; social drinker; quiet nights; long term; age open;
> financially secure; fun times; similar interests; Age open; poss
> rship; single mum; permanent relationship; slim build; seeks lady;
> Late 30s; Photo pls; Vibrant personality; European background; ASIAN
> LADY; country drives
> ```
>
> The collocations that emerge are very specific to the genre of the texts. In order to find *red wine* as a collocation, we would need to process a much larger body of text.
>
> — [NLTK Book], §1.3, Collocations and Bigrams, с. 20–21

«*Коллокация* — последовательность слов, которые встречаются вместе необычно часто.
Так, *red wine* — коллокация, а *the wine* — нет. Характерное свойство коллокаций —
устойчивость к замене словами с близким значением: например, *maroon wine*
(„тёмно-бордовое вино“) звучит очень странно.
Чтобы подступиться к коллокациям, начнём с извлечения из текста списка пар слов,
или *биграмм*. <…> Коллокации — это, по сути, просто частые биграммы, только нас больше
интересуют случаи с редкими словами. А именно, мы хотим найти биграммы, которые
встречаются чаще, чем можно ожидать исходя из частоты отдельных слов. <…>
Найденные коллокации очень специфичны для жанра текстов. Чтобы найти *red wine* как
коллокацию, понадобился бы гораздо больший массив текста».

*Примечание.* В NLTK 3 `bigrams()` возвращает генератор: `list(nltk.bigrams(...))`.

> Collocations are two or more words that tend to appear frequently together, such as "United States". Of course, there are many other words that can come after "United", for example "United Kingdom", "United Airlines", and so on. As with many aspects of natural language processing, context is very important, and for collocations, context is everything!
>
> ```python
> >>> from nltk.corpus import webtext
> >>> from nltk.collocations import BigramCollocationFinder
> >>> from nltk.metrics import BigramAssocMeasures
> >>> words = [w.lower() for w in webtext.words('grail.txt')]
> >>> bcf = BigramCollocationFinder.from_words(words)
> >>> bcf.nbest(BigramAssocMeasures.likelihood_ratio, 4)
> [("'", 's'), ('arthur', ':'), ('#', '1'), ("'", 't')]
> ```
>
> Well that's not very useful! Let's refine it a bit by adding a word filter to remove punctuation and stopwords.
>
> ```python
> >>> from nltk.corpus import stopwords
> >>> stopset = set(stopwords.words('english'))
> >>> filter_stops = lambda w: len(w) < 3 or w in stopset
> >>> bcf.apply_word_filter(filter_stops)
> >>> bcf.nbest(BigramAssocMeasures.likelihood_ratio, 4)
> [('black', 'knight'), ('clop', 'clop'), ('head', 'knight'), ('mumble', 'mumble')]
> ```
>
> — [Cookbook], гл. 1, Discovering word collocations, с. 21–22

«Коллокации — это два или более слова, которые склонны часто появляться вместе,
например „United States“. Разумеется, после „United“ могут идти и многие другие слова:
„United Kingdom“, „United Airlines“ и т. д. Как и во многих вопросах обработки
естественного языка, контекст очень важен, а для коллокаций контекст — это всё! <…>
Ну, это не очень полезно! Уточним результат, добавив фильтр слов, удаляющий
пунктуацию и стоп-слова».

> The BigramCollocationFinder constructs two frequency distributions: one for each word, and another for bigrams. A frequency distribution, or FreqDist in NLTK, is basically an enhanced dictionary where the keys are what's being counted, and the values are the counts. Any filtering functions that are applied, reduce the size of these two FreqDists by eliminating any words that don't pass the filter.
>
> — [Cookbook], гл. 1, с. 22

«`BigramCollocationFinder` строит два частотных распределения: одно для отдельных
слов, другое для биграмм. Частотное распределение, или `FreqDist` в NLTK, — это,
в сущности, расширенный словарь, где ключи — то, что подсчитывается, а значения —
частоты. Применённые функции-фильтры уменьшают оба распределения, удаляя слова,
не прошедшие фильтр».

### Закон Ципфа

> В начале XX века французский стенографист Жан-Батист Эсту (Jean-Baptiste Estoup) обнаружил закономерность в частотах слов, которые он старательно подсчитывал вручную во многих документах (хвала небесам, что у нас есть компьютеры и Python). В 1930-х годах американский лингвист Джордж Кингсли Ципф (George Kingsley Zipf) попытался формализовать наблюдения Эсту, и в итоге обнаруженные соотношения стали носить имя Ципфа:
>
> «В любом корпусе высказываний на естественном языке частота любого слова обратно пропорциональна его позиции в таблице частот».
>
> — [Лейн], §3.5, с. 164

> Zipf's Law: Let f(w) be the frequency of a word w in free text. Suppose that all the words of a text are ranked according to their frequency, with the most frequent word first. Zipf's Law states that the frequency of a word type is inversely proportional to its rank (i.e., f × r = k, for some constant k). For example, the 50th most common word type should occur three times as frequently as the 150th most common word type.
>
> — [NLTK Book], гл. 2, упр. 23, с. 76

«Закон Ципфа. Пусть f(w) — частота слова w в свободном тексте. Упорядочим все слова
текста по частоте, начиная с самого частого. Закон Ципфа утверждает, что частота
словесного типа обратно пропорциональна его рангу (то есть f × r = k для некоторой
константы k). Например, 50-й по частоте словесный тип должен встречаться втрое чаще,
чем 150-й».

> Но самое удивительное то, что эта зависимость становится линейной при отображении на логарифмическую шкалу. Например, первый элемент ранжированного списка может встречаться в два раза чаще, чем второй, и в три раза чаще, чем третий. Для любого корпуса или документа можно быстро построить график частот использования слов относительно их ранга (частоты). Любые аномальные значения, выделяющиеся на прямой линии логарифмического графика, заслуживают исследования.
>
> — [Лейн], §3.5, с. 164

> Оказывается, закон Ципфа применим к частотам множества явлений. <…> Нобелевский лауреат Пол Кругман (Paul Krugman), говоря об экономических моделях и законе Ципфа, сформулировал это так:
>
> «На экономические теории обычно жалуются, что наши модели излишне упрощены и их отражение сложной беспорядочной реальности слишком приглаженное. [Относительно закона Ципфа] верно обратное: модели сложны и беспорядочны, а реальность поразительно ясна и проста».
>
> — [Лейн], §3.5, с. 165

*Проверка на Брауновском корпусе:*

> ```python
> >>> from collections import Counter
> >>> puncs = set((',', '.', '--', '-', '!', '?',
> ...     ':', ';', '``', "''", '(', ')', '[', ']'))
> >>> word_list = (x.lower() for x in brown.words() if x not in puncs)
> >>> token_counts = Counter(word_list)
> >>> token_counts.most_common(10)
> [('the', 69971),
>  ('of', 36412),
>  ('and', 28853),
>  ('to', 26158),
>  ('a', 23195),
>  ('in', 21337),
>  ('that', 10594),
>  ('is', 10109),
>  ('was', 9815),
>  ('he', 9548)]
> ```
>
> Сразу заметно, что частоты слов в Brown Corpus соответствуют логарифмическим отношениям, предсказанным Ципфом. Слово the (на первом месте по частоте термина) встречается примерно в два раза чаще, чем of (на втором месте), и примерно в три раза чаще, чем and (на третьем месте).
>
> — [Лейн], §3.5, с. 166–167

*Упражнение 23 из NLTK Book предлагает проверить закон самостоятельно:*

> a. Write a function to process a large text and plot word frequency against word rank using pylab.plot. Do you confirm Zipf's law? (Hint: it helps to use a logarithmic scale.) What is going on at the extreme ends of the plotted line?
>
> b. Generate random text, e.g., using random.choice("abcdefg "), taking care to include the space character. You will need to import random first. Use the string concatenation operator to accumulate characters into a (very) long string. Then tokenize this string, generate the Zipf plot as before, and compare the two plots. What do you make of Zipf's Law in the light of this?
>
> — [NLTK Book], гл. 2, упр. 23, с. 76

«а. Напишите функцию, которая обрабатывает большой текст и строит график зависимости
частоты слова от его ранга с помощью `pylab.plot`. Подтверждается ли закон Ципфа?
(Подсказка: помогает логарифмическая шкала.) Что происходит на концах графика?
б. Сгенерируйте случайный текст, например с помощью `random.choice("abcdefg ")`,
не забыв включить пробел. Сначала нужно импортировать `random`. Накапливайте символы
в (очень) длинную строку операцией конкатенации. Затем токенизируйте эту строку,
постройте график Ципфа, как раньше, и сравните два графика. Что вы думаете о законе
Ципфа в свете этого?»

*Решение пункта (а), код составителя:*

```python
import matplotlib.pyplot as plt
from nltk import FreqDist
from nltk.corpus import gutenberg

words = [w.lower() for w in gutenberg.words("melville-moby_dick.txt") if w.isalpha()]
freqs = [f for _, f in FreqDist(words).most_common()]
ranks = range(1, len(freqs) + 1)

plt.loglog(ranks, freqs)
plt.xlabel("ранг")
plt.ylabel("частота")
plt.title("Закон Ципфа: Moby Dick")
plt.show()

for r in [1, 10, 100, 1000]:
    print(r, freqs[r - 1], r * freqs[r - 1])   # f × r
```

Заготовка для пункта (б):

```python
import random
random_text = "".join(random.choice("abcdefg ") for _ in range(1_000_000))
random_words = random_text.split()
```

---

## Итоги

> - A word "token" is a particular appearance of a given word in a text; a word "type" is the unique form of the word as a particular sequence of letters. We count word tokens using `len(text)` and word types using `len(set(text))`.
> - We obtain the vocabulary of a text `t` using `sorted(set(t))`.
> - To derive the vocabulary, collapsing case distinctions and ignoring punctuation, we can write `set([w.lower() for w in text if w.isalpha()])`.
> - A frequency distribution is a collection of items along with their frequency counts (e.g., the words of a text and their frequency of appearance).
>
> — [NLTK Book], §1.6 Summary, с. 33

«Словесный „токен“ — конкретное появление слова в тексте; словесный „тип“ —
уникальная форма слова как определённая последовательность букв. Токены считаем через
`len(text)`, типы — через `len(set(text))`. Словарь текста `t` получаем через
`sorted(set(t))`. Чтобы получить словарь без различия регистра и без пунктуации,
пишем `set([w.lower() for w in text if w.isalpha()])`. Частотное распределение —
это набор элементов с их частотами (например, слова текста и частота их появления)».

> NLTK's corpus readers support efficient access to a variety of corpora, and can be used to work with new corpora.
>
> — [NLTK Book], §2.1, с. 49

«Корпусные ридеры NLTK обеспечивают эффективный доступ к разнообразным корпусам
и годятся для работы с новыми корпусами».

> This was our first brush with the reality of the Web: texts found on the Web may contain unwanted material, and there may not be an automatic way to remove it.
>
> — [NLTK Book], §3.1, с. 81

«Это наше первое столкновение с реальностью веба: найденные в нём тексты могут
содержать лишний материал, и автоматического способа удалить его может не быть».

---

