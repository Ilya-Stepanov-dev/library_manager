# Library Manager
![Image](_resources/library_mamager.jpg)


## Содержание:
  - [Описание:](#описание)
  - [Требования:](#требования)
  - [Установка и запуск](#установка-и-запуск)
  - [Структура проекта](#структура-проекта)


## Описание:
Данное консольное приложение предназначено для управления библиотекой книг. Оно позволяет добавлять, удалять, искать и отображать книги. Каждая книга содержит уникальный идентификатор, название, автора, год издания и статус.


## Требования:
**Задание:** *Разработка системы управления библиотекой.*

**Описание:**
*Необходимо разработать консольное приложение для управления библиотекой книг. Приложение должно позволять добавлять, удалять, искать и отображать книги. Каждая книга должна содержать следующие поля:*
- id (уникальный идентификатор, генерируется автоматически)
- title (название книги)
- author (автор книги)
- year (год издания)
- status (статус книги: “в наличии”, “выдана”)
___
**Требования:**

 1. Добавление книги: Пользователь вводит title, author и year, после чего книга добавляется в библиотеку с уникальным id и статусом “в наличии”.
 2. Удаление книги: Пользователь вводит id книги, которую нужно удалить.
 3. Поиск книги: Пользователь может искать книги по title, author или year.
 4. Отображение всех книг: Приложение выводит список всех книг с их id, title, author, year и status.
 5. Изменение статуса книги: Пользователь вводит id книги и новый статус (“в наличии” или “выдана”).
___
**Дополнительные требования:**
- Реализовать хранение данных в текстовом или json формате.
- Обеспечить корректную обработку ошибок (например, попытка удалить несуществующую книгу).
- Написать функции для каждой операции (добавление, удаление, поиск, отображение, изменение статуса).
- Не использовать сторонние библиотеки.
___
**Критерии оценки:**
- Корректность и полнота реализации функционала.
- Чистота и читаемость кода.
- Обработка ошибок и исключений.
- Удобство использования интерфейса командной строки.
- Структура проекта.
___
**Будет плюсом:**
1. Аннотации: Аннотирование функций и переменных в коде.
2. Документация: Наличие документации к функциям и основным блокам кода.
3. Описание функционала: Подробное описание функционала приложения в README файле.
4. Тестирование.
5. Объектно-ориентированный подход программирования.
___

## Установка и запуск
### 1. Клонируйте репозиторий
   ```bash
   git clone https://github.com/Ilya-Stepanov-dev/library_menager.git
   ```

### 2. Запуск
   
1. Linux/Mac
   1. Сделать файл run.sh исполняемым
   ```bash
   chmod +x run_python.sh
   ```
   2. Запуск
   ```bash
   ./run.sh
   ```
2. Windows
   ```cmd
   run.bat
   ```
3. Попробовать запустить напрямую указав свой интерпретатор и пусть к файлу как к модулю
   Например:
   ```bash
   python3 -m app.main
   ```


## Структура проекта
```
├── app
│   ├── main.py
│   ├── library
│   │   ├── book.py
│   │   ├── library.py
│   ├── user_interfaces
│   │   ├── base.py
│   │   ├── cli.py
│   └── utils
│       ├── color_print.py
│       ├── data_helper.py
│       ├── enums.py
│       ├── exceptions.py
│       └── validator.py
└── tests
    ├── test_main.py
    └── test_validators
```

### Описание основных модулей

#### Library
Модуль в котором содержаться основная логика работы с данными.
   - **book** - класс содержащий атрибуты для Книг.
   - **library** - класс для работы с данными библиотеки (добавление, удаление, поиск, изменение статуса и отображение книг).

#### User_interfaces
Модуль пользовательских интерфейсов (Реализован только консольный интерфейс на основе машины состояний).

Основные методы интерфейса:
   - **on_enter** - выводит на экран меню или сообщения для пользователя.
   - **handle_input** - отслеживание входящих данных от пользователя и смена состояния.

#### Utils
Дополнительные вспомогательные модули:
   - **color_print** - модуль для цветного отображения текста.
   - **data_helper** - модуль для проверки и создания директории с базы данных (JSON файла), для хранения информации.
   - **exceptions** - модуль с кастомными ошибками, для отображения пользователю.
   - **validator** - модуль для проверки введенных пользователям данных.


#### Test
Модуль для тестирования(Реализовано тестирование для валидации).
