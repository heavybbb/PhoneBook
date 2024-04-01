
<h4 align="center">
  <a href="https://github.com/heavybbb/PhoneBook">
    <img src="https://github.com/heavybbb/PhoneBook/blob/PhoneBook/PhoneBook.jpeg">  </a>


<center><h1> Phone book</center>

### Введение
Phone book скрипт написанный на языке ``` Python ```.
Это "надежный" скрипт для хранения контактов, призванный совершить революцию в хранении номеров телефона.

### Возможности
Эта телефонная книга имеет графический интерфейс и сохраняет данные в базе SQL.
Позволяет хранить: имя, фамилию, телефонный номер и e-mail.
Ввод данных производится путем заполнением соответствующих полей или можно импортировать текстовый файл.
Скрипт позволяет не только добавлять данные, но и изменять, удалять и осуществлять поиск контактов.

### Установка и запуск
1. Клонирование репозитория 
```git clone https://github.com/heavybbb/PhoneBook.git ```
2. Установить библиотеки 
```pip3 install sqlite3``` и ```pip3 install easygui```.
3. Запуск производится выполнением команды 
```python PhoneBook.py```

### Структура файла импорта
В *.txt файле каждый контакт находится на отдельной строке и данные отделены запятой.
Пример одного контакта:

```Имя, Фамилия, телефонный номер, электронная почта```
### Пример использования
В одном каталоге со скриптом ```PhoneBook.py``` находится уже наполненная база ```PhoneBook.bd``` и пример текстового файла для импорта ```Contact.txt```