"""
Script to update grammar lesson content - Units 6-10.
Run: set PYTHONUTF8=1 && venv\Scripts\python update_grammar2.py
"""
import os, sys, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vstep.settings')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
django.setup()

from learning.models import Unit, GrammarLesson

CONTENT = {}

# ============================================================
# UNIT 6: Comparatives & Superlatives
# ============================================================
CONTENT[6] = """
<h3>1. So sánh hơn (Comparative)</h3>

<h4>1.1. Tính từ ngắn (1 âm tiết, hoặc 2 âm tiết tận cùng -y, -er, -ow, -le)</h4>
<table>
<tr><th>Công thức</th><th>Ví dụ</th></tr>
<tr><td>S1 + V + <b>adj-er + than</b> + S2</td><td>She is <b>taller than</b> her sister.<br>This book is <b>cheaper than</b> that one.</td></tr>
</table>

<p><b>Quy tắc thêm -er:</b></p>
<table>
<tr><th>Trường hợp</th><th>Quy tắc</th><th>Ví dụ</th></tr>
<tr><td>Hầu hết</td><td>Thêm <b>-er</b></td><td>tall → tall<b>er</b>, old → old<b>er</b>, fast → fast<b>er</b></td></tr>
<tr><td>Tận cùng -e</td><td>Thêm <b>-r</b></td><td>nice → nice<b>r</b>, large → large<b>r</b></td></tr>
<tr><td>1 nguyên âm + 1 phụ âm</td><td>Gấp đôi phụ âm + <b>-er</b></td><td>big → bi<b>gg</b>er, hot → ho<b>tt</b>er, thin → thi<b>nn</b>er</td></tr>
<tr><td>Tận cùng phụ âm + y</td><td>Đổi y → <b>ier</b></td><td>happy → happ<b>ier</b>, easy → eas<b>ier</b>, heavy → heav<b>ier</b></td></tr>
</table>

<h4>1.2. Tính từ dài (2 âm tiết trở lên)</h4>
<table>
<tr><th>Công thức</th><th>Ví dụ</th></tr>
<tr><td>S1 + V + <b>more + adj + than</b> + S2</td><td>English is <b>more interesting than</b> math.<br>This phone is <b>more expensive than</b> mine.</td></tr>
</table>

<h4>1.3. Tính từ bất quy tắc</h4>
<table>
<tr><th>Nguyên gốc</th><th>So sánh hơn</th><th>So sánh nhất</th></tr>
<tr><td>good / well</td><td><b>better</b></td><td>the <b>best</b></td></tr>
<tr><td>bad / badly</td><td><b>worse</b></td><td>the <b>worst</b></td></tr>
<tr><td>far</td><td><b>farther / further</b></td><td>the <b>farthest / furthest</b></td></tr>
<tr><td>much / many</td><td><b>more</b></td><td>the <b>most</b></td></tr>
<tr><td>little</td><td><b>less</b></td><td>the <b>least</b></td></tr>
<tr><td>old</td><td><b>older / elder</b></td><td>the <b>oldest / eldest</b></td></tr>
</table>
<div class="note"><b>💡 Lưu ý:</b><br>
• <b>farther</b> = xa hơn (khoảng cách vật lý). <b>further</b> = xa hơn (khoảng cách HOẶC nghĩa bóng: "further information" = thêm thông tin).<br>
• <b>elder/eldest</b> = chỉ dùng cho anh chị em trong gia đình ("my elder brother"). <b>older/oldest</b> = dùng chung.</div>

<h4>1.4. Ví dụ chi tiết</h4>
<div class="ex">Hanoi is <b>bigger than</b> Hue.<span class="vi">→ Hà Nội lớn hơn Huế.</span></div>
<div class="ex">Learning English is <b>more difficult than</b> I expected.<span class="vi">→ Học tiếng Anh khó hơn tôi nghĩ.</span></div>
<div class="ex">She speaks English <b>better than</b> me.<span class="vi">→ Cô ấy nói tiếng Anh giỏi hơn tôi. (bất quy tắc: good → better)</span></div>
<div class="ex">The weather today is <b>worse than</b> yesterday.<span class="vi">→ Thời tiết hôm nay tệ hơn hôm qua. (bất quy tắc: bad → worse)</span></div>

<h3>2. So sánh nhất (Superlative)</h3>

<h4>2.1. Công thức</h4>
<table>
<tr><th>Tính từ ngắn</th><th>Tính từ dài</th></tr>
<tr><td>S + V + <b>the + adj-est</b></td><td>S + V + <b>the most + adj</b></td></tr>
<tr><td>She is <b>the tallest</b> in her class.</td><td>This is <b>the most beautiful</b> city I've seen.</td></tr>
</table>

<p><b>Quy tắc thêm -est:</b> Giống thêm -er nhưng thay bằng -est (biggest, happiest, nicest...).</p>

<div class="ex">Mount Fansipan is <b>the highest</b> mountain in Vietnam.<span class="vi">→ Fansipan là ngọn núi cao nhất Việt Nam.</span></div>
<div class="ex">Ho Chi Minh City is <b>the most crowded</b> city in Vietnam.<span class="vi">→ TP.HCM là thành phố đông đúc nhất Việt Nam.</span></div>
<div class="ex">This is <b>the best</b> restaurant in town.<span class="vi">→ Đây là nhà hàng ngon nhất trong thành phố. (bất quy tắc)</span></div>
<div class="ex">That was <b>the worst</b> movie I have ever seen.<span class="vi">→ Đó là bộ phim tệ nhất tôi từng xem.</span></div>

<div class="warn"><b>⚠️ Luôn dùng THE trước so sánh nhất:</b><br>
✗ <s>She is tallest in the class.</s> → ✓ She is <b>the tallest</b> in the class.<br>
✗ <s>This is most important thing.</s> → ✓ This is <b>the most important</b> thing.</div>

<h3>3. So sánh bằng (as...as)</h3>
<table>
<tr><th>Dạng</th><th>Cấu trúc</th><th>Ví dụ</th></tr>
<tr><td>Khẳng định</td><td>S1 + V + <b>as + adj + as</b> + S2</td><td>She is <b>as tall as</b> her mother.<br><i>(Cô ấy cao bằng mẹ.)</i></td></tr>
<tr><td>Phủ định</td><td>S1 + V + <b>not as/so + adj + as</b> + S2</td><td>This bag is <b>not as expensive as</b> that one.<br><i>(Túi này không đắt bằng túi kia.)</i></td></tr>
</table>

<div class="ex">My house is <b>as big as</b> yours.<span class="vi">→ Nhà tôi lớn bằng nhà bạn.</span></div>
<div class="ex">He doesn't run <b>as fast as</b> his brother.<span class="vi">→ Anh ấy chạy không nhanh bằng anh trai.</span></div>
<div class="ex">Living in the city is <b>not as quiet as</b> living in the countryside.<span class="vi">→ Sống ở thành phố không yên tĩnh bằng sống ở nông thôn.</span></div>

<h3>4. Các cấu trúc so sánh nâng cao</h3>

<p><b>① So sánh kép (càng... càng...)</b></p>
<table>
<tr><th>Công thức</th><th>Ví dụ</th></tr>
<tr><td><b>The + comparative, the + comparative</b></td><td><b>The more</b> you practice, <b>the better</b> you become.<br><i>(Càng luyện tập nhiều, bạn càng giỏi hơn.)</i></td></tr>
</table>
<div class="ex"><b>The harder</b> you study, <b>the higher</b> your score will be.<span class="vi">→ Bạn càng học chăm, điểm càng cao.</span></div>
<div class="ex"><b>The more expensive</b> the hotel, <b>the better</b> the service.<span class="vi">→ Khách sạn càng đắt, dịch vụ càng tốt.</span></div>

<p><b>② So sánh bội số (gấp mấy lần)</b></p>
<table>
<tr><th>Công thức</th><th>Ví dụ</th></tr>
<tr><td>S + V + <b>twice/three times... as + adj + as</b></td><td>This car is <b>twice as expensive as</b> that one.<br><i>(Xe này đắt gấp đôi xe kia.)</i></td></tr>
</table>
<div class="ex">Her salary is <b>three times as high as</b> mine.<span class="vi">→ Lương cô ấy cao gấp ba lần lương tôi.</span></div>

<p><b>③ Nhấn mạnh so sánh hơn</b></p>
<p>Dùng: <i>much, far, a lot, significantly, considerably</i> + comparative</p>
<div class="ex">Tokyo is <b>much bigger than</b> Hanoi.<span class="vi">→ Tokyo lớn hơn Hà Nội nhiều. (much nhấn mạnh)</span></div>
<div class="ex">She is <b>far more talented than</b> her classmates.<span class="vi">→ Cô ấy tài năng hơn các bạn cùng lớp rất nhiều.</span></div>
<div class="ex">This exercise is <b>a lot easier than</b> the last one.<span class="vi">→ Bài tập này dễ hơn bài trước nhiều.</span></div>

<div class="warn"><b>⚠️ KHÔNG dùng "very" với so sánh hơn:</b><br>
✗ <s>She is very taller than me.</s> → ✓ She is <b>much taller</b> than me.</div>

<h3>5. Mẹo làm bài thi VSTEP</h3>
<div class="note"><b>💡 Chiến lược:</b><br>
<b>1.</b> Đếm số âm tiết của tính từ: 1 âm → -er/-est. 2 âm tận cùng -y → -ier/-iest. 2+ âm → more/most.<br>
<b>2.</b> Nhớ các tính từ bất quy tắc: good-better-best, bad-worse-worst.<br>
<b>3.</b> "Than" → so sánh hơn. "The...in/of" → so sánh nhất. "As...as" → so sánh bằng.<br>
<b>4.</b> "The more..., the more..." → so sánh kép (càng... càng...).<br>
<b>5.</b> Nhấn mạnh so sánh hơn dùng: much, far, a lot (KHÔNG dùng very).</div>
"""

# ============================================================
# UNIT 7: Modal Verbs
# ============================================================
CONTENT[7] = """
<h3>1. Tổng quan về động từ khuyết thiếu (Modal Verbs)</h3>

<p>Modal verbs là nhóm động từ đặc biệt đứng trước động từ chính, dùng để diễn tả khả năng, sự cho phép, nghĩa vụ, lời khuyên...</p>

<table>
<tr><th>Đặc điểm</th><th>Giải thích</th></tr>
<tr><td>Không chia theo ngôi</td><td>He <b>can</b> swim. (KHÔNG thêm -s: <s>He cans swim.</s>)</td></tr>
<tr><td>Sau modal + V nguyên mẫu</td><td>She <b>must go</b>. (KHÔNG: <s>She must to go / She must going.</s>)</td></tr>
<tr><td>Phủ định: modal + not</td><td>You <b>must not</b> smoke here. / He <b>can't</b> come.</td></tr>
<tr><td>Nghi vấn: đảo modal lên trước S</td><td><b>Can</b> you help me? / <b>Should</b> I call her?</td></tr>
</table>

<h3>2. Can / Could / Be able to – Khả năng</h3>

<h4>2.1. Can – Khả năng ở hiện tại</h4>
<div class="ex">She <b>can speak</b> three languages.<span class="vi">→ Cô ấy có thể nói ba thứ tiếng. (khả năng)</span></div>
<div class="ex"><b>Can</b> I sit here?<span class="vi">→ Tôi ngồi đây được không? (xin phép)</span></div>
<div class="ex">It <b>can be</b> very cold in Sapa in winter.<span class="vi">→ Sapa có thể rất lạnh vào mùa đông. (khả năng xảy ra)</span></div>

<h4>2.2. Could – Quá khứ / lịch sự / khả năng thấp</h4>
<div class="ex">I <b>could swim</b> when I was five.<span class="vi">→ Tôi biết bơi khi 5 tuổi. (khả năng trong quá khứ)</span></div>
<div class="ex"><b>Could</b> you open the window, please?<span class="vi">→ Bạn mở cửa sổ giùm được không? (lịch sự hơn can)</span></div>
<div class="ex">She <b>could be</b> at home right now.<span class="vi">→ Cô ấy có thể đang ở nhà. (phỏng đoán, không chắc lắm)</span></div>

<h4>2.3. Be able to – Thay thế can ở các thì khác</h4>
<div class="ex">I will <b>be able to</b> drive next year.<span class="vi">→ Năm sau tôi sẽ biết lái xe. (can không có dạng tương lai → dùng will be able to)</span></div>
<div class="ex">She has <b>been able to</b> speak English since she was 10.<span class="vi">→ Cô ấy đã nói được tiếng Anh từ năm 10 tuổi. (can không có dạng hoàn thành → dùng has been able to)</span></div>

<h3>3. Must / Have to / Should – Nghĩa vụ & Lời khuyên</h3>

<h4>3.1. Must – Bắt buộc (từ người nói, nội quy)</h4>
<div class="ex">You <b>must wear</b> a helmet when riding a motorbike.<span class="vi">→ Bạn phải đội mũ bảo hiểm khi đi xe máy. (luật pháp, bắt buộc)</span></div>
<div class="ex">I <b>must finish</b> this report today.<span class="vi">→ Tôi phải hoàn thành báo cáo hôm nay. (tự đặt nghĩa vụ cho mình)</span></div>

<h4>3.2. Have to – Bắt buộc (do hoàn cảnh bên ngoài)</h4>
<div class="ex">I <b>have to</b> get up early tomorrow. I have an exam.<span class="vi">→ Ngày mai tôi phải dậy sớm. Tôi có bài thi. (do hoàn cảnh)</span></div>
<div class="ex">She <b>had to</b> work late yesterday.<span class="vi">→ Hôm qua cô ấy phải làm việc muộn. (quá khứ — must không có dạng quá khứ)</span></div>

<h4>3.3. Phân biệt must not vs don't have to</h4>
<table>
<tr><th>must not (mustn't)</th><th>don't have to</th></tr>
<tr><td><b>CẤM</b>, không được phép</td><td><b>KHÔNG CẦN</b>, không bắt buộc</td></tr>
<tr><td>You <b>mustn't</b> park here.<br><i>(Cấm đỗ xe ở đây.)</i></td><td>You <b>don't have to</b> come if you're busy.<br><i>(Bạn không cần đến nếu bạn bận.)</i></td></tr>
<tr><td>You <b>mustn't</b> tell anyone.<br><i>(Cấm nói cho ai biết.)</i></td><td>You <b>don't have to</b> wear a suit.<br><i>(Bạn không cần mặc vest — nhưng mặc cũng được.)</i></td></tr>
</table>

<div class="warn"><b>⚠️ Rất dễ nhầm! Ghi nhớ:</b><br>
<b>mustn't</b> = CẤM! KHÔNG ĐƯỢC! (prohibition)<br>
<b>don't have to</b> = Không cần, tùy bạn (no obligation, optional)</div>

<h4>3.4. Should / Ought to – Lời khuyên</h4>
<div class="ex">You <b>should study</b> harder if you want to pass the VSTEP exam.<span class="vi">→ Bạn nên học chăm hơn nếu muốn đỗ kỳ thi VSTEP. (khuyên)</span></div>
<div class="ex">You <b>shouldn't eat</b> too much fast food.<span class="vi">→ Bạn không nên ăn quá nhiều đồ ăn nhanh.</span></div>
<div class="ex">You <b>ought to</b> see a doctor.<span class="vi">→ Bạn nên đi khám bác sĩ. (= should, trang trọng hơn một chút)</span></div>

<h3>4. May / Might – Khả năng xảy ra</h3>
<table>
<tr><th>Modal</th><th>Mức độ chắc chắn</th><th>Ví dụ</th></tr>
<tr><td><b>must</b></td><td>~95% (gần như chắc chắn)</td><td>She <b>must be</b> tired. She's been working all day.<br><i>(Cô ấy chắc hẳn mệt lắm.)</i></td></tr>
<tr><td><b>may / could</b></td><td>~50% (có thể)</td><td>It <b>may rain</b> this afternoon.<br><i>(Chiều nay có thể mưa.)</i></td></tr>
<tr><td><b>might</b></td><td>~30% (có lẽ, ít chắc)</td><td>He <b>might come</b> to the party.<br><i>(Anh ấy có lẽ sẽ đến bữa tiệc — không chắc lắm.)</i></td></tr>
<tr><td><b>can't</b></td><td>~0% (chắc chắn không)</td><td>She <b>can't be</b> 60. She looks so young!<br><i>(Cô ấy không thể 60 tuổi được. Trông trẻ quá!)</i></td></tr>
</table>

<div class="ex">He's not answering the phone. He <b>must be</b> busy.<span class="vi">→ Anh ấy không nghe điện. Anh ấy chắc hẳn đang bận.</span></div>
<div class="ex">Where is she? She <b>may be</b> at the library.<span class="vi">→ Cô ấy đâu rồi? Cô ấy có thể ở thư viện.</span></div>
<div class="ex">That <b>can't be</b> true!<span class="vi">→ Điều đó không thể đúng được!</span></div>

<h3>5. Shall / Will – Đề nghị & Tương lai</h3>
<div class="ex"><b>Shall</b> I help you with your bags?<span class="vi">→ Tôi giúp bạn xách túi nhé? (đề nghị giúp)</span></div>
<div class="ex"><b>Shall</b> we go to the cinema tonight?<span class="vi">→ Tối nay mình đi xem phim nhé? (gợi ý)</span></div>
<div class="note"><b>💡</b> <b>Shall</b> chỉ dùng với <b>I</b> và <b>we</b> trong câu hỏi, để đề nghị hoặc gợi ý.</div>

<h3>6. Bảng tổng hợp Modal Verbs</h3>
<table>
<tr><th>Modal</th><th>Chức năng</th><th>Ví dụ</th></tr>
<tr><td><b>can</b></td><td>Khả năng, xin phép</td><td>I can swim. / Can I go?</td></tr>
<tr><td><b>could</b></td><td>Khả năng QK, lịch sự, phỏng đoán</td><td>I could swim when I was 5. / Could you help me?</td></tr>
<tr><td><b>must</b></td><td>Bắt buộc, suy luận chắc chắn</td><td>You must stop. / She must be tired.</td></tr>
<tr><td><b>have to</b></td><td>Bắt buộc (hoàn cảnh)</td><td>I have to work tomorrow.</td></tr>
<tr><td><b>should</b></td><td>Lời khuyên</td><td>You should rest.</td></tr>
<tr><td><b>may</b></td><td>Xin phép (trang trọng), có thể</td><td>May I come in? / It may rain.</td></tr>
<tr><td><b>might</b></td><td>Có lẽ (ít chắc hơn may)</td><td>He might be late.</td></tr>
<tr><td><b>shall</b></td><td>Đề nghị, gợi ý (I/We)</td><td>Shall we dance?</td></tr>
</table>

<h3>7. Mẹo làm bài thi VSTEP</h3>
<div class="note"><b>💡 Chiến lược:</b><br>
<b>1.</b> Hỏi "Tôi có nên...?" → <b>should</b>.<br>
<b>2.</b> Bắt buộc, luật lệ → <b>must / have to</b>.<br>
<b>3.</b> Cấm → <b>mustn't</b>. Không cần → <b>don't have to</b>.<br>
<b>4.</b> Khả năng → <b>can</b> (hiện tại), <b>could</b> (quá khứ), <b>will be able to</b> (tương lai).<br>
<b>5.</b> Phỏng đoán: chắc chắn → <b>must</b>; có thể → <b>may/could</b>; ít khả năng → <b>might</b>; chắc chắn không → <b>can't</b>.</div>
"""

# ============================================================
# UNIT 8: Conditionals (If)
# ============================================================
CONTENT[8] = """
<h3>1. Câu điều kiện loại 0 – Sự thật, quy luật</h3>

<h4>1.1. Công thức</h4>
<table>
<tr><th>Mệnh đề If</th><th>Mệnh đề chính</th></tr>
<tr><td>If + S + V (hiện tại đơn)</td><td>S + V (hiện tại đơn)</td></tr>
</table>

<p>Diễn tả <b>sự thật luôn đúng, quy luật tự nhiên, kết quả tất yếu</b>. Có thể thay "if" bằng "when".</p>

<div class="ex">If you <b>heat</b> water to 100°C, it <b>boils</b>.<span class="vi">→ Nếu bạn đun nước đến 100°C, nó sẽ sôi. (quy luật tự nhiên)</span></div>
<div class="ex">If you <b>mix</b> red and yellow, you <b>get</b> orange.<span class="vi">→ Nếu bạn trộn đỏ và vàng, bạn được màu cam.</span></div>
<div class="ex">Plants <b>die</b> if they <b>don't get</b> water.<span class="vi">→ Cây chết nếu không có nước. (sự thật)</span></div>

<h3>2. Câu điều kiện loại 1 – Có thể xảy ra ở hiện tại/tương lai</h3>

<h4>2.1. Công thức</h4>
<table>
<tr><th>Mệnh đề If</th><th>Mệnh đề chính</th></tr>
<tr><td>If + S + V (<b>hiện tại đơn</b>)</td><td>S + <b>will</b> + V</td></tr>
</table>

<p>Diễn tả <b>tình huống có thể xảy ra</b> ở hiện tại hoặc tương lai, và kết quả của nó.</p>

<div class="ex">If it <b>rains</b> tomorrow, I <b>will stay</b> at home.<span class="vi">→ Nếu ngày mai trời mưa, tôi sẽ ở nhà. (có thể mưa, có thể không)</span></div>
<div class="ex">If you <b>study</b> hard, you <b>will pass</b> the exam.<span class="vi">→ Nếu bạn học chăm, bạn sẽ đỗ kỳ thi.</span></div>
<div class="ex">If she <b>doesn't hurry</b>, she <b>will be</b> late.<span class="vi">→ Nếu cô ấy không nhanh lên, cô ấy sẽ muộn.</span></div>
<div class="ex">I <b>won't go</b> to the party if you <b>don't come</b>.<span class="vi">→ Tôi sẽ không đi dự tiệc nếu bạn không đến.</span></div>

<div class="warn"><b>⚠️ Lỗi CỰC phổ biến:</b> Mệnh đề If KHÔNG dùng "will"!<br>
✗ <s>If it <b>will rain</b>, I will stay home.</s><br>
✓ If it <b>rains</b>, I will stay home.<br><br>
✗ <s>If you <b>will study</b> hard, you will pass.</s><br>
✓ If you <b>study</b> hard, you will pass.</div>

<div class="note"><b>💡 Biến thể:</b> Mệnh đề chính có thể dùng: can, may, should, must, hoặc mệnh lệnh.<br>
• If you feel tired, you <b>should</b> rest. (lời khuyên)<br>
• If the fire alarm rings, <b>leave</b> the building immediately. (mệnh lệnh)<br>
• If it stops raining, we <b>can</b> go outside.</div>

<h3>3. Câu điều kiện loại 2 – Không có thật ở hiện tại (giả định)</h3>

<h4>3.1. Công thức</h4>
<table>
<tr><th>Mệnh đề If</th><th>Mệnh đề chính</th></tr>
<tr><td>If + S + V (<b>quá khứ đơn</b>)</td><td>S + <b>would</b> + V</td></tr>
</table>

<p>Diễn tả <b>tình huống không có thật ở hiện tại</b>, tưởng tượng, ước muốn.</p>

<div class="ex">If I <b>had</b> a lot of money, I <b>would travel</b> around the world.<span class="vi">→ Nếu tôi có nhiều tiền, tôi sẽ đi du lịch vòng quanh thế giới. (thực tế: tôi KHÔNG có nhiều tiền)</span></div>
<div class="ex">If I <b>were</b> you, I <b>would accept</b> that job offer.<span class="vi">→ Nếu tôi là bạn, tôi sẽ nhận lời mời làm việc đó. (thực tế: tôi KHÔNG phải bạn)</span></div>
<div class="ex">If she <b>spoke</b> English fluently, she <b>would get</b> a better job.<span class="vi">→ Nếu cô ấy nói tiếng Anh lưu loát, cô ấy sẽ có công việc tốt hơn. (thực tế: cô ấy CHƯA nói lưu loát)</span></div>
<div class="ex">What <b>would</b> you <b>do</b> if you <b>won</b> the lottery?<span class="vi">→ Bạn sẽ làm gì nếu trúng xổ số? (tưởng tượng)</span></div>

<div class="note"><b>💡 Lưu ý:</b><br>
• Với động từ <b>be</b>, dùng <b>"were"</b> cho TẤT CẢ các ngôi (kể cả I, he, she, it):<br>
If I <b>were</b> rich... / If she <b>were</b> here... / If it <b>were</b> possible...<br>
(Trong văn nói, "was" cũng chấp nhận được, nhưng "were" là chuẩn ngữ pháp và dùng trong thi.)</div>

<h3>4. Câu điều kiện loại 3 – Không có thật trong quá khứ (hối tiếc)</h3>

<h4>4.1. Công thức</h4>
<table>
<tr><th>Mệnh đề If</th><th>Mệnh đề chính</th></tr>
<tr><td>If + S + <b>had + V3</b> (quá khứ hoàn thành)</td><td>S + <b>would have + V3</b></td></tr>
</table>

<p>Diễn tả <b>tình huống đã KHÔNG xảy ra trong quá khứ</b> — giả định, hối tiếc.</p>

<div class="ex">If I <b>had studied</b> harder, I <b>would have passed</b> the exam.<span class="vi">→ Nếu tôi đã học chăm hơn, tôi đã đỗ kỳ thi rồi. (thực tế: tôi KHÔNG học chăm → tôi TRƯỢT)</span></div>
<div class="ex">If she <b>had left</b> earlier, she <b>wouldn't have missed</b> the train.<span class="vi">→ Nếu cô ấy rời đi sớm hơn, cô ấy đã không lỡ tàu. (thực tế: cô ấy rời đi MUỘN → lỡ tàu)</span></div>
<div class="ex">If I <b>had known</b> about the party, I <b>would have come</b>.<span class="vi">→ Nếu tôi biết về bữa tiệc, tôi đã đến rồi. (thực tế: tôi KHÔNG biết → không đến)</span></div>
<div class="ex">I <b>would have helped</b> you if you <b>had asked</b> me.<span class="vi">→ Tôi đã giúp bạn rồi nếu bạn nhờ. (thực tế: bạn KHÔNG nhờ)</span></div>

<h3>5. Bảng tổng hợp 4 loại câu điều kiện</h3>
<table>
<tr><th>Loại</th><th>Mệnh đề If</th><th>Mệnh đề chính</th><th>Dùng khi</th></tr>
<tr><td><b>0</b></td><td>V (hiện tại đơn)</td><td>V (hiện tại đơn)</td><td>Sự thật, quy luật</td></tr>
<tr><td><b>1</b></td><td>V (hiện tại đơn)</td><td>will + V</td><td>Có thể xảy ra (tương lai)</td></tr>
<tr><td><b>2</b></td><td>V (quá khứ đơn)</td><td>would + V</td><td>Không thật ở hiện tại</td></tr>
<tr><td><b>3</b></td><td>had + V3</td><td>would have + V3</td><td>Không thật trong quá khứ</td></tr>
</table>

<h3>6. Unless = If...not</h3>
<div class="ex"><b>Unless</b> you study, you will fail. = <b>If</b> you <b>don't</b> study, you will fail.<span class="vi">→ Trừ khi bạn học, bạn sẽ trượt.</span></div>
<div class="ex">I won't go <b>unless</b> you come with me. = I won't go <b>if</b> you <b>don't</b> come with me.<span class="vi">→ Tôi sẽ không đi trừ khi bạn đi cùng.</span></div>

<div class="warn"><b>⚠️ KHÔNG dùng "not" với unless (vì unless đã mang nghĩa phủ định):</b><br>
✗ <s>Unless you don't study...</s> (phủ định kép → sai nghĩa)<br>
✓ Unless you study... = If you don't study...</div>

<h3>7. Mẹo làm bài thi VSTEP</h3>
<div class="note"><b>💡 Chiến lược xác định loại câu điều kiện:</b><br>
<b>1.</b> Đọc nghĩa câu: có thật hay không có thật? Hiện tại hay quá khứ?<br>
<b>2.</b> Nhìn mệnh đề chính: will → loại 1, would → loại 2, would have V3 → loại 3.<br>
<b>3.</b> Kiểm tra mệnh đề If: present → loại 0/1, past → loại 2, had V3 → loại 3.<br>
<b>4.</b> Loại 2: dùng <b>were</b> (không phải was) cho tất cả ngôi với be.<br>
<b>5.</b> Nhớ: mệnh đề If KHÔNG BAO GIỜ dùng will (loại 1) hoặc would (loại 2).</div>
"""

# ============================================================
# UNIT 9: Passive Voice
# ============================================================
CONTENT[9] = """
<h3>1. Câu bị động là gì?</h3>
<p>Câu bị động dùng khi muốn nhấn mạnh <b>đối tượng chịu tác động</b> (người/vật bị làm gì) hơn là người thực hiện hành động.</p>

<table>
<tr><th>Câu chủ động</th><th>Câu bị động</th></tr>
<tr><td>They <b>built</b> this bridge in 2010.</td><td>This bridge <b>was built</b> (by them) in 2010.</td></tr>
<tr><td>Nhấn mạnh: They (người xây)</td><td>Nhấn mạnh: This bridge (cây cầu)</td></tr>
</table>

<h4>1.1. Công thức chung</h4>
<table>
<tr><th>Chủ động</th><th>Bị động</th></tr>
<tr><td>S + V + O</td><td>O (→ S mới) + <b>be + V3</b> + (by + S cũ)</td></tr>
</table>

<h3>2. Bị động ở các thì</h3>
<table>
<tr><th>Thì</th><th>Chủ động</th><th>Bị động</th></tr>
<tr><td>Present Simple</td><td>She <b>cleans</b> the room.</td><td>The room <b>is cleaned</b> (by her).</td></tr>
<tr><td>Present Continuous</td><td>They <b>are building</b> a bridge.</td><td>A bridge <b>is being built</b>.</td></tr>
<tr><td>Past Simple</td><td>He <b>wrote</b> this book.</td><td>This book <b>was written</b> by him.</td></tr>
<tr><td>Past Continuous</td><td>They <b>were repairing</b> the road.</td><td>The road <b>was being repaired</b>.</td></tr>
<tr><td>Present Perfect</td><td>Someone <b>has stolen</b> my bike.</td><td>My bike <b>has been stolen</b>.</td></tr>
<tr><td>Past Perfect</td><td>They <b>had finished</b> the project.</td><td>The project <b>had been finished</b>.</td></tr>
<tr><td>Future (will)</td><td>They <b>will build</b> a new school.</td><td>A new school <b>will be built</b>.</td></tr>
<tr><td>Modal</td><td>You <b>must do</b> this exercise.</td><td>This exercise <b>must be done</b>.</td></tr>
<tr><td>be going to</td><td>They <b>are going to repair</b> it.</td><td>It <b>is going to be repaired</b>.</td></tr>
</table>

<h3>3. Cách chuyển câu chủ động sang bị động</h3>
<div class="note"><b>💡 3 bước cơ bản:</b><br>
<b>Bước 1:</b> Lấy <b>tân ngữ</b> (O) của câu chủ động → làm <b>chủ ngữ</b> câu bị động.<br>
<b>Bước 2:</b> Chia <b>"be" đúng thì</b> + <b>V3</b> (past participle).<br>
<b>Bước 3:</b> Chủ ngữ cũ → <b>"by + ..."</b> (có thể bỏ nếu không quan trọng).</div>

<div class="ex"><b>Chủ động:</b> Someone <b>stole</b> my phone yesterday.<br>
<b>Bước 1:</b> my phone → chủ ngữ mới.<br>
<b>Bước 2:</b> Thì Past Simple → was/were + V3 → was stolen.<br>
<b>Bước 3:</b> someone → bỏ (không quan trọng).<br>
<b>Bị động:</b> My phone <b>was stolen</b> yesterday.<span class="vi">→ Điện thoại của tôi bị mất cắp hôm qua.</span></div>

<div class="ex"><b>Chủ động:</b> People <b>speak</b> English all over the world.<br>
<b>Bị động:</b> English <b>is spoken</b> all over the world.<span class="vi">→ Tiếng Anh được nói trên toàn thế giới.</span></div>

<div class="ex"><b>Chủ động:</b> They <b>are painting</b> the house.<br>
<b>Bị động:</b> The house <b>is being painted</b>.<span class="vi">→ Ngôi nhà đang được sơn.</span></div>

<div class="ex"><b>Chủ động:</b> The government <b>will build</b> a new hospital.<br>
<b>Bị động:</b> A new hospital <b>will be built</b> (by the government).<span class="vi">→ Một bệnh viện mới sẽ được xây.</span></div>

<h3>4. Khi nào dùng câu bị động?</h3>
<table>
<tr><th>Tình huống</th><th>Ví dụ</th></tr>
<tr><td>Không biết / không quan tâm ai làm</td><td>My car <b>was stolen</b>. (ai lấy? Không biết.)</td></tr>
<tr><td>Nhấn mạnh đối tượng chịu tác động</td><td>The Mona Lisa <b>was painted</b> by Leonardo da Vinci.</td></tr>
<tr><td>Văn phong trang trọng, khoa học, tin tức</td><td>The experiment <b>was conducted</b> in 2023.</td></tr>
<tr><td>Quy trình, hướng dẫn</td><td>The rice <b>is washed</b>, then <b>cooked</b> for 20 minutes.</td></tr>
</table>

<h3>5. Bị động với "by" – khi nào giữ, khi nào bỏ?</h3>
<table>
<tr><th>Giữ "by..."</th><th>Bỏ "by..."</th></tr>
<tr><td>Khi người/vật thực hiện là <b>thông tin quan trọng</b></td><td>Khi người thực hiện là <b>ai đó chung chung</b> (someone, people, they)</td></tr>
<tr><td>"Hamlet" was written <b>by Shakespeare</b>.</td><td>English is spoken all over the world. <s>(by people)</s></td></tr>
<tr><td>The cake was made <b>by my mother</b>.</td><td>My phone was stolen. <s>(by someone)</s></td></tr>
</table>

<h3>6. Cấu trúc bị động đặc biệt</h3>

<p><b>① It is said that... / S + is said + to V</b></p>
<div class="ex">People say that he is very rich.<br>
→ <b>It is said that</b> he is very rich.<br>
→ He <b>is said to be</b> very rich.<span class="vi">→ Người ta nói rằng anh ấy rất giàu.</span></div>
<p>Tương tự: <i>It is believed/thought/reported/known/expected that...</i></p>

<p><b>② Have something done (nhờ ai làm)</b></p>
<div class="ex">I <b>had my hair cut</b> yesterday.<span class="vi">→ Tôi đã cắt tóc hôm qua. (nhờ thợ cắt, không tự cắt)</span></div>
<div class="ex">She <b>is having her car repaired</b>.<span class="vi">→ Cô ấy đang (nhờ) sửa xe.</span></div>

<h3>7. Mẹo làm bài thi VSTEP</h3>
<div class="note"><b>💡 Chiến lược:</b><br>
<b>1.</b> Xác định thì của câu chủ động → chia "be" đúng thì + V3.<br>
<b>2.</b> Nhớ công thức: <b>be + V3</b> là cốt lõi của câu bị động ở mọi thì.<br>
<b>3.</b> Modal + bị động: <b>modal + be + V3</b> (can be done, must be finished...).<br>
<b>4.</b> Lưu ý V3 bất quy tắc: written, spoken, stolen, built, made, seen, done...<br>
<b>5.</b> Phân biệt: "is done" (đã xong / bị làm) vs "is being done" (đang bị làm).</div>

<div class="warn"><b>⚠️ Lỗi thường gặp:</b><br>
✗ <s>English is speak all over the world.</s> → ✓ English is <b>spoken</b>. (phải dùng V3!)<br>
✗ <s>The book was wrote by him.</s> → ✓ The book was <b>written</b>. (wrote là V2, phải dùng V3: written)<br>
✗ <s>The house is build in 2010.</s> → ✓ The house <b>was built</b> in 2010. (quá khứ → was, build → built)</div>
"""

# ============================================================
# UNIT 10: Reported Speech (B2)
# ============================================================
CONTENT[10] = """
<h3>1. Câu tường thuật là gì?</h3>
<p>Câu tường thuật (Reported Speech) dùng khi bạn <b>kể lại lời người khác đã nói</b>, thay vì trích dẫn nguyên văn.</p>

<table>
<tr><th>Trực tiếp (Direct)</th><th>Gián tiếp (Reported)</th></tr>
<tr><td>She said, <b>"I am tired."</b></td><td>She said (that) she <b>was</b> tired.</td></tr>
</table>

<h3>2. Quy tắc lùi thì (Backshift)</h3>
<p>Khi động từ tường thuật (said, told...) ở <b>quá khứ</b>, các thì trong lời nói gốc phải <b>lùi một bậc</b>:</p>

<table>
<tr><th>Lời nói gốc</th><th>→ Tường thuật</th><th>Ví dụ</th></tr>
<tr><td>Present Simple</td><td>→ Past Simple</td><td>"I <b>like</b> coffee." → She said she <b>liked</b> coffee.</td></tr>
<tr><td>Present Continuous</td><td>→ Past Continuous</td><td>"I <b>am studying</b>." → He said he <b>was studying</b>.</td></tr>
<tr><td>Past Simple</td><td>→ Past Perfect</td><td>"I <b>went</b> home." → She said she <b>had gone</b> home.</td></tr>
<tr><td>Present Perfect</td><td>→ Past Perfect</td><td>"I <b>have finished</b>." → He said he <b>had finished</b>.</td></tr>
<tr><td>will</td><td>→ would</td><td>"I <b>will call</b> you." → She said she <b>would call</b> me.</td></tr>
<tr><td>can</td><td>→ could</td><td>"I <b>can swim</b>." → He said he <b>could swim</b>.</td></tr>
<tr><td>may</td><td>→ might</td><td>"I <b>may come</b>." → She said she <b>might come</b>.</td></tr>
<tr><td>must</td><td>→ had to</td><td>"I <b>must go</b>." → He said he <b>had to go</b>.</td></tr>
</table>

<div class="note"><b>💡 Không đổi:</b> would, could, might, should, ought to, had better, used to → <b>giữ nguyên</b>.<br>
Past Perfect → <b>giữ nguyên</b> (không lùi nữa).</div>

<h3>3. Đổi đại từ, tính từ sở hữu, trạng từ</h3>

<h4>3.1. Đại từ & Tính từ sở hữu</h4>
<table>
<tr><th>Trực tiếp</th><th>→ Gián tiếp</th></tr>
<tr><td>I / me / my / mine</td><td>→ he/she, him/her, his/her, his/hers</td></tr>
<tr><td>we / us / our</td><td>→ they / them / their</td></tr>
<tr><td>you (nếu = người nghe)</td><td>→ I/me/he/she (tùy ngữ cảnh)</td></tr>
</table>

<h4>3.2. Trạng từ chỉ thời gian & nơi chốn</h4>
<table>
<tr><th>Trực tiếp</th><th>→ Gián tiếp</th></tr>
<tr><td>today</td><td>→ that day</td></tr>
<tr><td>yesterday</td><td>→ the day before / the previous day</td></tr>
<tr><td>tomorrow</td><td>→ the next day / the following day</td></tr>
<tr><td>now</td><td>→ then / at that time</td></tr>
<tr><td>here</td><td>→ there</td></tr>
<tr><td>this</td><td>→ that</td></tr>
<tr><td>these</td><td>→ those</td></tr>
<tr><td>ago</td><td>→ before / earlier</td></tr>
<tr><td>last week</td><td>→ the week before / the previous week</td></tr>
<tr><td>next month</td><td>→ the following month</td></tr>
</table>

<h3>4. Các dạng câu tường thuật</h3>

<h4>4.1. Câu kể (Statements)</h4>
<p>S + <b>said (that)</b> / <b>told + O + (that)</b> + mệnh đề lùi thì</p>
<div class="ex">"I love this city." → He <b>said (that)</b> he <b>loved</b> that city.<span class="vi">→ Anh ấy nói rằng anh ấy yêu thành phố đó.</span></div>
<div class="ex">"I will call you tomorrow." → She <b>told me (that)</b> she <b>would call</b> me <b>the next day</b>.<span class="vi">→ Cô ấy nói với tôi rằng cô ấy sẽ gọi cho tôi ngày hôm sau.</span></div>

<div class="warn"><b>⚠️ said vs told:</b><br>
<b>said</b>: không cần tân ngữ. "He said (that)..."<br>
<b>told</b>: BẮT BUỘC có tân ngữ. "He told <b>me</b> (that)..."<br>
✗ <s>He told that he was busy.</s> → ✓ He told <b>me</b> that he was busy.</div>

<h4>4.2. Câu hỏi (Questions)</h4>
<p><b>Yes/No Questions:</b> S + asked + (O) + <b>if/whether</b> + S + V (lùi thì, KHÔNG đảo)</p>
<div class="ex">"Do you speak English?" → He <b>asked me if</b> I <b>spoke</b> English.<span class="vi">→ Anh ấy hỏi tôi có nói được tiếng Anh không.</span></div>
<div class="ex">"Are you coming?" → She <b>asked whether</b> I <b>was coming</b>.<span class="vi">→ Cô ấy hỏi liệu tôi có đến không.</span></div>

<p><b>Wh- Questions:</b> S + asked + (O) + <b>Wh- word</b> + S + V (lùi thì, KHÔNG đảo)</p>
<div class="ex">"Where do you live?" → He <b>asked me where</b> I <b>lived</b>.<span class="vi">→ Anh ấy hỏi tôi sống ở đâu.</span></div>
<div class="ex">"What time does the train leave?" → She <b>asked what time</b> the train <b>left</b>.<span class="vi">→ Cô ấy hỏi tàu mấy giờ chạy.</span></div>

<div class="warn"><b>⚠️ Câu hỏi gián tiếp KHÔNG đảo trợ động từ:</b><br>
✗ <s>He asked me where did I live.</s><br>
✓ He asked me where I <b>lived</b>. (S + V, không đảo)</div>

<h4>4.3. Câu mệnh lệnh, yêu cầu (Commands/Requests)</h4>
<p>S + <b>told/asked/ordered</b> + O + <b>(not) to + V</b></p>
<div class="ex">"Open the window." → She <b>told me to open</b> the window.<span class="vi">→ Cô ấy bảo tôi mở cửa sổ.</span></div>
<div class="ex">"Don't be late!" → He <b>told us not to be</b> late.<span class="vi">→ Anh ấy bảo chúng tôi đừng đến muộn.</span></div>
<div class="ex">"Please help me." → She <b>asked me to help</b> her.<span class="vi">→ Cô ấy nhờ tôi giúp.</span></div>

<h3>5. Khi nào KHÔNG cần lùi thì?</h3>
<table>
<tr><th>Tình huống</th><th>Ví dụ</th></tr>
<tr><td>Sự thật luôn đúng</td><td>"The earth goes around the sun." → He said the earth <b>goes</b> around the sun.</td></tr>
<tr><td>Vừa mới nói xong (vẫn đúng)</td><td>"I'm hungry." (vừa nói) → She says she <b>is</b> hungry. (dùng "says" → không lùi)</td></tr>
<tr><td>Động từ tường thuật ở hiện tại</td><td>He <b>says</b> he <b>likes</b> coffee. (says = hiện tại → không lùi)</td></tr>
</table>

<h3>6. Mẹo làm bài thi VSTEP</h3>
<div class="note"><b>💡 Chiến lược:</b><br>
<b>1.</b> Xác định loại câu: kể, hỏi, hay mệnh lệnh → chọn đúng cấu trúc.<br>
<b>2.</b> Lùi thì đúng: present → past, past → past perfect, will → would...<br>
<b>3.</b> Đổi đại từ: I → he/she, my → his/her, you → I/me...<br>
<b>4.</b> Đổi trạng từ: today → that day, tomorrow → the next day...<br>
<b>5.</b> Câu hỏi gián tiếp: KHÔNG đảo trợ động từ, KHÔNG có dấu "?".<br>
<b>6.</b> said vs told: <b>told</b> luôn cần tân ngữ (told me/him/her...).</div>
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

print(f"\nDone! Updated {len(CONTENT)} units (6-10).")
