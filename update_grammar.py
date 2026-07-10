"""
Script to update grammar lesson content with much more detailed explanations.
Run: set PYTHONUTF8=1 && venv\Scripts\python update_grammar.py
"""
import os, sys, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vstep.settings')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
django.setup()

from learning.models import Unit, GrammarLesson

CONTENT = {}

# ============================================================
# UNIT 1: Present Simple & Present Continuous
# ============================================================
CONTENT[1] = """
<h3>1. Present Simple – Thì hiện tại đơn</h3>

<h4>1.1. Công thức</h4>
<table>
<tr><th>Dạng</th><th>Cấu trúc</th><th>Ví dụ</th></tr>
<tr><td>Khẳng định</td><td>S + V(s/es)<br><i>I/You/We/They + V nguyên mẫu</i><br><i>He/She/It + V-s/es</i></td><td>I <b>work</b> from home.<br>She <b>works</b> in a bank.</td></tr>
<tr><td>Phủ định</td><td>S + do/does + not + V<br><i>I/You/We/They + <b>don't</b> + V</i><br><i>He/She/It + <b>doesn't</b> + V</i></td><td>I <b>don't like</b> coffee.<br>He <b>doesn't eat</b> meat.</td></tr>
<tr><td>Nghi vấn</td><td><b>Do/Does</b> + S + V?<br><i>Trả lời: Yes, S + do/does.<br>No, S + don't/doesn't.</i></td><td><b>Do</b> you <b>speak</b> English?<br>– Yes, I <b>do</b>.<br><b>Does</b> she <b>live</b> here?<br>– No, she <b>doesn't</b>.</td></tr>
</table>

<h4>1.2. Quy tắc thêm -s/-es cho ngôi thứ ba số ít (He/She/It)</h4>
<table>
<tr><th>Trường hợp</th><th>Quy tắc</th><th>Ví dụ</th></tr>
<tr><td>Hầu hết động từ</td><td>Thêm <b>-s</b></td><td>work → work<b>s</b>, play → play<b>s</b>, read → read<b>s</b></td></tr>
<tr><td>Tận cùng -s, -ss, -sh, -ch, -x, -z, -o</td><td>Thêm <b>-es</b></td><td>go → go<b>es</b>, wash → wash<b>es</b>, watch → watch<b>es</b>, miss → miss<b>es</b>, fix → fix<b>es</b></td></tr>
<tr><td>Tận cùng phụ âm + y</td><td>Đổi <b>y → ies</b></td><td>study → stud<b>ies</b>, carry → carr<b>ies</b>, fly → fl<b>ies</b></td></tr>
<tr><td>Tận cùng nguyên âm + y</td><td>Thêm <b>-s</b> bình thường</td><td>play → play<b>s</b>, enjoy → enjoy<b>s</b>, say → say<b>s</b></td></tr>
<tr><td>have</td><td>Bất quy tắc → <b>has</b></td><td>She <b>has</b> two brothers.</td></tr>
</table>

<h4>1.3. Cách dùng chi tiết</h4>

<p><b>① Thói quen, hành động lặp lại</b></p>
<p>Diễn tả việc ai đó thường xuyên làm. Thường đi với các trạng từ tần suất.</p>
<div class="ex">I usually <b>get up</b> at 6 o'clock every morning.<span class="vi">→ Tôi thường dậy lúc 6 giờ mỗi sáng.</span></div>
<div class="ex">She <b>drinks</b> green tea every afternoon.<span class="vi">→ Cô ấy uống trà xanh mỗi buổi chiều.</span></div>
<div class="ex">They never <b>eat</b> fast food.<span class="vi">→ Họ không bao giờ ăn đồ ăn nhanh.</span></div>
<div class="ex">My father <b>reads</b> the newspaper before breakfast.<span class="vi">→ Bố tôi đọc báo trước bữa sáng. (thói quen hàng ngày)</span></div>

<p><b>② Sự thật hiển nhiên, quy luật tự nhiên, chân lý</b></p>
<div class="ex">The Earth <b>goes</b> around the Sun.<span class="vi">→ Trái Đất quay quanh Mặt Trời. (quy luật tự nhiên)</span></div>
<div class="ex">Water <b>boils</b> at 100 degrees Celsius.<span class="vi">→ Nước sôi ở 100 độ C.</span></div>
<div class="ex">Cats <b>don't like</b> water.<span class="vi">→ Mèo không thích nước. (sự thật chung)</span></div>

<p><b>③ Lịch trình, thời gian biểu cố định</b></p>
<div class="ex">The train <b>leaves</b> at 8 a.m. tomorrow.<span class="vi">→ Tàu khởi hành lúc 8 giờ sáng mai. (lịch trình cố định)</span></div>
<div class="ex">The movie <b>starts</b> at 7:30 tonight.<span class="vi">→ Phim bắt đầu lúc 7:30 tối nay. (không dùng thì tương lai vì đây là lịch cố định)</span></div>
<div class="ex">What time <b>does</b> the bank <b>open</b>?<span class="vi">→ Ngân hàng mở cửa lúc mấy giờ?</span></div>

<h4>1.4. Trạng từ tần suất thường gặp</h4>
<table>
<tr><th>Trạng từ</th><th>Tần suất</th><th>Vị trí</th></tr>
<tr><td>always</td><td>100%</td><td rowspan="6"><b>Trước</b> động từ thường<br><b>Sau</b> động từ to be<br><br><i>I <b>always</b> eat breakfast.</i><br><i>She <b>is always</b> late.</i></td></tr>
<tr><td>usually</td><td>~90%</td></tr>
<tr><td>often</td><td>~70%</td></tr>
<tr><td>sometimes</td><td>~50%</td></tr>
<tr><td>rarely / seldom</td><td>~10%</td></tr>
<tr><td>never</td><td>0%</td></tr>
</table>
<p>Ngoài ra: <i>every day/week/month/year, once a week, twice a month, on Mondays, in the morning.</i></p>

<h3>2. Present Continuous – Thì hiện tại tiếp diễn</h3>

<h4>2.1. Công thức</h4>
<table>
<tr><th>Dạng</th><th>Cấu trúc</th><th>Ví dụ</th></tr>
<tr><td>Khẳng định</td><td>S + am/is/are + V-ing</td><td>I <b>am studying</b> English.<br>She <b>is cooking</b> dinner.<br>They <b>are playing</b> football.</td></tr>
<tr><td>Phủ định</td><td>S + am/is/are + not + V-ing</td><td>I<b>'m not watching</b> TV.<br>He <b>isn't sleeping</b>.</td></tr>
<tr><td>Nghi vấn</td><td>Am/Is/Are + S + V-ing?</td><td><b>Are</b> you <b>listening</b> to me?<br>– Yes, I <b>am</b>. / No, I<b>'m not</b>.</td></tr>
</table>

<h4>2.2. Quy tắc thêm -ing</h4>
<table>
<tr><th>Trường hợp</th><th>Quy tắc</th><th>Ví dụ</th></tr>
<tr><td>Hầu hết động từ</td><td>Thêm <b>-ing</b></td><td>go → go<b>ing</b>, play → play<b>ing</b>, read → read<b>ing</b></td></tr>
<tr><td>Tận cùng -e câm</td><td>Bỏ <b>e</b>, thêm <b>-ing</b></td><td>make → mak<b>ing</b>, write → writ<b>ing</b>, come → com<b>ing</b></td></tr>
<tr><td>Tận cùng -ie</td><td>Đổi <b>ie → y</b>, thêm <b>-ing</b></td><td>die → d<b>ying</b>, lie → l<b>ying</b>, tie → t<b>ying</b></td></tr>
<tr><td>1 nguyên âm + 1 phụ âm (từ 1 âm tiết hoặc trọng âm ở cuối)</td><td><b>Gấp đôi</b> phụ âm cuối, thêm <b>-ing</b></td><td>run → ru<b>nn</b>ing, sit → si<b>tt</b>ing, swim → swi<b>mm</b>ing, begin → begi<b>nn</b>ing</td></tr>
<tr><td>Tận cùng -c</td><td>Thêm <b>k</b> rồi <b>-ing</b></td><td>picnic → picnic<b>k</b>ing</td></tr>
</table>

<h4>2.3. Cách dùng chi tiết</h4>

<p><b>① Hành động đang xảy ra ngay tại thời điểm nói</b></p>
<div class="ex">Look! The baby <b>is smiling</b> at you!<span class="vi">→ Nhìn kìa! Em bé đang cười với bạn!</span></div>
<div class="ex">Be quiet! I <b>am trying</b> to concentrate.<span class="vi">→ Im đi! Tôi đang cố tập trung.</span></div>
<div class="ex">Where is Mom? – She <b>is cooking</b> in the kitchen.<span class="vi">→ Mẹ đâu? – Mẹ đang nấu ăn trong bếp.</span></div>

<p><b>② Hành động tạm thời xảy ra xung quanh thời điểm hiện tại</b></p>
<p>Không nhất thiết phải đang diễn ra ngay lúc nói, nhưng là việc tạm thời.</p>
<div class="ex">I <b>am reading</b> a really interesting book this week.<span class="vi">→ Tuần này tôi đang đọc một cuốn sách rất hay. (không phải đang đọc ngay lúc nói, nhưng là việc diễn ra trong tuần này)</span></div>
<div class="ex">My sister <b>is staying</b> with us until she finds a new apartment.<span class="vi">→ Chị tôi đang ở cùng chúng tôi cho đến khi chị ấy tìm được căn hộ mới. (tạm thời)</span></div>

<p><b>③ Kế hoạch đã sắp xếp cho tương lai gần</b></p>
<p>Khác với "will" (quyết định tại chỗ) và "be going to" (dự định), Present Continuous nhấn mạnh đã có sắp xếp cụ thể (đặt vé, hẹn giờ...).</p>
<div class="ex">I <b>am meeting</b> Nam at the café tonight.<span class="vi">→ Tối nay tôi sẽ gặp Nam ở quán cà phê. (đã hẹn rồi)</span></div>
<div class="ex">We <b>are flying</b> to Da Nang next Saturday.<span class="vi">→ Thứ Bảy tuần sau chúng tôi bay đi Đà Nẵng. (đã đặt vé rồi)</span></div>

<p><b>④ Phàn nàn với "always / constantly / forever"</b></p>
<p>Dùng thì tiếp diễn + always để diễn tả sự khó chịu, phàn nàn về thói quen xấu.</p>
<div class="ex">He <b>is always losing</b> his keys!<span class="vi">→ Anh ấy cứ mất chìa khóa hoài! (phàn nàn)</span></div>
<div class="ex">My roommate <b>is constantly leaving</b> dirty dishes in the sink.<span class="vi">→ Bạn cùng phòng tôi cứ để bát bẩn trong bồn rửa hoài. (bực mình)</span></div>

<h3>3. Động từ trạng thái (Stative Verbs) – KHÔNG dùng thì tiếp diễn</h3>
<p>Một số động từ diễn tả <b>trạng thái</b> (không phải hành động) nên KHÔNG chia ở thì tiếp diễn, dù có "now" hay "at the moment".</p>

<table>
<tr><th>Nhóm</th><th>Động từ</th></tr>
<tr><td>Giác quan</td><td>see, hear, smell, taste, feel</td></tr>
<tr><td>Cảm xúc</td><td>like, love, hate, want, need, prefer, wish</td></tr>
<tr><td>Nhận thức</td><td>know, understand, believe, remember, forget, think (= cho rằng), realize, suppose</td></tr>
<tr><td>Sở hữu</td><td>have (= có), own, belong, possess</td></tr>
<tr><td>Khác</td><td>seem, appear, cost, mean, contain, consist, depend, matter</td></tr>
</table>

<div class="warn"><b>⚠️ Lỗi thường gặp:</b><br>
✗ <s>I am knowing the answer.</s> → ✓ I <b>know</b> the answer.<br>
✗ <s>She is wanting a new phone.</s> → ✓ She <b>wants</b> a new phone.<br>
✗ <s>This book is belonging to me.</s> → ✓ This book <b>belongs</b> to me.<br>
✗ <s>I am understanding now.</s> → ✓ I <b>understand</b> now.</div>

<div class="note"><b>💡 Ngoại lệ quan trọng – Một số động từ có hai nghĩa:</b><br>
Khi mang nghĩa <b>hành động</b> → CÓ THỂ dùng tiếp diễn.<br>
• <b>think</b>: "I <i>think</i> he's right." (= cho rằng → trạng thái) vs "I <i>am thinking</i> about the problem." (= suy nghĩ → hành động)<br>
• <b>have</b>: "I <i>have</i> a car." (= sở hữu → trạng thái) vs "I <i>am having</i> lunch." (= ăn → hành động)<br>
• <b>see</b>: "I <i>see</i> a bird." (= nhìn thấy → trạng thái) vs "I <i>am seeing</i> the doctor tomorrow." (= gặp/hẹn → hành động)<br>
• <b>taste</b>: "This soup <i>tastes</i> delicious." (= có vị → trạng thái) vs "The chef <i>is tasting</i> the soup." (= nếm → hành động)</div>

<h3>4. Bảng so sánh: Present Simple vs Present Continuous</h3>
<table>
<tr><th></th><th>Present Simple</th><th>Present Continuous</th></tr>
<tr><td><b>Dùng khi</b></td><td>Thói quen, lặp đi lặp lại, sự thật</td><td>Đang xảy ra, tạm thời, kế hoạch</td></tr>
<tr><td><b>Dấu hiệu</b></td><td>always, usually, often, sometimes, never, every day/week, on Mondays</td><td>now, right now, at the moment, currently, today, this week, Look!, Listen!</td></tr>
<tr><td><b>Ví dụ</b></td><td>I <b>walk</b> to school every day.<br><i>(thói quen)</i></td><td>I <b>am walking</b> to school now.<br><i>(đang làm)</i></td></tr>
<tr><td><b>Ví dụ 2</b></td><td>She <b>lives</b> in Hanoi.<br><i>(nơi ở lâu dài)</i></td><td>She <b>is living</b> in Hanoi this year.<br><i>(tạm thời, năm nay)</i></td></tr>
</table>

<div class="ex"><b>So sánh hai câu:</b><br>
"He <b>drinks</b> coffee." → Anh ấy (hay) uống cà phê. (thói quen, anh ấy thích cà phê)<br>
"He <b>is drinking</b> coffee." → Anh ấy đang uống cà phê. (ngay lúc này, tại thời điểm nói)</div>

<div class="ex"><b>So sánh hai câu:</b><br>
"I <b>read</b> before bed." → Tôi đọc sách trước khi ngủ. (thói quen hàng đêm)<br>
"I <b>am reading</b> a novel by Nguyễn Nhật Ánh." → Tôi đang đọc một cuốn tiểu thuyết của NNA. (hiện tại, chưa đọc xong)</div>

<h3>5. Mẹo làm bài thi VSTEP</h3>
<div class="note"><b>💡 Chiến lược làm bài:</b><br>
<b>Bước 1:</b> Tìm dấu hiệu thời gian trong câu (every day? now? always? at the moment?).<br>
<b>Bước 2:</b> Kiểm tra chủ ngữ (He/She/It → thêm -s/-es cho hiện tại đơn).<br>
<b>Bước 3:</b> Kiểm tra động từ có phải stative verb không → nếu có, KHÔNG dùng tiếp diễn.<br>
<b>Bước 4:</b> Nếu không có dấu hiệu rõ ràng, dựa vào <b>ngữ cảnh</b>: hành động tạm thời hay lâu dài?</div>

<div class="warn"><b>⚠️ Các lỗi sai phổ biến trong đề thi:</b><br>
1. Quên thêm -s: <s>She work hard.</s> → She work<b>s</b> hard.<br>
2. Thêm -s sau doesn't: <s>He doesn't works.</s> → He doesn't work.<br>
3. Dùng tiếp diễn với stative verb: <s>I am believing you.</s> → I believe you.<br>
4. Nhầm "always" + tiếp diễn (phàn nàn) với hiện tại đơn (thói quen): "She always <b>comes</b> late." (sự thật) vs "She is always <b>coming</b> late!" (phàn nàn, bực mình)</div>
"""

# ============================================================
# UNIT 2: Past Simple & Past Continuous
# ============================================================
CONTENT[2] = """
<h3>1. Past Simple – Thì quá khứ đơn</h3>

<h4>1.1. Công thức</h4>
<table>
<tr><th>Dạng</th><th>Cấu trúc</th><th>Ví dụ</th></tr>
<tr><td>Khẳng định</td><td>S + V2/V-ed<br><i>(Cùng dạng cho tất cả ngôi)</i></td><td>I <b>visited</b> Hue last year.<br>She <b>went</b> to the market yesterday.</td></tr>
<tr><td>Phủ định</td><td>S + <b>did not (didn't)</b> + V nguyên mẫu</td><td>She <b>didn't come</b> to the party.<br>We <b>didn't know</b> the answer.</td></tr>
<tr><td>Nghi vấn</td><td><b>Did</b> + S + V nguyên mẫu?<br><i>Trả lời: Yes, S + did.<br>No, S + didn't.</i></td><td><b>Did</b> you <b>see</b> that film?<br>– Yes, I <b>did</b>.<br><b>Did</b> she <b>call</b> you?<br>– No, she <b>didn't</b>.</td></tr>
</table>

<div class="warn"><b>⚠️ Lưu ý:</b> Sau <b>did/didn't</b>, động từ luôn ở dạng <b>nguyên mẫu</b> (KHÔNG thêm -ed):<br>
✗ <s>Did you went there?</s> → ✓ Did you <b>go</b> there?<br>
✗ <s>She didn't played.</s> → ✓ She didn't <b>play</b>.</div>

<h4>1.2. Quy tắc thêm -ed cho động từ có quy tắc</h4>
<table>
<tr><th>Trường hợp</th><th>Quy tắc</th><th>Ví dụ</th></tr>
<tr><td>Hầu hết</td><td>Thêm <b>-ed</b></td><td>work → work<b>ed</b>, clean → clean<b>ed</b>, open → open<b>ed</b></td></tr>
<tr><td>Tận cùng -e</td><td>Thêm <b>-d</b></td><td>live → live<b>d</b>, arrive → arrive<b>d</b>, use → use<b>d</b></td></tr>
<tr><td>Tận cùng phụ âm + y</td><td>Đổi <b>y → ied</b></td><td>study → stud<b>ied</b>, carry → carr<b>ied</b>, try → tr<b>ied</b></td></tr>
<tr><td>Tận cùng nguyên âm + y</td><td>Thêm <b>-ed</b></td><td>play → play<b>ed</b>, enjoy → enjoy<b>ed</b>, stay → stay<b>ed</b></td></tr>
<tr><td>1 nguyên âm + 1 phụ âm (1 âm tiết / trọng âm cuối)</td><td><b>Gấp đôi</b> phụ âm cuối + <b>-ed</b></td><td>stop → sto<b>pp</b>ed, plan → pla<b>nn</b>ed, prefer → prefe<b>rr</b>ed</td></tr>
</table>

<h4>1.3. Động từ bất quy tắc thường gặp</h4>
<p>Phải <b>học thuộc</b> — không có quy tắc thêm -ed. Đây là danh sách quan trọng nhất:</p>
<table>
<tr><th>V1 (nguyên mẫu)</th><th>V2 (quá khứ)</th><th>Nghĩa</th></tr>
<tr><td>go</td><td><b>went</b></td><td>đi</td></tr>
<tr><td>come</td><td><b>came</b></td><td>đến</td></tr>
<tr><td>see</td><td><b>saw</b></td><td>nhìn thấy</td></tr>
<tr><td>take</td><td><b>took</b></td><td>lấy, mất (thời gian)</td></tr>
<tr><td>make</td><td><b>made</b></td><td>làm, tạo</td></tr>
<tr><td>buy</td><td><b>bought</b></td><td>mua</td></tr>
<tr><td>have</td><td><b>had</b></td><td>có, ăn</td></tr>
<tr><td>give</td><td><b>gave</b></td><td>cho</td></tr>
<tr><td>know</td><td><b>knew</b></td><td>biết</td></tr>
<tr><td>find</td><td><b>found</b></td><td>tìm thấy</td></tr>
<tr><td>tell</td><td><b>told</b></td><td>nói, kể</td></tr>
<tr><td>think</td><td><b>thought</b></td><td>nghĩ</td></tr>
<tr><td>get</td><td><b>got</b></td><td>nhận, trở nên</td></tr>
<tr><td>write</td><td><b>wrote</b></td><td>viết</td></tr>
<tr><td>read</td><td><b>read</b> /red/</td><td>đọc (phát âm khác!)</td></tr>
<tr><td>eat</td><td><b>ate</b></td><td>ăn</td></tr>
<tr><td>drink</td><td><b>drank</b></td><td>uống</td></tr>
<tr><td>speak</td><td><b>spoke</b></td><td>nói</td></tr>
<tr><td>put</td><td><b>put</b></td><td>đặt (không đổi)</td></tr>
<tr><td>cut</td><td><b>cut</b></td><td>cắt (không đổi)</td></tr>
</table>

<h4>1.4. Cách dùng chi tiết</h4>

<p><b>① Hành động đã xảy ra và kết thúc tại thời điểm xác định trong quá khứ</b></p>
<div class="ex">I <b>met</b> her at the station <b>yesterday</b>.<span class="vi">→ Hôm qua tôi đã gặp cô ấy ở nhà ga.</span></div>
<div class="ex">We <b>moved</b> to Ho Chi Minh City <b>in 2018</b>.<span class="vi">→ Chúng tôi chuyển đến TP.HCM năm 2018.</span></div>
<div class="ex">She <b>graduated</b> from university <b>last June</b>.<span class="vi">→ Cô ấy tốt nghiệp đại học tháng 6 năm ngoái.</span></div>
<div class="ex"><b>Did</b> you <b>watch</b> the football match <b>last night</b>?<span class="vi">→ Tối qua bạn có xem trận bóng không?</span></div>

<p><b>② Chuỗi hành động nối tiếp nhau trong quá khứ</b></p>
<div class="ex">He <b>came</b> home, <b>had</b> dinner and <b>went</b> to bed.<span class="vi">→ Anh ấy về nhà, ăn tối rồi đi ngủ. (lần lượt, hết hành động này mới đến hành động kia)</span></div>
<div class="ex">I <b>woke</b> up, <b>brushed</b> my teeth, <b>got dressed</b> and <b>left</b> the house.<span class="vi">→ Tôi thức dậy, đánh răng, mặc quần áo rồi rời khỏi nhà.</span></div>

<p><b>③ Thói quen trong quá khứ (không còn ở hiện tại)</b></p>
<div class="ex">When I was young, I <b>played</b> football every weekend.<span class="vi">→ Khi tôi còn nhỏ, tôi chơi bóng đá mỗi cuối tuần. (bây giờ không chơi nữa)</span></div>

<h4>1.5. Dấu hiệu nhận biết</h4>
<p><i>yesterday, last night/week/month/year, ago (two days ago, a long time ago), in 2010, when I was young, at that time, the other day.</i></p>

<h3>2. Past Continuous – Thì quá khứ tiếp diễn</h3>

<h4>2.1. Công thức</h4>
<table>
<tr><th>Dạng</th><th>Cấu trúc</th><th>Ví dụ</th></tr>
<tr><td>Khẳng định</td><td>S + <b>was/were</b> + V-ing<br><i>I/He/She/It + was</i><br><i>You/We/They + were</i></td><td>I <b>was cooking</b> at 7 p.m.<br>They <b>were watching</b> TV.</td></tr>
<tr><td>Phủ định</td><td>S + was/were + <b>not</b> + V-ing</td><td>She <b>wasn't listening</b>.<br>We <b>weren't playing</b>.</td></tr>
<tr><td>Nghi vấn</td><td><b>Was/Were</b> + S + V-ing?</td><td><b>Were</b> you <b>sleeping</b> when I called?<br>– Yes, I <b>was</b>.</td></tr>
</table>

<h4>2.2. Cách dùng chi tiết</h4>

<p><b>① Hành động đang diễn ra tại một thời điểm cụ thể trong quá khứ</b></p>
<div class="ex">At 8 o'clock last night, I <b>was studying</b> for the exam.<span class="vi">→ Lúc 8 giờ tối qua, tôi đang ôn thi.</span></div>
<div class="ex">This time yesterday, we <b>were sitting</b> on the beach.<span class="vi">→ Giờ này ngày hôm qua, chúng tôi đang ngồi trên bãi biển.</span></div>

<p><b>② Hành động đang diễn ra thì bị hành động khác cắt ngang</b></p>
<p>Hành động <b>dài</b> (đang diễn ra) → Past Continuous. Hành động <b>ngắn</b> (cắt ngang) → Past Simple.</p>
<div class="ex">I <b>was watching</b> TV <b>when</b> the phone <b>rang</b>.<span class="vi">→ Tôi đang xem TV thì điện thoại reo.</span></div>
<div class="ex">She <b>was crossing</b> the street <b>when</b> she <b>saw</b> an old friend.<span class="vi">→ Cô ấy đang qua đường thì nhìn thấy một người bạn cũ.</span></div>
<div class="ex"><b>While</b> I <b>was taking</b> a shower, someone <b>knocked</b> on the door.<span class="vi">→ Trong khi tôi đang tắm, có ai đó gõ cửa.</span></div>

<p><b>③ Hai hành động diễn ra song song cùng lúc</b></p>
<div class="ex"><b>While</b> I <b>was cooking</b>, my husband <b>was cleaning</b> the house.<span class="vi">→ Trong khi tôi nấu ăn thì chồng tôi dọn nhà.</span></div>
<div class="ex">The children <b>were playing</b> in the garden <b>while</b> their parents <b>were talking</b> inside.<span class="vi">→ Bọn trẻ đang chơi trong vườn trong khi bố mẹ chúng đang nói chuyện bên trong.</span></div>

<p><b>④ Miêu tả bối cảnh, khung cảnh trong câu chuyện</b></p>
<div class="ex">It <b>was raining</b> heavily. The wind <b>was blowing</b>. Nobody <b>was walking</b> on the street.<span class="vi">→ Trời đang mưa tầm tã. Gió đang thổi. Không ai đang đi trên đường. (dựng bối cảnh)</span></div>

<h3>3. Phân biệt when vs while</h3>
<table>
<tr><th>Từ nối</th><th>Đi với thì gì</th><th>Giải thích</th></tr>
<tr><td><b>when</b></td><td>Thường + Past Simple</td><td>Hành động ngắn, cắt ngang<br>"Khi" (tại thời điểm đó)</td></tr>
<tr><td><b>while</b></td><td>Thường + Past Continuous</td><td>Hành động dài, đang diễn ra<br>"Trong khi" (suốt quãng thời gian)</td></tr>
</table>

<div class="note"><b>💡 Công thức vàng — học thuộc 3 pattern này:</b><br>
<b>Pattern 1:</b> While + S1 + was/were + V-ing, S2 + V-ed. (đang làm gì thì bị cắt ngang)<br>
→ <i>While I was sleeping, the alarm went off.</i><br><br>
<b>Pattern 2:</b> S1 + was/were + V-ing + when + S2 + V-ed. (giống Pattern 1 nhưng đảo vế)<br>
→ <i>I was sleeping when the alarm went off.</i><br><br>
<b>Pattern 3:</b> While + S1 + was/were + V-ing, S2 + was/were + V-ing. (hai hành động song song)<br>
→ <i>While Mom was cooking, Dad was watching TV.</i></div>

<h3>4. Bảng so sánh: Past Simple vs Past Continuous</h3>
<table>
<tr><th></th><th>Past Simple</th><th>Past Continuous</th></tr>
<tr><td><b>Khi nào dùng</b></td><td>Hành động đã hoàn tất, kết thúc</td><td>Hành động đang diễn ra ở một thời điểm</td></tr>
<tr><td><b>Dấu hiệu</b></td><td>yesterday, last..., ago, in 2020</td><td>at that time, at 8 o'clock yesterday, while, when</td></tr>
<tr><td><b>Hai hành động nối tiếp</b></td><td>Cả hai Past Simple<br><i>I came in and sat down.</i></td><td>—</td></tr>
<tr><td><b>Cắt ngang</b></td><td>Hành động ngắn (cắt ngang)</td><td>Hành động dài (đang diễn ra)</td></tr>
<tr><td><b>Song song</b></td><td>—</td><td>Cả hai Past Continuous<br><i>While A was ..., B was ...</i></td></tr>
</table>

<h3>5. Mẹo làm bài thi VSTEP</h3>
<div class="note"><b>💡 Chiến lược:</b><br>
<b>1.</b> Thấy "when" → khả năng cao mệnh đề "when" dùng Past Simple (hành động ngắn).<br>
<b>2.</b> Thấy "while" → khả năng cao dùng Past Continuous (hành động dài).<br>
<b>3.</b> Chuỗi hành động nối tiếp (and, then) → tất cả Past Simple.<br>
<b>4.</b> Miêu tả bối cảnh, khung cảnh → Past Continuous.<br>
<b>5.</b> Thấy mốc thời gian xác định (yesterday, last year, in 2020) + hành động hoàn tất → Past Simple.</div>

<div class="warn"><b>⚠️ Lỗi thường gặp:</b><br>
1. Nhầm was/were: <s>They was playing.</s> → They <b>were</b> playing. (They → were)<br>
2. Dùng Past Continuous cho hành động hoàn tất: <s>I was going to school yesterday.</s> → I <b>went</b> to school yesterday. (đã đi xong → Past Simple)<br>
3. Quên dạng bất quy tắc: <s>I goed there.</s> → I <b>went</b> there.</div>
"""

# ============================================================
# UNIT 3: Present Perfect & Present Perfect Continuous
# ============================================================
CONTENT[3] = """
<h3>1. Present Perfect – Thì hiện tại hoàn thành</h3>

<h4>1.1. Công thức</h4>
<table>
<tr><th>Dạng</th><th>Cấu trúc</th><th>Ví dụ</th></tr>
<tr><td>Khẳng định</td><td>S + <b>have/has</b> + V3 (past participle)<br><i>I/You/We/They + have</i><br><i>He/She/It + has</i></td><td>I <b>have finished</b> my homework.<br>She <b>has visited</b> Japan twice.</td></tr>
<tr><td>Phủ định</td><td>S + have/has + <b>not</b> + V3<br><i>haven't / hasn't</i></td><td>I <b>haven't seen</b> that film.<br>He <b>hasn't called</b> me yet.</td></tr>
<tr><td>Nghi vấn</td><td><b>Have/Has</b> + S + V3?</td><td><b>Have</b> you ever <b>been</b> to Hanoi?<br>– Yes, I <b>have</b>. / No, I <b>haven't</b>.<br><b>Has</b> she <b>finished</b> yet?</td></tr>
</table>

<h4>1.2. V3 (Past Participle) – Quá khứ phân từ</h4>
<p>Với động từ <b>có quy tắc</b>: V3 = V-ed (giống V2). Ví dụ: worked, played, visited.<br>
Với động từ <b>bất quy tắc</b>: phải học thuộc riêng.</p>
<table>
<tr><th>V1</th><th>V2</th><th>V3</th><th>Nghĩa</th></tr>
<tr><td>go</td><td>went</td><td><b>gone</b></td><td>đi</td></tr>
<tr><td>see</td><td>saw</td><td><b>seen</b></td><td>thấy</td></tr>
<tr><td>do</td><td>did</td><td><b>done</b></td><td>làm</td></tr>
<tr><td>eat</td><td>ate</td><td><b>eaten</b></td><td>ăn</td></tr>
<tr><td>write</td><td>wrote</td><td><b>written</b></td><td>viết</td></tr>
<tr><td>speak</td><td>spoke</td><td><b>spoken</b></td><td>nói</td></tr>
<tr><td>take</td><td>took</td><td><b>taken</b></td><td>lấy</td></tr>
<tr><td>give</td><td>gave</td><td><b>given</b></td><td>cho</td></tr>
<tr><td>be</td><td>was/were</td><td><b>been</b></td><td>là, ở</td></tr>
<tr><td>have</td><td>had</td><td><b>had</b></td><td>có</td></tr>
<tr><td>know</td><td>knew</td><td><b>known</b></td><td>biết</td></tr>
<tr><td>break</td><td>broke</td><td><b>broken</b></td><td>vỡ</td></tr>
<tr><td>choose</td><td>chose</td><td><b>chosen</b></td><td>chọn</td></tr>
<tr><td>forget</td><td>forgot</td><td><b>forgotten</b></td><td>quên</td></tr>
</table>

<h4>1.3. Cách dùng chi tiết</h4>

<p><b>① Kinh nghiệm — đã từng / chưa từng (không nói rõ khi nào)</b></p>
<p>Thường dùng với: <i>ever, never, before, once, twice, three times, many times.</i></p>
<div class="ex">I <b>have never eaten</b> sushi before.<span class="vi">→ Tôi chưa bao giờ ăn sushi.</span></div>
<div class="ex"><b>Have</b> you ever <b>been</b> to a foreign country?<span class="vi">→ Bạn đã bao giờ đến nước ngoài chưa?</span></div>
<div class="ex">She <b>has visited</b> Paris <b>three times</b>.<span class="vi">→ Cô ấy đã đến Paris ba lần rồi.</span></div>
<div class="ex">This is the best book I <b>have ever read</b>.<span class="vi">→ Đây là cuốn sách hay nhất mà tôi từng đọc.</span></div>

<p><b>② Hành động vừa mới xảy ra</b></p>
<p>Thường dùng với: <i>just, recently, lately.</i></p>
<div class="ex">We <b>have just finished</b> the report.<span class="vi">→ Chúng tôi vừa hoàn thành bản báo cáo.</span></div>
<div class="ex">He <b>has recently moved</b> to a new apartment.<span class="vi">→ Anh ấy mới chuyển đến một căn hộ mới.</span></div>
<div class="ex">I <b>have just had</b> lunch, so I'm not hungry.<span class="vi">→ Tôi vừa ăn trưa xong nên không đói.</span></div>

<p><b>③ Đã làm / chưa làm (kết quả ở hiện tại)</b></p>
<p>Thường dùng với: <i>already (đã rồi — khẳng định), yet (chưa — phủ định/nghi vấn).</i></p>
<div class="ex">I <b>have already done</b> my homework.<span class="vi">→ Tôi đã làm bài tập rồi. (đừng hỏi nữa)</span></div>
<div class="ex">She <b>hasn't replied</b> to my email <b>yet</b>.<span class="vi">→ Cô ấy vẫn chưa trả lời email của tôi.</span></div>
<div class="ex"><b>Have</b> you <b>finished</b> your project <b>yet</b>?<span class="vi">→ Bạn đã làm xong dự án chưa?</span></div>
<div class="note"><b>💡 Vị trí:</b> <b>already</b> đứng <b>giữa</b> have và V3 (hoặc cuối câu). <b>yet</b> đứng <b>cuối</b> câu phủ định/nghi vấn.</div>

<p><b>④ Hành động bắt đầu trong quá khứ, kéo dài đến hiện tại</b></p>
<p>Thường dùng với: <i>for + khoảng thời gian, since + mốc thời gian.</i></p>
<div class="ex">She <b>has lived</b> here <b>since 2015</b>.<span class="vi">→ Cô ấy sống ở đây từ năm 2015 (và vẫn đang sống).</span></div>
<div class="ex">I <b>have known</b> him <b>for ten years</b>.<span class="vi">→ Tôi đã quen anh ấy được mười năm rồi.</span></div>
<div class="ex">They <b>have been</b> married <b>since 2010</b>.<span class="vi">→ Họ kết hôn từ năm 2010 (vẫn đang cưới).</span></div>

<h4>1.4. for vs since</h4>
<table>
<tr><th>for + khoảng thời gian</th><th>since + mốc thời gian</th></tr>
<tr><td>for three years (3 năm)</td><td>since 2020 (từ năm 2020)</td></tr>
<tr><td>for a long time (lâu rồi)</td><td>since last Monday (từ thứ Hai tuần trước)</td></tr>
<tr><td>for two hours (2 tiếng)</td><td>since 8 o'clock (từ lúc 8 giờ)</td></tr>
<tr><td>for ages (lâu lắm rồi)</td><td>since I was a child (từ khi tôi còn nhỏ)</td></tr>
<tr><td>for six months (6 tháng)</td><td>since she moved here (từ khi cô ấy chuyển đến đây)</td></tr>
</table>

<h3>2. Present Perfect Continuous – Hiện tại hoàn thành tiếp diễn</h3>

<h4>2.1. Công thức</h4>
<table>
<tr><th>Dạng</th><th>Cấu trúc</th><th>Ví dụ</th></tr>
<tr><td>Khẳng định</td><td>S + <b>have/has been</b> + V-ing</td><td>I <b>have been waiting</b> for 2 hours.</td></tr>
<tr><td>Phủ định</td><td>S + have/has + <b>not been</b> + V-ing</td><td>She <b>hasn't been sleeping</b> well.</td></tr>
<tr><td>Nghi vấn</td><td><b>Have/Has</b> + S + <b>been</b> + V-ing?</td><td><b>Have</b> you <b>been studying</b> all day?</td></tr>
</table>

<h4>2.2. Cách dùng</h4>
<p>Nhấn mạnh <b>quá trình kéo dài</b>, thường thấy <b>kết quả ở hiện tại</b> (mệt, ướt, đói, vui...).</p>

<div class="ex">I <b>have been waiting</b> for you for two hours!<span class="vi">→ Tôi đã đợi bạn suốt 2 tiếng rồi đấy! (nhấn mạnh quá trình dài, hơi trách móc)</span></div>
<div class="ex">Her eyes are red. She <b>has been crying</b>.<span class="vi">→ Mắt cô ấy đỏ. Cô ấy vừa khóc (suốt nãy giờ). (kết quả nhìn thấy ở hiện tại)</span></div>
<div class="ex">You look tired. <b>Have</b> you <b>been working</b> all night?<span class="vi">→ Trông bạn mệt quá. Bạn làm việc cả đêm à?</span></div>
<div class="ex">The ground is wet. It <b>has been raining</b>.<span class="vi">→ Mặt đất ướt. Trời vừa mưa (suốt nãy giờ).</span></div>
<div class="ex">I <b>have been studying</b> English <b>for five years</b>.<span class="vi">→ Tôi đã học tiếng Anh được 5 năm rồi. (vẫn đang học, nhấn mạnh quá trình)</span></div>

<h3>3. Phân biệt Present Perfect vs Present Perfect Continuous</h3>
<table>
<tr><th></th><th>Present Perfect</th><th>Present Perfect Continuous</th></tr>
<tr><td><b>Nhấn mạnh</b></td><td><b>Kết quả</b>, hoàn thành</td><td><b>Quá trình</b>, thời gian kéo dài</td></tr>
<tr><td><b>Ví dụ</b></td><td>I <b>have read</b> three books this month.<br><i>(nhấn mạnh: đọc xong 3 cuốn)</i></td><td>I <b>have been reading</b> this book for a week.<br><i>(nhấn mạnh: đọc suốt 1 tuần, chưa xong)</i></td></tr>
<tr><td><b>Ví dụ 2</b></td><td>She <b>has written</b> five emails today.<br><i>(5 email đã xong)</i></td><td>She <b>has been writing</b> emails all morning.<br><i>(viết suốt sáng, nhấn mạnh thời gian)</i></td></tr>
</table>

<h3>4. Phân biệt Present Perfect vs Past Simple</h3>
<table>
<tr><th>Present Perfect</th><th>Past Simple</th></tr>
<tr><td><b>KHÔNG</b> nói rõ thời điểm, hoặc còn liên quan đến hiện tại</td><td>Thời điểm <b>xác định</b>, đã kết thúc hoàn toàn</td></tr>
<tr><td>I <b>have lost</b> my key.<br><i>(giờ vẫn chưa tìm thấy → ảnh hưởng hiện tại)</i></td><td>I <b>lost</b> my key <b>yesterday</b>.<br><i>(hôm qua, có thể đã tìm thấy rồi)</i></td></tr>
<tr><td><b>Have</b> you ever <b>been</b> to Da Lat?<br><i>(kinh nghiệm, không hỏi khi nào)</i></td><td><b>Did</b> you <b>go</b> to Da Lat <b>last summer</b>?<br><i>(hỏi cụ thể: hè năm ngoái)</i></td></tr>
<tr><td>I <b>have lived</b> here <b>for 5 years</b>.<br><i>(bắt đầu 5 năm trước, vẫn đang ở)</i></td><td>I <b>lived</b> there <b>for 5 years</b>.<br><i>(đã sống 5 năm, giờ không ở nữa)</i></td></tr>
</table>

<div class="warn"><b>⚠️ Lỗi cực phổ biến:</b> KHÔNG dùng Present Perfect với thời điểm xác định!<br>
✗ <s>I have seen him yesterday.</s> → ✓ I <b>saw</b> him yesterday.<br>
✗ <s>She has gone to Paris last year.</s> → ✓ She <b>went</b> to Paris last year.<br>
✗ <s>Have you eaten breakfast this morning?</s> (nếu bây giờ là buổi chiều → sáng đã qua) → ✓ <b>Did</b> you eat breakfast this morning?<br>
Nhưng: <b>Have</b> you eaten breakfast? (nếu bây giờ vẫn là buổi sáng → vẫn liên quan) → ✓</div>

<h3>5. Mẹo làm bài thi VSTEP</h3>
<div class="note"><b>💡 Chiến lược:</b><br>
<b>1.</b> Thấy <b>just, already, yet, ever, never, recently, so far, up to now</b> → Present Perfect.<br>
<b>2.</b> Thấy <b>for, since</b> + nhấn mạnh quá trình → Present Perfect Continuous; nhấn mạnh kết quả → Present Perfect.<br>
<b>3.</b> Thấy <b>yesterday, last..., ago, in 2020</b> → Past Simple (KHÔNG dùng Present Perfect!).<br>
<b>4.</b> Câu "This is the first/best/worst... I have ever..." → Present Perfect.<br>
<b>5.</b> Câu "How long have you...?" → Present Perfect hoặc Present Perfect Continuous.</div>
"""

# ============================================================
# UNIT 4: Past Perfect & used to
# ============================================================
CONTENT[4] = """
<h3>1. Past Perfect – Thì quá khứ hoàn thành</h3>

<h4>1.1. Công thức</h4>
<table>
<tr><th>Dạng</th><th>Cấu trúc</th><th>Ví dụ</th></tr>
<tr><td>Khẳng định</td><td>S + <b>had</b> + V3<br><i>(Cùng dạng cho tất cả ngôi)</i></td><td>I <b>had finished</b> dinner before she arrived.</td></tr>
<tr><td>Phủ định</td><td>S + <b>had not (hadn't)</b> + V3</td><td>They <b>hadn't seen</b> each other for years.</td></tr>
<tr><td>Nghi vấn</td><td><b>Had</b> + S + V3?</td><td><b>Had</b> you <b>met</b> him before the party?<br>– Yes, I <b>had</b>. / No, I <b>hadn't</b>.</td></tr>
</table>

<h4>1.2. Khi nào dùng Past Perfect?</h4>
<p>Dùng khi có <b>hai sự việc trong quá khứ</b> và bạn muốn nói rõ <b>sự việc nào xảy ra trước</b>.</p>
<p>Hãy tưởng tượng "quá khứ của quá khứ" — hành động xảy ra <b>trước</b> một hành động khác trong quá khứ.</p>

<table>
<tr><th>Thứ tự thời gian</th><th>Hành động 1 (xảy ra trước)</th><th>Hành động 2 (xảy ra sau)</th></tr>
<tr><td></td><td><b>Past Perfect</b> (had + V3)</td><td><b>Past Simple</b> (V2/V-ed)</td></tr>
</table>

<p><b>① Hành động xảy ra trước một hành động khác trong quá khứ</b></p>
<div class="ex">When I <b>arrived</b> at the cinema, the film <b>had already started</b>.<span class="vi">→ Khi tôi đến rạp, phim đã bắt đầu rồi. (phim bắt đầu TRƯỚC, tôi đến SAU)</span></div>
<div class="ex">She <b>had left</b> the office before I <b>got</b> there.<span class="vi">→ Cô ấy đã rời văn phòng trước khi tôi đến đó. (rời đi TRƯỚC, tôi đến SAU)</span></div>
<div class="ex">I <b>didn't have</b> any money because I <b>had lost</b> my wallet.<span class="vi">→ Tôi không có tiền vì tôi đã mất ví. (mất ví TRƯỚC → không có tiền SAU)</span></div>
<div class="ex">He <b>was</b> very tired because he <b>had worked</b> all day.<span class="vi">→ Anh ấy rất mệt vì đã làm việc cả ngày. (làm việc TRƯỚC → mệt SAU)</span></div>

<p><b>② Với before, after, by the time</b></p>
<div class="ex">I <b>had finished</b> my homework <b>before</b> Mom <b>came</b> home.<span class="vi">→ Tôi đã làm xong bài tập trước khi mẹ về nhà.</span></div>
<div class="ex"><b>After</b> she <b>had eaten</b> dinner, she <b>went</b> for a walk.<span class="vi">→ Sau khi ăn tối xong, cô ấy đi dạo.</span></div>
<div class="ex"><b>By the time</b> we <b>arrived</b>, the concert <b>had ended</b>.<span class="vi">→ Đến lúc chúng tôi đến nơi, buổi hòa nhạc đã kết thúc rồi.</span></div>

<p><b>③ Lần đầu tiên làm gì (It was the first time...)</b></p>
<div class="ex">It was the first time I <b>had flown</b> on an airplane.<span class="vi">→ Đó là lần đầu tiên tôi đi máy bay.</span></div>
<div class="ex">It was the most beautiful place she <b>had ever seen</b>.<span class="vi">→ Đó là nơi đẹp nhất mà cô ấy từng thấy (tính đến thời điểm đó).</span></div>

<div class="note"><b>💡 Khi nào KHÔNG cần Past Perfect?</b><br>
Nếu thứ tự thời gian đã rõ ràng (nhờ before, after, then...) và không gây nhầm lẫn, bạn CÓ THỂ dùng Past Simple cho cả hai.<br>
"I had lunch and <b>then</b> went to work." = "I had lunch and then went to work." (cả hai đều OK)<br>
Nhưng nếu muốn nhấn mạnh hành động hoàn tất trước, nên dùng Past Perfect.</div>

<h3>2. Used to / Would – Thói quen trong quá khứ</h3>

<h4>2.1. Used to + V</h4>
<table>
<tr><th>Dạng</th><th>Cấu trúc</th><th>Ví dụ</th></tr>
<tr><td>Khẳng định</td><td>S + <b>used to</b> + V</td><td>I <b>used to play</b> football. (Tôi từng chơi bóng đá.)</td></tr>
<tr><td>Phủ định</td><td>S + <b>didn't use to</b> + V</td><td>She <b>didn't use to like</b> coffee. (Cô ấy trước đây không thích cà phê.)</td></tr>
<tr><td>Nghi vấn</td><td><b>Did</b> + S + <b>use to</b> + V?</td><td><b>Did</b> you <b>use to</b> live in Hanoi? (Bạn trước đây sống ở HN à?)</td></tr>
</table>

<p>Diễn tả <b>thói quen hoặc trạng thái</b> trong quá khứ mà <b>bây giờ không còn nữa</b>.</p>

<div class="ex">I <b>used to smoke</b>, but I quit three years ago.<span class="vi">→ Tôi từng hút thuốc, nhưng tôi bỏ cách đây 3 năm. (bây giờ không hút nữa)</span></div>
<div class="ex">There <b>used to be</b> a cinema here, but now it's a parking lot.<span class="vi">→ Ở đây từng có một rạp chiếu phim, nhưng giờ là bãi đỗ xe.</span></div>
<div class="ex">She <b>didn't use to like</b> vegetables, but now she eats them every day.<span class="vi">→ Cô ấy trước đây không thích rau, nhưng giờ cô ấy ăn mỗi ngày.</span></div>
<div class="ex">We <b>used to walk</b> to school when we were children.<span class="vi">→ Chúng tôi từng đi bộ đến trường khi còn nhỏ.</span></div>

<h4>2.2. Phân biệt: used to vs would vs Past Simple</h4>
<table>
<tr><th>Cấu trúc</th><th>Dùng cho</th><th>Ví dụ</th></tr>
<tr><td><b>used to</b></td><td>Thói quen HOẶC trạng thái quá khứ (không còn nữa)</td><td>I <b>used to live</b> in Hanoi. (trạng thái)<br>I <b>used to play</b> football. (thói quen)</td></tr>
<tr><td><b>would</b></td><td>CHỈ thói quen quá khứ (không dùng cho trạng thái)</td><td>Every summer, we <b>would go</b> to the beach.<br>✗ <s>I would live in Hanoi.</s> (trạng thái → sai)</td></tr>
<tr><td><b>Past Simple</b></td><td>Hành động cụ thể tại thời điểm xác định</td><td>I <b>played</b> football yesterday.</td></tr>
</table>

<div class="warn"><b>⚠️ Phân biệt 3 cấu trúc dễ nhầm:</b><br>
• <b>used to + V</b>: "I used to play tennis." (từng chơi, giờ không nữa)<br>
• <b>be used to + V-ing</b>: "I am used to waking up early." (đã quen với việc dậy sớm — hiện tại)<br>
• <b>get used to + V-ing</b>: "I'm getting used to the new job." (đang dần quen với công việc mới)<br>
→ Đề thi VSTEP rất hay hỏi sự khác biệt này!</div>

<h3>3. Mẹo làm bài thi VSTEP</h3>
<div class="note"><b>💡 Chiến lược:</b><br>
<b>1.</b> Thấy <b>before, after, by the time, already</b> + hai hành động quá khứ → hành động xảy ra trước dùng <b>Past Perfect</b>.<br>
<b>2.</b> Thấy <b>"It was the first time..."</b> → Past Perfect.<br>
<b>3.</b> Thấy <b>"used to"</b> → thói quen/trạng thái quá khứ không còn nữa.<br>
<b>4.</b> Phân biệt <b>"used to + V"</b> vs <b>"be used to + V-ing"</b> → rất hay ra trong đề!</div>
"""

# ============================================================
# UNIT 5: Future Forms
# ============================================================
CONTENT[5] = """
<h3>1. Will – Tương lai đơn</h3>

<h4>1.1. Công thức</h4>
<table>
<tr><th>Dạng</th><th>Cấu trúc</th><th>Ví dụ</th></tr>
<tr><td>Khẳng định</td><td>S + <b>will ('ll)</b> + V nguyên mẫu</td><td>I <b>will help</b> you. / I<b>'ll help</b> you.</td></tr>
<tr><td>Phủ định</td><td>S + <b>will not (won't)</b> + V</td><td>She <b>won't come</b> to the party.</td></tr>
<tr><td>Nghi vấn</td><td><b>Will</b> + S + V?</td><td><b>Will</b> you <b>be</b> there tomorrow?</td></tr>
</table>

<h4>1.2. Cách dùng</h4>

<p><b>① Quyết định tại chỗ, ngay lúc nói</b></p>
<div class="ex">A: "It's cold in here." — B: "I<b>'ll close</b> the window."<span class="vi">→ A: "Ở đây lạnh quá." — B: "Tôi sẽ đóng cửa sổ." (quyết định ngay lúc nói)</span></div>
<div class="ex">A: "I don't have a pen." — B: "Wait, I<b>'ll lend</b> you mine."<span class="vi">→ A: "Tôi không có bút." — B: "Đợi chút, tôi cho bạn mượn."</span></div>

<p><b>② Dự đoán (không có bằng chứng cụ thể, dựa vào cảm giác/ý kiến)</b></p>
<div class="ex">I think it <b>will rain</b> tomorrow.<span class="vi">→ Tôi nghĩ ngày mai trời sẽ mưa. (ý kiến cá nhân)</span></div>
<div class="ex">She <b>will probably pass</b> the exam. She's very smart.<span class="vi">→ Cô ấy có lẽ sẽ đỗ. Cô ấy rất thông minh.</span></div>

<p><b>③ Lời hứa, đề nghị, đe dọa</b></p>
<div class="ex">I <b>will always love</b> you. (lời hứa)<span class="vi">→ Anh sẽ luôn yêu em.</span></div>
<div class="ex"><b>Will</b> you <b>help</b> me with this? (yêu cầu lịch sự)<span class="vi">→ Bạn giúp tôi việc này được không?</span></div>
<div class="ex">If you don't study, you <b>will fail</b>. (cảnh báo)<span class="vi">→ Nếu bạn không học, bạn sẽ trượt.</span></div>

<h3>2. Be going to – Dự định, kế hoạch</h3>

<h4>2.1. Công thức</h4>
<table>
<tr><th>Dạng</th><th>Cấu trúc</th><th>Ví dụ</th></tr>
<tr><td>Khẳng định</td><td>S + <b>am/is/are going to</b> + V</td><td>I <b>am going to study</b> abroad next year.</td></tr>
<tr><td>Phủ định</td><td>S + am/is/are + <b>not going to</b> + V</td><td>She <b>isn't going to buy</b> a new car.</td></tr>
<tr><td>Nghi vấn</td><td><b>Am/Is/Are</b> + S + <b>going to</b> + V?</td><td><b>Are</b> you <b>going to travel</b> this summer?</td></tr>
</table>

<h4>2.2. Cách dùng</h4>

<p><b>① Dự định, kế hoạch đã nghĩ trước (nhưng chưa sắp xếp cụ thể)</b></p>
<div class="ex">I <b>am going to learn</b> Japanese next year.<span class="vi">→ Năm sau tôi định học tiếng Nhật. (đã nghĩ từ trước, nhưng chưa đăng ký lớp)</span></div>
<div class="ex">They <b>are going to move</b> to a bigger house.<span class="vi">→ Họ định chuyển đến nhà lớn hơn.</span></div>

<p><b>② Dự đoán dựa trên bằng chứng hiện tại (nhìn thấy, biết chắc)</b></p>
<div class="ex">Look at those dark clouds! It <b>is going to rain</b>.<span class="vi">→ Nhìn mây đen kia kìa! Trời sắp mưa. (bằng chứng: mây đen)</span></div>
<div class="ex">She hasn't studied at all. She <b>is going to fail</b> the exam.<span class="vi">→ Cô ấy không học gì cả. Cô ấy sẽ trượt. (bằng chứng: không học)</span></div>
<div class="ex">Be careful! You <b>are going to drop</b> those plates!<span class="vi">→ Cẩn thận! Bạn sắp làm rơi mấy cái đĩa! (nhìn thấy sắp rơi)</span></div>

<h3>3. Present Continuous cho tương lai</h3>
<p>Dùng khi đã có <b>sắp xếp cụ thể</b>: đã đặt vé, đã hẹn giờ, đã book phòng...</p>
<div class="ex">I <b>am meeting</b> the doctor at 3 p.m. tomorrow.<span class="vi">→ Ngày mai tôi gặp bác sĩ lúc 3 giờ chiều. (đã hẹn lịch)</span></div>
<div class="ex">We <b>are flying</b> to Singapore next Friday.<span class="vi">→ Thứ Sáu tuần sau chúng tôi bay đi Singapore. (đã đặt vé)</span></div>
<div class="ex">She <b>is having</b> dinner with her boss tonight.<span class="vi">→ Tối nay cô ấy ăn tối với sếp. (đã sắp xếp)</span></div>

<h3>4. Bảng so sánh 3 cách diễn đạt tương lai</h3>
<table>
<tr><th></th><th>will</th><th>be going to</th><th>Present Continuous</th></tr>
<tr><td><b>Khi nào</b></td><td>Quyết định tại chỗ<br>Dự đoán (ý kiến)<br>Lời hứa</td><td>Dự định đã nghĩ trước<br>Dự đoán (có bằng chứng)</td><td>Đã sắp xếp cụ thể<br>(đặt vé, hẹn lịch)</td></tr>
<tr><td><b>Ví dụ</b></td><td>"I<b>'ll call</b> you later."<br><i>(vừa quyết định)</i></td><td>"I<b>'m going to call</b> her."<br><i>(đã tính từ trước)</i></td><td>"I<b>'m calling</b> her at 5."<br><i>(đã hẹn giờ cụ thể)</i></td></tr>
<tr><td><b>Dự đoán</b></td><td>"I think she <b>will</b> win."<br><i>(ý kiến)</i></td><td>"Look, she<b>'s going to</b> win!"<br><i>(bằng chứng: đang dẫn trước)</i></td><td>—</td></tr>
</table>

<div class="ex"><b>So sánh 3 câu:</b><br>
"I<b>'ll buy</b> a new laptop." → Tôi sẽ mua (vừa quyết định, tại chỗ).<br>
"I<b>'m going to buy</b> a new laptop." → Tôi định mua (đã nghĩ từ trước).<br>
"I<b>'m buying</b> a new laptop tomorrow." → Ngày mai tôi mua (đã đặt hàng/hẹn mua).</div>

<h3>5. Present Simple cho tương lai</h3>
<p>Dùng cho <b>lịch trình, thời gian biểu cố định</b> (tàu, máy bay, lớp học, phim...):</p>
<div class="ex">The train <b>leaves</b> at 8:30 a.m.<span class="vi">→ Tàu khởi hành lúc 8:30 sáng. (lịch trình cố định)</span></div>
<div class="ex">The exam <b>starts</b> at 9 o'clock next Monday.<span class="vi">→ Kỳ thi bắt đầu lúc 9 giờ thứ Hai tuần sau.</span></div>

<h3>6. Mẹo làm bài thi VSTEP</h3>
<div class="note"><b>💡 Chiến lược:</b><br>
<b>1.</b> "I think / I'm sure / probably" → <b>will</b> (dự đoán theo ý kiến).<br>
<b>2.</b> "Look! / The sky is dark / She's very tired" → <b>be going to</b> (bằng chứng).<br>
<b>3.</b> Đã có lịch hẹn, vé, booking → <b>Present Continuous</b>.<br>
<b>4.</b> Lịch tàu/máy bay/trường → <b>Present Simple</b>.<br>
<b>5.</b> Quyết định ngay lúc nói ("Wait, I'll..." / "OK, I'll...") → <b>will</b>.</div>

<div class="warn"><b>⚠️ Lỗi thường gặp:</b><br>
✗ <s>I will go to buy a laptop. I decided last week.</s> (đã quyết định từ trước → không dùng will)<br>
✓ I <b>am going to</b> buy a laptop. I decided last week.<br><br>
✗ <s>Look at the clouds! It will rain.</s> (có bằng chứng → không dùng will)<br>
✓ Look at the clouds! It <b>is going to</b> rain.</div>
"""

# Apply updates
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
    except GrammarLesson.DoesNotExist:
        print(f"✗ Unit {order} has no lesson")

print(f"\nDone! Updated {len(CONTENT)} units.")
