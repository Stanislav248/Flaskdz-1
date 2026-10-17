# Візитка

Міні-сайт «Візитка» на Flask.

## Маршрути

| URL | Опис |
|-----|------|
| `/` | Головна сторінка зі списком проєктів |
| `/about` | Про мене |
| `/skills` | Навички |
| `/project/<id>` | Один із проєктів; для неіснуючого id — «Проєкт не знайдено» (404) |
| `/api/me` | Мої дані у форматі JSON |

## Запуск

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux / macOS:
source .venv/bin/activate

pip install -r requirements.txt
python app.py
```

Сайт буде доступний на http://127.0.0.1:5000

Свої дані (ім'я, вік, місто, навички) та список проєктів змінюються на початку файлу `app.py`.
