# -*- coding: utf-8 -*-
"""Ngu phap Units 11-14."""

UNITS_3 = [
{
 'order': 11, 'level': 'B1',
 'title': 'Relative Clauses',
 'title_vi': 'Mệnh đề quan hệ',
 'description': 'who, whom, which, that, whose, where, when; mệnh đề xác định và không xác định.',
 'content': """
<h3>1. Đại từ quan hệ</h3>
<table>
<tr><th>Từ</th><th>Thay cho</th><th>Ví dụ</th></tr>
<tr><td><b>who</b></td><td>người (chủ ngữ)</td><td>The man <b>who</b> lives next door is a doctor.</td></tr>
<tr><td><b>whom</b></td><td>người (tân ngữ)</td><td>The woman <b>whom</b> I met was friendly.</td></tr>
<tr><td><b>which</b></td><td>vật, sự việc</td><td>The book <b>which</b> you lent me is great.</td></tr>
<tr><td><b>that</b></td><td>người &amp; vật (mệnh đề xác định)</td><td>The car <b>that</b> he bought is expensive.</td></tr>
<tr><td><b>whose</b></td><td>sở hữu</td><td>The girl <b>whose</b> phone rang blushed.</td></tr>
<tr><td><b>where</b></td><td>nơi chốn</td><td>This is the house <b>where</b> I was born.</td></tr>
<tr><td><b>when</b></td><td>thời gian</td><td>I remember the day <b>when</b> we first met.</td></tr>
</table>
<div class="ex">The students <b>who</b> study hard will pass the exam.<span class="vi">→ Những sinh viên (mà) học chăm sẽ đỗ kỳ thi.</span></div>
<div class="ex">Da Lat is a city <b>where</b> the weather is cool all year.<span class="vi">→ Đà Lạt là thành phố nơi thời tiết mát mẻ quanh năm.</span></div>

<h3>2. Mệnh đề xác định vs không xác định</h3>
<ul>
<li><b>Xác định</b> (defining): cần thiết để hiểu nghĩa, KHÔNG có dấu phẩy, có thể dùng "that".</li>
<li><b>Không xác định</b> (non-defining): chỉ bổ sung thông tin, CÓ dấu phẩy, KHÔNG dùng "that".</li>
</ul>
<div class="ex">My brother, <b>who</b> lives in Hue, is an engineer.<span class="vi">→ Anh trai tôi, người đang sống ở Huế, là kỹ sư. (thông tin thêm — có dấu phẩy, không dùng that)</span></div>
<div class="warn"><b>⚠️ Ghi nhớ:</b> Sau dấu phẩy không dùng THAT: ✗ <s>My mother, that is 60, ...</s> → ✓ My mother, <b>who</b> is 60, ...</div>

<h3>3. Lược bỏ đại từ quan hệ</h3>
<p>Khi đại từ quan hệ làm <b>tân ngữ</b> trong mệnh đề xác định, có thể lược bỏ:</p>
<div class="ex">The film (which/that) <b>we watched</b> last night was boring.<span class="vi">→ Bộ phim (mà) chúng tôi xem tối qua thật chán. ("which" là tân ngữ của watched → bỏ được)</span></div>
""",
 'questions': [
  ('The woman ___ teaches us English is from Australia.', 'which', 'who', 'whose', 'where', 'B',
   'Thay cho "the woman" (người) và làm CHỦ NGỮ của động từ "teaches" → who.'),
  ('This is the school ___ my mother used to study.', 'which', 'who', 'where', 'when', 'C',
   'Chỉ NƠI CHỐN ("ngôi trường nơi mẹ tôi từng học") và sau chỗ trống là mệnh đề đầy đủ (S+V) → where. Nếu dùng which thì phải có giới từ: at which.'),
  ('The boy ___ bicycle was stolen reported it to the police.', 'who', 'whom', 'whose', 'which', 'C',
   'Chỉ sự SỞ HỮU: "chiếc xe đạp CỦA cậu bé" → whose + danh từ (whose bicycle).'),
  ('The cake ___ my mother made was delicious.', 'who', 'whom', 'where', 'which', 'D',
   '"The cake" là VẬT → dùng which (hoặc that). Who/whom chỉ dùng cho người.'),
  ('My father, ___ is 55 years old, still plays football every week.', 'that', 'who', 'whom', 'which', 'B',
   'Mệnh đề KHÔNG xác định (có dấu phẩy, bổ sung thông tin về bố tôi) → không được dùng that, dùng who (chỉ người, chủ ngữ).'),
  ("I'll never forget the day ___ I graduated from university.", 'where', 'which', 'when', 'who', 'C',
   '"The day" là THỜI GIAN → dùng when: ngày mà tôi tốt nghiệp đại học.'),
  ('The people ___ we met on holiday were very kind.', 'whom', 'which', 'whose', 'where', 'A',
   'Thay cho "the people" (người) và làm TÂN NGỮ của "met" (we met them) → whom (hoặc who/that trong văn nói).'),
  ('Is that the restaurant ___ serves Vietnamese food?', 'where', 'who', 'that', 'whom', 'C',
   'Thay cho "the restaurant" (vật) làm CHỦ NGỮ của "serves" → that/which. "Where" sai vì sau nó phải là mệnh đề đủ S+V.'),
 ],
},
{
 'order': 12, 'level': 'B1',
 'title': 'Gerunds and Infinitives',
 'title_vi': 'Danh động từ và động từ nguyên mẫu',
 'description': 'V-ing hay to V? Các động từ theo sau bởi gerund/infinitive và khác biệt về nghĩa.',
 'content': """
<h3>1. Động từ + V-ing (gerund)</h3>
<p><b>enjoy, finish, mind, avoid, practise, suggest, keep, admit, deny, imagine, miss, give up</b></p>
<div class="ex">I <b>enjoy listening</b> to music.<span class="vi">→ Tôi thích nghe nhạc.</span></div>
<div class="ex">Would you <b>mind opening</b> the window?<span class="vi">→ Bạn có phiền mở cửa sổ không?</span></div>

<h3>2. Động từ + to V (infinitive)</h3>
<p><b>want, hope, decide, plan, expect, promise, agree, refuse, offer, learn, manage, afford, choose</b></p>
<div class="ex">She <b>decided to study</b> abroad.<span class="vi">→ Cô ấy quyết định đi du học.</span></div>
<div class="ex">We <b>can't afford to buy</b> a new car.<span class="vi">→ Chúng tôi không đủ tiền mua ô tô mới.</span></div>

<h3>3. Động từ + O + to V</h3>
<p><b>ask, tell, want, advise, allow, encourage, invite, remind, warn</b></p>
<div class="ex">The doctor <b>advised me to rest</b>.<span class="vi">→ Bác sĩ khuyên tôi nghỉ ngơi.</span></div>

<h3>4. Cả hai nhưng KHÁC nghĩa</h3>
<table>
<tr><th>Động từ</th><th>+ V-ing</th><th>+ to V</th></tr>
<tr><td><b>stop</b></td><td>dừng hẳn việc gì<br><i>He stopped smoking.</i> (bỏ thuốc)</td><td>dừng lại để làm việc khác<br><i>He stopped to smoke.</i> (dừng lại để hút thuốc)</td></tr>
<tr><td><b>remember</b></td><td>nhớ đã làm (quá khứ)<br><i>I remember locking the door.</i></td><td>nhớ phải làm (tương lai)<br><i>Remember to lock the door!</i></td></tr>
<tr><td><b>forget</b></td><td>quên đã làm</td><td>quên phải làm</td></tr>
<tr><td><b>try</b></td><td>thử làm xem sao</td><td>cố gắng làm</td></tr>
</table>
<div class="note"><b>💡 Vị trí khác cần V-ing:</b><br>• Sau giới từ: <i>interested <b>in learning</b>, good <b>at swimming</b>, look forward <b>to seeing</b> you.</i><br>• Làm chủ ngữ: <i><b>Swimming</b> is good for your health.</i></div>
<div class="warn"><b>⚠️ "look forward to" + V-ing</b> ("to" ở đây là giới từ): I look forward to <b>hearing</b> from you. — câu kết thư kinh điển trong bài thi Viết!</div>
""",
 'questions': [
  ('I enjoy ___ books in my free time.', 'read', 'to read', 'reading', 'reads', 'C',
   '"Enjoy" luôn đi với V-ing → enjoy reading. Nhóm động từ enjoy, finish, mind, avoid... + gerund.'),
  ('She decided ___ a new language this year.', 'learning', 'to learn', 'learn', 'learned', 'B',
   '"Decide" đi với to V → decided to learn. Nhóm decide, want, hope, plan... + infinitive.'),
  ('Would you mind ___ the door? It is cold in here.', 'close', 'to close', 'closing', 'closed', 'C',
   '"Mind" đi với V-ing → Would you mind closing...? (Bạn có phiền đóng cửa không?)'),
  ('Remember ___ the lights before you leave the office.', 'turning off', 'to turn off', 'turn off', 'turned off', 'B',
   '"Remember + to V" = nhớ PHẢI làm (việc chưa làm, hướng tương lai). Ở đây là lời nhắc nhở tắt đèn trước khi về → to turn off.'),
  ('He gave up ___ two years ago and feels much healthier now.', 'smoking', 'to smoke', 'smoke', 'smoked', 'A',
   '"Give up" (từ bỏ) + V-ing → gave up smoking (bỏ thuốc lá).'),
  ('My parents don\'t allow me ___ out late at night.', 'staying', 'to stay', 'stay', 'stayed', 'B',
   'Cấu trúc "allow + O + to V" → allow me to stay out (cho phép tôi ở ngoài muộn).'),
  ('I look forward to ___ from you soon.', 'hear', 'hearing', 'be heard', 'heard', 'B',
   '"Look forward to" — "to" là GIỚI TỪ nên theo sau là V-ing: look forward to hearing. Đây là câu kết thư trang trọng rất hay gặp.'),
  ('She is interested ___ photography.', 'in learning', 'to learn', 'in learn', 'learning in', 'A',
   'Tính từ + giới từ "interested in" + V-ing → interested in learning photography.'),
 ],
},
{
 'order': 13, 'level': 'B1',
 'title': 'Comparisons',
 'title_vi': 'So sánh hơn, so sánh nhất, so sánh bằng',
 'description': 'Comparative, superlative, as...as, so sánh kép và các dạng bất quy tắc.',
 'content': """
<h3>1. So sánh hơn (Comparative)</h3>
<table>
<tr><th>Loại tính từ</th><th>Công thức</th><th>Ví dụ</th></tr>
<tr><td>Ngắn (1 âm tiết)</td><td>adj-er + than</td><td>taller than, bigger than</td></tr>
<tr><td>Dài (2+ âm tiết)</td><td>more + adj + than</td><td>more beautiful than</td></tr>
</table>
<div class="ex">This exam is <b>easier than</b> the last one.<span class="vi">→ Bài thi này dễ hơn bài trước.</span></div>
<div class="ex">Living in the city is <b>more expensive than</b> living in the countryside.<span class="vi">→ Sống ở thành phố đắt đỏ hơn ở nông thôn.</span></div>

<h3>2. So sánh nhất (Superlative)</h3>
<table>
<tr><th>Loại tính từ</th><th>Công thức</th><th>Ví dụ</th></tr>
<tr><td>Ngắn</td><td>the + adj-est</td><td>the tallest, the biggest</td></tr>
<tr><td>Dài</td><td>the most + adj</td><td>the most interesting</td></tr>
</table>
<div class="ex">Phong Nha is one of <b>the most beautiful</b> caves in the world.<span class="vi">→ Phong Nha là một trong những hang động đẹp nhất thế giới.</span></div>

<h3>3. Bất quy tắc</h3>
<table>
<tr><th>Tính từ</th><th>So sánh hơn</th><th>So sánh nhất</th></tr>
<tr><td>good</td><td>better</td><td>the best</td></tr>
<tr><td>bad</td><td>worse</td><td>the worst</td></tr>
<tr><td>far</td><td>farther/further</td><td>the farthest/furthest</td></tr>
<tr><td>little</td><td>less</td><td>the least</td></tr>
<tr><td>many/much</td><td>more</td><td>the most</td></tr>
</table>

<h3>4. So sánh bằng: as + adj + as</h3>
<div class="ex">He is <b>as tall as</b> his father.<span class="vi">→ Anh ấy cao bằng bố.</span></div>
<div class="ex">This bag is<b>n't as expensive as</b> I thought.<span class="vi">→ Cái túi này không đắt như tôi nghĩ.</span></div>

<h3>5. Cấu trúc nâng cao (hay gặp ở B2)</h3>
<ul>
<li><b>So sánh kép:</b> The + comparative..., the + comparative...: <i><b>The more</b> you practise, <b>the better</b> you become.</i> (Càng luyện nhiều, càng giỏi.)</li>
<li><b>Càng ngày càng:</b> comparative + and + comparative: <i>It's getting <b>hotter and hotter</b>.</i></li>
<li><b>Gấp bao nhiêu lần:</b> twice/three times + as...as: <i>This house is <b>twice as big as</b> mine.</i></li>
</ul>
<div class="warn"><b>⚠️ Lỗi thường gặp:</b> ✗ <s>more better</s>, ✗ <s>more easier</s> — không dùng "more" với dạng -er. ✗ <s>than me thought</s> → chú ý "than" chứ không phải "then".</div>
""",
 'questions': [
  ('My new phone is much ___ than my old one.', 'fast', 'faster', 'fastest', 'more fast', 'B',
   '"Fast" là tính từ ngắn → so sánh hơn thêm -er: faster than. "Much" đứng trước để nhấn mạnh (nhanh hơn nhiều).'),
  ('This is ___ film I have ever seen.', 'the more interesting', 'most interesting', 'the most interesting', 'more interesting', 'C',
   'Cấu trúc "the + so sánh nhất + I have ever + V3" → the most interesting film (bộ phim hay nhất tôi từng xem). "Interesting" là tính từ dài → the most.'),
  ('Her English is getting ___ .', 'good and good', 'better and better', 'more and more good', 'best and best', 'B',
   '"Càng ngày càng" với tính từ ngắn: comparative + and + comparative; "good" bất quy tắc → better and better.'),
  ('He is not ___ his brother.', 'so tall than', 'as tall as', 'taller', 'the tallest', 'B',
   'So sánh bằng phủ định: not as + adj + as → not as tall as (không cao bằng anh trai).'),
  ('___ you study, ___ results you will get.', 'The harder / the better', 'Harder / better', 'The hardest / the best', 'The more hard / the more good', 'A',
   'So sánh kép "càng... càng...": The + comparative, the + comparative → The harder you study, the better results you will get.'),
  ('Today is even ___ than yesterday.', 'bad', 'worse', 'worst', 'badder', 'B',
   '"Bad" là tính từ bất quy tắc: bad → worse → the worst. So sánh hơn với than → worse than.'),
  ('Hanoi is one of ___ cities in Southeast Asia.', 'older', 'the oldest', 'the older', 'oldest', 'B',
   'Cấu trúc "one of the + so sánh nhất + danh từ số nhiều" → one of the oldest cities.'),
  ('This suitcase is twice ___ heavy ___ that one.', 'more / than', 'as / as', 'so / as', 'much / than', 'B',
   'So sánh gấp bội: twice + as + adj + as → twice as heavy as (nặng gấp đôi).'),
 ],
},
{
 'order': 14, 'level': 'B1',
 'title': 'Articles & Quantifiers',
 'title_vi': 'Mạo từ & lượng từ',
 'description': 'a/an/the, some/any, much/many, (a) few/(a) little, a lot of.',
 'content': """
<h3>1. Mạo từ a / an / the</h3>
<table>
<tr><th>Mạo từ</th><th>Dùng khi</th><th>Ví dụ</th></tr>
<tr><td><b>a</b></td><td>danh từ số ít, phụ âm đầu, chưa xác định</td><td>a book, a university (/juː/)</td></tr>
<tr><td><b>an</b></td><td>danh từ số ít, NGUYÊN ÂM đầu (theo âm)</td><td>an apple, an hour (/aʊə/)</td></tr>
<tr><td><b>the</b></td><td>đã xác định, duy nhất, nhắc lại lần 2</td><td>the sun, the book I bought</td></tr>
</table>
<div class="ex">I saw <b>a</b> dog. <b>The</b> dog was chasing <b>a</b> cat.<span class="vi">→ Tôi thấy một con chó. Con chó (đó) đang đuổi một con mèo. (lần 1: a, nhắc lại: the)</span></div>
<div class="warn"><b>⚠️ Chú ý theo ÂM chứ không theo chữ:</b> a <b>u</b>niversity (/j/), an <b>h</b>our (h câm), a <b>E</b>uropean country (/j/), an MBA (/em/).</div>
<h4>Không dùng mạo từ (zero article)</h4>
<ul><li>Danh từ số nhiều/không đếm được nói chung: <i>I like music. Cats are cute.</i></li>
<li>Bữa ăn, môn học, môn thể thao: <i>have breakfast, play football, study English.</i></li>
<li>go to school/work/bed (nghĩa chức năng).</li></ul>

<h3>2. some / any</h3>
<ul>
<li><b>some</b>: câu khẳng định, lời mời: <i>There are <b>some</b> eggs. Would you like <b>some</b> tea?</i></li>
<li><b>any</b>: câu phủ định, nghi vấn: <i>There aren't <b>any</b> eggs. Do you have <b>any</b> questions?</i></li>
</ul>

<h3>3. much / many / a lot of</h3>
<table>
<tr><th>Lượng từ</th><th>Đi với</th><th>Ví dụ</th></tr>
<tr><td><b>many</b></td><td>danh từ đếm được số nhiều</td><td>How <b>many</b> students...?</td></tr>
<tr><td><b>much</b></td><td>danh từ KHÔNG đếm được</td><td>How <b>much</b> money...?</td></tr>
<tr><td><b>a lot of</b></td><td>cả hai</td><td>a lot of friends / a lot of time</td></tr>
</table>

<h3>4. (a) few / (a) little</h3>
<table>
<tr><th>Lượng từ</th><th>Đi với</th><th>Nghĩa</th></tr>
<tr><td><b>a few</b></td><td>đếm được</td><td>một vài (đủ dùng — tích cực)</td></tr>
<tr><td><b>few</b></td><td>đếm được</td><td>rất ít (gần như không — tiêu cực)</td></tr>
<tr><td><b>a little</b></td><td>không đếm được</td><td>một chút (đủ dùng)</td></tr>
<tr><td><b>little</b></td><td>không đếm được</td><td>rất ít (gần như không)</td></tr>
</table>
<div class="ex">I have <b>a few</b> close friends, so I never feel lonely.<span class="vi">→ Tôi có một vài người bạn thân nên chẳng bao giờ thấy cô đơn. (tích cực)</span></div>
<div class="ex">He has <b>little</b> money, so he can't buy it.<span class="vi">→ Anh ấy có rất ít tiền nên không mua nổi. (tiêu cực)</span></div>
""",
 'questions': [
  ('She is ___ honest person.', 'a', 'an', 'the', 'no article', 'B',
   '"Honest" có chữ h CÂM, bắt đầu bằng NGUYÊN ÂM /ɒ/ → dùng an: an honest person.'),
  ('How ___ sugar do you want in your coffee?', 'many', 'much', 'few', 'a few', 'B',
   '"Sugar" (đường) là danh từ KHÔNG đếm được → How much. "Many" chỉ dùng với danh từ đếm được số nhiều.'),
  ("I don't have ___ money with me now.", 'some', 'any', 'a', 'many', 'B',
   'Câu PHỦ ĐỊNH → dùng any: don\'t have any money. "Some" dùng trong câu khẳng định.'),
  ('He knows ___ people here, so he feels lonely.', 'a few', 'few', 'a little', 'little', 'B',
   'Cảm giác cô đơn → nghĩa TIÊU CỰC "rất ít, gần như không có" → few (không có "a"). "People" đếm được nên loại little/a little.'),
  ('___ moon goes around ___ earth.', 'A / an', 'The / the', 'A / the', 'The / an', 'B',
   'Mặt trăng và trái đất là những vật DUY NHẤT → đều dùng the: The moon... the earth.'),
  ('Would you like ___ orange juice?', 'any', 'some', 'many', 'a', 'B',
   'Lời MỜI dùng some dù là câu hỏi: Would you like some...? (Bạn dùng chút nước cam nhé?)'),
  ('My father goes to ___ work by motorbike every day.', 'a', 'an', 'the', 'no article', 'D',
   '"Go to work" (đi làm) là cụm chỉ chức năng, KHÔNG dùng mạo từ — giống go to school, go to bed.'),
  ('There is ___ milk left — just enough for one cup of coffee.', 'a few', 'few', 'a little', 'many', 'C',
   '"Milk" không đếm được + nghĩa TÍCH CỰC "còn một chút, đủ dùng" ("just enough") → a little.'),
 ],
},
]
