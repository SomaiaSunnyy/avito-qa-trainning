# avito-qa-trainning

Привет! 👋  

Меня зовут Зангенех Сомаиех и в эту репу я положила тестовое задание для отбора на стражировку в Авито на позицию QA-инженера.  

Второе задание выбрала в варианте 2.2, где нужно покрыть тестами сайт с объявлениями, так как я совсем не знаком с автотестами, покрывающими api и немного знаком с ui автотестами.  

Ссылка на задание: [winter-2025](https://github.com/avito-tech/tech-internship/blob/main/Tech%20Internships/QA/QA-trainee-assignment-winter-2025/QA-trainee-assignment-winter-2025.md)

---

# Структура проекта:

Файлы для задания 1:
- [task_1](./TASK_1.md) - решение задания  
- [images_task_1](./images_task_1) - директория со скринами к заданию  

Файлы для задания 2:
- [TESTCASES.md](./TESTCASES.md) - список тест-кейсов для проверки пользовательских сценариев  
- [BUGS.md](./BUGS.md) - список с найденными во время выполнения задания багами  
- [images_task_2](./images_task_2) - директория со скринами к файлу BUGS.md
- [Пункт с инструкцией для запуска тестов](#инструкция-по-запуску-тестов-ко-второму-заданию). Модули, которые относятся к запуску автотестов:  
  - [base_page.py](./base_page.py) - класс описывающий "базовую" страницу с основными методами
  - [ad_page.py](./ad_page.py) - класс, описывающий страницу объявления
  - [catalog_page.py](./catalog_page.py) - класс, описывающий страницу каталога
  - [test_1.py](./test_1.py) - тест-кейс проверки создания объявления
  - [test_2.py](./test_2.py) - тест-кейс проверки редактирования объявления
  - [test_3.py](./test_3.py) - тест-кейс проверки поиска по каталогу


# Задание 1

В данном задании нужно проанализировать скриншот страницы Авито с результатами поиска и:
1. перечислить все имеющиеся баги
2. указать их приоритет (high, medium, low)


# Задание 2

Нужно протестировать сайт с доской объявлений http://tech-avito-intern.jumpingcrab.com/ по пунктам, указанным ниже.

**Требования к выполнению:**

1. Составить тест-кейсы на пользовательские сценарии и оформить их в [TESTCASES.md](./TESTCASES.md)
   1. Создание объявления  
   2. Редактирование объявления  
   3. Поиск объявлений  
2. Автоматизировать тест кейсы (в  тест-кейсах нужно проверять результат)  
3. Запустить автоматизированные тесты:  
   1. Все тесты должны быть пройдены   
4. Написать понятную и воспроизводимую инструкцию, оформить её в файле с названием [README.md](#инструкция-по-запуску-тестов-ко-второму-заданию)  
5. Если в результате тестирования найдены баги, то составить баг-репорт в файле с названием [BUGS.md](./BUGS.md)

---

## Инструкция по запуску тестов ко второму заданию

1. Склонировать репозиторий с выполненными заданиями:
   ```
   git clone https://gitverse.ru/SAndSmirnov/avito-qa-trainee-assigment.git
   ```
      1. Можно скачать альтернативным способом отсюда: https://gitverse.ru/SAndSmirnov/avito-qa-trainee-assigment  

2. Проверить, что на ПК есть python:
   ```
   python -V
   ```
   1. Если после ввода команды появлась ошибка, вместо версии, то нужно установить его с офф сайта: https://www.python.org/downloads/  

3. На ПК должен быть Google Chrome. Если нет, то установить с https://www.google.com/intl/ru_ru/chrome/  

4. Чтобы не захламлять глобальное окружение, можно создать виртуальное для текущего проекта, **либо пропустить этот шаг**.  
   
   1. Для создания окружения понадобится venv, который является стандартной библиотекой для Win/MacOS систем, а вот на Linux ее может не быть. Если вдруг так произошло, то (на Ubuntu/Debian) ее можно установить следующей командой:  
      ```
      sudo apt install -y python3-venv
      ```

   2. Создать окружение:
      ```
      python -m venv .venv
      ```

   3. Перейти в виртуальное окружение:
      Для Windows: 
      ```
      venv\Scripts\activate.bat
      ```
      Для Linux / MacOS:
      ```
      source .venv/bin/activate
      ```
5. Теперь нужно установить зависимости, указанные в файле requirements.txt:  
   ```
   pip install -r requirements.txt
   ```
6. Все готово! Можно запускать тесты:
   ```
   pytest -v
   ```
   1. Если нужно прогнать их по отдельности, то:
      `pytest <Название файла с тестами>`
      Напр.: `pytest test_1.py`




