# API социальной сети Yatube (RU)

Описание проекта
---
Проект представляет собой API для платформы Yatube. В нем реализованы ключевые функции: создание, редактирование и удаление постов, групп и комментариев, а также аутентификация пользователей с помощью токенов. Аутентифицированный пользователь авторизован на изменение и удаление своего контента, в остальных случаях доступ предоставляется только для чтения. При попытке изменить чужие данные должен возвращаться код ответа 403 Forbidden.

Основные задачи
---
✔️ Реализация API для моделей постов, групп и комментариев  
✔️ Настройка аутентификации по токенам  
✔️ Обработка запросов для создания, обновления и удаления контента

Эндпоинты для взаимодействия:
---
- `api/v1/api-token-auth/` (POST): передаём логин и пароль, получаем токен.   
- `api/v1/posts/` (GET, POST): получаем список всех постов или создаём новый пост.   
- `api/v1/posts/{post_id}/` (GET, PUT, PATCH, DELETE): получаем, редактируем или удаляем пост с идентификатором `post_id`.   
- `api/v1/groups/` (GET): получаем список всех групп.   
- `api/v1/groups/{group_id}/` (GET): получаем информацию о группе с идентификатором `group_id`.  
- `api/v1/posts/{post_id}/comments/`  
(GET): получаем список всех комментариев поста с идентификатором `post_id`.  
(POST): создаём новый комментарий для поста с идентификатором `post_id`.  
- `api/v1/posts/{post_id}/comments/{comment_id}/` (GET, PUT, PATCH, DELETE): получаем, редактируем или удаляем комментарий с идентификатором `comment_id` в посте с `id=post_id`.

Стек технологий
---
- Python 3.9
- Django REST Framework 3.12
- Django 3.2

Установка проекта из репозитория (Windows)
---
1. Клонировать репозиторий:
```bash
git clone git@github.com:JarexTI/api_yatube.git
```
2. Перейти в папку проекта:
```bash
cd api_yatube
```
3. Создать и активировать виртуальное окружение:
```bash
python -m venv venv

source venv/Scripts/activate
```
4. Установить зависимости из файла `requirements.txt`:
```bash
python -m pip install --upgrade pip

pip install -r requirements.txt
```
5. Выполнить миграции:
```bash
python yatube_api/manage.py migrate
```
6. Запустить проект:
```bash
python yatube_api/manage.py runserver
```
<br>

# Yatube Social Network API (EN)

Project Description
---
The project is an API for the Yatube platform. It implements key features such as creating, editing, and deleting posts, groups, and comments, as well as user authentication using tokens. An authenticated user is authorized to modify and delete their own content, while in other cases, access is granted only for reading. If an attempt is made to modify someone else's data, a 403 Forbidden response code should be returned.

Main Tasks
---
✔️ Implementing the API for post, group, and comment models  
✔️ Setting up token-based authentication  
✔️ Handling requests for creating, updating, and deleting content

Endpoints for interaction:
---
- `api/v1/api-token-auth/` (POST): send login and password to receive a token.  
- `api/v1/posts/` (GET, POST): get a list of all posts or create a new post.  
- `api/v1/posts/{post_id}/` (GET, PUT, PATCH, DELETE): get, edit, or delete the post with the identifier `post_id`.  
- `api/v1/groups/` (GET): get a list of all groups.  
- `api/v1/groups/{group_id}/` (GET): get information about the group with the identifier `group_id`.  
- `api/v1/posts/{post_id}/comments/`  
  (GET): get a list of all comments for the post with the identifier `post_id`.  
  (POST): create a new comment for the post with the identifier `post_id`.  
- `api/v1/posts/{post_id}/comments/{comment_id}/` (GET, PUT, PATCH, DELETE): get, edit, or delete the comment with the identifier `comment_id` in the post with `id=post_id`.

Technology Stack
---
- Python 3.9
- Django REST Framework 3.12
- Django 3.2

## Project Installation from Repository (Windows)

1. Clone the repository:

```bash
git clone git@github.com:JarexTI/api_yatube.git
```

2. Navigate to the project folder:

```bash
cd api_yatube
```

3. Create and activate a virtual environment:

```bash
python -m venv venv

source venv/Scripts/activate
```

4. Install dependencies from `requirements.txt`:

```bash
python -m pip install --upgrade pip

pip install -r requirements.txt
```

5. Run migrations:

```bash
python yatube_api/manage.py migrate
```

6. Start the project:

```bash
python yatube_api/manage.py runserver
```
