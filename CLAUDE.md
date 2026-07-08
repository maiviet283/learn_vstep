# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**VSTEP Master** — web luyện thi tiếng Anh VSTEP B1/B2 cho người Việt, xây bằng Django 6 (app duy nhất: `learning`). Nội dung theo giáo trình Destination B1/B2: ngữ pháp, từ vựng (flashcard), đọc, nghe, viết, nói, thi thử, và theo dõi tiến độ. Toàn bộ UI và nội dung bằng tiếng Việt (`LANGUAGE_CODE = 'vi'`, timezone `Asia/Ho_Chi_Minh`).

## Commands

Chạy trên Windows, dùng venv trong repo. **Luôn đặt `PYTHONUTF8=1`** khi chạy lệnh manage.py có đụng dữ liệu (nội dung tiếng Việt sẽ gây lỗi `charmap codec` nếu thiếu):

```powershell
$env:PYTHONUTF8 = '1'
venv\Scripts\python manage.py runserver      # chạy dev server (cổng 8000)
venv\Scripts\python manage.py migrate        # áp migration lên Supabase
venv\Scripts\python manage.py makemigrations learning
venv\Scripts\python manage.py test learning  # chạy test
venv\Scripts\pip install <package>           # cài package vào venv
```

## Database & Secrets

- Database là **PostgreSQL trên Supabase** (không còn SQLite — `db.sqlite3` đã xóa). Driver: `psycopg`.
- Mọi secret (SECRET_KEY, DB_PASSWORD, DB_HOST...) nằm trong **`.env`** ở gốc repo, được `python-dotenv` nạp trong `vstep/settings.py`. Không bao giờ hard-code secret vào code hay commit `.env` (đã có trong `.gitignore`); mẫu biến ở `.env.example`.
- `DEBUG` đọc từ `.env`, mặc định `False` nếu không khai báo.
- `data.json` là bản backup dữ liệu (dump từ SQLite cũ), đã gitignore. Nạp lại bằng `loaddata data.json` nếu cần.
- Lưu ý: migrate/test chạy trực tiếp trên database cloud — cẩn thận với thao tác xóa dữ liệu.

## Architecture

- `vstep/` — project config (settings, urls gốc chỉ include `learning.urls` + admin).
- `learning/` — toàn bộ logic. Function-based views trong `views.py`, routes trong `urls.py`, templates server-rendered ở `learning/templates/learning/` (kế thừa `base.html`).
- Models chính (`learning/models.py`):
  - Nội dung học: `Unit` → `GrammarLesson` (1-1, content là HTML), `VocabTopic` → `VocabWord`, `ReadingPassage`, `ListeningTrack`, `WritingLesson`, `SpeakingLesson`.
  - `Question` — trắc nghiệm dùng chung cho 4 kỹ năng, phân biệt bằng field `skill` và FK nullable tới unit/topic/passage/track; đáp án A–D (D tùy chọn), luôn có `explanation` tiếng Việt.
  - Tiến độ user: `QuizAttempt` (điểm các lần làm bài), `WordProgress` (từ đã thuộc, unique theo user+word).
- Auth dùng `django.contrib.auth` sẵn có (LoginView/LogoutView + view `register` tự viết).
