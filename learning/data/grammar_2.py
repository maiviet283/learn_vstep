# -*- coding: utf-8 -*-
"""Ngu phap Units 6-10."""

UNITS_2 = [
{
 'order': 6, 'level': 'B1',
 'title': 'Modal Verbs 1: ability, permission, advice',
 'title_vi': 'Động từ khuyết thiếu 1: khả năng, xin phép, lời khuyên',
 'description': 'can, could, be able to, may, might, should, ought to, had better.',
 'content': """
<h3>1. Khả năng: can / could / be able to</h3>
<table>
<tr><th>Cấu trúc</th><th>Nghĩa</th><th>Ví dụ</th></tr>
<tr><td>can + V</td><td>có thể (hiện tại)</td><td>She <b>can speak</b> three languages.</td></tr>
<tr><td>could + V</td><td>có thể (quá khứ)</td><td>I <b>could swim</b> when I was five.</td></tr>
<tr><td>be able to + V</td><td>có thể (mọi thì)</td><td>He <b>will be able to</b> come tomorrow.</td></tr>
</table>
<div class="ex">I <b>can't hear</b> you. Can you speak louder?<span class="vi">→ Tôi không nghe thấy bạn. Bạn nói to hơn được không?</span></div>
<div class="note"><b>💡</b> "can" không có dạng tương lai/hoàn thành → dùng <b>be able to</b>: will be able to, has been able to.</div>

<h3>2. Xin phép &amp; cho phép: can / could / may</h3>
<div class="ex"><b>Could</b> I use your phone, please?<span class="vi">→ Tôi dùng nhờ điện thoại của bạn được không? (could lịch sự hơn can)</span></div>
<div class="ex"><b>May</b> I come in?<span class="vi">→ Tôi vào được không ạ? (may trang trọng nhất)</span></div>

<h3>3. Khả năng xảy ra: may / might / could</h3>
<p>Diễn tả điều <b>có thể xảy ra nhưng không chắc chắn</b> (might &lt; may ≈ could &lt; will).</p>
<div class="ex">Take an umbrella. It <b>might rain</b> later.<span class="vi">→ Mang ô đi. Lát nữa trời có thể mưa (không chắc).</span></div>

<h3>4. Lời khuyên: should / ought to / had better</h3>
<table>
<tr><th>Cấu trúc</th><th>Sắc thái</th><th>Ví dụ</th></tr>
<tr><td>should + V</td><td>nên (khuyên chung)</td><td>You <b>should see</b> a doctor.</td></tr>
<tr><td>ought to + V</td><td>nên (≈ should)</td><td>You <b>ought to apologize</b>.</td></tr>
<tr><td>had better + V</td><td>tốt hơn hết là (mạnh, cảnh báo)</td><td>You<b>'d better hurry</b> or you'll miss the bus.</td></tr>
</table>
<div class="warn"><b>⚠️ Ghi nhớ:</b> Sau modal verb, động từ luôn ở <b>nguyên mẫu không to</b> (trừ ought <b>to</b>, be able <b>to</b>, had better + V không to). Modal không thêm s: ✗ <s>He cans swim</s>.</div>
""",
 'questions': [
  ('My grandmother is 80, but she ___ still read without glasses.', 'can', 'may', 'should', 'must', 'A',
   'Diễn tả khả năng ở hiện tại (vẫn đọc được không cần kính) → can + V nguyên mẫu.'),
  ('___ I borrow your dictionary, please? — Of course.', 'Should', 'Could', 'Must', 'Would', 'B',
   'Xin phép một cách lịch sự → Could I...? (lịch sự hơn Can I...?). Should dùng cho lời khuyên, must là bắt buộc.'),
  ("You ___ smoke here. It's a hospital.", 'should', "shouldn't", 'can', 'might', 'B',
   'Bệnh viện là nơi không được hút thuốc → lời khuyên phủ định mạnh: shouldn\'t smoke (không nên hút thuốc).'),
  ('Take your coat. It ___ get cold this evening.', 'must', 'should', 'might', 'need', 'C',
   'Diễn tả khả năng KHÔNG chắc chắn ("có thể trời sẽ lạnh") → might. Must là suy luận chắc chắn, should là lời khuyên.'),
  ('When I was a child, I ___ climb trees very well.', 'can', 'could', 'may', 'am able to', 'B',
   '"When I was a child" là quá khứ → dùng could (dạng quá khứ của can): could climb.'),
  ("You'd better ___ now, or you'll be late for the exam.", 'to leave', 'leaving', 'leave', 'left', 'C',
   'Cấu trúc "had better + V nguyên mẫu không to" → You\'d better leave. Đây là lời khuyên mạnh kèm cảnh báo hậu quả.'),
  ('He broke his leg, so he ___ play in the final next week.', "won't be able to", "can't to", "isn't able", "couldn't", 'A',
   'Nói về khả năng trong TƯƠNG LAI (trận chung kết tuần sau) — "can" không có dạng tương lai → will/won\'t be able to.'),
  ('Students ___ hand in their essays by Friday.', 'might', 'ought to', 'could', 'may', 'B',
   'Ngữ cảnh nghĩa vụ/lời khuyên mạnh (phải nộp bài trước thứ Sáu) → ought to (= should). Might/may/could chỉ khả năng, không hợp nghĩa.'),
 ],
},
{
 'order': 7, 'level': 'B1',
 'title': 'Modal Verbs 2: obligation, necessity, deduction',
 'title_vi': 'Động từ khuyết thiếu 2: bắt buộc, cần thiết, suy luận',
 'description': 'must, have to, mustn\'t, don\'t have to, need, can\'t (suy luận).',
 'content': """
<h3>1. Bắt buộc: must / have to</h3>
<table>
<tr><th>Cấu trúc</th><th>Sắc thái</th><th>Ví dụ</th></tr>
<tr><td>must + V</td><td>bắt buộc (người nói tự thấy cần)</td><td>I <b>must finish</b> this today.</td></tr>
<tr><td>have to + V</td><td>bắt buộc (do quy định bên ngoài)</td><td>You <b>have to wear</b> a helmet.</td></tr>
</table>
<div class="ex">I <b>must study</b> harder. (tự mình thấy cần)<span class="vi">→ Mình phải học chăm hơn mới được.</span></div>
<div class="ex">We <b>have to check in</b> two hours before the flight. (quy định)<span class="vi">→ Chúng tôi phải làm thủ tục 2 tiếng trước giờ bay.</span></div>

<h3>2. Cấm ≠ Không cần thiết</h3>
<div class="warn"><b>⚠️ Cặp dễ nhầm nhất trong đề thi:</b><br>
• <b>mustn't + V</b> = CẤM, không được làm: <i>You <b>mustn't park</b> here.</i> (Cấm đỗ xe)<br>
• <b>don't have to / don't need to + V</b> = KHÔNG CẦN làm (làm cũng được): <i>You <b>don't have to come</b> early.</i> (Không cần đến sớm)</div>

<h3>3. Suy luận: must / can't</h3>
<ul>
<li><b>must + V</b>: chắc hẳn là (suy luận khẳng định gần như chắc chắn): <i>He has a Rolls-Royce. He <b>must be</b> rich.</i></li>
<li><b>can't + V</b>: không thể nào (suy luận phủ định): <i>She <b>can't be</b> at home. The lights are off.</i></li>
</ul>
<div class="ex">You've been working all day. You <b>must be</b> tired.<span class="vi">→ Bạn làm việc cả ngày rồi. Chắc hẳn bạn mệt lắm.</span></div>
<div class="ex">He <b>can't be</b> John's father — he's too young!<span class="vi">→ Ông ấy không thể là bố của John được — ông ấy quá trẻ!</span></div>

<h3>4. need</h3>
<ul>
<li><b>need to + V</b>: cần làm gì — <i>I <b>need to buy</b> some milk.</i></li>
<li><b>needn't + V</b> (= don't have to): không cần — <i>You <b>needn't worry</b>.</i></li>
</ul>
<div class="note"><b>💡 Quá khứ:</b> must (bắt buộc) → <b>had to</b>: <i>I <b>had to</b> work late yesterday.</i></div>
""",
 'questions': [
  ('You ___ drive over 60 km/h in this area. It is against the law.', "don't have to", "mustn't", "needn't", "shouldn't have", 'B',
   '"against the law" (phạm luật) → sự CẤM ĐOÁN tuyệt đối: mustn\'t (không được phép). "Don\'t have to" nghĩa là "không cần" — sai nghĩa.'),
  ("Tomorrow is Sunday, so I ___ get up early.", "mustn't", "don't have to", "can't", "may not", 'B',
   'Chủ nhật không phải đi làm → KHÔNG CẦN dậy sớm (chứ không phải bị cấm) → don\'t have to.'),
  ('Look! That man is climbing into the window. He ___ be a thief!', 'must', "can't", 'should', 'need', 'A',
   'Suy luận gần như chắc chắn dựa trên bằng chứng (trèo cửa sổ) → must be (chắc hẳn là trộm).'),
  ("She ___ be Vietnamese. She doesn't speak a word of Vietnamese.", 'must', 'has to', "can't", 'should', 'C',
   'Suy luận PHỦ ĐỊNH (không thể nào là người Việt vì không nói được tiếng Việt) → can\'t be.'),
  ('In my school, students ___ wear a uniform. It is a rule.', 'have to', 'might', 'could', "needn't", 'A',
   'Quy định của nhà trường (bắt buộc từ bên ngoài) → have to wear.'),
  ('I ___ work late yesterday because we had an urgent project.', 'must', 'have to', 'had to', 'should', 'C',
   '"Must" không có dạng quá khứ → thay bằng had to: I had to work late yesterday (hôm qua tôi đã phải làm muộn).'),
  ('You ___ shout. I can hear you clearly.', "mustn't", "needn't", "can't", "may not", 'B',
   'Không CẦN hét lên (vì tôi nghe rõ rồi) → needn\'t (= don\'t have to). Mustn\'t = cấm, quá mạnh so với ngữ cảnh.'),
  ('Passengers ___ fasten their seatbelts during take-off.', 'might', 'must', 'could', 'would', 'B',
   'Quy định an toàn hàng không bắt buộc → must fasten (phải thắt dây an toàn).'),
 ],
},
{
 'order': 8, 'level': 'B1',
 'title': 'Conditionals & Wishes',
 'title_vi': 'Câu điều kiện & câu ước',
 'description': 'Câu điều kiện loại 0, 1, 2, 3 và cấu trúc wish.',
 'content': """
<h3>1. Bốn loại câu điều kiện</h3>
<table>
<tr><th>Loại</th><th>Mệnh đề If</th><th>Mệnh đề chính</th><th>Dùng khi</th></tr>
<tr><td><b>0</b></td><td>hiện tại đơn</td><td>hiện tại đơn</td><td>Chân lý, thói quen</td></tr>
<tr><td><b>1</b></td><td>hiện tại đơn</td><td>will + V</td><td>Có thể xảy ra ở tương lai</td></tr>
<tr><td><b>2</b></td><td>quá khứ đơn</td><td>would + V</td><td>Không có thật ở hiện tại</td></tr>
<tr><td><b>3</b></td><td>had + V3</td><td>would have + V3</td><td>Không có thật trong quá khứ (tiếc nuối)</td></tr>
</table>
<div class="ex"><b>Loại 0:</b> If you <b>heat</b> ice, it <b>melts</b>.<span class="vi">→ Nếu đun nóng đá, nó tan chảy. (chân lý)</span></div>
<div class="ex"><b>Loại 1:</b> If it <b>rains</b> tomorrow, we <b>will stay</b> at home.<span class="vi">→ Nếu mai mưa, chúng tôi sẽ ở nhà. (hoàn toàn có thể xảy ra)</span></div>
<div class="ex"><b>Loại 2:</b> If I <b>had</b> a lot of money, I <b>would travel</b> around the world.<span class="vi">→ Nếu tôi có nhiều tiền, tôi sẽ đi du lịch vòng quanh thế giới. (thực tế là không có tiền)</span></div>
<div class="ex"><b>Loại 3:</b> If you <b>had studied</b> harder, you <b>would have passed</b> the exam.<span class="vi">→ Nếu bạn học chăm hơn thì đã đỗ rồi. (thực tế: đã không học chăm và đã trượt)</span></div>
<div class="note"><b>💡 Ghi nhớ:</b> Loại 2 với "to be" dùng <b>were</b> cho mọi ngôi: <i>If I <b>were</b> you, I would accept the offer.</i> (Nếu tôi là bạn... — câu khuyên kinh điển)</div>

<h3>2. unless = if ... not</h3>
<div class="ex"><b>Unless</b> you hurry, you will miss the train. (= If you <b>don't</b> hurry...)<span class="vi">→ Trừ khi bạn nhanh lên, bạn sẽ lỡ tàu.</span></div>

<h3>3. Câu ước với wish</h3>
<table>
<tr><th>Ước về</th><th>Cấu trúc</th><th>Ví dụ</th></tr>
<tr><td>Hiện tại</td><td>wish + QK đơn</td><td>I wish I <b>knew</b> the answer.</td></tr>
<tr><td>Quá khứ</td><td>wish + QK hoàn thành</td><td>I wish I <b>hadn't said</b> that.</td></tr>
<tr><td>Tương lai (phàn nàn)</td><td>wish + would + V</td><td>I wish he <b>would stop</b> smoking.</td></tr>
</table>
<div class="ex">I wish I <b>were</b> taller.<span class="vi">→ Ước gì tôi cao hơn. (thực tế hiện tại: không cao)</span></div>
""",
 'questions': [
  ('If it rains this afternoon, we ___ the picnic.', 'cancel', 'will cancel', 'would cancel', 'cancelled', 'B',
   'Điều kiện CÓ THỂ xảy ra ở tương lai (chiều nay có thể mưa) → câu điều kiện loại 1: If + hiện tại đơn, will + V.'),
  ('If I ___ you, I would take that job.', 'am', 'was', 'were', 'be', 'C',
   'Câu điều kiện loại 2 (giả định không có thật), động từ "to be" dùng WERE cho mọi ngôi: If I were you.'),
  ('If she had left earlier, she ___ the bus.', "wouldn't miss", "wouldn't have missed", "won't miss", "didn't miss", 'B',
   'Mệnh đề if chia QK hoàn thành (had left) → điều kiện loại 3 (tiếc nuối quá khứ): would have + V3 → wouldn\'t have missed.'),
  ('You will fail the exam ___ you study harder.', 'if', 'when', 'unless', 'because', 'C',
   '"Unless" = if...not: Bạn sẽ trượt TRỪ KHI học chăm hơn. Dùng "if" sẽ ngược nghĩa (nếu học chăm mà vẫn trượt).'),
  ('If you heat water to 100°C, it ___ .', 'boils', 'will boil', 'would boil', 'boiled', 'A',
   'Chân lý khoa học → câu điều kiện loại 0: If + hiện tại đơn, hiện tại đơn → boils.'),
  ('I wish I ___ how to drive a car.', 'know', 'knew', 'have known', 'will know', 'B',
   'Ước về HIỆN TẠI (bây giờ không biết lái xe) → wish + quá khứ đơn: knew.'),
  ('If I ___ enough money now, I would buy that laptop.', 'have', 'had', 'had had', 'will have', 'B',
   '"Now" + would ở mệnh đề chính → điều kiện loại 2 (không có thật ở hiện tại): If + quá khứ đơn → had.'),
  ('She wishes she ___ to the party last night.', 'went', 'had gone', 'would go', 'goes', 'B',
   'Ước về QUÁ KHỨ ("last night" — tiếc vì đã không đi) → wish + quá khứ hoàn thành: had gone.'),
 ],
},
{
 'order': 9, 'level': 'B1',
 'title': 'The Passive Voice',
 'title_vi': 'Câu bị động',
 'description': 'Chuyển câu chủ động sang bị động ở các thì; bị động với modal verbs.',
 'content': """
<h3>1. Cấu trúc chung</h3>
<p><b>be + V3 (past participle)</b> — "be" chia theo thì của câu chủ động; tân ngữ câu chủ động lên làm chủ ngữ.</p>
<table>
<tr><th>Thì</th><th>Chủ động</th><th>Bị động</th></tr>
<tr><td>Hiện tại đơn</td><td>They <b>make</b> cars here.</td><td>Cars <b>are made</b> here.</td></tr>
<tr><td>HT tiếp diễn</td><td>They <b>are building</b> a bridge.</td><td>A bridge <b>is being built</b>.</td></tr>
<tr><td>Quá khứ đơn</td><td>He <b>wrote</b> this book in 1990.</td><td>This book <b>was written</b> in 1990.</td></tr>
<tr><td>HT hoàn thành</td><td>Someone <b>has stolen</b> my bike.</td><td>My bike <b>has been stolen</b>.</td></tr>
<tr><td>Tương lai (will)</td><td>They <b>will announce</b> the results.</td><td>The results <b>will be announced</b>.</td></tr>
<tr><td>Modal</td><td>You <b>must do</b> it now.</td><td>It <b>must be done</b> now.</td></tr>
</table>
<div class="ex">Rice <b>is grown</b> in the Mekong Delta.<span class="vi">→ Lúa được trồng ở Đồng bằng sông Cửu Long.</span></div>
<div class="ex">The letter <b>was sent</b> two days ago.<span class="vi">→ Bức thư đã được gửi cách đây 2 ngày.</span></div>

<h3>2. Khi nào dùng bị động?</h3>
<ul>
<li>Không biết/không quan trọng ai làm: <i>My wallet <b>was stolen</b>.</i></li>
<li>Muốn nhấn mạnh đối tượng chịu tác động.</li>
<li>Thêm "by + tác nhân" nếu cần: <i>This song <b>was written by</b> Trinh Cong Son.</i></li>
</ul>

<h3>3. Các bước chuyển đổi</h3>
<div class="note">
<b>Chủ động:</b> The chef <u>cooks</u> <i>the meals</i>. (Đầu bếp nấu các bữa ăn.)<br>
<b>Bước 1:</b> Tân ngữ "the meals" → chủ ngữ.<br>
<b>Bước 2:</b> Thì hiện tại đơn → be = are. <b>Bước 3:</b> cooks → V3 = cooked.<br>
<b>Bị động:</b> <i>The meals</i> <u>are cooked</u> (by the chef).
</div>
<div class="warn"><b>⚠️ Lỗi thường gặp:</b> Quên chia "be" đúng thì, hoặc quên dùng V3. Nội động từ (happen, die, arrive, sleep...) KHÔNG có dạng bị động: ✗ <s>The accident was happened.</s> → ✓ The accident <b>happened</b>.</div>
""",
 'questions': [
  ('English ___ all over the world.', 'speaks', 'is spoken', 'is speaking', 'spoke', 'B',
   'Tiếng Anh ĐƯỢC NÓI (bị động, hiện tại đơn): is/are + V3 → is spoken. Chủ ngữ "English" không tự "nói" được.'),
  ('This bridge ___ in 2005.', 'built', 'was built', 'was building', 'is built', 'B',
   'Cây cầu ĐƯỢC XÂY (bị động) + thời điểm quá khứ "in 2005" → was built.'),
  ('The report must ___ before Friday.', 'finish', 'be finished', 'be finishing', 'finished', 'B',
   'Bị động với modal verb: modal + be + V3 → must be finished (báo cáo phải ĐƯỢC hoàn thành).'),
  ('A new hospital ___ in our city at the moment.', 'is built', 'is being built', 'builds', 'has built', 'B',
   '"at the moment" → hiện tại tiếp diễn + bị động: is/are being + V3 → is being built (đang được xây).'),
  ('My laptop ___ . I left it in the café and now it is gone!', 'has stolen', 'has been stolen', 'was stealing', 'stole', 'B',
   'Kết quả còn ảnh hưởng hiện tại (giờ không còn) + bị động → hiện tại hoàn thành bị động: has been stolen.'),
  ('The accident ___ at the crossroads last night.', 'was happened', 'happened', 'was happening by', 'is happened', 'B',
   '"Happen" là NỘI động từ (không có tân ngữ) nên KHÔNG có dạng bị động → chia chủ động quá khứ đơn: happened.'),
  ('These photos ___ by my brother.', 'took', 'were taken', 'were taking', 'take', 'B',
   'Có "by my brother" (tác nhân) → câu bị động; "photos" số nhiều, quá khứ → were taken.'),
  ('The winners ___ next Monday.', 'will announce', 'will be announced', 'are announcing', 'announce', 'B',
   'Người thắng cuộc ĐƯỢC CÔNG BỐ (bị động, tương lai): will + be + V3 → will be announced.'),
 ],
},
{
 'order': 10, 'level': 'B2',
 'title': 'Reported Speech',
 'title_vi': 'Câu tường thuật (gián tiếp)',
 'description': 'Tường thuật câu kể, câu hỏi, câu mệnh lệnh; quy tắc lùi thì.',
 'content': """
<h3>1. Quy tắc lùi thì</h3>
<table>
<tr><th>Câu trực tiếp</th><th>Câu gián tiếp</th></tr>
<tr><td>Hiện tại đơn (V/Vs)</td><td>Quá khứ đơn (V2)</td></tr>
<tr><td>Hiện tại tiếp diễn (am/is/are + V-ing)</td><td>QK tiếp diễn (was/were + V-ing)</td></tr>
<tr><td>Hiện tại hoàn thành (have/has + V3)</td><td>QK hoàn thành (had + V3)</td></tr>
<tr><td>Quá khứ đơn (V2)</td><td>QK hoàn thành (had + V3)</td></tr>
<tr><td>will</td><td>would</td></tr>
<tr><td>can</td><td>could</td></tr>
<tr><td>must / have to</td><td>had to</td></tr>
</table>
<div class="ex">"I <b>am</b> tired," she said. → She said (that) she <b>was</b> tired.<span class="vi">→ Cô ấy nói rằng cô ấy mệt.</span></div>

<h3>2. Đổi trạng từ thời gian – nơi chốn</h3>
<table>
<tr><th>Trực tiếp</th><th>Gián tiếp</th></tr>
<tr><td>now / today / tonight</td><td>then / that day / that night</td></tr>
<tr><td>tomorrow</td><td>the next day / the following day</td></tr>
<tr><td>yesterday</td><td>the day before / the previous day</td></tr>
<tr><td>ago</td><td>before</td></tr>
<tr><td>here / this</td><td>there / that</td></tr>
</table>

<h3>3. Tường thuật câu hỏi</h3>
<ul>
<li><b>Câu hỏi Wh-:</b> asked + wh-word + <b>S + V</b> (trật tự câu kể, KHÔNG đảo): <br><i>"Where <b>do you live</b>?" → He asked me where <b>I lived</b>.</i></li>
<li><b>Câu hỏi Yes/No:</b> asked + <b>if/whether</b> + S + V: <br><i>"Are you hungry?" → She asked <b>if I was</b> hungry.</i></li>
</ul>
<div class="warn"><b>⚠️ Lỗi kinh điển:</b> Giữ nguyên đảo ngữ trong câu hỏi gián tiếp: ✗ <s>He asked where did I live.</s> → ✓ He asked where I lived.</div>

<h3>4. Tường thuật mệnh lệnh, yêu cầu</h3>
<ul>
<li><b>told/asked + O + to V:</b> <i>"Close the door!" → He <b>told me to close</b> the door.</i></li>
<li><b>Phủ định:</b> told + O + <b>not to</b> V: <i>"Don't be late!" → She told us <b>not to be</b> late.</i></li>
</ul>
<div class="ex">"Please help me," he said. → He <b>asked me to help</b> him.<span class="vi">→ Anh ấy nhờ tôi giúp.</span></div>
""",
 'questions': [
  ('"I am learning English," she said. → She said she ___ English.', 'is learning', 'was learning', 'learned', 'has learned', 'B',
   'Lùi thì: hiện tại tiếp diễn (am learning) → quá khứ tiếp diễn (was learning).'),
  ('"I will call you tomorrow," he said. → He said he ___ me the next day.', 'will call', 'would call', 'called', 'calls', 'B',
   'Lùi thì: will → would; "tomorrow" đổi thành "the next day" → would call.'),
  ('He asked me where ___ .', 'do I live', 'did I live', 'I lived', 'I live', 'C',
   'Câu hỏi gián tiếp dùng trật tự CÂU KỂ (S + V), không đảo trợ động từ, và lùi thì live → lived: where I lived.'),
  ('She asked me ___ I liked coffee.', 'what', 'if', 'that', 'which', 'B',
   'Tường thuật câu hỏi Yes/No ("Do you like coffee?") → dùng if/whether: asked me if I liked coffee.'),
  ('The teacher told us ___ in the library.', "don't talk", 'not to talk', 'not talking', 'to not talking', 'B',
   'Tường thuật mệnh lệnh phủ định: told + O + NOT TO + V → not to talk.'),
  ('"I saw this film last week," Tom said. → Tom said he ___ that film the week before.', 'saw', 'has seen', 'had seen', 'would see', 'C',
   'Lùi thì: quá khứ đơn (saw) → quá khứ hoàn thành (had seen); "last week" → "the week before".'),
  ('"Can you swim?" she asked. → She asked me if I ___ swim.', 'can', 'could', 'may', 'will', 'B',
   'Lùi thì modal: can → could. Câu hỏi Yes/No dùng if: asked me if I could swim.'),
  ('"Please open the window," he said to me. → He ___ me to open the window.', 'said', 'told', 'asked', 'spoke', 'C',
   '"Please" thể hiện lời NHỜ/yêu cầu lịch sự → asked + O + to V. "Said" không đi trực tiếp với tân ngữ + to V; "told" thiên về ra lệnh.'),
 ],
},
]
