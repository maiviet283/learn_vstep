# -*- coding: utf-8 -*-
"""Bai nghe bo sung (5-7): thong bao, hoi thoai, bai giang."""

TRACKS_2 = [
{
 'title': 'Airport Announcement', 'level': 'B1', 'order': 5,
 'transcript': """Attention all passengers. This is an announcement for passengers on flight VN 254 to Da Nang. We are sorry to inform you that this flight has been delayed due to bad weather conditions. The new departure time is 3:45 p.m., from gate number 12, instead of gate 8. Passengers are advised to stay near the boarding area and listen for further announcements. As an apology, meal vouchers will be provided at the information desk on the second floor. Please have your boarding pass ready to receive your voucher. Passengers with connecting flights in Da Nang, please contact our staff at the transfer desk for assistance. We apologize again for this inconvenience and thank you for your patience.""",
 'translation_vi': """Xin chú ý, toàn thể hành khách. Đây là thông báo dành cho hành khách chuyến bay VN 254 đi Đà Nẵng. Chúng tôi rất tiếc phải thông báo chuyến bay bị hoãn do thời tiết xấu. Giờ khởi hành mới là 15:45, tại cửa số 12 thay vì cửa số 8. Hành khách vui lòng ở gần khu vực lên máy bay và chú ý các thông báo tiếp theo. Để xin lỗi quý khách, phiếu ăn sẽ được phát tại quầy thông tin trên tầng hai. Vui lòng chuẩn bị sẵn thẻ lên máy bay để nhận phiếu. Hành khách có chuyến bay nối chuyến tại Đà Nẵng, vui lòng liên hệ nhân viên tại quầy trung chuyển để được hỗ trợ. Một lần nữa xin lỗi vì sự bất tiện này và cảm ơn sự kiên nhẫn của quý khách.""",
 'questions': [
  ('Why has flight VN 254 been delayed?',
   'a technical problem', 'bad weather', 'a late crew', 'airport construction', 'B',
   'Thông báo nêu rõ: "delayed due to bad weather conditions" → do thời tiết xấu.'),
  ('Which gate will the flight now depart from?',
   'gate 8', 'gate 12', 'gate 2', 'gate 45', 'B',
   '"from gate number 12, instead of gate 8" — cửa MỚI là 12; cửa 8 là cửa cũ (bẫy "instead of").'),
  ('Where can passengers get meal vouchers?',
   'at gate 8', 'at the boarding area', 'at the information desk on the second floor', 'on the plane', 'C',
   '"meal vouchers will be provided at the information desk on the second floor" → quầy thông tin tầng 2.'),
  ('Who should contact the transfer desk?',
   'passengers with children', 'passengers with connecting flights',
   'passengers without boarding passes', 'all passengers', 'B',
   '"Passengers with connecting flights in Da Nang, please contact our staff at the transfer desk" → khách nối chuyến.'),
 ],
},
{
 'title': 'Booking a Hotel Room by Phone', 'level': 'B1', 'order': 6,
 'transcript': """Receptionist: Good morning, Ocean View Hotel. How may I help you?
Customer: Hi, I'd like to book a room for two people, please. We're arriving on Friday the fifteenth and leaving on Sunday the seventeenth.
Receptionist: So that's two nights. Would you prefer a standard room or a sea-view room?
Customer: What's the difference in price?
Receptionist: A standard room is one million dong per night, and a sea-view room is one million four hundred thousand.
Customer: Hmm. Does the price include breakfast?
Receptionist: Breakfast is included with the sea-view room, but for standard rooms it costs an extra one hundred thousand dong per person.
Customer: In that case, I'll take the sea-view room. It sounds like better value.
Receptionist: Excellent choice. Could I have your name, please?
Customer: It's Hoa. H-O-A. Tran Thi Hoa.
Receptionist: Thank you, Ms Hoa. Your room will be ready from 2 p.m. on Friday. We look forward to seeing you!""",
 'translation_vi': """Lễ tân: Chào buổi sáng, khách sạn Ocean View xin nghe. Tôi có thể giúp gì ạ?
Khách: Chào chị, tôi muốn đặt một phòng cho hai người. Chúng tôi đến thứ Sáu ngày 15 và rời đi Chủ nhật ngày 17.
Lễ tân: Vậy là hai đêm ạ. Anh/chị muốn phòng tiêu chuẩn hay phòng hướng biển?
Khách: Giá chênh nhau thế nào ạ?
Lễ tân: Phòng tiêu chuẩn 1 triệu đồng/đêm, phòng hướng biển 1 triệu 400 nghìn.
Khách: Hmm. Giá đã gồm bữa sáng chưa?
Lễ tân: Phòng hướng biển bao gồm bữa sáng, còn phòng tiêu chuẩn phải trả thêm 100 nghìn mỗi người.
Khách: Vậy tôi lấy phòng hướng biển. Nghe có vẻ hời hơn.
Lễ tân: Lựa chọn tuyệt vời ạ. Cho tôi xin tên anh/chị?
Khách: Tôi tên Hoa. H-O-A. Trần Thị Hoa.
Lễ tân: Cảm ơn chị Hoa. Phòng sẽ sẵn sàng từ 2 giờ chiều thứ Sáu. Rất mong được đón tiếp chị!""",
 'questions': [
  ('How many nights will the customer stay?',
   'one night', 'two nights', 'three nights', 'five nights', 'B',
   'Đến thứ Sáu 15, đi Chủ nhật 17 → lễ tân xác nhận "So that\'s two nights" → 2 đêm. Đừng nhầm với các con số ngày 15, 17.'),
  ('How much does a sea-view room cost per night?',
   '1,000,000 dong', '1,100,000 dong', '1,400,000 dong', '400,000 dong', 'C',
   '"a sea-view room is one million four hundred thousand" → 1,4 triệu đồng. 1 triệu là giá phòng TIÊU CHUẨN.'),
  ('Why does the customer choose the sea-view room?',
   'It is cheaper', 'It includes breakfast and seems better value',
   'It is on the top floor', 'The standard room is full', 'B',
   'Khách hỏi về bữa sáng, biết phòng hướng biển đã gồm bữa sáng rồi nói "It sounds like better value" → thấy hời hơn.'),
  ('What time will the room be ready on Friday?',
   'from 12 p.m.', 'from 2 p.m.', 'from 5 p.m.', 'from 7 a.m.', 'B',
   'Câu cuối: "Your room will be ready from 2 p.m. on Friday" → từ 2 giờ chiều.'),
 ],
},
{
 'title': 'Short Lecture: The History of the Bicycle', 'level': 'B2', 'order': 7,
 'transcript': """Good afternoon, everyone. Today's short talk is about a simple machine that changed the world: the bicycle.
The first bicycle-like machine appeared in Germany in 1817. It was made of wood, had no pedals, and riders pushed it along with their feet. People called it the "running machine". It was fun, but not very practical.
The real breakthrough came in the 1860s, when French inventors added pedals to the front wheel. Then, in 1885, the English engineer John Starley created the "safety bicycle". It had two wheels of equal size and a chain connecting the pedals to the back wheel — basically the same design we use today.
The bicycle had a surprising social impact. It gave ordinary people, especially women, a cheap way to travel independently for the first time. Some historians say the bicycle did more for women's freedom than almost any other invention of that century.
Today, as cities fight traffic jams and air pollution, the bicycle is making a comeback. Cities like Amsterdam and Copenhagen have built thousands of kilometres of bike lanes, and bike-sharing programs have appeared in Hanoi and Ho Chi Minh City. After two hundred years, this simple machine may once again change how we live.""",
 'translation_vi': """Chào buổi chiều mọi người. Bài nói ngắn hôm nay về một cỗ máy giản đơn đã thay đổi thế giới: chiếc xe đạp.
Cỗ máy giống xe đạp đầu tiên xuất hiện ở Đức năm 1817. Nó làm bằng gỗ, không có bàn đạp, người lái đẩy bằng chân. Người ta gọi nó là "cỗ máy chạy". Vui đấy, nhưng không thực dụng lắm.
Bước đột phá thật sự đến vào thập niên 1860 khi các nhà phát minh Pháp gắn bàn đạp vào bánh trước. Rồi năm 1885, kỹ sư người Anh John Starley tạo ra "xe đạp an toàn": hai bánh bằng nhau và xích nối bàn đạp với bánh sau — về cơ bản chính là thiết kế ta dùng ngày nay.
Xe đạp có tác động xã hội đáng kinh ngạc. Lần đầu tiên nó cho người bình thường, đặc biệt là phụ nữ, một cách di chuyển độc lập với chi phí rẻ. Một số sử gia nói xe đạp đóng góp cho tự do của phụ nữ nhiều hơn hầu hết các phát minh khác của thế kỷ đó.
Ngày nay, khi các thành phố chống chọi với kẹt xe và ô nhiễm, xe đạp đang trở lại. Amsterdam và Copenhagen đã xây hàng nghìn km làn xe đạp, và các chương trình chia sẻ xe đạp đã xuất hiện ở Hà Nội, TP.HCM. Sau hai trăm năm, cỗ máy giản đơn này có thể một lần nữa thay đổi cách chúng ta sống.""",
 'questions': [
  ('What was special about the first bicycle-like machine in 1817?',
   'It had a chain', 'It had no pedals and was pushed by feet',
   'It was made of metal', 'It had three wheels', 'B',
   '"It was made of wood, had no pedals, and riders pushed it along with their feet" → không có bàn đạp, đẩy bằng chân.'),
  ('What did John Starley invent in 1885?',
   'the running machine', 'the safety bicycle', 'the front pedal', 'the bike lane', 'B',
   '"in 1885, the English engineer John Starley created the safety bicycle" → xe đạp an toàn. Bàn đạp bánh trước là của người PHÁP thập niên 1860 — bẫy tráo thông tin.'),
  ('According to the talk, how did the bicycle affect women?',
   'It gave them a cheap way to travel independently', 'It helped them find jobs in factories',
   'It made them better at sports', 'It changed their fashion', 'A',
   '"It gave ordinary people, especially women, a cheap way to travel independently for the first time" → phương tiện đi lại độc lập, rẻ.'),
  ('Why is the bicycle becoming popular again today?',
   'It is faster than cars', 'Cities have problems with traffic and pollution',
   'Petrol is no longer available', 'People cannot afford motorbikes', 'B',
   '"as cities fight traffic jams and air pollution, the bicycle is making a comeback" → vì kẹt xe và ô nhiễm không khí.'),
 ],
},
]
