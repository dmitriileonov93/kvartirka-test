# Тестовое задание для Kvartirka

### Задание:
Реализовать REST API для системы комментариев блога.

Функциональные требования: 
У системы должны быть методы API, которые обеспечивают 
- Добавление статьи (Можно чисто номинально, как сущность, к которой крепятся комментарии). 
- Добавление комментария к статье. 
- Добавление коментария в ответ на другой комментарий (возможна любая вложенность). 
- Получение всех комментариев к статье вплоть до 3 уровня вложенности. 
- Получение всех вложенных комментариев для комментария 3 уровня. 
- По ответу API комментариев можно воссоздать древовидную структуру.

Нефункциональные требования: 
- Использование Django ORM. 
- Следование принципам REST. 
- Число запросов к базе данных не должно напрямую зависеть от количества комментариев, уровня вложенности. 
- Решение в виде репозитория на Github, Gitlab или Bitbucket. 
- readme, в котором указано, как собирать и запускать проект. Зависимости указать в requirements.txt либо использовать poetry/pipenv. 
- Использование свежих версий python и Django.

Будет плюсом: 
- Использование PostgreSQL. 
- docker-compose для запуска api и базы данных. 
- Swagger либо иная документация к апи.

### Описание:
Проект реализован в трёх docker контейнерах:
- db (PostgreSQL)
- nginx
- web (DRF, Gunicorn)
    Древовидные комментарии реализованы с помощью пакета Django MPTT.
    Количество запросов к БД не зависит от количества комментариев и их вложенности.

Документация API доступна после запуска пректа по эндпоинту '/api/docs/'

### Запуск проекта:
- Для загрузки введите в командную строку:
```
git clone https://github.com/dmitriileonov93/kvartirka-test.git
```
- Перейти в корневую папку проекта:
```
cd kvartirka-test/
```
- Создайте файл .env для переменных окружения:
```
touch kvartirka-test/kvartirka-test/.env
```
- Добайте в этот файл переменные окружения:
```
echo <ПЕРЕМЕННАЯ>=<значение> >> kvartirka-test/kvartirka-test/.env
```
- Запуск приложения из корневой папки проекта:
```
docker-compose up -d
```
После запуска проект уже имеет фикстуры в БД и суперпользователя для простоты тестирования.



