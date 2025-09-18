# FastAPI Backend Practice

## What is this?
A learning repository to practice backend development with **FastAPI**.  
Covers REST APIs, status codes, routing, Pydantic models, authentication, middleware, documentation, and more.

---

## Quickstart

### 1️⃣ Create & activate virtual environment
```bash
python -m venv venv

# Mac/Linux
source venv/bin/activate

# Windows
venv\Scripts\activate
````

### 2️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Run the app
```bash
uvicorn app.main:app --reload
```

## API Documentation
- **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## Endpoints
> This section will grow as features are added.

### Endpoints List

### SAMPLE
- `GET /` → Welcome message
- `GET /sample/` → Sample JSON response

### DAY 1 ENDPOINTS
- `POST /day1/items` → Create a new item

- `GET /day1/items` → Get all items

- `GET /day1/items/{item_id}` → Get item by ID

- `PUT /day1/items/{item_id}` → Update item by ID

- `DELETE /day1/items/{item_id}` → Delete item by ID

### DAY 2 ENDPOINTS
- `POST /day2/token` → Generate JWT access token using username & password

- `GET /day2/secure-data` → Access secure data (requires valid Bearer token in header)

### DAY 3 ENDPOINTS
- `GET /custom_exception/custom/{name}` → Returns the name, but raises CustomException if name is "bad"

- `GET /middleware/` → Simple home endpoint returning a welcome message

- `GET /middleware/slow` → Simulates a slow request (waits 2 seconds before responding)

### DAY 4 ENDPOINTS
- `POST /notes/create_note` → Creates a Note

- `GET /notes/` → Returns Notes List

- `GET /notes/{note_id}` → Returns Note by ID

### DAY 5 ENDPOINTS
- `POST /items-management/item` → Creates an Item

- `GET /items-management/items` → Returns Items List

- `GET /items-management/{item_id}` → Returns an Item by ID

- `DELETE /items-management/{item_id}` → Deletes an Item by ID


### DAY 6 ENDPOINTS
- `POST /auth-example/login` → Login endpoint

- `GET /auth-example/protected` → Checks the authenticity of the user


### TASK MANAGER ENDPOINTS
- `POST /taskmanager/token` → Login endpoint

- `POST /taskmanager/tasks` → Creates task only for admin role

- `GET /taskmanager/tasks` → Returns all the tasks

- `PUT /taskmanager/tasks/{task_id}` → Update the particular task only by admin

- `DELETE /taskmanager/tasks/{task_id}` → Deletes the particular task only by admin



## Documentation
- [HTTP Status Codes Notes](docs/status_codes.md)
- [Postman Collection](docs/postman_collection.json)

---

## Tech Stack
- Python 3.x
- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/)

---

# 🧪 Testing Endpoints

You can test the APIs using **cURL** in your terminal after starting the server.

## 1️⃣ Start the app
```bash
uvicorn app.main:app --reload
```

## 2️⃣ Open a new terminal tab/window and run
```bash
# Check root endpoint
curl http://127.0.0.1:8000/

# Check sample endpoint
curl http://127.0.0.1:8000/sample/

```

## Windows PowerShell users:
```bash
curl.exe http://127.0.0.1:8000/

```




## Progress Log
This repository will be updated regularly with new backend concepts and features.  
The `docs/` folder contains selected public documentation related to APIs created here.

