# Python, VS Code и Jupyter на локальной машине

**Инструкции даны для **Windows** и **macOS**, отдельно отмечены варианты
**без прав администратора**.

После каждого шага есть проверка. Не переходить к следующему шагу, пока проверка не прошла.

## Состав среды

| Компонент | Назначение |
|---|---|
| **Python** | интерпретатор языка |
| **VS Code** | редактор кода и ноутбуков |
| **Расширения Python + Jupyter** | запуск кода и `.ipynb` в редакторе |
| **venv** | изолированное окружение с библиотеками курса |
| **Git** | `02_Git_и_GitHub.md` |
| **GigaCode** | `03_GigaCode_CLI.md`, `04_GigaCode_плагин_в_IDE.md` |

## Шаг 1. Терминал

**Windows:** `Win` → `PowerShell` → **Windows PowerShell**.
**macOS:** `Cmd + Пробел` → `Терминал`.

*Проверка:* команда `echo Привет` печатает `Привет`.

## Шаг 2. Python

### Windows

1. **https://www.python.org/downloads/** → **Download Python 3.x** (нужна версия ≥ 3.10).
2. Запустить установщик.
3. **В первом окне отметить «Add python.exe to PATH».** Без этой галочки команда `python`
   не будет работать; если пропущена — переустановить.
4. **Install Now**.


*Без прав администратора:* **Customize installation → Install for all users: снять галочку**.
Либо установить Python из Microsoft Store.

### macOS

Установщик с **https://www.python.org/downloads/**, настройки по умолчанию.
Системный Python macOS не трогать.

### Проверка

Закрыть терминал и открыть заново, затем:

```
python --version     # Windows
python3 --version    # macOS
```

Ожидается `Python 3.1x.x`.

| Ошибка | Причина |
|---|---|
| `python не является внутренней или внешней командой` | не отмечена галочка PATH → переустановить |
| `command not found: python3` | установщик не отработал → установить заново |
| печатается `Python 2.7.x` | использовать `python3` |

Далее в тексте: где написано `python` и `pip`, в macOS набирать `python3` и `pip3`.

## Шаг 3. VS Code

1. **https://code.visualstudio.com/** → **Download**.
2. Установить.
   - Windows: отметить «Добавить действие Открыть с помощью Code…».
   - macOS: перетащить `Visual Studio Code` в `Программы`.

*Без прав администратора (Windows):* вариант **User Installer**.

*Проверка:* VS Code запускается.

## Шаг 4. Расширения

1. Панель **Extensions** (`Ctrl/Cmd + Shift + X`).
2. Установить **Python** (Microsoft) и **Jupyter** (Microsoft).
3. Опционально: **Russian Language Pack**.


*Проверка:* `Ctrl/Cmd + Shift + P` → команда `Jupyter: Create New Blank Notebook` есть в списке.

## Шаг 5. Папка проекта и виртуальное окружение

**venv** — каталог с копией интерпретатора и библиотеками одного проекта. Изолирует версии
библиотек разных проектов друг от друга.

1. Создать папку `mglu-python`. **Без пробелов и кириллицы в пути.**
2. VS Code: `Файл → Открыть папку`.
3. `Терминал → Новый терминал` (`` Ctrl + ` ``).
4. Создать и активировать окружение:

```
python -m venv .venv          # Windows
.venv\Scripts\activate

python3 -m venv .venv         # macOS
source .venv/bin/activate
```

В начале строки терминала появляется `(.venv)`.

> Windows, `выполнение сценариев отключено в этой системе`:
> `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned`, подтвердить `Y`,
> повторить активацию.

5. Установить библиотеки:

```
pip install --upgrade pip
pip install jupyter ipykernel nltk
```

*Проверка:*
```
python -c "import nltk; print(nltk.__version__)"
```

`(.venv)` действует до закрытия терминала; при новом запуске команду активации повторить.
VS Code активирует окружение сам, если выбран интерпретатор (шаг 6).

## Шаг 6. Выбрать интерпретатор в VS Code

`Ctrl/Cmd + Shift + P` → `Python: Select Interpreter` → путь, содержащий `.venv`.

*Проверка:* файл `check.py` со строкой `print(2 + 2)`, запуск кнопкой ▶ → в терминале `4`.

## Шаг 7. Ноутбук локально

1. Скопировать `notebooks/` и `data/` внутрь `mglu-python`.
2. Открыть `.ipynb` двойным щелчком.
3. Вверху справа: **Select Kernel → Python Environments → .venv**.
4. Выполнить первую ячейку.

Классический интерфейс Jupyter в браузере: команда `jupyter notebook`, остановка — `Ctrl + C`.

## Структура проекта

```
mglu-python/
├── .venv/                   ← окружение: не редактировать, не копировать, не коммитить
├── notebooks/
│   └── 01_Первые_шаги.ipynb
├── data/
│   └── text_clean.txt
└── check.py
```

## Чек-лист

- [ ] `python --version` / `python3 --version` печатает 3.10+
- [ ] расширения Python и Jupyter установлены
- [ ] в терминале VS Code видно `(.venv)`
- [ ] `python -c "import nltk"` выполняется без ошибок
- [ ] `.ipynb` открывается, ячейка выполняется
- [ ] Git установлен (`02_Git_и_GitHub.md`)

