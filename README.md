## Nếu bạn muốn xem phiên bản được viết bằng python với các file .py thì hãy chuyển sang nhánh master
## Tiền xử lý dữ liệu văn bản Tiếng Việt
Dữ liệu thô được lây từ [https://github.com/duyvuleo/](https://github.com/duyvuleo/VNTC/tree/master/Data/27Topics/Ver1.1) đặt trong thư mục `raw-data`.

Dữ liệu sau khi xử lý được đặt trong thư mục `clean-data`.

Tiền xử lý dữ liệu được thực hiện qua các bước : 
- Chuẩn hóa unicode 
- Chuẩn hóa cách gõ dấu tiếng Việt
- Chuẩn hóa chữ viết thường
- Tách từ tiếng Việt
- Đưa cả đoạn văn về trên 1 dòng, xóa các khoảng cách thừa

### Ví dụ 
Có một đoạn văn bản gốc như trong file `text.txt`, sau khi xử lý thì nó sẽ thành :
```
tp hcm phạt người không đeo khẩu trang nơi công cộng người dân ở thành phố không đeo khẩu trang nơi công cộng sẽ bị xử phạt mức cao nhất 300 000 đồng từ ngày 58 yêu cầu này được chủ tịch ubnd thành phố nguyễn thành phong đưa ra tại cuộc họp ban chỉ đạo phòng chống dịch bệnh covid 19 của tp hcm chiều 38 việc xử phạt không đeo khẩu trang nơi công cộng được tp hcm cũng như các địa phương khác thực hiện từ cuối tháng 3 khi covid 19 bùng phát tuy nhiên sau khi hết thực hiện cách ly xã hội từ ngày 234 việc đeo khẩu trang nơi công cộng chỉ dừng lại ở mức khuyến cáo theo nghị định số 1762013 người dân không đeo khẩu trang nơi công cộng sẽ bị xử phạt từ 100 000 đến 300 000 đồng trong khoảng một tháng áp dụng trước đó tp hcm đã xử phạt hơn 4 300 trường hợp với gần 870 triệu đồng theo ông phong việc đeo khẩu trang đã được khẳng định có thể tránh lây lan dịch bệnh cho người khác và bảo vệ sức khỏe cho người sử dụng sở công thương phải nắm nguồn cung ứng khẩu trang chủ động thông báo các điểm bán để người dân dễ dàng mua vì đã xử phạt thì phải bảo đảm đủ nguồn cung ông phong nói đội trật tự đô thị phường bến nghé quận 1 xử phạt người không đeo khẩu trang trên phố đi bộ nguyễn huệ chiều 154 ảnh quỳnh trần đội trật tự đô thị phường bến nghé quận 1 xử phạt người không đeo khẩu trang trên phố đi bộ nguyễn huệ chiều 154 ảnh quỳnh trần bí thư thành ủy nguyễn thiện nhân cũng cho rằng việc đeo khẩu trang là một trong những biện pháp cơ bản để tránh dịch bệnh lây lan việc này rất dễ làm không tốn nhiều tiền nhưng nhiều nước bỏ lơi và đã bị vỡ trận ngoài đường hiện có ít nhất 20 người không đeo khẩu trang người không đeo không những tự rước bệnh vào mình mà còn nguy cơ lây cho người khác đeo khẩu trang hơi cực tí thôi nhưng đi đâu cũng nên đeo để giữ an toàn ông nhân nói và khẳng định thành phố bảo đảm không thiếu khẩu trang cho người dân chủ tịch ubnd thành phố nguyễn thành phong cũng cho biết đã đồng ý việc tái lập các chốt kiểm soát ở cửa ngõ tp hcm để phòng chống covid 19 trước đó thành phố đã lập 62 chốt kiểm soát hoạt động 2424 từ ngày 44 để phòng chống dịch lực lượng tham gia là công an thành phố sở y tế bộ tư lệnh thành phố thanh tra giao thông ban quản lý an toàn thực phẩm quản lý thị trường trong đó 16 chốt chính cấp thành phố đặt tại trạm thu phí long phước cao tốc tp hcm long thành dầu giây cao tốc trung lương cầu đôi đường trần văn giàu đường ba làng đường xuyên á quốc lộ 22 cầu phú cường cầu vĩnh bình cầu vượt sóng thần quốc lộ 1k quốc lộ 50 quốc lộ 1a cầu đồng nai bến xe miền tây bến xe miền đông sân bay tân sơn nhất cảng cát lái đến ngày 234 chính quyền thành phố dừng hoạt động các chốt này vì dịch bệnh đã được khống chế tp hcm dừng cách ly xã hội theo chỉ thị 19 của thủ tướng sau 19 ngày hoạt động các chốt chính đã kiểm tra gần 270 000 xe trong đó có 235 000 ôtô gần 600 000 người được kiểm tra y tế đo thân nhiệt bao gồm cả 3 000 người nước ngoài hơn 130 000 người được yêu cầu khai báo y tế
```

Project được tham khảo từ trang [https://nguyenvanhieu.vn/phan-loai-van-ban-tieng-viet/](https://nguyenvanhieu.vn/phan-loai-van-ban-tieng-viet/) và phục vụ cho bài tập lớn môn học.    
