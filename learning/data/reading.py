# -*- coding: utf-8 -*-
"""Bai doc hieu theo format VSTEP. Question: (text, A, B, C, D, correct, explanation)."""

PASSAGES = [
{
 'title': 'The Benefits of Learning a Second Language', 'level': 'B1', 'order': 1,
 'content': """<p>Learning a second language is one of the most useful things you can do. First of all, it opens many doors in your career. Companies today do business with partners all over the world, so employees who can speak a foreign language often earn higher salaries and get better positions. In Vietnam, for example, many job advertisements ask for candidates with good English skills.</p>
<p>Second, learning a language is good for your brain. Scientists have found that bilingual people are better at solving problems and can concentrate for longer. Some studies even suggest that speaking two languages may delay memory diseases in old age.</p>
<p>Finally, a second language helps you understand other cultures. When you travel, you can talk to local people, read signs and menus, and enjoy films and music in their original language. This makes your experiences richer and more meaningful.</p>
<p>Of course, learning a language takes time and effort. Experts recommend practising a little every day rather than studying for many hours once a week. With patience and regular practice, anyone can succeed.</p>""",
 'translation_vi': """<p>Học một ngoại ngữ là một trong những việc hữu ích nhất bạn có thể làm. Trước hết, nó mở ra nhiều cánh cửa trong sự nghiệp. Các công ty ngày nay làm ăn với đối tác khắp thế giới, vì vậy nhân viên biết ngoại ngữ thường có lương cao hơn và vị trí tốt hơn. Ví dụ ở Việt Nam, nhiều tin tuyển dụng yêu cầu ứng viên có kỹ năng tiếng Anh tốt.</p>
<p>Thứ hai, học ngôn ngữ tốt cho não bộ. Các nhà khoa học phát hiện người song ngữ giải quyết vấn đề tốt hơn và tập trung lâu hơn. Một số nghiên cứu còn cho thấy nói hai thứ tiếng có thể làm chậm các bệnh suy giảm trí nhớ khi về già.</p>
<p>Cuối cùng, ngoại ngữ giúp bạn hiểu các nền văn hóa khác. Khi du lịch, bạn có thể trò chuyện với người bản địa, đọc biển hiệu, thực đơn và thưởng thức phim, nhạc bằng ngôn ngữ gốc. Điều này khiến trải nghiệm của bạn phong phú và ý nghĩa hơn.</p>
<p>Tất nhiên, học ngôn ngữ cần thời gian và nỗ lực. Các chuyên gia khuyên nên luyện tập một chút mỗi ngày thay vì học nhiều giờ mỗi tuần một lần. Với sự kiên nhẫn và luyện tập đều đặn, ai cũng có thể thành công.</p>""",
 'questions': [
  ('What is the main idea of the passage?',
   'Learning languages is very difficult', 'The advantages of learning a second language',
   'How to get a better job', 'English is the most important language', 'B',
   'Câu hỏi ý chính (main idea). Bài viết nêu 3 lợi ích của việc học ngoại ngữ: sự nghiệp, não bộ, văn hóa → đáp án B "Những lợi ích của việc học ngôn ngữ thứ hai". Các đáp án khác chỉ là chi tiết nhỏ hoặc không được nhắc đến.'),
  ('According to the passage, employees who speak a foreign language often ___ .',
   'travel around the world', 'work for the government',
   'earn more money', 'study in other countries', 'C',
   'Đoạn 1 viết: "employees who can speak a foreign language often earn higher salaries" (thường có lương cao hơn) → earn more money. Đây là dạng câu hỏi paraphrase: "earn higher salaries" = "earn more money".'),
  ('What does the word "bilingual" in paragraph 2 probably mean?',
   'people who speak two languages', 'people who are very intelligent',
   'people who study science', 'people who have good memory', 'A',
   'Câu hỏi đoán nghĩa từ theo ngữ cảnh. Tiền tố "bi-" nghĩa là "hai" (như bicycle - xe 2 bánh); cả đoạn đang nói về việc học ngôn ngữ THỨ HAI → bilingual = người nói được hai thứ tiếng.'),
  ('Which benefit is NOT mentioned in the passage?',
   'better career opportunities', 'understanding other cultures',
   'improved problem-solving', 'making more friends online', 'D',
   'Câu hỏi loại trừ (NOT). Bài nhắc đến: cơ hội nghề nghiệp (đoạn 1), giải quyết vấn đề (đoạn 2), hiểu văn hóa (đoạn 3). "Kết bạn trên mạng" không được nhắc đến → D.'),
  ('What do experts recommend about learning a language?',
   'studying many hours once a week', 'practising a little every day',
   'travelling to other countries', 'watching films in English', 'B',
   'Đoạn cuối: "Experts recommend practising a little every day rather than studying for many hours once a week" → luyện một chút mỗi ngày. Chú ý cấu trúc "A rather than B" = chọn A, không chọn B.'),
 ],
},
{
 'title': 'Urban Life vs Country Life', 'level': 'B1', 'order': 2,
 'content': """<p>More and more young Vietnamese people are moving from the countryside to big cities such as Ho Chi Minh City and Hanoi. They hope to find better jobs, modern services and an exciting lifestyle. Cities offer many opportunities: there are more companies, universities, hospitals and entertainment centres.</p>
<p>However, city life also has serious disadvantages. The cost of living is high, especially for housing. Many young workers have to share small rented rooms far from the city centre. Traffic jams waste hours of their time every week, and air pollution is getting worse. Life in the city can also be lonely, as neighbours often do not know each other.</p>
<p>In contrast, life in the countryside is slower and more peaceful. The air is fresh, food is cheap, and people live close to their families and neighbours. On the other hand, there are fewer jobs and schools, and young people may feel bored because there is little entertainment.</p>
<p>In recent years, thanks to the internet, some people have started to move back to their home villages. They can work online while enjoying a quieter and cheaper life. Perhaps in the future, the gap between urban and rural life will become smaller.</p>""",
 'translation_vi': """<p>Ngày càng nhiều bạn trẻ Việt Nam rời nông thôn lên các thành phố lớn như TP.HCM và Hà Nội. Họ hy vọng tìm được việc làm tốt hơn, dịch vụ hiện đại và lối sống sôi động. Thành phố mang lại nhiều cơ hội: nhiều công ty, trường đại học, bệnh viện và trung tâm giải trí hơn.</p>
<p>Tuy nhiên, cuộc sống thành thị cũng có những bất lợi nghiêm trọng. Chi phí sinh hoạt cao, đặc biệt là nhà ở. Nhiều lao động trẻ phải ở ghép trong những phòng trọ nhỏ xa trung tâm. Tắc đường lãng phí hàng giờ mỗi tuần, ô nhiễm không khí ngày càng tệ. Cuộc sống thành phố cũng có thể cô đơn vì hàng xóm thường không quen biết nhau.</p>
<p>Ngược lại, cuộc sống ở nông thôn chậm rãi và yên bình hơn. Không khí trong lành, thức ăn rẻ, con người sống gần gia đình và láng giềng. Mặt khác, ở đó ít việc làm và trường học hơn, người trẻ có thể thấy buồn chán vì ít chỗ giải trí.</p>
<p>Những năm gần đây, nhờ internet, một số người bắt đầu trở về quê. Họ có thể làm việc trực tuyến trong khi tận hưởng cuộc sống yên tĩnh, rẻ hơn. Có lẽ trong tương lai, khoảng cách giữa thành thị và nông thôn sẽ thu hẹp lại.</p>""",
 'questions': [
  ('Why do many young people move to big cities?',
   'to enjoy fresh air', 'to find better jobs and services',
   'to live with their families', 'to avoid traffic jams', 'B',
   'Đoạn 1: "They hope to find better jobs, modern services and an exciting lifestyle" → tìm việc làm và dịch vụ tốt hơn. Các đáp án A, C, D đều là đặc điểm của NÔNG THÔN hoặc trái với nội dung bài.'),
  ('Which problem of city life is NOT mentioned?',
   'expensive housing', 'traffic jams', 'crime', 'air pollution', 'C',
   'Đoạn 2 nêu: chi phí nhà ở cao, tắc đường, ô nhiễm không khí, cô đơn. "Crime" (tội phạm) KHÔNG được nhắc đến → C.'),
  ('The phrase "In contrast" at the beginning of paragraph 3 shows that ___ .',
   'the writer gives an example', 'the writer adds similar information',
   'the writer shows an opposite idea', 'the writer gives a conclusion', 'C',
   '"In contrast" (ngược lại) là từ nối chỉ sự ĐỐI LẬP: đoạn 2 nói về nhược điểm thành phố, đoạn 3 chuyển sang cuộc sống nông thôn với đặc điểm trái ngược → C.'),
  ('According to paragraph 4, what has helped some people return to their villages?',
   'cheaper houses', 'the internet', 'new roads', 'better schools', 'B',
   'Đoạn 4: "thanks to the internet, some people have started to move back to their home villages" — nhờ internet họ có thể làm việc online từ quê → B.'),
  ('What is the writer\'s prediction about the future?',
   'Everyone will leave the cities', 'Country life will disappear',
   'The difference between city and country life will get smaller', 'Cities will become less crowded', 'C',
   'Câu cuối: "Perhaps in the future, the gap between urban and rural life will become smaller" → khoảng cách giữa đời sống thành thị và nông thôn sẽ nhỏ lại. "Gap... become smaller" = "difference... get smaller".'),
 ],
},
{
 'title': 'The History of Coffee in Vietnam', 'level': 'B1', 'order': 3,
 'content': """<p>Coffee was first brought to Vietnam by the French in 1857. At the beginning, it was grown in small gardens in the north. Later, farmers discovered that the Central Highlands, with its red soil and cool climate, was perfect for coffee trees. Today, this region produces most of the country's coffee.</p>
<p>Vietnam is now the second largest coffee producer in the world, after Brazil, and the largest producer of robusta coffee. Robusta beans have a strong, bitter taste and contain more caffeine than arabica beans. Millions of Vietnamese families depend on coffee farming for their income.</p>
<p>Coffee is not just a product for export; it is an important part of Vietnamese culture. People drink coffee slowly at street cafés, watching life go by. The most famous drink is "ca phe sua da" — strong black coffee served with sweet condensed milk over ice. In recent years, creative drinks such as egg coffee and coconut coffee have become popular with both locals and tourists.</p>
<p>However, coffee farmers face several challenges. Climate change is making the weather less predictable, and coffee prices go up and down quickly. Many farmers are now learning modern methods to produce higher quality beans that can be sold at better prices.</p>""",
 'translation_vi': """<p>Cà phê được người Pháp đưa vào Việt Nam lần đầu năm 1857. Ban đầu, nó được trồng trong những khu vườn nhỏ ở miền Bắc. Về sau, nông dân phát hiện Tây Nguyên với đất đỏ và khí hậu mát mẻ rất phù hợp với cây cà phê. Ngày nay, khu vực này sản xuất phần lớn cà phê của cả nước.</p>
<p>Việt Nam hiện là nước sản xuất cà phê lớn thứ hai thế giới, sau Brazil, và là nước sản xuất robusta lớn nhất. Hạt robusta có vị đậm, đắng và chứa nhiều caffeine hơn arabica. Hàng triệu gia đình Việt Nam sống nhờ nghề trồng cà phê.</p>
<p>Cà phê không chỉ là mặt hàng xuất khẩu mà còn là một phần quan trọng của văn hóa Việt. Người ta nhâm nhi cà phê ở quán vỉa hè, ngắm dòng đời trôi qua. Thức uống nổi tiếng nhất là cà phê sữa đá — cà phê đen đậm pha với sữa đặc ngọt và đá. Những năm gần đây, các món sáng tạo như cà phê trứng, cà phê dừa được cả người dân lẫn du khách yêu thích.</p>
<p>Tuy nhiên, nông dân trồng cà phê đối mặt nhiều thách thức. Biến đổi khí hậu khiến thời tiết khó đoán, giá cà phê lên xuống nhanh. Nhiều nông dân đang học các phương pháp hiện đại để sản xuất hạt chất lượng cao hơn, bán được giá tốt hơn.</p>""",
 'questions': [
  ('When did coffee arrive in Vietnam?',
   'in 1758', 'in 1857', 'in 1875', 'in 1957', 'B',
   'Thông tin chi tiết ở câu đầu tiên: "Coffee was first brought to Vietnam by the French in 1857". Cẩn thận với các đáp án đảo số (1758, 1875) — bẫy phổ biến trong bài thi.'),
  ('Why is the Central Highlands good for growing coffee?',
   'It is near the sea', 'It has red soil and cool climate',
   'It has many rivers', 'It is close to big cities', 'B',
   'Đoạn 1: "the Central Highlands, with its red soil and cool climate, was perfect for coffee trees" → đất đỏ và khí hậu mát mẻ.'),
  ('What is special about robusta coffee?',
   'It is sweeter than arabica', 'It is grown only in Brazil',
   'It has more caffeine than arabica', 'It is more expensive', 'C',
   'Đoạn 2: "Robusta beans... contain more caffeine than arabica beans" → chứa nhiều caffeine hơn. Bài không nói robusta ngọt hơn hay đắt hơn.'),
  ('What is "ca phe sua da" made of?',
   'coffee, fresh milk and sugar', 'coffee, condensed milk and ice',
   'coffee, egg and ice', 'coffee, coconut and milk', 'B',
   'Đoạn 3: "strong black coffee served with sweet condensed milk over ice" → cà phê đen + sữa đặc + đá. Cà phê trứng và cà phê dừa là những món khác được nhắc riêng.'),
  ('What challenge do coffee farmers face, according to the passage?',
   'There are not enough workers', 'Coffee prices change quickly',
   'People drink less coffee', 'The soil is becoming poor', 'B',
   'Đoạn 4: "coffee prices go up and down quickly" (giá lên xuống nhanh) = "prices change quickly". Các thách thức khác trong bài là biến đổi khí hậu — không phải thiếu lao động hay đất bạc màu.'),
 ],
},
{
 'title': 'Online Learning: Opportunities and Challenges', 'level': 'B2', 'order': 4,
 'content': """<p>Over the past decade, online learning has changed education dramatically. Students can now attend courses given by universities on the other side of the world without leaving their homes. This flexibility is particularly valuable for working adults, who can study in the evenings or at weekends, and for people living in remote areas with limited access to schools.</p>
<p>Online courses are also generally cheaper than traditional classes. There are no costs for travel or accommodation, and digital materials can be shared with thousands of learners at almost no extra cost. Furthermore, students can learn at their own pace: they can pause a video lecture, repeat difficult sections, or skip material they already know.</p>
<p>Nevertheless, online learning is not without problems. Many students find it difficult to stay motivated without face-to-face contact with teachers and classmates. Technical issues, such as poor internet connections, can interrupt lessons. In addition, some skills — such as laboratory work or medical practice — simply cannot be taught effectively through a screen.</p>
<p>Research suggests that the most effective approach may be "blended learning", which combines online study with regular classroom sessions. In this way, students enjoy the convenience of technology while keeping the human contact that is so important for successful learning.</p>""",
 'translation_vi': """<p>Trong thập kỷ qua, học trực tuyến đã thay đổi giáo dục một cách mạnh mẽ. Sinh viên giờ đây có thể tham gia các khóa học của các trường đại học ở nửa kia thế giới mà không cần rời khỏi nhà. Sự linh hoạt này đặc biệt quý giá với người đi làm — họ có thể học buổi tối hoặc cuối tuần — và với người ở vùng sâu vùng xa, nơi ít trường lớp.</p>
<p>Các khóa học trực tuyến nhìn chung cũng rẻ hơn lớp truyền thống. Không tốn chi phí đi lại, ăn ở; tài liệu số có thể chia sẻ cho hàng nghìn người học mà gần như không tốn thêm chi phí. Hơn nữa, người học có thể học theo tốc độ riêng: tạm dừng bài giảng, xem lại phần khó, hoặc bỏ qua phần đã biết.</p>
<p>Tuy vậy, học trực tuyến không phải không có vấn đề. Nhiều người học khó duy trì động lực khi thiếu tiếp xúc trực tiếp với giáo viên và bạn học. Sự cố kỹ thuật như mạng yếu có thể làm gián đoạn bài học. Ngoài ra, một số kỹ năng — như thực hành thí nghiệm hay y khoa — đơn giản là không thể dạy hiệu quả qua màn hình.</p>
<p>Nghiên cứu cho thấy cách tiếp cận hiệu quả nhất có thể là "học kết hợp" (blended learning) — kết hợp học online với các buổi học trên lớp. Nhờ đó, người học tận hưởng sự tiện lợi của công nghệ mà vẫn giữ được sự kết nối con người rất quan trọng cho việc học thành công.</p>""",
 'questions': [
  ('Who benefits most from the flexibility of online learning, according to paragraph 1?',
   'young children', 'university teachers',
   'working adults and people in remote areas', 'students who live near universities', 'C',
   'Đoạn 1: "particularly valuable for working adults... and for people living in remote areas" → người đi làm và người ở vùng xa.'),
  ('Why are online courses usually cheaper?',
   'Teachers are paid less', 'There are no travel or accommodation costs',
   'The quality is lower', 'Governments pay for them', 'B',
   'Đoạn 2: "There are no costs for travel or accommodation, and digital materials can be shared... at almost no extra cost" → không tốn chi phí đi lại, ăn ở.'),
  ('The phrase "at their own pace" in paragraph 2 means students can ___ .',
   'study with their friends', 'choose their own teachers',
   'learn as fast or slowly as they want', 'pay in small amounts', 'C',
   '"At one\'s own pace" = theo tốc độ của riêng mình. Ngay sau đó bài giải thích: có thể tạm dừng, xem lại, bỏ qua — tức là học nhanh hay chậm tùy ý → C.'),
  ('Which of the following is mentioned as a problem of online learning?',
   'expensive course fees', 'lack of motivation without face-to-face contact',
   'too much homework', 'shortage of teachers', 'B',
   'Đoạn 3: "Many students find it difficult to stay motivated without face-to-face contact" → khó duy trì động lực khi không gặp mặt trực tiếp.'),
  ('What is "blended learning"?',
   'learning only through videos', 'a combination of online and classroom learning',
   'studying two subjects at the same time', 'learning without teachers', 'B',
   'Đoạn 4 định nghĩa rõ: "blended learning, which combines online study with regular classroom sessions" → kết hợp học trực tuyến và học trên lớp.'),
 ],
},
{
 'title': 'Plastic Waste: A Global Problem', 'level': 'B2', 'order': 5,
 'content': """<p>Every year, the world produces about 400 million tonnes of plastic waste, and at least eight million tonnes of it end up in the oceans. Scientists warn that if nothing changes, there could be more plastic than fish in the sea by 2050. Plastic does not disappear; it only breaks down into smaller and smaller pieces called microplastics, which are now found in drinking water, sea salt and even the food we eat.</p>
<p>The main reason for this crisis is our "throw-away culture". Half of all plastic is used only once and then thrown away — plastic bags, straws, cups and food packaging. A plastic bag is used for an average of just fifteen minutes, but it takes hundreds of years to break down.</p>
<p>Many countries are now taking action. Some have banned single-use plastic bags, while others charge customers for them. Companies are developing new materials made from plants that break down naturally. In Vietnam, several supermarkets have started wrapping vegetables in banana leaves instead of plastic.</p>
<p>Individuals can also make a difference. Simple habits — carrying a reusable shopping bag, refusing plastic straws, and using a personal water bottle — can significantly reduce the amount of plastic we throw away. As one environmental activist said, "We do not need a few people doing zero waste perfectly. We need millions of people doing it imperfectly."</p>""",
 'translation_vi': """<p>Mỗi năm thế giới thải ra khoảng 400 triệu tấn rác nhựa, và ít nhất 8 triệu tấn trong số đó trôi ra đại dương. Các nhà khoa học cảnh báo nếu không có gì thay đổi, đến năm 2050 nhựa trong biển có thể nhiều hơn cá. Nhựa không biến mất; nó chỉ vỡ thành những mảnh nhỏ dần gọi là vi nhựa — thứ hiện đã có trong nước uống, muối biển và cả thức ăn của chúng ta.</p>
<p>Nguyên nhân chính của khủng hoảng này là "văn hóa dùng một lần". Một nửa lượng nhựa chỉ được dùng một lần rồi vứt bỏ — túi nylon, ống hút, cốc và bao bì thực phẩm. Một chiếc túi nylon trung bình chỉ được dùng 15 phút nhưng cần hàng trăm năm để phân hủy.</p>
<p>Nhiều quốc gia đang hành động. Một số nước cấm túi nylon dùng một lần, số khác thu phí. Các công ty đang phát triển vật liệu mới từ thực vật có thể phân hủy tự nhiên. Ở Việt Nam, vài siêu thị đã bắt đầu gói rau bằng lá chuối thay vì túi nylon.</p>
<p>Mỗi cá nhân cũng có thể tạo nên khác biệt. Những thói quen đơn giản — mang túi mua sắm dùng lại, từ chối ống hút nhựa, dùng bình nước cá nhân — có thể giảm đáng kể lượng nhựa vứt đi. Như một nhà hoạt động môi trường nói: "Chúng ta không cần vài người sống không rác thải một cách hoàn hảo. Chúng ta cần hàng triệu người làm điều đó một cách chưa hoàn hảo."</p>""",
 'questions': [
  ('What may happen by 2050, according to scientists?',
   'All fish will disappear', 'There may be more plastic than fish in the sea',
   'People will stop using plastic', 'The oceans will be clean', 'B',
   'Đoạn 1: "there could be more plastic than fish in the sea by 2050" → nhựa có thể nhiều hơn cá. Đáp án A quá cực đoan — bài không nói cá sẽ biến mất hết.'),
  ('What are microplastics?',
   'new types of strong plastic', 'very small pieces of broken plastic',
   'plastic products for the kitchen', 'machines that recycle plastic', 'B',
   'Đoạn 1 định nghĩa: "it only breaks down into smaller and smaller pieces called microplastics" → những mảnh nhựa vỡ rất nhỏ.'),
  ('How long is a plastic bag typically used?',
   'about 15 minutes', 'about one day', 'about one week', 'hundreds of years', 'A',
   'Đoạn 2: "A plastic bag is used for an average of just fifteen minutes". "Hàng trăm năm" là thời gian PHÂN HỦY, không phải thời gian sử dụng — bẫy đảo thông tin kinh điển.'),
  ('What have some Vietnamese supermarkets done?',
   'banned all plastic products', 'charged customers for vegetables',
   'used banana leaves to wrap vegetables', 'stopped selling packaged food', 'C',
   'Đoạn 3: "several supermarkets have started wrapping vegetables in banana leaves instead of plastic" → gói rau bằng lá chuối.'),
  ('What is the message of the activist\'s quote in the last paragraph?',
   'Only experts can solve the problem', 'Perfect behaviour is necessary',
   'Small efforts from many people matter', 'Zero waste is impossible', 'C',
   'Câu trích: "We need millions of people doing it imperfectly" — cần hàng triệu người cùng làm dù chưa hoàn hảo → nỗ lực nhỏ của số đông mới quan trọng → C.'),
 ],
},
]
