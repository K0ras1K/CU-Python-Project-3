# Сервис прогноза погоды

Это сервис прогноза погоды, состоящий из веб-приложения и Telegram-бота. Он позволяет пользователям:
1. Получать прогнозы погоды для определённых городов, маршрутов и интервалов.
2. Использовать веб-интерфейс для визуализации погодных данных с помощью интерактивных графиков.
3. Обращаться к боту для быстрого доступа к прогнозам по командам и кнопкам.

## Компоненты

- **Веб-сервер**: Сервис на базе Flask и Dash, который отображает прогнозы погоды с помощью графиков Plotly.
- **Telegram-бот**: Бот, созданный на базе aiogram (версия 3), который обрабатывает команды и предоставляет информацию о погоде.

### Используемые технологии

- **Flask** и **Dash** для веб-сервера и визуализации данных.
- **Plotly** для создания графиков.
- **aiogram** для работы с Telegram API.
- **dotenv** для загрузки переменных окружения.

## Предварительные требования

1. **Python версии 3.10 или выше** рекомендуется для стабильной работы.
2. **Зависимости**: Установите необходимые библиотеки с помощью команд, приведённых ниже.

## Установка

1. **Склонируйте репозиторий**:
   ```bash
   git clone <repository_url>
   cd <repository_folder>
   ```

2. **Создайте виртуальное окружение**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Для Windows используйте `venv\Scripts\activate`
   ```

3. **Установите зависимости по отдельности**:

   - **aiogram** — библиотека для работы с Telegram API:
     ```bash
     pip install aiogram
     ```

   - **Flask** — фреймворк для веб-сервера:
     ```bash
     pip install flask
     ```

   - **python-dotenv** — модуль для работы с переменными окружения из файла `.env`:
     ```bash
     pip install python-dotenv
     ```

   - **requests** — для выполнения HTTP-запросов к внешним API:
     ```bash
     pip install requests
     ```

   - **Plotly** — библиотека для построения графиков:
     ```bash
     pip install plotly
     ```

   - **Dash** и **Dash Bootstrap Components** — фреймворк для построения веб-приложений и компонентов интерфейса:
     ```bash
     pip install dash dash-bootstrap-components
     ```

4. **Создайте файл `.env`** в корневой директории проекта и добавьте следующие переменные:

   ```plaintext
   ACCUWEATHER_TOKEN=your_accuweather_api_token
   YANDEX_GEOCODE_TOKEN=your_yandex_geocode_token
   YANDEX_WEATHER_TOKEN=your_yandex_weather_token
   WEATHER_API_TOKEN=your_weatherapi_token
   TELEGRAM_BOT_TOKEN=your_telegram_bot_token
   FRONT_DASHBOARD_URL=https://your_dashboard_url
   ```

### Описание переменных окружения:

- `ACCUWEATHER_TOKEN`: Токен для AccuWeather API, предоставляющий прогнозы погоды.
- `YANDEX_GEOCODE_TOKEN`: Токен для Yandex Geocoding API, который получает координаты по названию города.
- `YANDEX_WEATHER_TOKEN`: Токен для Yandex Weather API для получения данных о погоде.
- `WEATHER_API_TOKEN`: Токен для WeatherAPI, используемый для альтернативных данных о погоде.
- `TELEGRAM_BOT_TOKEN`: Токен для вашего Telegram-бота, который можно получить через [BotFather](https://core.telegram.org/bots#botfather).
- `FRONT_DASHBOARD_URL`: URL-адрес для отображения графиков в боте. Обычно размещается на вашем сервере или облачной платформе.

## Запуск проекта

**Убедитесь, что файл `.env` находится в корневой директории и содержит все необходимые API-ключи.**

1. **Запустите веб-сервер**:
   ```bash
   python app.py
   ```

   - Веб-сервер на основе Flask и Dash начнёт работать, и его можно будет открыть по адресу `http://localhost:5000`.

2. **Запустите Telegram-бота**:
   ```bash
   python bot.py
   ```

   - Бот будет обрабатывать команды и предоставлять прогнозы погоды для заданных пользователем маршрутов.

### Использование

- **Telegram-бот**: 
  - Отправьте команду `/start` для приветствия и инструкции.
  - Используйте команду `Weather <город_начала> : <город_конца>` для получения прогноза для маршрута. Выберите прогноз на день, 7 или 10 дней через интерактивные кнопки.
  
- **Веб-интерфейс**:
  - Просматривайте почасовые, дневные и недельные прогнозы и визуализируйте данные о температуре, осадках и скорости ветра для выбранных локаций.

### Деплой

Сейчас приложение задеплоено.
**Тестовый бот:** `@loliland_support_test_test_bot`
**Тестовый сайт:** `https://weather.k0ras1k.online`

**WARNING**: На проде может кончится токен accuweather. Если сломается генерация, app.py нужно поднять локально с вашими токенами!