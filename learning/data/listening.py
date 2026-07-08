# -*- coding: utf-8 -*-
"""Bai nghe (doc bang Web Speech API). Question: (text, A, B, C, D, correct, explanation)."""

TRACKS = [
{
 'title': 'A Conversation at the Library', 'level': 'B1', 'order': 1,
 'transcript': """Librarian: Good morning. Can I help you?
Student: Yes, please. I'd like to borrow some books for my English exam. Where can I find them?
Librarian: English books are on the second floor, section B. You can take the stairs or the lift.
Student: Great. How many books can I borrow at one time?
Librarian: Students can borrow five books for two weeks. If you need more time, you can renew them online or by phone.
Student: That's very convenient. And is there a fee if I return them late?
Librarian: Yes, I'm afraid so. It's five thousand dong per book per day.
Student: I see. One more thing — do you have quiet rooms for studying?
Librarian: Yes, there are study rooms on the third floor, but you need to book them at least one day in advance.
Student: Perfect. Thank you so much for your help!""",
 'translation_vi': """Thủ thư: Chào buổi sáng. Tôi có thể giúp gì cho bạn?
Sinh viên: Vâng ạ. Em muốn mượn vài cuốn sách ôn thi tiếng Anh. Em tìm chúng ở đâu ạ?
Thủ thư: Sách tiếng Anh ở tầng hai, khu B. Em có thể đi thang bộ hoặc thang máy.
Sinh viên: Hay quá. Mỗi lần em mượn được mấy cuốn ạ?
Thủ thư: Sinh viên được mượn 5 cuốn trong 2 tuần. Nếu cần thêm thời gian, em có thể gia hạn online hoặc qua điện thoại.
Sinh viên: Tiện quá ạ. Nếu trả muộn có bị phạt không ạ?
Thủ thư: Có đấy. Phí là 5.000 đồng mỗi cuốn mỗi ngày.
Sinh viên: Em hiểu rồi. Một điều nữa — thư viện có phòng yên tĩnh để tự học không ạ?
Thủ thư: Có, phòng tự học ở tầng ba, nhưng em cần đặt trước ít nhất một ngày.
Sinh viên: Tuyệt vời. Em cảm ơn cô nhiều ạ!""",
 'questions': [
  ('Where are the English books?',
   'on the first floor', 'on the second floor', 'on the third floor', 'near the entrance', 'B',
   'Thủ thư nói: "English books are on the second floor, section B" → tầng hai. Tầng ba là phòng tự học — thông tin gây nhiễu.'),
  ('How many books can a student borrow at one time?',
   'three', 'four', 'five', 'ten', 'C',
   '"Students can borrow five books for two weeks" → 5 cuốn. Số 2 (tuần) dễ gây nhiễu với số lượng sách.'),
  ('What happens if a student returns books late?',
   'They cannot borrow again', 'They must pay a fee',
   'They must write a report', 'Nothing happens', 'B',
   'Khi sinh viên hỏi về phí trả muộn, thủ thư trả lời "Yes... It\'s five thousand dong per book per day" → phải trả phí phạt.'),
  ('What must students do to use a study room?',
   'pay five thousand dong', 'ask the librarian on the same day',
   'book at least one day in advance', 'borrow five books first', 'C',
   'Câu gần cuối: "you need to book them at least one day in advance" → đặt trước ít nhất 1 ngày.'),
 ],
},
{
 'title': 'Weather Forecast', 'level': 'B1', 'order': 2,
 'transcript': """Good evening, and welcome to the national weather forecast. Tomorrow will be a mixed day across the country. In the north, the morning will start cold and foggy, with temperatures around fifteen degrees. The fog should clear by midday, and the afternoon will be sunny and pleasant, reaching twenty-two degrees. In the central regions, expect heavy rain throughout the day, with a risk of flooding in low areas near the rivers. People are advised to avoid travelling if possible. In the south, it will be hot and humid, with temperatures up to thirty-four degrees. There may be short thunderstorms in the late afternoon, so remember to take an umbrella if you go out after four o'clock. That's all for tonight's forecast. Have a good evening!""",
 'translation_vi': """Chào buổi tối, chào mừng đến với bản tin dự báo thời tiết toàn quốc. Ngày mai thời tiết cả nước sẽ khá đa dạng. Ở miền Bắc, buổi sáng trời lạnh và có sương mù, nhiệt độ khoảng 15 độ. Sương mù sẽ tan vào giữa trưa, buổi chiều trời nắng đẹp, lên tới 22 độ. Ở miền Trung, mưa lớn cả ngày, nguy cơ ngập lụt ở vùng trũng gần sông. Người dân được khuyến cáo hạn chế đi lại nếu có thể. Ở miền Nam, trời nóng ẩm, nhiệt độ lên tới 34 độ. Có thể có giông ngắn vào cuối chiều, nên nhớ mang ô nếu ra ngoài sau 4 giờ. Đó là toàn bộ bản tin tối nay. Chúc quý vị buổi tối tốt lành!""",
 'questions': [
  ('What will the weather be like in the north tomorrow morning?',
   'sunny and warm', 'cold and foggy', 'rainy and windy', 'hot and humid', 'B',
   '"In the north, the morning will start cold and foggy" → lạnh và có sương mù. Nắng đẹp là thời tiết buổi CHIỀU — chú ý mốc thời gian.'),
  ('What is the highest temperature in the north tomorrow afternoon?',
   '15 degrees', '22 degrees', '30 degrees', '34 degrees', 'B',
   '"the afternoon will be sunny and pleasant, reaching twenty-two degrees" → 22 độ. 15 độ là buổi sáng, 34 độ là miền NAM — bài nghe thường gây nhiễu bằng nhiều con số.'),
  ('What problem may happen in the central regions?',
   'strong winds', 'flooding near rivers', 'very cold weather', 'dust storms', 'B',
   '"expect heavy rain... with a risk of flooding in low areas near the rivers" → nguy cơ ngập lụt vùng trũng gần sông.'),
  ('Why should people in the south take an umbrella after 4 p.m.?',
   'It will be very sunny', 'There may be thunderstorms',
   'It will be foggy', 'It will snow', 'B',
   '"There may be short thunderstorms in the late afternoon, so remember to take an umbrella... after four o\'clock" → có thể có giông.'),
 ],
},
{
 'title': 'A Phone Call about a Job Interview', 'level': 'B2', 'order': 3,
 'transcript': """Receptionist: Good afternoon, Sunrise Trading Company. How can I help you?
Mr Nam: Good afternoon. This is Nam Tran calling. I received an email inviting me to a job interview for the marketing assistant position, but I'm afraid I have a problem with the time.
Receptionist: Let me check. Ah yes, Mr Tran. Your interview is scheduled for Thursday at nine a.m. What seems to be the problem?
Mr Nam: Unfortunately, I have a final exam at university that morning. Would it be possible to change the interview to another time?
Receptionist: I understand. Let me see what's available. We could offer you Friday at two p.m., or Monday next week at ten a.m.
Mr Nam: Friday at two would be perfect. Thank you so much.
Receptionist: No problem. I'll update the schedule. Please remember to bring your CV, your university certificates, and one photo. The interview will last about forty-five minutes.
Mr Nam: Great. Could you tell me the address again, please?
Receptionist: Of course. It's the fifth floor, twenty-eight Le Loi Street, District One.
Mr Nam: Thank you very much. See you on Friday!""",
 'translation_vi': """Lễ tân: Chào buổi chiều, công ty Thương mại Sunrise xin nghe. Tôi có thể giúp gì ạ?
Anh Nam: Chào chị. Tôi là Trần Nam. Tôi nhận được email mời phỏng vấn vị trí trợ lý marketing, nhưng tôi e là bị trùng lịch.
Lễ tân: Để tôi kiểm tra. À vâng, anh Trần. Lịch phỏng vấn của anh là thứ Năm lúc 9 giờ sáng. Có vấn đề gì vậy ạ?
Anh Nam: Tiếc là sáng hôm đó tôi có bài thi cuối kỳ ở trường. Liệu có thể đổi lịch phỏng vấn sang buổi khác không ạ?
Lễ tân: Tôi hiểu. Để tôi xem lịch trống. Chúng tôi có thể xếp anh vào thứ Sáu lúc 2 giờ chiều, hoặc thứ Hai tuần sau lúc 10 giờ sáng.
Anh Nam: Thứ Sáu 2 giờ chiều là hoàn hảo. Cảm ơn chị nhiều.
Lễ tân: Không có gì. Tôi sẽ cập nhật lịch. Anh nhớ mang CV, bằng cấp đại học và một ảnh thẻ nhé. Buổi phỏng vấn kéo dài khoảng 45 phút.
Anh Nam: Tuyệt. Chị có thể cho tôi xin lại địa chỉ không ạ?
Lễ tân: Tất nhiên. Tầng 5, số 28 đường Lê Lợi, Quận 1.
Anh Nam: Cảm ơn chị rất nhiều. Hẹn gặp thứ Sáu!""",
 'questions': [
  ('Why is Mr Nam calling the company?',
   'to apply for a job', 'to change his interview time',
   'to cancel his interview', 'to ask about the salary', 'B',
   'Anh Nam nói anh có vấn đề với thời gian và hỏi "Would it be possible to change the interview to another time?" → gọi để ĐỔI LỊCH phỏng vấn.'),
  ('Why can\'t Mr Nam come on Thursday morning?',
   'He has another interview', 'He will be on holiday',
   'He has an exam at university', 'He is sick', 'C',
   '"I have a final exam at university that morning" → anh ấy có bài thi cuối kỳ.'),
  ('When will the interview take place?',
   'Thursday at 9 a.m.', 'Friday at 2 p.m.', 'Monday at 10 a.m.', 'Friday at 10 a.m.', 'B',
   'Lễ tân đưa ra 2 lựa chọn và anh Nam chọn: "Friday at two would be perfect" → thứ Sáu 2 giờ chiều. Thứ Năm 9h là lịch CŨ — bẫy điển hình.'),
  ('What does Mr Nam NOT need to bring?',
   'his CV', 'his certificates', 'a photo', 'a reference letter', 'D',
   'Lễ tân dặn mang: "your CV, your university certificates, and one photo". Thư giới thiệu (reference letter) KHÔNG được nhắc đến → D.'),
 ],
},
{
 'title': 'Talk: How to Improve Your Memory', 'level': 'B2', 'order': 4,
 'transcript': """Good morning, everyone, and thank you for coming to today's talk about memory. Many students tell me they study hard but forget everything in the exam room. Today I'll share three simple techniques that really work.
First, use spaced repetition. Instead of studying a topic once for three hours, study it for thirty minutes today, review it briefly tomorrow, then again after three days, and once more after a week. Research shows this method can double how much you remember.
Second, sleep matters more than you think. When you sleep, your brain moves information from short-term to long-term memory. Students who sleep seven to eight hours before an exam usually perform better than those who stay up all night studying.
Third, teach what you learn. When you explain an idea to a friend — or even to yourself in the mirror — you quickly discover which parts you don't really understand. Teaching forces your brain to organise information clearly.
Finally, remember that stress is the enemy of memory. Light exercise, deep breathing, and short breaks every forty-five minutes will keep your mind fresh. Good luck with your studies!""",
 'translation_vi': """Chào buổi sáng mọi người, cảm ơn các bạn đã đến buổi nói chuyện hôm nay về trí nhớ. Nhiều bạn học sinh nói với tôi rằng họ học rất chăm nhưng vào phòng thi lại quên hết. Hôm nay tôi sẽ chia sẻ ba kỹ thuật đơn giản mà thực sự hiệu quả.
Thứ nhất, dùng phương pháp lặp lại ngắt quãng. Thay vì học một chủ đề liền 3 tiếng, hãy học 30 phút hôm nay, ôn nhanh ngày mai, rồi sau 3 ngày, và một lần nữa sau một tuần. Nghiên cứu cho thấy phương pháp này có thể tăng gấp đôi lượng kiến thức bạn nhớ.
Thứ hai, giấc ngủ quan trọng hơn bạn nghĩ. Khi ngủ, não chuyển thông tin từ trí nhớ ngắn hạn sang dài hạn. Học sinh ngủ 7-8 tiếng trước kỳ thi thường làm bài tốt hơn những người thức trắng đêm học.
Thứ ba, hãy dạy lại điều bạn học. Khi giải thích một ý tưởng cho bạn bè — hoặc thậm chí cho chính mình trước gương — bạn nhanh chóng phát hiện phần nào mình chưa thực sự hiểu. Việc dạy buộc não sắp xếp thông tin rõ ràng.
Cuối cùng, hãy nhớ căng thẳng là kẻ thù của trí nhớ. Vận động nhẹ, hít thở sâu và nghỉ ngắn mỗi 45 phút sẽ giữ đầu óc tỉnh táo. Chúc các bạn học tốt!""",
 'questions': [
  ('What is the talk mainly about?',
   'how to pass exams without studying', 'techniques to improve memory',
   'the importance of exercise', 'how the brain works', 'B',
   'Người nói giới thiệu ngay từ đầu: "I\'ll share three simple techniques that really work" về trí nhớ → các kỹ thuật cải thiện trí nhớ.'),
  ('According to the speaker, how should students use spaced repetition?',
   'study one topic for three hours', 'review the topic several times over days',
   'only study the night before', 'read the textbook once', 'B',
   'Người nói mô tả: học 30 phút hôm nay, ôn lại ngày mai, sau 3 ngày, sau 1 tuần → ôn lại nhiều lần cách quãng trong nhiều ngày.'),
  ('What happens when we sleep, according to the talk?',
   'The brain deletes old information', 'The brain moves information to long-term memory',
   'The brain stops working', 'The brain creates new ideas', 'B',
   '"When you sleep, your brain moves information from short-term to long-term memory" → chuyển thông tin sang trí nhớ dài hạn.'),
  ('Why does the speaker recommend teaching what you learn?',
   'It helps you find what you don\'t understand', 'It makes friends happy',
   'It is easier than studying', 'Teachers earn more money', 'A',
   '"you quickly discover which parts you don\'t really understand" → dạy lại giúp phát hiện phần mình chưa hiểu.'),
 ],
},
]
