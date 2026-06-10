# GROUP README TEMPLATE

## Tên sản phẩm

FOMOPOLY

## Mã nhóm

G07

## Thành viên

| Họ tên | Mã sinh viên | Vai trò chính |
|---|---|---|
| Vương Huy Hoàng | 2312380010 | Leader, App Backbone design, . Data Management, logic test |
| Đào Minh Quang | 2312380030 | Data readiness and scenario design |
| Nguyễn Hoàng Thiều Trang | 2313380037 | Design trading rule, logic test |
| Trần Trung Hiếu | 2312380009 | Design bias detecion rule and scoring rule |
| Nguyễn Hạnh Trang | 2312380038 | UI design |

## Mô tả ngắn về sản phẩm

FOMOPOLY là một game mô phỏng đầu tư được xây dựng bằng Python/Streamlit. Người chơi bắt đầu với tài khoản ảo 100,000 USD và ra quyết định đầu tư đối với một cổ phiếu giả lập tên là STEELSTOX. Qua 8 vòng chơi, người chơi đọc các scenario thị trường, ra quyết định đầu tư, xác nhận quyết định bằng câu hỏi ngắn và xem kết quả danh mục sau từng round. Điểm khác biệt của sản phẩm là game không chỉ tính lãi/lỗ, mà còn phân tích các behavioral biases có thể xuất hiện trong quá trình ra quyết định. Cuối game, người chơi nhận được final dashboard gồm kết quả đầu tư, bias summary, rationality score và feedback.

## Vấn đề sản phẩm giải quyết

Nhiều sinh viên học tài chính được học lý thuyết về đầu tư, nhưng có ít cơ hội thực hành ra quyết định đầu tư trong môi trường an toàn. Khi mới tiếp cận thị trường chứng khoán, người học có thể chưa nhận ra rằng quyết định của mình bị ảnh hưởng bởi cảm xúc, tin tức, biến động giá, đám đông hoặc trạng thái lãi/lỗ.

FOMOPOLY giải quyết vấn đề này bằng cách tạo ra một môi trường mô phỏng, nơi người chơi có thể giao dịch bằng tài khoản ảo mà không có rủi ro tài chính thật. Sau mỗi quyết định, hệ thống cập nhật danh mục và ghi nhận các dấu hiệu behavioral bias. Nhờ đó, sản phẩm giúp người học hiểu rằng đầu tư không chỉ là vấn đề tính toán lợi nhuận, mà còn là vấn đề kiểm soát hành vi và ra quyết định hợp lý.

## Người dùng mục tiêu

Người dùng chính của sản phẩm là sinh viên đại học, đặc biệt là sinh viên năm 1 và năm 2 thuộc các ngành tài chính, ngân hàng, kinh tế, kinh doanh hoặc các ngành liên quan.

Họ có thể dùng sản phẩm trong lớp học, buổi demo nhóm, hoạt động thảo luận về behavioral finance hoặc tự học cá nhân. Game phù hợp với người mới học đầu tư vì giao diện đơn giản, quyết định chỉ gồm Buy, Sell hoặc Hold, nhưng vẫn đủ logic để giúp người chơi hiểu mối liên hệ giữa thông tin thị trường, hành vi giao dịch và bias

## Tính năng chính

- Mô phỏng đầu tư vào cổ phiếu giả lập STEELSTOX với tài khoản ảo 100,000 USD.
- Cung cấp các scenario thị trường theo từng round, gồm bối cảnh, giá cổ phiếu, tín hiệu và thông tin đám đông.
- Randomize thứ tự các round trong mỗi lượt chơi để tạo trải nghiệm khác nhau.
- Cho phép người chơi ra quyết định Buy, Sell hoặc Hold.
- Cho phép chọn trade size khi Buy hoặc Sell.
- Yêu cầu người chơi trả lời câu hỏi ngắn sau mỗi round để xác nhận quyết định.
- Xử lý giao dịch theo số cổ phiếu nguyên và cập nhật danh mục sau mỗi quyết định.
- Hiển thị các chỉ số chính như cash, shares, portfolio value, round return và total return.
- Ghi nhận và phân tích các behavioral biases của người chơi.
- Tạo final dashboard cuối game gồm kết quả danh mục, tổng lợi nhuận, bias summary, score và feedback ngắn.

## Cách mở hoặc chạy sản phẩm

Cách 1: Nhóm khyến nghị người chơi sử dụng cách này

Có thể chạy sản phẩm trực tiếp từ repo bằng Streamlit theo các bước sau:

1. Mở repo của nhóm trên GitHub.
2. Tải repo về máy 
3. Mở folder project bằng VS Code hoặc terminal (ưu tiên VS Code)
4. Cài đặt các thư viện cần thiết nếu chưa có.
5. Chạy file app chính bằng Streamlit.
6. Nhập tên người chơi và bắt đầu game.
8. Sau khi hoàn thành 8 rounds, xem final dashboard.

Nếu chạy bằng terminal, có thể dùng các lệnh sau:

```bash
pip install -r requirements.txt
streamlit run app.py
```

Nếu không có file requirements.txt, có thể cài các thư viện chính thường dùng bằng các lệnh sau

```bash
pip install streamlit pandas numpy matplotlib
streamlit run app.py
```

Cách 2: người chơi có thể mở trực tiếp game bằng cách nhập link sau: bit.ly/3RR5kJQ

## Link demo nếu có

bit.ly/3RR5kJQ

## Ghi chú về dữ liệu nếu có

Sản phẩm sử dụng dữ liệu giả lập và dữ liệu tự tạo bởi nhóm. Dữ liệu chính là bộ scenario thị trường cho cổ phiếu giả lập STEELSTOX, bao gồm giá cổ phiếu, bối cảnh thị trường, tin tức, fundamentals, tín hiệu đám đông, câu hỏi checkpoint và các biến phục vụ bias detection.

Converted from Markdown template
