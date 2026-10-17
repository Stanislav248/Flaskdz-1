from flask import Flask, render_template, jsonify

app = Flask(__name__)
# Щоб кирилиця в /api/me відображалась читабельно, а не як \uXXXX
app.json.ensure_ascii = False

# Дані про себе — єдине джерело правди для всіх шаблонів і для /api/me
ME = {
    "name": "Ім'я Прізвище",
    "age": 20,
    "city": "Івано-Франківськ",
    "bio": "Студент, який вивчає веброзробку на Python і Flask.",
    "skills": ["Python", "Flask", "HTML", "CSS", "Git", "SQL"],
}

# Список проєктів: id -> дані проєкту
PROJECTS = [
    {
        "id": 1,
        "title": "Сайт-візитка",
        "description": "Міні-сайт на Flask з шаблонами Jinja2 та JSON API.",
        "tech": ["Python", "Flask", "Jinja2"],
    },
    {
        "id": 2,
        "title": "Список справ",
        "description": "Консольний застосунок для керування щоденними завданнями.",
        "tech": ["Python", "JSON"],
    },
    {
        "id": 3,
        "title": "Калькулятор витрат",
        "description": "Невеликий вебзастосунок для обліку особистих витрат.",
        "tech": ["Python", "Flask", "SQLite"],
    },
]


@app.route("/")
def index():
    return render_template("index.html", me=ME, projects=PROJECTS)


@app.route("/about")
def about():
    return render_template("about.html", me=ME)


@app.route("/skills")
def skills():
    return render_template("skills.html", me=ME)


@app.route("/project/<project_id>")
def project(project_id):
    # Приймаємо будь-який рядок, щоб і /project/abc давав «Проєкт не знайдено»
    found = next((p for p in PROJECTS if str(p["id"]) == project_id), None)
    if found is None:
        return "Проєкт не знайдено", 404
    return render_template("project.html", me=ME, project=found)


@app.route("/api/me")
def api_me():
    return jsonify(ME)


if __name__ == "__main__":
    app.run(debug=True)
