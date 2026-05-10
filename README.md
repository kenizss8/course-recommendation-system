# Course Recommendation System

He thong goi y khoa hoc phu hop voi nhu cau hoc vien.

Du an su dung:

- Frontend: React + Vite + Bootstrap + Axios
- Backend: FastAPI
- Database: MongoDB
- Recommendation logic: rule-based + TF-IDF + cosine similarity

## Main features

- Hien thi danh sach khoa hoc tu MongoDB
- CRUD khoa hoc qua FastAPI
- Goi y khoa hoc dua tren:
  - category mong muon
  - level mong muon
  - keywords/skills
  - mo ta nhu cau hoc tap
- Seed 18 khoa hoc mau de demo nhanh

## Project structure

```text
course-recommendation-system/
|-- backend/
|   |-- main.py
|   |-- database.py
|   |-- schemas.py
|   |-- sample_courses.py
|   |-- seed_courses.py
|   |-- requirements.txt
|   `-- .env.example
|-- frontend/
|   |-- src/
|   |-- public/
|   |-- package.json
|   `-- package-lock.json
|-- PROJECT_PLAN.md
|-- README.md
`-- .gitignore
```

## Backend setup

```powershell
cd backend
copy .env.example .env
cd ..
```

Cap nhat `.env` neu MongoDB cua ban dung URL hoac ten database khac.

## Run backend

```powershell
.\venv\Scripts\Activate.ps1
python -m uvicorn backend.main:app --reload
```

Backend chay mac dinh tai:

- `http://127.0.0.1:8000`
- Swagger docs: `http://127.0.0.1:8000/docs`

## Run frontend

```powershell
cd frontend
npm install
npm run dev
```

Frontend goi API backend tai `http://127.0.0.1:8000`.

## Seed sample courses

```powershell
.\venv\Scripts\Activate.ps1
python -m backend.seed_courses
```

Lenh nay them 18 khoa hoc mau vao MongoDB va cap nhat theo `title` neu du lieu da ton tai.

## Important notes

- Khong upload `venv/`, `venv_broken_backup/`, `node_modules/`, `dist/`
- Khong upload `backend/.env`
- Chi can upload source code, file huong dan, va file khai bao dependency
