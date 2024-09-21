# python-web-backend
### This is a repo for homeworks on web backend course [ref] (https://github.com/katunilya/hse-python-backend).
## To Run:
1. git clone https://github.com/Levliv/python-web-backend.git
2. pip install -r requirements.txt
3. uvicorn myapp:app

### Table of content:
#### 1. Лекция 1 - Основы сети и Python Backend
Реализовать "Математическое API" из примера напрямую через ASGI-compatible функцию. В частности

запросы, для которых нет обработчиков (не тот метод, не тот путь) должны возвращать ошибку 404 Not Found
запрос GET /factorial (n!)
возвращается в тело запроса в формате json вида {"result": 123}
в query-параметре запроса должен быть параметр n: int
если параметра нет, или он не является числом - возвращаем 422 Unprocessable Entity
если параметр не валидное число (меньше 0) - возвращаем 400 Bad Request
запрос GET /fibonacci (n-ое число fibonacci)
возвращается в тело запроса в формате json вида {"result": 123}
в path-параметре запроса (fibonacci/{n}) должен быть параметр n: int
если параметра нет, или он не является числом - возвращаем 422 Unprocessable Entity
если параметр не валидное число (меньше 0) - возвращаем 400 Bad Request
запрос GET /mean (среднее массива)
возвращается в тело запроса в формате json вида {"result": 123}
в теле запроса не пустой массив из float'ов (например [1, 2.3, 3.6])
тело не является массивом float'ов - возвращаем 422 Unprocessable Entity
если массив пустой - возвращаем 400 Bad Request
