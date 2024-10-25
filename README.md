https://github.com/DrTECHNIC/Shell_Emulator/
# **Задание №1**
Разработать эмулятор для языка оболочки ОС. Необходимо сделать работу эмулятора как можно более похожей на сеанс shell в UNIX-подобной ОС. Эмулятор должен запускаться из реальной командной строки, а файл с виртуальной файловой системой не нужно распаковывать у пользователя. Эмулятор принимает образ виртуальной файловой системы в виде файла формата **tar**. Эмулятор должен работать в режиме **GUI**.

Конфигурационный файл имеет формат **json** и содержит:

• Имя пользователя для показа в приглашении к вводу.

• Путь к архиву виртуальной файловой системы.

Необходимо поддержать в эмуляторе команды ls, cd и exit, а также следующие команды:
1. touch.
2. cat.

Все функции эмулятора должны быть покрыты тестами, а для каждой из поддерживаемых команд необходимо написать 3 теста.

# Запуск
Перед запуском необходимо клонировать репозиторий в среду разработки

Обязательно прописать путь к файловой системе в config.json

Запуск main.py:
```Bash
py main.py config.json 
```
Запуск тестов
```Bash
pytest -v test.py
```
# Необходимые библиотеки и их установка
Библиотека для тестов
```Bash
pip install -U pytest
```
# Команды
``` ls ``` - Список файлов и директорий

``` cd <path> ``` - Смена директории

``` exit ``` - Выход из эмулятора

``` touch <name> ``` - Создание файла

``` cat <path> ``` - Вывод содержимого файла
# Тесты
## ls
![](https://github.com/DrTECHNIC/Shell_Emulator/blob/main/ls.png)
## cd
![](https://github.com/DrTECHNIC/Shell_Emulator/blob/main/cd.png)
## exit
![](https://github.com/DrTECHNIC/Shell_Emulator/blob/main/exit.gif)
## touch
![](https://github.com/DrTECHNIC/Shell_Emulator/blob/main/tou%D1%81%D1%80.png)
## cat
![](https://github.com/DrTECHNIC/Shell_Emulator/blob/main/cat.png)
## Общие тесты через pytest
![](https://github.com/DrTECHNIC/Shell_Emulator/blob/main/pytest.png)
