# VSTEP Master – Website luyện thi VSTEP B1 · B2

Web học tiếng Anh luyện thi VSTEP bậc 3-4 (B1–B2), xây dựng bằng **Django + SQLite**, nội dung bám theo giáo trình **Destination B1/B2**.

## Tính năng

| Mục | Nội dung |
|---|---|
| 📘 Ngữ pháp | **18 unit** lý thuyết tiếng Việt (bảng công thức, ví dụ song ngữ, lỗi thường gặp) + **244 câu bài tập**, sai câu nào giải thích câu đó. Gồm cả các unit B2: **Word Formation, Causative, Đảo ngữ & Câu chẻ, Từ nối & Mệnh đề rút gọn** |
| 📗 Từ vựng | **484 từ & cụm từ / 22 chủ đề**: IPA, nghĩa, ví dụ song ngữ, nút 🔊 phát âm, **flashcard** và **quiz** sinh đề ngẫu nhiên. Gồm 18 chủ đề từ vựng (Gia đình, Giáo dục, Môi trường, Xã hội...) + 4 chủ đề cụm từ chuyên biệt: **Phrasal Verbs, Collocations, Idioms, Cụm câu cho Nói & Viết** |
| 📖 Đọc hiểu | **9 bài đọc** format VSTEP + 45 câu hỏi có giải thích, kèm bản dịch tiếng Việt |
| 🎧 Nghe hiểu | **7 bài nghe** đủ dạng đề thật (thông báo, hội thoại, bài giảng) + 28 câu hỏi, sau khi nộp hiện transcript + bản dịch |
| ✍️ Viết | Hướng dẫn Task 1 (thư/email) & Task 2 (luận): khung bài, mẫu câu, bài mẫu ~band 8 có phân tích |
| 🎤 Nói | Chiến lược 3 part, khung trả lời A.R.E, bài nói mẫu có dịch |
| ⏱️ Thi thử | Đề trắc nghiệm tổng hợp **45 câu** (25 ngữ pháp + 10 từ vựng + 2 bài đọc, ngẫu nhiên mỗi lần từ ngân hàng **317 câu**), đồng hồ đếm ngược 40 phút, tự nộp khi hết giờ |
| 📊 Tiến độ | Đăng ký/đăng nhập, lưu lịch sử điểm mọi bài làm, đánh dấu từ đã thuộc |

## Chạy dự án

```bash
pip install -r requirements.txt
python manage.py migrate       # tạo database SQLite
python manage.py seed_data     # nạp toàn bộ học liệu
python manage.py runserver     # mở http://127.0.0.1:8000
```

Tạo tài khoản quản trị (trang /admin để thêm/sửa câu hỏi, từ vựng):

```bash
python manage.py createsuperuser
```

## Cấu trúc học liệu

Toàn bộ nội dung nằm trong `learning/data/`:

- `grammar_1.py … grammar_4.py` — 18 unit ngữ pháp + câu hỏi
- `grammar_extra1.py, grammar_extra2.py` — câu hỏi luyện tập bổ sung (map theo unit order)
- `vocab_1.py … vocab_4.py` — 22 chủ đề từ vựng & cụm từ
- `vocab_5.py` — từ bổ sung cho 12 chủ đề gốc (map theo tên chủ đề)
- `reading.py, reading_2.py` — 9 bài đọc + câu hỏi
- `listening.py, listening_2.py` — 7 bài nghe (transcript + bản dịch) + câu hỏi
- `skills.py` — bài học Viết & Nói

Muốn thêm nội dung: sửa các file trên rồi chạy lại `python manage.py seed_data`
(lệnh này xóa và nạp lại học liệu, **không** ảnh hưởng tài khoản và điểm đã lưu).

## Lưu ý

- Nút 🔊 phát âm và nghe bài dùng Web Speech API — hoạt động tốt nhất trên Chrome/Edge.
- Đề thi thử và quiz từ vựng được trộn ngẫu nhiên, mỗi lần làm là một đề khác nhau.
