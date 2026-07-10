"""
Script to update grammar lesson content - Units 11-14.
"""
import os, sys, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vstep.settings')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
django.setup()

from learning.models import Unit, GrammarLesson

CONTENT = {}

# ============================================================
# UNIT 11: Relative Clauses
# ============================================================
CONTENT[11] = """
<h3>1. Mệnh đề quan hệ là gì?</h3>
<p>Mệnh đề quan hệ dùng để <b>bổ nghĩa cho danh từ</b> đứng trước nó, giúp xác định hoặc thêm thông tin cho danh từ đó.</p>

<div class="ex">The girl <b>who is wearing a red dress</b> is my sister.<span class="vi">→ Cô gái <b>đang mặc váy đỏ</b> là chị tôi. (mệnh đề "who is wearing a red dress" bổ nghĩa cho "the girl")</span></div>

<h3>2. Các đại từ quan hệ</h3>
<table>
<tr><th>Đại từ</th><th>Thay cho</th><th>Chức năng</th><th>Ví dụ</th></tr>
<tr><td><b>who</b></td><td>Người</td><td>Chủ ngữ / Tân ngữ</td><td>The man <b>who</b> called you is my boss.</td></tr>
<tr><td><b>whom</b></td><td>Người</td><td>Tân ngữ (trang trọng)</td><td>The person <b>whom</b> I met was very kind.</td></tr>
<tr><td><b>which</b></td><td>Vật / Động vật</td><td>Chủ ngữ / Tân ngữ</td><td>The book <b>which</b> I bought is interesting.</td></tr>
<tr><td><b>that</b></td><td>Người / Vật</td><td>Chủ ngữ / Tân ngữ</td><td>The girl <b>that</b> sits next to me is smart.</td></tr>
<tr><td><b>whose</b></td><td>Người / Vật</td><td>Sở hữu (= of whom/which)</td><td>The woman <b>whose</b> car was stolen called the police.</td></tr>
<tr><td><b>where</b></td><td>Nơi chốn</td><td>Trạng từ (= in/at which)</td><td>The city <b>where</b> I grew up is small.</td></tr>
<tr><td><b>when</b></td><td>Thời gian</td><td>Trạng từ (= at/in which)</td><td>I remember the day <b>when</b> we first met.</td></tr>
<tr><td><b>why</b></td><td>Lý do</td><td>Trạng từ (= for which)</td><td>Tell me the reason <b>why</b> you were late.</td></tr>
</table>

<h3>3. Mệnh đề quan hệ xác định vs không xác định</h3>

<h4>3.1. Mệnh đề xác định (Defining)</h4>
<p><b>Cần thiết</b> để hiểu danh từ chỉ ai/cái gì. Bỏ đi → câu mất nghĩa hoặc đổi nghĩa. <b>KHÔNG có dấu phẩy.</b></p>
<div class="ex">The students <b>who passed the exam</b> were very happy.<span class="vi">→ Những sinh viên <b>đã đỗ kỳ thi</b> rất vui. (chỉ những SV đỗ, không phải tất cả SV)</span></div>
<div class="ex">The hotel <b>where we stayed</b> was excellent.<span class="vi">→ Khách sạn <b>mà chúng tôi ở</b> rất tuyệt.</span></div>
<div class="note"><b>💡</b> Trong mệnh đề xác định, có thể dùng <b>that</b> thay cho who/which. Nếu đại từ QH làm tân ngữ, có thể <b>lược bỏ</b>.<br>
The book (that/which) I bought = The book I bought.</div>

<h4>3.2. Mệnh đề không xác định (Non-defining)</h4>
<p>Thêm <b>thông tin phụ</b>, bỏ đi câu vẫn đủ nghĩa. <b>CÓ dấu phẩy.</b> <b>KHÔNG dùng "that".</b></p>
<div class="ex">My mother<b>, who is 55,</b> still works every day.<span class="vi">→ Mẹ tôi, <b>55 tuổi</b>, vẫn làm việc mỗi ngày. (thêm thông tin về tuổi, bỏ đi câu vẫn đủ nghĩa)</span></div>
<div class="ex">Hanoi<b>, which is the capital of Vietnam,</b> has a population of about 8 million.<span class="vi">→ Hà Nội, <b>thủ đô của Việt Nam</b>, có dân số khoảng 8 triệu.</span></div>
<div class="ex">Mr. Nguyen<b>, whose son studies abroad,</b> is my neighbor.<span class="vi">→ Ông Nguyễn, <b>con trai ông ấy du học</b>, là hàng xóm tôi.</span></div>

<div class="warn"><b>⚠️ Phân biệt quan trọng:</b><br>
<b>Xác định:</b> The students <b>who</b> passed the exam were happy. (chỉ những ai đỗ)<br>
<b>Không xác định:</b> The students<b>, who</b> passed the exam<b>,</b> were happy. (TẤT CẢ SV đã đỗ, chỉ thêm thông tin)</div>

<h3>4. Cách dùng whose</h3>
<p><b>whose</b> = "mà ... của (ai đó)" — thể hiện sự <b>sở hữu</b>.</p>
<div class="ex">I know the girl <b>whose father</b> is a doctor.<span class="vi">→ Tôi quen cô gái <b>mà bố cô ấy</b> là bác sĩ.</span></div>
<div class="ex">The house <b>whose roof</b> was damaged has been repaired.<span class="vi">→ Ngôi nhà <b>mà mái</b> bị hỏng đã được sửa. (whose cũng dùng cho vật)</span></div>

<h3>5. Rút gọn mệnh đề quan hệ</h3>
<table>
<tr><th>Đầy đủ</th><th>→ Rút gọn</th><th>Khi nào</th></tr>
<tr><td>...who/which + <b>is/are + V-ing</b></td><td>→ <b>V-ing</b></td><td>Chủ động</td></tr>
<tr><td>The man <b>who is standing</b> there...</td><td>→ The man <b>standing</b> there...</td><td></td></tr>
<tr><td>...who/which + <b>is/are + V3</b></td><td>→ <b>V3</b></td><td>Bị động</td></tr>
<tr><td>The book <b>which was written</b> by her...</td><td>→ The book <b>written</b> by her...</td><td></td></tr>
<tr><td>...who/which + <b>is/are + adj/noun</b></td><td>→ <b>adj/noun</b> (bỏ be)</td><td>To be + tính từ/danh từ</td></tr>
</table>

<div class="ex">The students <b>sitting</b> in the front row are the best.<span class="vi">→ Rút gọn từ: "The students <b>who are sitting</b> in the front row..."</span></div>
<div class="ex">The letter <b>written</b> in French was hard to understand.<span class="vi">→ Rút gọn từ: "The letter <b>which was written</b> in French..."</span></div>

<h3>6. Mẹo làm bài thi VSTEP</h3>
<div class="note"><b>💡 Chiến lược:</b><br>
<b>1.</b> Người → who/whom/that. Vật → which/that. Sở hữu → whose. Nơi → where. Lúc → when.<br>
<b>2.</b> Có dấu phẩy → mệnh đề không xác định → KHÔNG dùng "that".<br>
<b>3.</b> Danh từ riêng (tên người, thành phố) → mệnh đề không xác định (có phẩy).<br>
<b>4.</b> Nếu sau chỗ trống có S + V (đủ chủ-vị) → đại từ QH làm tân ngữ (whom/which hoặc lược bỏ).<br>
<b>5.</b> Nếu sau chỗ trống thiếu chủ ngữ → đại từ QH làm chủ ngữ (who/which/that).</div>
"""

# ============================================================
# UNIT 12: Gerunds & Infinitives
# ============================================================
CONTENT[12] = """
<h3>1. Gerund (V-ing) là gì?</h3>
<p>Gerund = động từ thêm <b>-ing</b> và dùng như <b>danh từ</b>.</p>
<div class="ex"><b>Swimming</b> is good exercise.<span class="vi">→ Bơi lội là bài tập tốt. (Swimming = danh từ, làm chủ ngữ)</span></div>
<div class="ex">I enjoy <b>reading</b> books.<span class="vi">→ Tôi thích đọc sách. (reading = tân ngữ sau enjoy)</span></div>

<h3>2. Infinitive (to V) là gì?</h3>
<p>Infinitive = <b>to + V nguyên mẫu</b>.</p>
<div class="ex">I want <b>to learn</b> English.<span class="vi">→ Tôi muốn học tiếng Anh.</span></div>
<div class="ex">It's important <b>to study</b> every day.<span class="vi">→ Việc học mỗi ngày là quan trọng.</span></div>

<h3>3. Động từ theo sau bởi V-ing (Gerund)</h3>
<p>Các động từ này <b>BẮT BUỘC</b> đi với V-ing:</p>
<table>
<tr><th>Động từ</th><th>Nghĩa</th><th>Ví dụ</th></tr>
<tr><td>enjoy</td><td>thích</td><td>I enjoy <b>cooking</b>.</td></tr>
<tr><td>avoid</td><td>tránh</td><td>He avoids <b>eating</b> sugar.</td></tr>
<tr><td>finish</td><td>hoàn thành</td><td>I finished <b>writing</b> the report.</td></tr>
<tr><td>mind</td><td>phiền</td><td>Do you mind <b>opening</b> the window?</td></tr>
<tr><td>suggest</td><td>gợi ý</td><td>She suggested <b>going</b> to the beach.</td></tr>
<tr><td>practice / practise</td><td>luyện tập</td><td>You should practice <b>speaking</b> English.</td></tr>
<tr><td>consider</td><td>cân nhắc</td><td>I'm considering <b>changing</b> my job.</td></tr>
<tr><td>keep (on)</td><td>tiếp tục</td><td>He keeps <b>making</b> the same mistake.</td></tr>
<tr><td>give up</td><td>từ bỏ</td><td>She gave up <b>smoking</b>.</td></tr>
<tr><td>deny</td><td>phủ nhận</td><td>He denied <b>stealing</b> the money.</td></tr>
<tr><td>admit</td><td>thừa nhận</td><td>She admitted <b>making</b> a mistake.</td></tr>
<tr><td>postpone / put off</td><td>hoãn</td><td>They postponed <b>holding</b> the meeting.</td></tr>
<tr><td>can't help</td><td>không nhịn được</td><td>I can't help <b>laughing</b>.</td></tr>
<tr><td>can't stand</td><td>không chịu nổi</td><td>I can't stand <b>waiting</b> in line.</td></tr>
<tr><td>look forward to</td><td>mong đợi</td><td>I look forward to <b>hearing</b> from you.</td></tr>
<tr><td>be used to</td><td>quen với</td><td>I'm used to <b>getting</b> up early.</td></tr>
</table>

<div class="note"><b>💡 Mẹo nhớ:</b> Nhiều động từ diễn tả <b>cảm xúc, thái độ</b> (enjoy, mind, can't stand, can't help) hoặc <b>thời điểm</b> (finish, give up, keep on, postpone) thường đi với V-ing.</div>

<h3>4. Động từ theo sau bởi to V (Infinitive)</h3>
<table>
<tr><th>Động từ</th><th>Nghĩa</th><th>Ví dụ</th></tr>
<tr><td>want</td><td>muốn</td><td>I want <b>to go</b> home.</td></tr>
<tr><td>need</td><td>cần</td><td>We need <b>to talk</b>.</td></tr>
<tr><td>decide</td><td>quyết định</td><td>She decided <b>to study</b> abroad.</td></tr>
<tr><td>plan</td><td>lên kế hoạch</td><td>I plan <b>to travel</b> next month.</td></tr>
<tr><td>hope</td><td>hi vọng</td><td>I hope <b>to see</b> you again.</td></tr>
<tr><td>expect</td><td>mong đợi</td><td>I didn't expect <b>to win</b>.</td></tr>
<tr><td>promise</td><td>hứa</td><td>He promised <b>to help</b> me.</td></tr>
<tr><td>offer</td><td>đề nghị</td><td>She offered <b>to drive</b> me home.</td></tr>
<tr><td>agree</td><td>đồng ý</td><td>They agreed <b>to work</b> together.</td></tr>
<tr><td>refuse</td><td>từ chối</td><td>He refused <b>to answer</b>.</td></tr>
<tr><td>learn</td><td>học</td><td>I'm learning <b>to drive</b>.</td></tr>
<tr><td>afford</td><td>có đủ khả năng</td><td>I can't afford <b>to buy</b> a car.</td></tr>
<tr><td>manage</td><td>xoay xở</td><td>She managed <b>to finish</b> on time.</td></tr>
<tr><td>pretend</td><td>giả vờ</td><td>He pretended <b>to be</b> asleep.</td></tr>
<tr><td>seem / appear</td><td>dường như</td><td>She seems <b>to be</b> happy.</td></tr>
<tr><td>would like</td><td>muốn (lịch sự)</td><td>I'd like <b>to order</b> a coffee.</td></tr>
</table>

<div class="note"><b>💡 Mẹo nhớ:</b> Các động từ diễn tả <b>dự định, mong muốn, quyết định hướng tới tương lai</b> (want, plan, hope, decide, expect, promise) thường đi với to V.</div>

<h3>5. Động từ đi với cả V-ing VÀ to V — KHÁC NGHĨA</h3>
<p>Đây là phần <b>HAY THI NHẤT</b>!</p>

<table>
<tr><th>Động từ</th><th>+ V-ing</th><th>+ to V</th></tr>
<tr><td><b>remember</b></td><td>Nhớ <b>đã làm</b> (quá khứ)<br><i>I remember <b>locking</b> the door.</i><br>(Tôi nhớ đã khóa cửa.)</td><td>Nhớ <b>phải làm</b> (tương lai)<br><i>Remember <b>to lock</b> the door!</i><br>(Nhớ khóa cửa nhé!)</td></tr>
<tr><td><b>forget</b></td><td>Quên <b>đã làm</b><br><i>I'll never forget <b>meeting</b> her.</i><br>(Tôi không bao giờ quên lần gặp cô ấy.)</td><td>Quên <b>phải làm</b><br><i>I forgot <b>to buy</b> milk.</i><br>(Tôi quên mua sữa.)</td></tr>
<tr><td><b>stop</b></td><td>Dừng <b>việc đang làm</b><br><i>He stopped <b>smoking</b>.</i><br>(Anh ấy bỏ hút thuốc.)</td><td>Dừng lại <b>để làm việc khác</b><br><i>He stopped <b>to smoke</b>.</i><br>(Anh ấy dừng lại để hút thuốc.)</td></tr>
<tr><td><b>try</b></td><td>Thử <b>làm</b> (xem kết quả)<br><i>Try <b>adding</b> more salt.</i><br>(Thử thêm muối xem.)</td><td>Cố gắng <b>làm</b><br><i>I tried <b>to open</b> the door.</i><br>(Tôi cố mở cửa nhưng không được.)</td></tr>
<tr><td><b>regret</b></td><td>Hối tiếc <b>đã làm</b><br><i>I regret <b>telling</b> her the truth.</i><br>(Tôi hối hận đã nói sự thật.)</td><td>Tiếc phải <b>thông báo</b><br><i>I regret <b>to inform</b> you that...</i><br>(Tôi rất tiếc phải thông báo...)</td></tr>
</table>

<div class="warn"><b>⚠️ So sánh cực kỳ quan trọng (stop):</b><br>
"He stopped <b>smoking</b>." = Anh ấy <b>bỏ</b> hút thuốc. (thuốc là thứ anh ấy dừng)<br>
"He stopped <b>to smoke</b>." = Anh ấy dừng lại <b>để</b> hút thuốc. (dừng công việc khác, rồi hút)</div>

<h3>6. V-ing sau giới từ</h3>
<p>Sau <b>TẤT CẢ giới từ</b> (in, on, at, about, of, for, without, before, after...) → luôn dùng <b>V-ing</b>.</p>
<div class="ex">I'm interested <b>in learning</b> Japanese.<span class="vi">→ Tôi thích thú về việc học tiếng Nhật.</span></div>
<div class="ex">She left without <b>saying</b> goodbye.<span class="vi">→ Cô ấy rời đi mà không nói tạm biệt.</span></div>
<div class="ex">Thank you <b>for helping</b> me.<span class="vi">→ Cảm ơn bạn đã giúp tôi.</span></div>
<div class="ex">I'm thinking <b>about changing</b> my job.<span class="vi">→ Tôi đang nghĩ về việc đổi việc.</span></div>

<div class="warn"><b>⚠️ Lưu ý "to" là giới từ hay thuộc to-infinitive?</b><br>
• "I want <b>to go</b>." → to thuộc infinitive → V nguyên mẫu.<br>
• "I look forward <b>to seeing</b> you." → "to" là giới từ trong cụm "look forward to" → V-ing.<br>
• "I'm used <b>to working</b> late." → "to" là giới từ trong "be used to" → V-ing.<br>
Nếu "to" đi liền sau: be used to, look forward to, object to, be accustomed to → <b>V-ing</b>!</div>

<h3>7. Mẹo làm bài thi VSTEP</h3>
<div class="note"><b>💡 Chiến lược:</b><br>
<b>1.</b> Thuộc danh sách: enjoy, avoid, finish, mind, suggest... → V-ing. want, need, decide, hope, plan... → to V.<br>
<b>2.</b> Sau giới từ → LUÔN V-ing (in doing, about going, for helping...).<br>
<b>3.</b> remember/forget/stop/try → hỏi nghĩa: đã làm hay sẽ làm?<br>
<b>4.</b> Nếu là "look forward to" / "be used to" → V-ing (to = giới từ).</div>
"""

# ============================================================
# UNIT 13: Articles (a/an/the)
# ============================================================
CONTENT[13] = """
<h3>1. Mạo từ không xác định: a / an</h3>

<h4>1.1. Khi nào dùng a/an?</h4>
<table>
<tr><th>Dùng khi</th><th>Ví dụ</th></tr>
<tr><td>Nói về <b>một thứ chưa xác định</b>, nhắc đến <b>lần đầu</b></td><td>I saw <b>a</b> cat in the garden. (một con mèo nào đó, chưa biết con nào)</td></tr>
<tr><td>Nói về <b>nghề nghiệp</b></td><td>She is <b>a</b> teacher. / He is <b>an</b> engineer.</td></tr>
<tr><td>Diễn tả <b>một trong nhiều</b></td><td>Can I have <b>a</b> glass of water? (một cốc bất kỳ)</td></tr>
<tr><td>Sau <b>what</b> trong câu cảm thán</td><td>What <b>a</b> beautiful day!</td></tr>
</table>

<h4>1.2. a hay an?</h4>
<table>
<tr><th><b>a</b></th><th><b>an</b></th></tr>
<tr><td>Trước <b>phụ âm</b> (âm đọc, KHÔNG phải chữ cái)</td><td>Trước <b>nguyên âm</b> (âm đọc: /æ/, /e/, /ɪ/, /ɒ/, /ʌ/)</td></tr>
<tr><td>a book, a car, a student</td><td>an apple, an egg, an idea</td></tr>
<tr><td>a <b>u</b>niversity /juːnɪˈvɜːsɪti/ (âm /j/)</td><td>an <b>u</b>mbrella /ʌmˈbrelə/ (âm /ʌ/)</td></tr>
<tr><td>a <b>E</b>uropean /jʊərəˈpiːən/ (âm /j/)</td><td>an <b>h</b>our /aʊə/ (h câm, âm /aʊ/)</td></tr>
<tr><td>a <b>o</b>ne-way ticket /wʌn/ (âm /w/)</td><td>an <b>h</b>onest person /ˈɒnɪst/ (h câm)</td></tr>
</table>

<div class="warn"><b>⚠️ Lỗi cực phổ biến:</b><br>
✗ <s>an university</s> → ✓ <b>a</b> university (phát âm bắt đầu bằng /j/, là phụ âm)<br>
✗ <s>a hour</s> → ✓ <b>an</b> hour (h câm, phát âm bắt đầu bằng /aʊ/, là nguyên âm)<br>
→ Quy tắc: dựa vào <b>ÂM ĐỌC</b>, không phải chữ cái!</div>

<h3>2. Mạo từ xác định: the</h3>

<h4>2.1. Khi nào dùng the?</h4>
<table>
<tr><th>Dùng khi</th><th>Ví dụ</th></tr>
<tr><td>Cả người nói và người nghe đều <b>biết</b> đang nói về cái gì</td><td>Please close <b>the</b> door. (cánh cửa cụ thể mà cả hai đều thấy)</td></tr>
<tr><td>Đã nhắc đến <b>trước đó</b> (lần 2 trở đi)</td><td>I saw <b>a</b> dog. <b>The</b> dog was very big. (lần 1: a dog, lần 2: the dog)</td></tr>
<tr><td>Chỉ vật <b>duy nhất</b></td><td><b>the</b> sun, <b>the</b> moon, <b>the</b> Earth, <b>the</b> Internet</td></tr>
<tr><td>So sánh <b>nhất</b></td><td>She is <b>the</b> tallest girl in the class.</td></tr>
<tr><td>Với <b>số thứ tự</b></td><td><b>the</b> first, <b>the</b> second, <b>the</b> last</td></tr>
<tr><td><b>Nhạc cụ</b> (chơi nhạc)</td><td>She plays <b>the</b> piano. / He plays <b>the</b> guitar.</td></tr>
<tr><td>Tên <b>sông, biển, đại dương, sa mạc, dãy núi, quần đảo</b></td><td><b>the</b> Mekong, <b>the</b> Pacific Ocean, <b>the</b> Sahara, <b>the</b> Alps</td></tr>
<tr><td>Tên nước có <b>Republic, Kingdom, States, Union</b></td><td><b>the</b> United States, <b>the</b> United Kingdom, <b>the</b> Czech Republic</td></tr>
</table>

<h3>3. Không dùng mạo từ (Zero article – Ø)</h3>
<table>
<tr><th>Không dùng the khi</th><th>Ví dụ</th></tr>
<tr><td>Nói <b>chung chung</b>, tổng quát</td><td>Ø <b>Dogs</b> are friendly animals. (chó nói chung, không phải con chó cụ thể)</td></tr>
<tr><td>Danh từ <b>không đếm được</b> (nói chung)</td><td>Ø <b>Water</b> is essential for life. / I like Ø <b>music</b>.</td></tr>
<tr><td>Tên <b>người, thành phố, quốc gia</b> (hầu hết)</td><td>Ø <b>Vietnam</b>, Ø <b>Hanoi</b>, Ø <b>John</b></td></tr>
<tr><td>Tên <b>núi đơn lẻ, hồ, lục địa</b></td><td>Ø <b>Mount Everest</b>, Ø <b>Lake Baikal</b>, Ø <b>Asia</b></td></tr>
<tr><td>Tên <b>bữa ăn</b></td><td>I have Ø <b>breakfast</b> at 7 a.m.</td></tr>
<tr><td>Tên <b>môn thể thao, môn học</b></td><td>She plays Ø <b>tennis</b>. / I study Ø <b>math</b>.</td></tr>
<tr><td>Tên <b>ngôn ngữ</b></td><td>I speak Ø <b>English</b> and Ø <b>Vietnamese</b>.</td></tr>
<tr><td><b>Phương tiện</b> (by + ...)</td><td>I go to school <b>by</b> Ø <b>bus</b>. (nhưng: in <b>the</b> bus = bên trong xe buýt)</td></tr>
</table>

<h3>4. Bảng so sánh nhanh</h3>
<div class="ex"><b>So sánh 3 câu:</b><br>
"I like Ø <b>coffee</b>." → Tôi thích cà phê. (cà phê nói chung)<br>
"I'd like <b>a</b> coffee." → Tôi muốn (gọi) một ly cà phê. (một ly bất kỳ)<br>
"<b>The</b> coffee is cold." → Ly cà phê (này/đó) nguội rồi. (ly cà phê cụ thể trước mặt)</div>

<div class="ex"><b>So sánh:</b><br>
"She goes to Ø <b>school</b>." → Cô ấy đi học. (mục đích: học)<br>
"She goes to <b>the school</b>." → Cô ấy đến trường (cụ thể). (mục đích: gặp ai đó, không phải đi học)</div>

<h3>5. Mẹo làm bài thi VSTEP</h3>
<div class="note"><b>💡 Chiến lược 3 câu hỏi:</b><br>
<b>Q1:</b> Danh từ này đếm được số ít? → Cần mạo từ (a/an hoặc the).<br>
<b>Q2:</b> Cả hai người đều biết đang nói về cái gì cụ thể? → <b>the</b>. Chưa biết? → <b>a/an</b>.<br>
<b>Q3:</b> Nói chung chung, tổng quát? → Không dùng mạo từ (Ø).<br><br>
<b>Lỗi hay gặp:</b><br>
✗ <s>She is teacher.</s> → ✓ She is <b>a</b> teacher. (nghề nghiệp cần a/an)<br>
✗ <s>The life is beautiful.</s> → ✓ Ø <b>Life</b> is beautiful. (nói chung → không the)<br>
✗ <s>I play the football.</s> → ✓ I play Ø <b>football</b>. (môn thể thao → không the)</div>
"""

# ============================================================
# UNIT 14: Quantifiers
# ============================================================
CONTENT[14] = """
<h3>1. Tổng quan về từ chỉ số lượng</h3>
<p>Từ chỉ số lượng đứng trước danh từ để cho biết <b>bao nhiêu</b>, nhưng mỗi từ chỉ đi với loại danh từ cụ thể.</p>

<h3>2. Đếm được vs Không đếm được</h3>
<table>
<tr><th></th><th>Đếm được (Countable)</th><th>Không đếm được (Uncountable)</th></tr>
<tr><td><b>Đặc điểm</b></td><td>Có thể đếm: 1, 2, 3...<br>Có dạng số ít và số nhiều</td><td>Không đếm: dạng khối, chất liệu<br>Chỉ có 1 dạng, không thêm -s</td></tr>
<tr><td><b>Ví dụ</b></td><td>a book → two books<br>an apple → three apples</td><td>water, money, information<br>advice, furniture, news, rice</td></tr>
</table>

<div class="warn"><b>⚠️ Danh từ không đếm được hay nhầm:</b><br>
<b>information</b> (thông tin), <b>advice</b> (lời khuyên), <b>news</b> (tin tức), <b>furniture</b> (đồ nội thất), <b>equipment</b> (thiết bị), <b>homework</b> (bài tập về nhà), <b>research</b> (nghiên cứu), <b>knowledge</b> (kiến thức), <b>luggage/baggage</b> (hành lý), <b>weather</b> (thời tiết), <b>traffic</b> (giao thông).<br>
→ Tất cả KHÔNG thêm -s, KHÔNG dùng a/an.<br>
✗ <s>an information, two advices, furnitures</s><br>
✓ <b>a piece of</b> information, <b>some</b> advice, <b>a lot of</b> furniture</div>

<h3>3. Bảng từ chỉ số lượng</h3>
<table>
<tr><th>Từ</th><th>Đếm được</th><th>Không đếm được</th><th>Nghĩa</th></tr>
<tr><td><b>many</b></td><td>✓</td><td>✗</td><td>nhiều</td></tr>
<tr><td><b>much</b></td><td>✗</td><td>✓</td><td>nhiều</td></tr>
<tr><td><b>a lot of / lots of</b></td><td>✓</td><td>✓</td><td>nhiều (cả hai loại)</td></tr>
<tr><td><b>some</b></td><td>✓</td><td>✓</td><td>một số, một ít</td></tr>
<tr><td><b>any</b></td><td>✓</td><td>✓</td><td>nào (phủ định/nghi vấn)</td></tr>
<tr><td><b>few</b></td><td>✓</td><td>✗</td><td>ít (gần như không đủ)</td></tr>
<tr><td><b>a few</b></td><td>✓</td><td>✗</td><td>một vài (đủ dùng)</td></tr>
<tr><td><b>little</b></td><td>✗</td><td>✓</td><td>ít (gần như không đủ)</td></tr>
<tr><td><b>a little</b></td><td>✗</td><td>✓</td><td>một chút (đủ dùng)</td></tr>
<tr><td><b>every / each</b></td><td>✓ (số ít)</td><td>✗</td><td>mỗi, mọi</td></tr>
<tr><td><b>no</b></td><td>✓</td><td>✓</td><td>không có</td></tr>
<tr><td><b>all</b></td><td>✓ (số nhiều)</td><td>✓</td><td>tất cả</td></tr>
</table>

<h3>4. Phân biệt chi tiết</h3>

<h4>4.1. many vs much vs a lot of</h4>
<div class="ex">There are <b>many</b> students in the class. (đếm được)<span class="vi">→ Có nhiều học sinh trong lớp.</span></div>
<div class="ex">I don't have <b>much</b> time. (không đếm được)<span class="vi">→ Tôi không có nhiều thời gian.</span></div>
<div class="ex">She has <b>a lot of</b> friends. (đếm được)<br>There is <b>a lot of</b> water. (không đếm được)<span class="vi">→ a lot of dùng được cho cả hai loại, thường dùng trong câu khẳng định.</span></div>
<div class="note"><b>💡</b> <b>many/much</b> thường dùng trong câu <b>phủ định và nghi vấn</b>. Trong câu khẳng định, <b>a lot of</b> tự nhiên hơn.<br>
"I have <b>a lot of</b> books." (tự nhiên) thay vì "I have <b>many</b> books." (hơi cứng)</div>

<h4>4.2. few vs a few / little vs a little</h4>
<table>
<tr><th></th><th>Đếm được</th><th>Không đếm được</th><th>Sắc thái</th></tr>
<tr><td><b>Tiêu cực</b> (ít, gần như không đủ)</td><td><b>few</b></td><td><b>little</b></td><td>😟 Ít quá, đáng lo</td></tr>
<tr><td><b>Tích cực</b> (một ít, đủ dùng)</td><td><b>a few</b></td><td><b>a little</b></td><td>🙂 Có một chút, ổn</td></tr>
</table>

<div class="ex">He has <b>few</b> friends, so he's very lonely.<span class="vi">→ Anh ấy có ít bạn, nên rất cô đơn. (ít đến mức đáng buồn)</span></div>
<div class="ex">He has <b>a few</b> friends, so he's not lonely.<span class="vi">→ Anh ấy có vài người bạn, nên không cô đơn. (đủ, ổn)</span></div>
<div class="ex">There is <b>little</b> milk left. We need to buy more.<span class="vi">→ Còn rất ít sữa. Phải mua thêm. (gần hết, lo)</span></div>
<div class="ex">There is <b>a little</b> milk left. That's enough for one cup.<span class="vi">→ Còn một chút sữa. Đủ cho một cốc. (có một chút, ổn)</span></div>

<div class="warn"><b>⚠️ Quy tắc nhớ:</b> Có <b>"a"</b> → tích cực (a few, a little = có một ít, đủ). Không có "a" → tiêu cực (few, little = quá ít, không đủ).</div>

<h4>4.3. some vs any</h4>
<table>
<tr><th>some</th><th>any</th></tr>
<tr><td>Câu <b>khẳng định</b></td><td>Câu <b>phủ định</b> và <b>nghi vấn</b></td></tr>
<tr><td>I need <b>some</b> help.</td><td>I don't need <b>any</b> help.<br>Do you need <b>any</b> help?</td></tr>
</table>

<div class="note"><b>💡 Ngoại lệ:</b> Dùng <b>some</b> trong câu hỏi khi <b>mời, đề nghị, hoặc mong đợi câu trả lời "yes"</b>:<br>
"Would you like <b>some</b> coffee?" (mời)<br>
"Can I have <b>some</b> water, please?" (yêu cầu lịch sự)</div>

<h4>4.4. every vs each</h4>
<div class="ex"><b>Every</b> student must take the exam. (= tất cả, nhìn tổng thể)<span class="vi">→ Mọi học sinh đều phải thi.</span></div>
<div class="ex"><b>Each</b> student received a certificate. (= từng người một, nhìn cá thể)<span class="vi">→ Mỗi học sinh nhận được một chứng chỉ.</span></div>
<div class="note"><b>💡</b> <b>every</b> = nhấn mạnh TỔNG THỂ (≥3). <b>each</b> = nhấn mạnh TỪNG CÁ THỂ (≥2).</div>

<h3>5. Mẹo làm bài thi VSTEP</h3>
<div class="note"><b>💡 Chiến lược:</b><br>
<b>1.</b> Xác định danh từ đếm được hay không đếm được → chọn đúng từ chỉ số lượng.<br>
<b>2.</b> many = đếm được, much = không đếm được, a lot of = cả hai.<br>
<b>3.</b> few/a few = đếm được, little/a little = không đếm được. Có "a" = tích cực.<br>
<b>4.</b> some = khẳng định (+ mời/đề nghị). any = phủ định, nghi vấn.<br>
<b>5.</b> Nhớ các danh từ không đếm được hay nhầm: information, advice, news, furniture...</div>
"""

for order, content in CONTENT.items():
    try:
        unit = Unit.objects.get(order=order)
        lesson = unit.lesson
        old_len = len(lesson.content)
        lesson.content = content.strip()
        lesson.save()
        print(f"✓ Unit {order}: {old_len} → {len(lesson.content)} chars ({unit.title})")
    except Unit.DoesNotExist:
        print(f"✗ Unit {order} not found")
    except Exception as e:
        print(f"✗ Unit {order} error: {e}")

print(f"\nDone! Updated {len(CONTENT)} units (11-14).")
