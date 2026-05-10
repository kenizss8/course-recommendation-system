# Project Plan

## Project scope

Do an mon: `He thong goi y khoa hoc phu hop voi nhu cau hoc vien`

Stack bat buoc:

- Frontend: React + Vite + Bootstrap + Axios
- Backend: FastAPI
- Database: MongoDB
- Recommendation: rule-based + TF-IDF/Cosine Similarity

Nguyen tac lam bai:

- Uu tien chay duoc truoc
- Giu scope gon, khong them login, chatbot, thanh toan, deploy phuc tap
- Moi ngay co mot muc tieu ro rang
- Moi ngay co mot commit Git de de theo doi tien do

## Current status

Da hoan thanh:

- Tach cau truc thanh `backend/` va `frontend/`
- Chay duoc FastAPI
- Ket noi duoc MongoDB
- CRUD `courses`
- API `POST /recommend`
- React goi duoc backend
- Hien thi duoc danh sach khoa hoc
- Co 18 khoa hoc mau trong MongoDB

## Roadmap 8 weeks

Muc tieu: trong 2 thang, moi ngay lam mot it nhung chac, moi tuan chot duoc mot moc ro rang.

### Week 1: Stable foundation

| Day | Muc tieu | San pham can dat | Goi y commit |
|---|---|---|---|
| 1 | Chot cau truc project | `backend/`, `frontend/`, `venv/`, README co lenh chay | `chore: standardize project structure` |
| 2 | Chot ket noi backend + MongoDB | `/health`, `/db-health` chay on dinh | `feat: connect fastapi to mongodb` |
| 3 | CRUD khoa hoc | `GET/POST/PUT/DELETE /courses` chay duoc | `feat: add course crud api` |
| 4 | Test CRUD bang Swagger | Them, sua, xoa course thanh cong | `test: verify course crud endpoints` |
| 5 | Ket noi React voi backend | React hien duoc danh sach khoa hoc | `feat: fetch and display courses in frontend` |
| 6 | Don dep project | Ghi lai README va cach chay | `docs: add local run instructions` |

### Week 2: Recommendation core

| Day | Muc tieu | San pham can dat | Goi y commit |
|---|---|---|---|
| 7 | Tao logic rule-based | So khop category, level, skills | `feat: add rule based scoring` |
| 8 | Them TF-IDF + Cosine | Tinh duoc similarity score | `feat: add tfidf cosine recommendation` |
| 9 | Tao API `/recommend` | Swagger test duoc recommend | `feat: add recommend endpoint` |
| 10 | Hien thi ket qua recommend tren React | Form gui nhu cau va hien ket qua | `feat: show recommendation results in frontend` |
| 11 | Them 18 course mau | MongoDB co du data de demo | `feat: add sample courses dataset` |
| 12 | Tao script seed | Chay 1 lenh de seed lai du lieu | `feat: add mongodb seed script` |

### Week 3: Make the demo believable

| Day | Muc tieu | San pham can dat | Goi y commit |
|---|---|---|---|
| 13 | Test 3 tinh huong goi y | Python, Web, Data Science | `test: add recommendation scenarios` |
| 14 | Dieu chinh trong so score | Ket qua goi y hop ly hon | `refactor: tune recommendation scoring` |
| 15 | Chi giu top 3 hoac top 5 | Ket qua gon va de hieu | `refactor: limit top recommendation results` |
| 16 | Them ly do goi y | Hien `matched_skills`, score | `feat: explain recommendation reasons` |
| 17 | Kiem tra du lieu trung lap | Seed nhieu lan van on | `fix: make seed script idempotent` |
| 18 | Viet file test tay | Co checklist test on dinh | `docs: add manual api test checklist` |

### Week 4: Input and validation

| Day | Muc tieu | San pham can dat | Goi y commit |
|---|---|---|---|
| 19 | Kiem tra du lieu dau vao backend | Validation ro rang cho API | `feat: validate request payloads` |
| 20 | Xu ly course id loi | Thong bao loi de hieu | `fix: improve invalid course id handling` |
| 21 | Xu ly recommend khi khong co data | Khong vo app, thong bao de hieu | `fix: handle empty recommendation dataset` |
| 22 | Xu ly recommend khi user nhap thieu | Van co ket qua hop ly | `fix: improve recommend fallback behavior` |
| 23 | Kiem tra loi CORS va ket noi FE-BE | Frontend goi API on dinh | `fix: stabilize frontend backend integration` |
| 24 | Chot backend v1 | Backend on dinh, khong them route moi | `release: stabilize backend v1` |

### Week 5: Simple UI completion

| Day | Muc tieu | San pham can dat | Goi y commit |
|---|---|---|---|
| 25 | Chot trang danh sach khoa hoc | Hien thong tin ro rang | `feat: finalize course list page` |
| 26 | Chot form recommend | Input de hieu, de demo | `feat: finalize recommend form` |
| 27 | Chot trang ket qua recommend | Hien top goi y ro rang | `feat: finalize recommendation result view` |
| 28 | Them trang them khoa hoc neu can | Cho demo CRUD de quan | `feat: add simple add course page` |
| 29 | Don CSS va bo text thua | Giao dien gon, de nhin | `style: clean up frontend ui` |
| 30 | Chot frontend v1 | Khong vo layout, khong loi console | `release: stabilize frontend v1` |

### Week 6: Testing and polishing

| Day | Muc tieu | San pham can dat | Goi y commit |
|---|---|---|---|
| 31 | Test lai CRUD tu dau den cuoi | Khong loi co ban | `test: verify full course crud flow` |
| 32 | Test lai recommend voi 5 case | Co ghi ket qua tung case | `test: verify recommendation cases` |
| 33 | So sanh ket qua voi mong doi | Ghi chu xem top course co hop ly khong | `docs: note recommendation evaluation` |
| 34 | Sua cac bug nho | Fix bug phat hien khi test | `fix: resolve manual testing issues` |
| 35 | Don file va comment | Code de doc hon | `refactor: clean up project files` |
| 36 | Chot ban demo on dinh | Build frontend, backend chay on | `release: demo stable version` |

### Week 7: Report and presentation prep

| Day | Muc tieu | San pham can dat | Goi y commit |
|---|---|---|---|
| 37 | Viet mo ta bai toan | Muc tieu, doi tuong, dau vao dau ra | `docs: add problem statement` |
| 38 | Ve so do use case hoac flow | So do luong he thong | `docs: add system flow diagram notes` |
| 39 | Viet mo ta database | Truong du lieu course | `docs: add database description` |
| 40 | Viet mo ta thuat toan | Rule-based + TF-IDF + Cosine | `docs: document recommendation algorithm` |
| 41 | Chuan bi anh demo man hinh | CRUD, recommend, ket qua | `docs: add demo screenshot checklist` |
| 42 | Viet kich ban thuyet trinh ngan | 3-5 phut demo khong lung tung | `docs: add presentation outline` |

### Week 8: Buffer and final lock

| Day | Muc tieu | San pham can dat | Goi y commit |
|---|---|---|---|
| 43 | Sua bug cuoi cung | Fix theo luc demo thu | `fix: final bug fixes` |
| 44 | Kiem tra lai toan bo link chay | FE, BE, MongoDB, Swagger | `test: final environment check` |
| 45 | Kiem tra lai du lieu mau | 18 khoa hoc co day du thong tin | `test: verify seeded sample courses` |
| 46 | Build va chay thu tu dau | Chay lai tu workspace rong | `test: full cold start verification` |
| 47 | Chot README cuoi | Ai mo vao cung chay duoc | `docs: finalize project readme` |
| 48 | Tao tag hoac commit cuoi | Ban nop bai on dinh | `release: final submission version` |

## Minimal daily workflow

Moi ngay nen lam theo 6 buoc nay:

1. `git pull` neu ban lam tren nhieu may
2. Chon 1 muc tieu nho trong bang tren
3. Lam xong thi test ngay
4. Sua loi neu co
5. `git add .`
6. `git commit -m "noi dung hom nay"`

Neu muon day len GitHub:

```powershell
git add .
git commit -m "feat: message"
git push
```

## Priority order

Neu thieu thoi gian, uu tien theo thu tu nay:

1. CRUD `courses`
2. `/recommend`
3. Seed du lieu 18 course
4. Frontend hien duoc ket qua
5. Test 3-5 tinh huong
6. Bao cao va thuyet trinh

## Notes

- Khong mo rong scope qua som
- Chot logic on dinh truoc, giao dien tinh sau
- Moi ngay chi can tien len mot it nhung chac
- Neu co bug, uu tien fix bug truoc khi them tinh nang moi
