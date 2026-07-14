# -*- coding: utf-8 -*-
"""Bo de nghe theo format de thi VSTEP that — Part 1 (thong bao ngan) & Part 2 (hoi thoai)."""

TRACKS_3 = [
{
 'title': 'Đề thật Part 1: Eight Short Announcements', 'level': 'B1', 'order': 8,
 'transcript': """Announcement one. Attention all passengers on flight VN 254 to Da Nang. The departure gate has been changed from gate 12 to gate 18. Please proceed to gate 18. Boarding will begin in twenty minutes.
Announcement two. Welcome to Big Green Supermarket. Today only, all fresh fruit and vegetables are twenty per cent off. You can find this special offer in aisle five, at the back of the store.
Announcement three. This is an announcement for passengers waiting for the 9.30 train to Hue. Due to a technical problem, the train will be delayed by approximately forty-five minutes. We apologise for the inconvenience.
Announcement four. Ladies and gentlemen, the museum will close in fifteen minutes. Please make your way to the exit on the ground floor. The gift shop will remain open until six o'clock.
Announcement five. Attention library users. Please note that from next Monday, the library will open at seven a.m. instead of eight a.m. Closing time remains the same, at nine p.m.
Announcement six. Good afternoon, shoppers. A blue car, licence plate 30 A, 5, 6, 7, 8, 9, is blocking the entrance of the car park. Would the owner please move it immediately?
Announcement seven. Before tonight's performance begins, we kindly remind you to switch off your mobile phones. Taking photos or videos during the show is not allowed. Enjoy the performance.
Announcement eight. Attention all tour members. Our bus will leave the hotel at eight fifteen tomorrow morning, fifteen minutes earlier than planned. Please have your breakfast early and wait in the lobby by eight ten.""",
 'translation_vi': """Thông báo 1. Kính mời hành khách chuyến bay VN 254 đi Đà Nẵng chú ý. Cửa khởi hành đã đổi từ cửa 12 sang cửa 18. Quý khách vui lòng di chuyển đến cửa 18. Việc lên máy bay bắt đầu sau 20 phút nữa.
Thông báo 2. Chào mừng đến siêu thị Big Green. Chỉ riêng hôm nay, toàn bộ rau củ quả tươi giảm 20%. Quý khách xem ưu đãi tại lối đi số 5, cuối cửa hàng.
Thông báo 3. Thông báo dành cho hành khách chờ chuyến tàu 9 giờ 30 đi Huế. Do sự cố kỹ thuật, tàu sẽ trễ khoảng 45 phút. Chúng tôi xin lỗi vì sự bất tiện này.
Thông báo 4. Kính thưa quý khách, bảo tàng sẽ đóng cửa sau 15 phút nữa. Xin di chuyển ra lối ra ở tầng trệt. Cửa hàng lưu niệm vẫn mở đến 6 giờ.
Thông báo 5. Bạn đọc thư viện chú ý. Từ thứ Hai tuần tới, thư viện mở cửa lúc 7 giờ sáng thay vì 8 giờ. Giờ đóng cửa giữ nguyên, 9 giờ tối.
Thông báo 6. Chào quý khách. Một ô tô màu xanh, biển số 30A-56789, đang chắn lối vào bãi đỗ xe. Đề nghị chủ xe di chuyển xe ngay lập tức.
Thông báo 7. Trước khi buổi biểu diễn tối nay bắt đầu, xin nhắc quý vị tắt điện thoại di động. Không được chụp ảnh, quay phim trong suốt buổi diễn. Chúc quý vị xem vui vẻ.
Thông báo 8. Các thành viên đoàn tour chú ý. Xe sẽ rời khách sạn lúc 8 giờ 15 sáng mai, sớm hơn kế hoạch 15 phút. Vui lòng ăn sáng sớm và có mặt ở sảnh trước 8 giờ 10.""",
 'questions': [
  ('(Announcement 1) Where should passengers on flight VN 254 go?',
   'gate 12', 'gate 18', 'gate 20', 'the check-in counter', 'B',
   'Part 1 đề thật luôn gài 2 con số: cửa CŨ (12) và cửa MỚI (18). Từ khóa "changed from... to..." — đáp án là số đứng sau "to" → gate 18.'),
  ('(Announcement 2) What is on sale at the supermarket today?',
   'meat and fish', 'fresh fruit and vegetables', 'drinks and snacks', 'rice and noodles', 'B',
   '"all fresh fruit and vegetables are twenty per cent off" → rau củ quả tươi giảm giá. "Aisle five" chỉ là vị trí, không phải mặt hàng.'),
  ('(Announcement 3) How long will the train to Hue be delayed?',
   'fifteen minutes', 'thirty minutes', 'forty-five minutes', 'one hour', 'C',
   '"the train will be delayed by approximately forty-five minutes" → trễ 45 phút. Giờ khởi hành 9.30 là thông tin gây nhiễu.'),
  ('(Announcement 4) What will stay open until 6 o\'clock?',
   'the museum', 'the gift shop', 'the café', 'the ticket office', 'B',
   'Bảo tàng đóng sau 15 phút NHƯNG "The gift shop will remain open until six o\'clock" → cửa hàng lưu niệm. Chú ý từ "remain open" (vẫn mở).'),
  ('(Announcement 5) What will change about the library from next Monday?',
   'its opening time', 'its closing time', 'its location', 'its membership fee', 'A',
   '"will open at seven a.m. instead of eight a.m. Closing time remains the same" → giờ MỞ cửa thay đổi, giờ đóng giữ nguyên. Dạng hỏi "cái gì thay đổi" rất phổ biến ở Part 1.'),
  ('(Announcement 6) What is the problem with the blue car?',
   'It was stolen', 'It is blocking the car park entrance',
   'Its lights are on', 'It was damaged', 'B',
   '"is blocking the entrance of the car park" → chắn lối vào bãi đỗ xe. Biển số dài chỉ để gây nhiễu, không cần nhớ.'),
  ('(Announcement 7) What are the audience asked to do?',
   'buy tickets early', 'turn off their mobile phones',
   'take photos of the show', 'leave the theatre', 'B',
   '"we kindly remind you to switch off your mobile phones" → tắt điện thoại. "Switch off" = "turn off" — đề thi luôn paraphrase như vậy.'),
  ('(Announcement 8) What time will the tour bus leave tomorrow?',
   'at 8.00', 'at 8.10', 'at 8.15', 'at 8.30', 'C',
   '"Our bus will leave the hotel at eight fifteen" → 8h15. Bẫy: 8h10 là giờ phải CÓ MẶT ở sảnh, còn "15 phút" là khoảng thời gian sớm hơn kế hoạch.'),
 ],
},
{
 'title': 'Đề thật Part 2 – Hội thoại 1: Joining a Gym', 'level': 'B1', 'order': 9,
 'transcript': """Receptionist: Good morning! Welcome to Star Fitness. How can I help you?
Customer: Hi, I'd like to ask about your membership. How much does it cost?
Receptionist: We have two options. The standard membership is four hundred thousand dong a month, which includes the gym and all group classes. The premium membership is six hundred thousand and also includes the swimming pool and sauna.
Customer: I see. I'm mainly interested in yoga classes. Are they included in the standard package?
Receptionist: Yes, all group classes are included: yoga, dance and boxing. Yoga classes run every Monday, Wednesday and Friday, at six in the morning and seven thirty in the evening.
Customer: Perfect, the evening class suits me better because I work during the day. Do I need to bring anything?
Receptionist: Just comfortable clothes and a water bottle. We provide yoga mats and towels for free. Oh, and if you sign up today, you'll get the first week free.
Customer: That sounds great. Can I pay by card?
Receptionist: Of course. I just need your ID card to complete the registration form.
Customer: Here you are. Thank you!""",
 'translation_vi': """Lễ tân: Chào buổi sáng! Chào mừng đến Star Fitness. Tôi giúp gì được cho bạn?
Khách: Chào chị, tôi muốn hỏi về gói hội viên. Giá bao nhiêu ạ?
Lễ tân: Chúng tôi có hai lựa chọn. Gói tiêu chuẩn 400 nghìn đồng/tháng, gồm phòng gym và tất cả lớp tập nhóm. Gói cao cấp 600 nghìn, thêm hồ bơi và xông hơi.
Khách: Tôi hiểu rồi. Tôi chủ yếu quan tâm lớp yoga. Gói tiêu chuẩn có bao gồm không?
Lễ tân: Có, mọi lớp nhóm đều bao gồm: yoga, nhảy và boxing. Lớp yoga vào thứ Hai, Tư, Sáu hằng tuần, lúc 6 giờ sáng và 7 rưỡi tối.
Khách: Tuyệt, lớp tối hợp với tôi hơn vì ban ngày tôi đi làm. Tôi cần mang gì không?
Lễ tân: Chỉ cần quần áo thoải mái và chai nước. Thảm yoga và khăn chúng tôi cung cấp miễn phí. À, nếu đăng ký hôm nay, bạn được tuần đầu miễn phí.
Khách: Nghe hay đấy. Tôi trả bằng thẻ được không?
Lễ tân: Tất nhiên. Tôi chỉ cần CMND/CCCD của bạn để hoàn tất mẫu đăng ký.
Khách: Đây ạ. Cảm ơn chị!""",
 'questions': [
  ('How much is the standard membership per month?',
   '300,000 dong', '400,000 dong', '500,000 dong', '600,000 dong', 'B',
   '"The standard membership is four hundred thousand dong a month" → 400 nghìn. 600 nghìn là gói PREMIUM — hội thoại giá cả luôn có 2 con số để gây nhiễu.'),
  ('What does the premium membership include that the standard does not?',
   'group classes', 'yoga mats', 'the swimming pool and sauna', 'free towels', 'C',
   'Gói premium "also includes the swimming pool and sauna" — hồ bơi và xông hơi là phần THÊM so với gói tiêu chuẩn.'),
  ('Why does the customer prefer the evening yoga class?',
   'It is cheaper', 'She works during the day',
   'The morning class is full', 'The teacher is better', 'B',
   'Khách nói: "the evening class suits me better because I work during the day" → ban ngày bận đi làm. Từ khóa "because" báo hiệu đáp án.'),
  ('What will the customer get if she signs up today?',
   'a free water bottle', 'a discount on the price',
   'the first week free', 'a free yoga mat to keep', 'C',
   '"if you sign up today, you\'ll get the first week free" → tuần đầu miễn phí. Thảm yoga miễn phí là cho MỌI buổi tập chứ không phải quà đăng ký — bẫy tinh vi.'),
 ],
},
{
 'title': 'Đề thật Part 2 – Hội thoại 2: Renting an Apartment', 'level': 'B1', 'order': 10,
 'transcript': """Agent: Hello, Golden Home real estate, Minh speaking.
Customer: Hi, I'm calling about the apartment for rent on Tran Phu Street that I saw online. Is it still available?
Agent: Yes, it is. It's a one-bedroom apartment on the seventh floor, fully furnished, with a nice view of the park.
Customer: Sounds good. The advertisement says six million a month. Does that include everything?
Agent: The rent covers water and the management fee, but electricity and internet are separate. There's also a deposit of one month's rent when you sign the contract.
Customer: OK. How far is it from the city centre?
Agent: About three kilometres. There's a bus stop right in front of the building, and a big supermarket just around the corner.
Customer: Great. Is it possible to see the apartment this week?
Agent: Of course. I'm free on Thursday afternoon and Saturday morning. Which is better for you?
Customer: Saturday morning, please. Around nine?
Agent: Nine on Saturday works fine. Can I have your name and phone number?
Customer: It's Hoa, zero nine one, two three four, five six seven eight.
Agent: Perfect, Ms Hoa. See you on Saturday!""",
 'translation_vi': """Môi giới: Xin chào, bất động sản Golden Home, Minh nghe ạ.
Khách: Chào anh, tôi gọi về căn hộ cho thuê trên đường Trần Phú tôi thấy trên mạng. Còn trống không ạ?
Môi giới: Còn chị ạ. Căn hộ một phòng ngủ tầng 7, đầy đủ nội thất, view công viên rất đẹp.
Khách: Nghe ổn đấy. Tin đăng ghi 6 triệu/tháng. Giá đó gồm tất cả chưa?
Môi giới: Tiền thuê gồm nước và phí quản lý, nhưng điện và internet tính riêng. Ngoài ra đặt cọc một tháng tiền nhà khi ký hợp đồng.
Khách: OK. Cách trung tâm bao xa anh?
Môi giới: Khoảng 3 km. Có trạm xe buýt ngay trước tòa nhà, siêu thị lớn ngay góc phố.
Khách: Tốt quá. Tuần này xem nhà được không ạ?
Môi giới: Được chứ. Tôi rảnh chiều thứ Năm và sáng thứ Bảy. Chị tiện hôm nào?
Khách: Sáng thứ Bảy nhé. Khoảng 9 giờ?
Môi giới: 9 giờ thứ Bảy được ạ. Cho tôi xin tên và số điện thoại?
Khách: Tôi là Hoa, 091 234 5678.
Môi giới: Cảm ơn chị Hoa. Hẹn gặp thứ Bảy!""",
 'questions': [
  ('What kind of apartment is for rent?',
   'a two-bedroom apartment without furniture', 'a one-bedroom apartment with furniture',
   'a studio near the supermarket', 'a house with a garden', 'B',
   '"a one-bedroom apartment on the seventh floor, fully furnished" → 1 phòng ngủ, đầy đủ nội thất. "Fully furnished" = có sẵn nội thất — từ vựng thuê nhà quan trọng.'),
  ('Which of the following is NOT included in the rent?',
   'water', 'the management fee', 'electricity', 'the park view', 'C',
   '"The rent covers water and the management fee, but electricity and internet are separate" → điện tính riêng. Từ khóa "but" đảo thông tin — vị trí bẫy quen thuộc.'),
  ('How much is the deposit?',
   'one month\'s rent', 'two months\' rent', 'three million dong', 'six hundred thousand dong', 'A',
   '"a deposit of one month\'s rent" → cọc 1 tháng tiền nhà (= 6 triệu, nhưng đề hỏi theo cách nói trong bài). Deposit = tiền đặt cọc.'),
  ('When will the customer see the apartment?',
   'Thursday afternoon', 'Saturday morning', 'Saturday afternoon', 'Sunday morning', 'B',
   'Môi giới đưa 2 lựa chọn (chiều thứ Năm / sáng thứ Bảy), khách chốt "Saturday morning, please" → sáng thứ Bảy. Luôn nghe câu CHỐT cuối cùng, không phải các phương án được nêu.'),
 ],
},
]
