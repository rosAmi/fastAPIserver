Fast Api Server

Installation: 
# pip install "fastapi[all]"
# or
# pip install fastapi  + # pip install "uvicorn[standard]"
# or
# pip install fastapi + # pip install uvicorn

Run:
run server: $ uvicorn main:app --reload

open localhost:
url: http://127.0.0.1:8000
# JSON (schema): http://127.0.0.1:8000/openapi.json
# Option 1 API docs 'swagger': http://127.0.0.1:8000/docs
# Option 2 API docs 'redoc': http://127.0.0.1:8000/redoc