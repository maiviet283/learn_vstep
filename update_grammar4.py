"""
Script to update grammar lesson content - Units 15-18.
"""
import os, sys, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vstep.settings')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
django.setup()

from learning.models import Unit, GrammarLesson

CONTENT = {}

# ============================================================
# UNIT 15: Prepositions of Time & Place
# ============================================================
CONTENT[15] = """
<h3>1. Giới từ chỉ thời gian: in, on, at</h3>

<table>
<tr><th>Giới từ</th><th>Dùng với</th><th>Ví dụ</th></tr>
<tr><td rowspan="4"><b>AT</b><br>(điểm cụ thể)</td><td>Giờ cụ thể</td><td><b>at</b> 7 o'clock, <b>at</b> 3:30 p.m.</td></tr>
<tr><td>Bữa ăn</td><td><b>at</b> breakfast, <b>at</b> lunchtime</td></tr>
<tr><td>Cụm cố định</td><td><b>at</b> night, <b>at</b> the weekend (BrE), <b>at</b> the moment, <b>at</b> the same time</td></tr>
<tr><td>Ngày lễ (khoảng thời gian)</td><td><b>at</b> Christmas, <b>at</b> Easter, <b>at</b> Tet</td></tr>
<tr><td rowspan="3"><b>ON</b><br>(ngày, ngày cụ thể)</td><td>Thứ trong tuần</td><td><b>on</b> Monday, <b>on</b> Fridays</td></tr>
<tr><td>Ngày tháng</td><td><b>on</b> March 5th, <b>on</b> July 20th, 2025</td></tr>
<tr><td>Ngày đặc biệt</td><td><b>on</b> my birthday, <b>on</b> New Year's Day, <b>on</b> Christmas Day</td></tr>
<tr><td rowspan="4"><b>IN</b><br>(khoảng thời gian dài)</td><td>Tháng</td><td><b>in</b> January, <b>in</b> March</td></tr>
<tr><td>Năm</td><td><b>in</b> 2025, <b>in</b> 1990</td></tr>
<tr><td>Mùa</td><td><b>in</b> (the) summer, <b>in</b> (the) winter</td></tr>
<tr><td>Buổi trong ngày</td><td><b>in</b> the morning, <b>in</b> the afternoon, <b>in</b> the evening</td></tr>
</table>

<div class="note"><b>💡 Mẹo nhớ nhanh:</b><br>
<b>AT</b> = điểm nhỏ nhất (giờ, thời điểm) 📍<br>
<b>ON</b> = bề mặt = ngày (nằm trên lịch) 📅<br>
<b>IN</b> = bên trong = khoảng dài (tháng, năm, mùa) 📦</div>

<div class="warn"><b>⚠️ Ngoại lệ quan trọng — KHÔNG dùng in/on/at với:</b><br>
• <b>this, last, next, every</b> + thời gian → KHÔNG cần giới từ.<br>
✗ <s>on last Monday</s> → ✓ <b>last</b> Monday<br>
✗ <s>in next summer</s> → ✓ <b>next</b> summer<br>
✗ <s>at every day</s> → ✓ <b>every</b> day<br><br>
• <b>today, tonight, tomorrow, yesterday</b> → KHÔNG cần giới từ.<br>
✗ <s>on today</s> → ✓ <b>today</b></div>

<div class="ex"><b>Buổi sáng nhưng đêm:</b><br>
<b>in</b> the morning / afternoon / evening → <b>AT</b> night (ngoại lệ!)</div>

<h3>2. Giới từ chỉ nơi chốn: in, on, at</h3>

<table>
<tr><th>Giới từ</th><th>Dùng với</th><th>Ví dụ</th></tr>
<tr><td rowspan="3"><b>AT</b><br>(điểm cụ thể)</td><td>Địa chỉ cụ thể</td><td><b>at</b> 25 Tran Hung Dao Street</td></tr>
<tr><td>Nơi dừng chân, địa điểm nhỏ</td><td><b>at</b> the bus stop, <b>at</b> the door, <b>at</b> the airport, <b>at</b> school, <b>at</b> home, <b>at</b> work</td></tr>
<tr><td>Sự kiện</td><td><b>at</b> the party, <b>at</b> the meeting, <b>at</b> the concert</td></tr>
<tr><td rowspan="2"><b>ON</b><br>(bề mặt)</td><td>Trên bề mặt</td><td><b>on</b> the table, <b>on</b> the wall, <b>on</b> the floor, <b>on</b> the ceiling</td></tr>
<tr><td>Phương tiện (bên trên)</td><td><b>on</b> the bus, <b>on</b> the train, <b>on</b> the plane (nhưng: <b>in</b> the car, <b>in</b> a taxi)</td></tr>
<tr><td rowspan="3"><b>IN</b><br>(bên trong)</td><td>Không gian kín</td><td><b>in</b> the room, <b>in</b> the box, <b>in</b> the kitchen, <b>in</b> the car</td></tr>
<tr><td>Thành phố, quốc gia</td><td><b>in</b> Hanoi, <b>in</b> Vietnam, <b>in</b> Asia</td></tr>
<tr><td>Nước, chất lỏng</td><td><b>in</b> the water, <b>in</b> the sea, <b>in</b> the pool</td></tr>
</table>

<div class="note"><b>💡 Mẹo nhớ:</b><br>
<b>AT</b> = điểm, vị trí 📍 (at the door, at school)<br>
<b>ON</b> = trên bề mặt, tiếp xúc 📐 (on the table, on the wall)<br>
<b>IN</b> = bên trong, không gian 3D 📦 (in the room, in Vietnam)</div>

<div class="warn"><b>⚠️ Phương tiện:</b><br>
<b>on</b> the bus / train / plane / ship / bike / motorbike (phương tiện lớn, đứng/đi lại được bên trong)<br>
<b>in</b> the/a car / taxi (phương tiện nhỏ, phải ngồi bên trong)<br>
Nhưng: get <b>on</b> / get <b>off</b> the bus (lên/xuống xe buýt)<br>
get <b>in</b> / get <b>out of</b> the car (vào/ra xe hơi)</div>

<h3>3. Các giới từ nơi chốn khác</h3>
<table>
<tr><th>Giới từ</th><th>Nghĩa</th><th>Ví dụ</th></tr>
<tr><td><b>between</b></td><td>giữa (2 vật)</td><td>The bank is <b>between</b> the school and the post office.</td></tr>
<tr><td><b>among</b></td><td>giữa (≥3 vật)</td><td>She sat <b>among</b> her friends.</td></tr>
<tr><td><b>next to / beside</b></td><td>bên cạnh</td><td>The café is <b>next to</b> the bookshop.</td></tr>
<tr><td><b>opposite</b></td><td>đối diện</td><td>The park is <b>opposite</b> the hospital.</td></tr>
<tr><td><b>in front of</b></td><td>phía trước</td><td>There's a tree <b>in front of</b> my house.</td></tr>
<tr><td><b>behind</b></td><td>phía sau</td><td>The garden is <b>behind</b> the house.</td></tr>
<tr><td><b>above / over</b></td><td>phía trên</td><td>The lamp is <b>above</b> the table.</td></tr>
<tr><td><b>below / under</b></td><td>phía dưới</td><td>The cat is <b>under</b> the bed.</td></tr>
<tr><td><b>near / close to</b></td><td>gần</td><td>My school is <b>near</b> the market.</td></tr>
<tr><td><b>far from</b></td><td>xa</td><td>The airport is <b>far from</b> the city center.</td></tr>
</table>

<h3>4. Giới từ chỉ sự di chuyển</h3>
<table>
<tr><th>Giới từ</th><th>Nghĩa</th><th>Ví dụ</th></tr>
<tr><td><b>to</b></td><td>đến (đích)</td><td>I go <b>to</b> school every day.</td></tr>
<tr><td><b>from</b></td><td>từ (xuất phát)</td><td>She comes <b>from</b> Da Nang.</td></tr>
<tr><td><b>into</b></td><td>vào (bên trong)</td><td>He walked <b>into</b> the room.</td></tr>
<tr><td><b>out of</b></td><td>ra (bên ngoài)</td><td>She ran <b>out of</b> the building.</td></tr>
<tr><td><b>through</b></td><td>xuyên qua</td><td>We drove <b>through</b> the tunnel.</td></tr>
<tr><td><b>across</b></td><td>băng qua (bề mặt)</td><td>She walked <b>across</b> the street.</td></tr>
<tr><td><b>along</b></td><td>dọc theo</td><td>We walked <b>along</b> the river.</td></tr>
<tr><td><b>past</b></td><td>đi ngang qua</td><td>He walked <b>past</b> the church.</td></tr>
<tr><td><b>towards</b></td><td>về phía</td><td>She ran <b>towards</b> the exit.</td></tr>
</table>

<div class="warn"><b>⚠️ Không dùng "to" với home, here, there, abroad, upstairs, downstairs:</b><br>
✗ <s>I go to home.</s> → ✓ I go <b>home</b>.<br>
✗ <s>Come to here.</s> → ✓ Come <b>here</b>.</div>

<h3>5. Mẹo làm bài thi VSTEP</h3>
<div class="note"><b>💡 Chiến lược:</b><br>
<b>Thời gian:</b> giờ → at, ngày → on, tháng/năm/mùa → in. Có this/last/next/every → KHÔNG giới từ.<br>
<b>Nơi chốn:</b> điểm → at, bề mặt → on, bên trong / thành phố / nước → in.<br>
<b>Phương tiện:</b> bus/train/plane → on; car/taxi → in.<br>
<b>"at night"</b> là ngoại lệ (không phải "in the night").</div>
"""

# ============================================================
# UNIT 16: Connectors & Linking Words (B2)
# ============================================================
CONTENT[16] = """
<h3>1. Tổng quan</h3>
<p>Từ nối (Connectors / Linking Words) giúp liên kết các ý, câu và đoạn văn, làm bài viết mạch lạc và logic hơn. Đây là phần <b>rất quan trọng</b> cho bài thi VSTEP Writing và Reading.</p>

<h3>2. Từ nối theo chức năng</h3>

<h4>2.1. Thêm ý (Addition)</h4>
<table>
<tr><th>Từ nối</th><th>Nghĩa</th><th>Ví dụ</th></tr>
<tr><td><b>and</b></td><td>và</td><td>She is smart <b>and</b> hardworking.</td></tr>
<tr><td><b>also / too / as well</b></td><td>cũng</td><td>He <b>also</b> speaks Japanese. / I like it <b>too</b>.</td></tr>
<tr><td><b>moreover / furthermore</b></td><td>hơn nữa (trang trọng)</td><td>The hotel is cheap. <b>Moreover</b>, it's near the beach.</td></tr>
<tr><td><b>in addition (to)</b></td><td>ngoài ra</td><td><b>In addition to</b> English, she speaks French.</td></tr>
<tr><td><b>besides</b></td><td>bên cạnh đó</td><td><b>Besides</b>, the food there is excellent.</td></tr>
<tr><td><b>not only...but also</b></td><td>không chỉ...mà còn</td><td>She is <b>not only</b> beautiful <b>but also</b> intelligent.</td></tr>
</table>

<h4>2.2. Tương phản (Contrast)</h4>
<table>
<tr><th>Từ nối</th><th>Nghĩa</th><th>Vị trí / Cấu trúc</th><th>Ví dụ</th></tr>
<tr><td><b>but</b></td><td>nhưng</td><td>Nối 2 mệnh đề</td><td>I'm tired <b>but</b> I can't sleep.</td></tr>
<tr><td><b>however</b></td><td>tuy nhiên</td><td>Đầu câu / giữa câu + dấu phẩy</td><td>The test was hard. <b>However</b>, I passed.</td></tr>
<tr><td><b>although / though / even though</b></td><td>mặc dù</td><td>Đầu mệnh đề phụ</td><td><b>Although</b> it rained, we still went out.</td></tr>
<tr><td><b>despite / in spite of</b></td><td>mặc dù</td><td>+ N / V-ing</td><td><b>Despite</b> the rain, we went out.<br><b>In spite of being</b> tired, she worked.</td></tr>
<tr><td><b>while / whereas</b></td><td>trong khi</td><td>So sánh hai sự khác biệt</td><td>I like tea, <b>while</b> my sister prefers coffee.</td></tr>
<tr><td><b>on the other hand</b></td><td>mặt khác</td><td>Đầu câu mới</td><td>City life is exciting. <b>On the other hand</b>, it's stressful.</td></tr>
<tr><td><b>nevertheless / nonetheless</b></td><td>tuy nhiên (nhấn mạnh)</td><td>Đầu câu + phẩy</td><td>It was expensive. <b>Nevertheless</b>, it was worth it.</td></tr>
</table>

<div class="warn"><b>⚠️ Phân biệt although vs despite:</b><br>
<b>although / though / even though</b> + <b>S + V</b> (mệnh đề)<br>
→ <b>Although</b> <i>it was raining</i>, we went out.<br><br>
<b>despite / in spite of</b> + <b>N / V-ing</b> (cụm danh từ / danh động từ)<br>
→ <b>Despite</b> <i>the rain</i>, we went out.<br>
→ <b>In spite of</b> <i>being tired</i>, she continued working.<br><br>
✗ <s>Despite it was raining...</s> → ✓ Despite <b>the rain</b>... / Although <b>it was raining</b>...</div>

<h4>2.3. Nguyên nhân – Kết quả (Cause – Effect)</h4>
<table>
<tr><th>Từ nối</th><th>Nghĩa</th><th>Ví dụ</th></tr>
<tr><td><b>because</b></td><td>bởi vì (+ mệnh đề)</td><td>I stayed home <b>because</b> I was sick.</td></tr>
<tr><td><b>because of</b></td><td>bởi vì (+ danh từ)</td><td>I stayed home <b>because of</b> the rain.</td></tr>
<tr><td><b>since / as</b></td><td>vì (đặt đầu câu)</td><td><b>Since</b> you're here, let's start.</td></tr>
<tr><td><b>due to / owing to</b></td><td>do (+ danh từ, trang trọng)</td><td>The delay was <b>due to</b> bad weather.</td></tr>
<tr><td><b>therefore</b></td><td>vì vậy</td><td>He was sick. <b>Therefore</b>, he didn't come.</td></tr>
<tr><td><b>so</b></td><td>nên</td><td>It was late, <b>so</b> we went home.</td></tr>
<tr><td><b>as a result</b></td><td>kết quả là</td><td>He didn't study. <b>As a result</b>, he failed.</td></tr>
<tr><td><b>consequently</b></td><td>do đó</td><td>Prices rose. <b>Consequently</b>, demand fell.</td></tr>
</table>

<div class="warn"><b>⚠️ because vs because of:</b><br>
<b>because</b> + <b>S + V</b> (mệnh đề): I was late <b>because</b> <i>the traffic was heavy</i>.<br>
<b>because of</b> + <b>N</b> (danh từ/cụm danh từ): I was late <b>because of</b> <i>the heavy traffic</i>.<br>
✗ <s>Because of the traffic was heavy...</s></div>

<h4>2.4. Mục đích (Purpose)</h4>
<table>
<tr><th>Từ nối</th><th>Nghĩa</th><th>Ví dụ</th></tr>
<tr><td><b>to / in order to / so as to</b></td><td>để (+ V)</td><td>She studies hard <b>to</b> pass the exam.</td></tr>
<tr><td><b>so that</b></td><td>để mà (+ mệnh đề)</td><td>I saved money <b>so that</b> I could buy a car.</td></tr>
<tr><td><b>in order not to / so as not to</b></td><td>để không</td><td>He left early <b>in order not to</b> be late.</td></tr>
</table>

<h4>2.5. Liệt kê & Tổng kết</h4>
<table>
<tr><th>Chức năng</th><th>Từ nối</th></tr>
<tr><td>Liệt kê</td><td><b>firstly, secondly, thirdly, finally, first of all, to begin with, next, then, lastly</b></td></tr>
<tr><td>Ví dụ</td><td><b>for example, for instance, such as, namely</b></td></tr>
<tr><td>Tổng kết</td><td><b>in conclusion, to sum up, in summary, overall, all in all, in short</b></td></tr>
<tr><td>Nói cách khác</td><td><b>in other words, that is (to say), namely</b></td></tr>
</table>

<h3>3. Mẹo làm bài thi VSTEP</h3>
<div class="note"><b>💡 Chiến lược cho VSTEP Writing:</b><br>
<b>1.</b> Mở bài: <i>It is widely believed that... / There is a growing concern about...</i><br>
<b>2.</b> Thêm ý: <i>Moreover, Furthermore, In addition, Not only...but also</i><br>
<b>3.</b> Tương phản: <i>However, Although, Despite, On the other hand</i><br>
<b>4.</b> Nguyên nhân: <i>because, due to, therefore, as a result</i><br>
<b>5.</b> Kết luận: <i>In conclusion, To sum up, All in all</i><br><br>
Dùng đa dạng từ nối sẽ được điểm cao hơn cho phần <b>Coherence and Cohesion</b>!</div>
"""

# ============================================================
# UNIT 17: Word Formation (B2)
# ============================================================
CONTENT[17] = """
<h3>1. Word Formation – Cấu tạo từ</h3>
<p>Word formation là kỹ năng <b>biến đổi dạng từ</b> (danh từ, tính từ, động từ, trạng từ) bằng cách thêm tiền tố (prefix) hoặc hậu tố (suffix). Đây là dạng bài <b>rất phổ biến</b> trong VSTEP.</p>

<h3>2. Hậu tố tạo danh từ (Noun Suffixes)</h3>
<table>
<tr><th>Hậu tố</th><th>Thêm vào</th><th>Ví dụ</th></tr>
<tr><td><b>-tion / -sion</b></td><td>Động từ → Danh từ</td><td>educate → educa<b>tion</b>, decide → deci<b>sion</b>, inform → informa<b>tion</b></td></tr>
<tr><td><b>-ment</b></td><td>Động từ → Danh từ</td><td>develop → develop<b>ment</b>, manage → manage<b>ment</b>, achieve → achieve<b>ment</b></td></tr>
<tr><td><b>-ness</b></td><td>Tính từ → Danh từ</td><td>happy → happi<b>ness</b>, kind → kind<b>ness</b>, dark → dark<b>ness</b></td></tr>
<tr><td><b>-ity</b></td><td>Tính từ → Danh từ</td><td>popular → popular<b>ity</b>, possible → possibil<b>ity</b>, creative → creativ<b>ity</b></td></tr>
<tr><td><b>-ance / -ence</b></td><td>Tính từ → Danh từ</td><td>important → import<b>ance</b>, different → differ<b>ence</b>, independent → independ<b>ence</b></td></tr>
<tr><td><b>-er / -or</b></td><td>Động từ → Người</td><td>teach → teach<b>er</b>, act → act<b>or</b>, drive → driv<b>er</b></td></tr>
<tr><td><b>-ist</b></td><td>→ Người (chuyên gia)</td><td>science → scient<b>ist</b>, tour → tour<b>ist</b>, art → art<b>ist</b></td></tr>
<tr><td><b>-ship</b></td><td>→ Trạng thái, quan hệ</td><td>friend → friend<b>ship</b>, leader → leader<b>ship</b>, relation → relation<b>ship</b></td></tr>
<tr><td><b>-dom</b></td><td>→ Trạng thái, vương quốc</td><td>free → free<b>dom</b>, king → king<b>dom</b>, bore → bore<b>dom</b></td></tr>
</table>

<h3>3. Hậu tố tạo tính từ (Adjective Suffixes)</h3>
<table>
<tr><th>Hậu tố</th><th>Ví dụ</th></tr>
<tr><td><b>-ful</b> (đầy đủ, có)</td><td>beauty → beauti<b>ful</b>, help → help<b>ful</b>, care → care<b>ful</b>, success → success<b>ful</b></td></tr>
<tr><td><b>-less</b> (không có)</td><td>care → care<b>less</b>, hope → hope<b>less</b>, use → use<b>less</b>, home → home<b>less</b></td></tr>
<tr><td><b>-able / -ible</b> (có thể)</td><td>comfort → comfort<b>able</b>, eat → eat<b>able</b>, access → access<b>ible</b>, flex → flex<b>ible</b></td></tr>
<tr><td><b>-ous / -ious</b></td><td>danger → danger<b>ous</b>, fame → fam<b>ous</b>, religion → religi<b>ous</b>, ambition → ambiti<b>ous</b></td></tr>
<tr><td><b>-ive</b></td><td>create → creat<b>ive</b>, attract → attract<b>ive</b>, act → act<b>ive</b>, effect → effect<b>ive</b></td></tr>
<tr><td><b>-al</b></td><td>nation → nation<b>al</b>, tradition → tradition<b>al</b>, culture → cultur<b>al</b></td></tr>
<tr><td><b>-ic</b></td><td>science → scientif<b>ic</b>, economy → econom<b>ic</b>, history → histor<b>ic</b></td></tr>
<tr><td><b>-y</b></td><td>rain → rain<b>y</b>, cloud → cloud<b>y</b>, health → health<b>y</b>, wealth → wealth<b>y</b></td></tr>
</table>

<div class="note"><b>💡 -ful vs -less (cặp đối lập):</b><br>
care<b>ful</b> (cẩn thận) ↔ care<b>less</b> (bất cẩn)<br>
hope<b>ful</b> (đầy hy vọng) ↔ hope<b>less</b> (vô vọng)<br>
use<b>ful</b> (hữu ích) ↔ use<b>less</b> (vô dụng)<br>
help<b>ful</b> (hay giúp đỡ) ↔ help<b>less</b> (bất lực)</div>

<h3>4. Hậu tố tạo động từ (Verb Suffixes)</h3>
<table>
<tr><th>Hậu tố</th><th>Ví dụ</th></tr>
<tr><td><b>-ize / -ise</b></td><td>modern → modern<b>ize</b>, organ → organ<b>ize</b>, apolog → apolog<b>ize</b>, real → real<b>ize</b></td></tr>
<tr><td><b>-en</b></td><td>wide → wid<b>en</b>, short → short<b>en</b>, strength → strength<b>en</b>, dark → dark<b>en</b></td></tr>
<tr><td><b>-ify</b></td><td>simple → simpl<b>ify</b>, class → class<b>ify</b>, identity → ident<b>ify</b>, beauty → beaut<b>ify</b></td></tr>
<tr><td><b>-ate</b></td><td>active → activ<b>ate</b>, education → educ<b>ate</b>, motive → motiv<b>ate</b></td></tr>
</table>

<h3>5. Hậu tố tạo trạng từ (Adverb Suffixes)</h3>
<table>
<tr><th>Hậu tố</th><th>Ví dụ</th></tr>
<tr><td><b>-ly</b> (hầu hết tính từ → trạng từ)</td><td>quick → quick<b>ly</b>, careful → careful<b>ly</b>, happy → happi<b>ly</b>, easy → easi<b>ly</b></td></tr>
</table>
<div class="warn"><b>⚠️ Ngoại lệ:</b> Một số từ tận cùng -ly KHÔNG phải trạng từ mà là tính từ:<br>
<b>friendly</b> (thân thiện), <b>lovely</b> (đáng yêu), <b>lonely</b> (cô đơn), <b>lively</b> (sôi động), <b>daily</b> (hàng ngày), <b>elderly</b> (cao tuổi).<br>
→ Không nói <s>"She spoke friendly."</s> → ✓ "She spoke <b>in a friendly way</b>."</div>

<h3>6. Tiền tố phủ định (Negative Prefixes)</h3>
<table>
<tr><th>Tiền tố</th><th>Ví dụ</th></tr>
<tr><td><b>un-</b></td><td><b>un</b>happy, <b>un</b>able, <b>un</b>usual, <b>un</b>comfortable, <b>un</b>fair, <b>un</b>lucky</td></tr>
<tr><td><b>in-</b></td><td><b>in</b>correct, <b>in</b>complete, <b>in</b>dependent, <b>in</b>visible</td></tr>
<tr><td><b>im-</b> (trước m, p)</td><td><b>im</b>possible, <b>im</b>polite, <b>im</b>patient, <b>im</b>mature</td></tr>
<tr><td><b>ir-</b> (trước r)</td><td><b>ir</b>regular, <b>ir</b>responsible, <b>ir</b>relevant</td></tr>
<tr><td><b>il-</b> (trước l)</td><td><b>il</b>legal, <b>il</b>logical, <b>il</b>literate</td></tr>
<tr><td><b>dis-</b></td><td><b>dis</b>agree, <b>dis</b>like, <b>dis</b>honest, <b>dis</b>advantage, <b>dis</b>appear</td></tr>
<tr><td><b>mis-</b></td><td><b>mis</b>understand, <b>mis</b>lead, <b>mis</b>behave, <b>mis</b>spell</td></tr>
</table>

<div class="note"><b>💡 Mẹo nhớ in-/im-/ir-/il-:</b><br>
Trước <b>m, p</b> → <b>im</b>- (impossible, impolite)<br>
Trước <b>r</b> → <b>ir</b>- (irregular)<br>
Trước <b>l</b> → <b>il</b>- (illegal)<br>
Còn lại → <b>in</b>- (incorrect, incomplete)</div>

<h3>7. Cách xác định loại từ cần điền</h3>
<div class="note"><b>💡 Chiến lược làm bài thi VSTEP:</b><br>
<b>1.</b> Trước danh từ → cần <b>tính từ</b> (a <b>beautiful</b> city).<br>
<b>2.</b> Sau a/an/the/this/my + (adj) → cần <b>danh từ</b> (the <b>development</b> of...).<br>
<b>3.</b> Sau động từ thường → cần <b>trạng từ</b> (She runs <b>quickly</b>.).<br>
<b>4.</b> Sau be/become/seem/look/feel → cần <b>tính từ</b> (She looks <b>beautiful</b>.).<br>
<b>5.</b> Đầu câu / chủ ngữ → cần <b>danh từ</b> hoặc <b>danh động từ</b>.<br>
<b>6.</b> Kiểm tra nghĩa: tích cực hay tiêu cực? → thêm tiền tố phủ định (un-, dis-, im-...)?</div>

<div class="ex"><b>Bài tập mẫu:</b> "She is very _______ (CREATE)."<br>
→ Sau be + very → cần tính từ → create → creat<b>ive</b>.<br>
✓ She is very <b>creative</b>.</div>

<div class="ex"><b>Bài tập mẫu:</b> "His _______ (BEHAVE) at the party was unacceptable."<br>
→ His + ... → cần danh từ → behave → behav<b>iour</b>.<br>
✓ His <b>behaviour</b> at the party was unacceptable.</div>
"""

# ============================================================
# UNIT 18: Phrasal Verbs (B2)
# ============================================================
CONTENT[18] = """
<h3>1. Phrasal Verb là gì?</h3>
<p>Phrasal verb = <b>Động từ + Giới từ/Trạng từ</b>, tạo thành nghĩa mới, thường rất khác nghĩa gốc.</p>
<div class="ex"><b>give up</b> = từ bỏ (give = cho, up = lên → nhưng "give up" = từ bỏ, không liên quan!)</div>

<h3>2. Phrasal Verbs theo chủ đề</h3>

<h4>2.1. Cuộc sống hàng ngày</h4>
<table>
<tr><th>Phrasal Verb</th><th>Nghĩa</th><th>Ví dụ</th></tr>
<tr><td><b>wake up</b></td><td>thức dậy</td><td>I usually <b>wake up</b> at 6 a.m.</td></tr>
<tr><td><b>get up</b></td><td>trở dậy (rời giường)</td><td>I <b>got up</b> and went to the bathroom.</td></tr>
<tr><td><b>turn on / off</b></td><td>bật / tắt</td><td>Can you <b>turn on</b> the light?<br>Please <b>turn off</b> the TV.</td></tr>
<tr><td><b>put on</b></td><td>mặc vào</td><td><b>Put on</b> your jacket. It's cold outside.</td></tr>
<tr><td><b>take off</b></td><td>cởi ra / cất cánh</td><td><b>Take off</b> your shoes before entering.<br>The plane <b>took off</b> at 9 a.m.</td></tr>
<tr><td><b>pick up</b></td><td>nhặt lên / đón (ai)</td><td>She <b>picked up</b> the pen from the floor.<br>I'll <b>pick you up</b> at the airport.</td></tr>
<tr><td><b>throw away</b></td><td>vứt đi</td><td>Don't <b>throw away</b> plastic bottles.</td></tr>
<tr><td><b>tidy up / clean up</b></td><td>dọn dẹp</td><td>Please <b>tidy up</b> your room.</td></tr>
</table>

<h4>2.2. Học tập & Công việc</h4>
<table>
<tr><th>Phrasal Verb</th><th>Nghĩa</th><th>Ví dụ</th></tr>
<tr><td><b>look up</b></td><td>tra (từ điển)</td><td>If you don't know the word, <b>look it up</b> in a dictionary.</td></tr>
<tr><td><b>find out</b></td><td>tìm ra, phát hiện</td><td>I need to <b>find out</b> the answer.</td></tr>
<tr><td><b>give up</b></td><td>từ bỏ</td><td>Don't <b>give up</b>! Keep trying.</td></tr>
<tr><td><b>carry on / go on</b></td><td>tiếp tục</td><td>Let's <b>carry on</b> with the lesson.</td></tr>
<tr><td><b>catch up (with)</b></td><td>bắt kịp</td><td>I need to <b>catch up with</b> the rest of the class.</td></tr>
<tr><td><b>hand in / turn in</b></td><td>nộp (bài)</td><td>Please <b>hand in</b> your essays by Friday.</td></tr>
<tr><td><b>point out</b></td><td>chỉ ra</td><td>The teacher <b>pointed out</b> my mistakes.</td></tr>
<tr><td><b>figure out</b></td><td>hiểu ra, tìm ra cách</td><td>I can't <b>figure out</b> how to solve this problem.</td></tr>
<tr><td><b>set up</b></td><td>thành lập, cài đặt</td><td>She <b>set up</b> her own business.</td></tr>
<tr><td><b>take over</b></td><td>tiếp quản</td><td>He <b>took over</b> the company from his father.</td></tr>
</table>

<h4>2.3. Quan hệ & Giao tiếp</h4>
<table>
<tr><th>Phrasal Verb</th><th>Nghĩa</th><th>Ví dụ</th></tr>
<tr><td><b>get along (with)</b></td><td>hòa hợp</td><td>I <b>get along</b> well <b>with</b> my colleagues.</td></tr>
<tr><td><b>look after</b></td><td>chăm sóc</td><td>She <b>looks after</b> her elderly parents.</td></tr>
<tr><td><b>look for</b></td><td>tìm kiếm</td><td>I'm <b>looking for</b> my keys.</td></tr>
<tr><td><b>look forward to</b></td><td>mong đợi</td><td>I <b>look forward to</b> meeting you.</td></tr>
<tr><td><b>bring up</b></td><td>nuôi dạy / đề cập</td><td>She was <b>brought up</b> by her grandparents.<br>He <b>brought up</b> an interesting topic.</td></tr>
<tr><td><b>come across</b></td><td>tình cờ gặp</td><td>I <b>came across</b> an old friend at the mall.</td></tr>
<tr><td><b>fall out (with)</b></td><td>cãi nhau, giận nhau</td><td>They <b>fell out</b> over money.</td></tr>
<tr><td><b>make up</b></td><td>làm hòa / bịa (chuyện)</td><td>They argued but <b>made up</b> the next day.</td></tr>
<tr><td><b>run into</b></td><td>tình cờ gặp</td><td>I <b>ran into</b> my teacher at the supermarket.</td></tr>
<tr><td><b>turn down</b></td><td>từ chối / vặn nhỏ</td><td>She <b>turned down</b> the job offer.<br>Can you <b>turn down</b> the music?</td></tr>
</table>

<h4>2.4. Sức khỏe & Thay đổi</h4>
<table>
<tr><th>Phrasal Verb</th><th>Nghĩa</th><th>Ví dụ</th></tr>
<tr><td><b>break down</b></td><td>hỏng (máy) / suy sụp</td><td>My car <b>broke down</b> on the highway.<br>She <b>broke down</b> in tears.</td></tr>
<tr><td><b>break out</b></td><td>bùng phát</td><td>A fire <b>broke out</b> in the factory.</td></tr>
<tr><td><b>cut down (on)</b></td><td>giảm bớt</td><td>You should <b>cut down on</b> sugar.</td></tr>
<tr><td><b>work out</b></td><td>tập thể dục / giải quyết</td><td>I <b>work out</b> three times a week.<br>Things will <b>work out</b> in the end.</td></tr>
<tr><td><b>grow up</b></td><td>lớn lên</td><td>I <b>grew up</b> in a small village.</td></tr>
<tr><td><b>pass away</b></td><td>qua đời (lịch sự)</td><td>Her grandfather <b>passed away</b> last year.</td></tr>
<tr><td><b>put off</b></td><td>hoãn lại</td><td>Don't <b>put off</b> going to the dentist.</td></tr>
<tr><td><b>call off</b></td><td>hủy bỏ</td><td>The match was <b>called off</b> due to rain.</td></tr>
</table>

<h3>3. Phrasal Verbs tách được vs không tách được</h3>

<h4>3.1. Tách được (Separable)</h4>
<p>Tân ngữ có thể đứng giữa hoặc sau phrasal verb. Nếu tân ngữ là <b>đại từ</b> (it, them, her...) → <b>BẮT BUỘC</b> đứng giữa.</p>
<div class="ex">Turn <b>off</b> the TV. = Turn the TV <b>off</b>. (cả hai đều đúng)<br>
Turn <b>it off</b>. ✓ (đại từ → bắt buộc đứng giữa)<br>
<s>Turn off it.</s> ✗ (sai!)</div>

<h4>3.2. Không tách được (Inseparable)</h4>
<p>Tân ngữ LUÔN đứng <b>sau</b> toàn bộ phrasal verb.</p>
<div class="ex">I <b>look after</b> my little sister. ✓<br>
<s>I look my little sister after.</s> ✗<br>
I <b>look after her</b>. ✓ (đại từ vẫn đứng sau)</div>

<div class="note"><b>💡 Phân biệt nhanh:</b><br>
<b>Tách được:</b> turn on/off, pick up, put on, take off, throw away, look up, hand in, call off, give up, figure out, set up, bring up, turn down<br>
<b>Không tách được:</b> look after, look for, look forward to, get along with, come across, run into, carry on, catch up with, break down, grow up</div>

<h3>4. Mẹo làm bài thi VSTEP</h3>
<div class="note"><b>💡 Chiến lược:</b><br>
<b>1.</b> Đọc kỹ ngữ cảnh để xác định nghĩa phrasal verb (nhiều PV có nhiều nghĩa).<br>
<b>2.</b> Học theo chủ đề (cuộc sống, học tập, quan hệ...) dễ nhớ hơn học riêng lẻ.<br>
<b>3.</b> Nhớ quy tắc: đại từ (it, them, her...) + phrasal verb tách được → đặt ở giữa.<br>
<b>4.</b> VSTEP Reading thường dùng phrasal verb → hiểu nghĩa giúp đọc hiểu tốt hơn.<br>
<b>5.</b> VSTEP Writing: dùng phrasal verb phù hợp thay vì từ đơn sẽ tự nhiên hơn (look into thay vì investigate, find out thay vì discover).</div>
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

print(f"\nDone! Updated {len(CONTENT)} units (15-18).")
