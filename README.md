# WeatherApp
## Описание
WeatherApp - сайт, на котором пользователь может получить прогноз погоды города.
Сервис предоставляет координаты указанного места, температуру и погоду за 24ч.

(написаны тесты, всё помещено в докер контейнер, при повторном посещении сайта будет предложено посмотреть погоду в городе, в котором пользователь уже смотрел ранее, сохраняться история поиска для каждого пользователя)

(Планируется написать api показывающее сколько раз вводили какой город)
## Технологии:
* Python
* Django
* Docker
* HTML
* CSS

## Запуcк из Docker 
### Клонирование
Клонируйте репозиторий
```
git@github.com:V0yager01/WeatherApp_Django.git
```
### Запуск Docker compose 
В директории запускаем docker-compose.yml
```
docker compose up  -d
```
### Подготовка Django
Выполняeм миграцию
```
docker compose exec weatherapp python manage.py migrate
```
### Проверка работоспособности 
```
docker compose exec weatherapp python manage.py test
```

## Обычный запуск
### Клонирование
Клонируйте репозиторий
```
git@github.com:V0yager01/WeatherApp_Django.git
```
### Подготовка виртуального окружения
Создаем и включаем окружение для проекта
```
python -m venv venv
source venv/Scripts/activate
```
### Установка зависимостей
```
cd weatherStatus/
pip install -r requirements.txt
```
### Подготовка Django
Выполням миграцию
```
python manage.py migrate
```
### Запуск
```
python manage.py runserver
```

## Автор
Халиуллин Ильяс
