import requests  # Импорт библиотеки requests, которая позволяет выполнять HTTP-запросы.

# URL для API GitHub, который используется для поиска репозиториев.
search_url = "https://api.github.com/search/repositories"
# Параметры запроса, мы ищем репозитории по ключевому слову "html".
params = {
    "q": "html",
}

# Выполнение GET-запроса к API с указанным URL и параметрами.
response = requests.get(search_url, params=params)
# Вывод статуса ответа (200 означает успешный запрос).
print("Статус код:", response.status_code)

# Проверяем, что статус код равен 200 (успешный запрос).
if response.status_code == 200:
    # Преобразуем ответ в формат JSON и сохраняем в переменной data.
    data = response.json()
    # Вывод полученного ответа в формате JSON.
    print("Ответ в формате JSON:", data)
else:
    # Если произошла ошибка, выводим текст ошибки.
    print("Ошибка при получении данных:", response.text)

# Указываем userId, для которого нам нужны посты.
userId = 1
# URL для API JSONPlaceholder, который возвращает посты.
posts_url = "https://jsonplaceholder.typicode.com/posts"
# Параметры для запроса - выбираем посты, созданные пользователем с userId = 1.
user_id_param = {
    "userId": 1
}

# Выполняем GET-запрос к API для получения постов пользователя с заданным userId.
response = requests.get(posts_url, params=user_id_param)

# Проверяем статус код на успешность.
if response.status_code == 200:
    # Преобразуем ответ в формат JSON и сохраняем в переменной posts.
    posts = response.json()
    # Выводим найденные посты.
    print("Записи:", posts)
else:
    # Если произошла ошибка, выводим текст ошибки.
    print("Ошибка при получении данных:", response.text)

# URL для API JSONPlaceholder, куда мы будем отправлять новый пост.
post_url = "https://jsonplaceholder.typicode.com/posts"
# Данные, которые мы хотим отправить. Создаем новый пост.
data_to_send = {
    'title': 'foo',  # Заголовок поста.
    'body': 'bar',   # Содержимое поста.
    'userId': 1      # ID пользователя, к которому относится пост.
}

# Выполняем POST-запрос для создания нового поста, отправляя данные в формате JSON.
response = requests.post(post_url, json=data_to_send)
# Выводим статус код ответа на POST-запрос.
print("Статус код POST-запроса:", response.status_code)

# Проверяем, что статус код равен 201 (успешно создано).
if response.status_code == 201:
    # Если пост успешно создан, выводим созданные данные в формате JSON.
    print("Созданные данные:", response.json())
else:
    # Если произошла ошибка, выводим текст ошибки.
    print("Ошибка при отправке данных:", response.text)