# Individual Footprint

Individual footprint là phần ghi lại đóng góp của từng thành viên.

Mỗi thành viên cần viết rõ mình đã làm gì, phần đó liên quan thế nào đến sản phẩm cuối cùng và có bằng chứng gì để kiểm tra.

Footprint không chỉ là danh sách công việc.

Footprint cũng cần nói rõ bạn học được gì trong quá trình làm phần việc của mình.

Trong buổi thi cuối kỳ, mỗi thành viên cần có thể giải thích phần việc của mình.

Nhóm cần nộp bản cứng của individual footprint.

Mỗi thành viên cần có một mục riêng theo mẫu dưới đây.

## Thành viên 1: Họ tên và mã sinh viên

### Vai trò trong dự án

- **Team leader**

- Điều phối công việc chung của nhóm.

- Theo dõi tiến độ và đảm bảo các phần của sản phẩm được phát triển theo cùng một định hướng.

- Giữ vai trò kết nối giữa các thành viên để sản phẩm cuối không bị rời rạc giữa các module.

- **App backbone và module integration**

- Phụ trách xây dựng và kiểm soát luồng chính của game.

- Đảm bảo các bước trong game được kết nối mạch lạc, Kết nối các phần như scenario data, UI, trading logic, bias detection, scoring và dashboard thành một game hoàn chỉnh.

- **Data Manager module**

- Phụ trách phần quản lý dữ liệu scenario.

- Đảm bảo dữ liệu được đọc, xử lý và đưa vào từng round đúng cách.

- Hỗ trợ việc randomize thứ tự các rounds và đảm bảo scenario data khớp với app flow.

- **Testing logic của game**

- Tham gia kiểm tra logic của sản phẩm, đặc biệt là **bias detection logic**.

- **Lập Project plan**

- Hỗ trợ cập nhật và theo dõi tiến độ của nhóm.

- Đặc biệt phụ trách chuẩn hóa phần **Key Common Variables** trong Project Plan.

- Đảm bảo các biến quan trọng trong code, dữ liệu và tài liệu được sử dụng thống nhất, giúp sản phẩm dễ hiểu và dễ demo hơn..

### Dấu ấn cá nhân trong sản phẩm

Dấu ấn cá nhân rõ nhất của em thể hiện ở ba phần chính:

- **Kết nối các module thành một flow chơi hoàn chỉnh**

  - Tham gia kết nối các phần riêng lẻ như scenario data, UI, trading logic, bias rules, scoring và final dashboard. Thay vì để các module hoạt động rời rạc, em giúp sắp xếp chúng theo một flow thống nhất để game có thể chạy từ đầu đến cuối.

  - Điều này giúp sản phẩm cuối hoạt động như một game hoàn chỉnh, không chỉ là tập hợp các file code riêng lẻ.

- **Thiết lập Key Common Variables để thống nhất logic giữa các thành viên**

  - Lập và rà soát các Key Common Variables trong project plan để cả nhóm dùng chung một hệ biến. Việc này giúp giảm sai lệch khi ghép các module lại với nhau, đặc biệt giữa trading logic, bias detection, scoring và UI.

- **Xây dựng flow chính của game**

> Đóng góp vào việc thiết kế luồng chơi chính:

- người chơi đọc scenario;

- đưa ra quyết định Buy/Sell/Hold;

- trả lời checkpoint question để xác nhận quyết định;

- hệ thống xử lý giao dịch;

- kết quả của round được hiển thị;

- người chơi tiếp tục sang round tiếp theo hoặc xem final dashboard.

- Flow này giúp trải nghiệm chơi rõ ràng hơn và giúp người chơi hiểu mình đang ở bước nào trong quá trình ra quyết định.

- **Phụ trách Data Manager module**

  - Data Manager module là một dấu ấn quan trọng của em trong sản phẩm.

  - Module này giúp quản lý cách scenario data được đọc, xử lý và đưa vào từng round. Nó cũng hỗ trợ randomize thứ tự các rounds, giúp mỗi lượt chơi có trình tự scenario khác nhau.

  - Nhờ đó, dữ liệu scenario được sử dụng đúng trong app flow và kết nối tốt hơn với các phần như bias detection, checkpoint question và final dashboard
.

### Những việc đã thực sự làm

- Điều phối nhóm, chia đầu việc và theo dõi tiến độ hoàn thiện sản phẩm.

- Xây dựng và chỉnh sửa app backbone để game có thể chạy theo từng round.

- Phụ trách Data Manager module để đọc, quản lý và cung cấp scenario data cho game.

- Kết hợp các module chính gồm scenario data, trading logic, bias detection, scoring và UI.

- Test bias detection logic để kiểm tra hệ thống có ghi nhận bias hợp lý theo decision, trade size, portfolio state, scenario context và decision history hay không.

- Lập project plan để giúp cả nhóm thống nhất logic sản phẩm, đảm bảo code, dữ liệu và tài liệu khớp với nhau, Lập ra các Key Common Variables trong project plan để thống nhất code

### File, tính năng, dữ liệu, logic, giao diện, tài liệu hoặc phần demo đã đóng góp

- File app.py, thể hiện app backbone và luồng chính của game.
- File data_manager.py, thể hiện phần quản lý dữ liệu scenario do em phụ trách.

- File config.py Đây là file giúp các module trong game dùng chung một bộ cấu hình thống nhất, tránh việc mỗi file tự định nghĩa biến riêng và gây lệch logic giữa app flow, trading logic, bias detection, scoring và project plan.

- Project plan , đặc biệt là phần Key Common Variables,
- Logic test cho phần bias detection rule
- README, group footprint và individual footprint thể hiện phần documentation được cập nhật theo bản final.

### Bằng chứng đóng góp

- File app.py, .

- File data_manager.py

File config.py

- Project plan, đặc biệt các sheet “key common variable”, “team task”, “flow”, “python module”

- Bản game chạy được theo flow: nhập tên → đọc scenario → chọn Buy/Sell/Hold → trả lời checkpoint question → confirm decision → xem kết quả round → chơi round tiếp theo → xem final dashboard.

- Ảnh màn hình thể hiện phần việc test logic

### Phần đóng góp đó kết nối thế nào với sản phẩm cuối cùng

Phần em làm giúp sản phẩm cuối cùng hoạt động như một game hoàn chỉnh thay vì chỉ là các module rời rạc. App backbone giữ vai trò kết nối các phần chính: scenario data, UI, trading logic, bias detection, scoring và final dashboard.

Data Manager module giúp game lấy dữ liệu scenario từ file dữ liệu và đưa vào từng round một cách có tổ chức. Đây là phần quan trọng vì scenario là input chính của sản phẩm. Nếu dữ liệu không được quản lý tốt, game sẽ khó randomize rounds, khó hiển thị đúng scenario và khó kết nối với bias detection.

Ngoài ra, việc chuẩn hóa Key Common Variables trong project plan và file config.py giúp cả nhóm dùng chung một hệ biến thống nhất. Điều này làm cho code, dữ liệu, tài liệu và phần demo khớp với nhau hơn, giúp sản phẩm dễ hiểu và dễ bảo vệ trong buổi thi.

### Điều cá nhân học được

Qua dự án này, em học được nhiều bài học trực tiếp từ những khó khăn mà nhóm gặp phải trong quá trình xây dựng sản phẩm:

- **Một sản phẩm tài chính không chỉ cần ý tưởng hay, mà cần logic rõ ràng**

  - Ban đầu, nhóm có định hướng khá rõ về việc xây dựng một behavioral investing simulation game.

  - Tuy nhiên, khi triển khai thành game thật, nhóm gặp nhiều lỗi như code chưa kết nối mượt, bias rule không detect đúng, trading rule hiển thị nhầm return hoặc tài liệu chưa khớp với bản game cuối.

  - Từ đó, em học được rằng một sản phẩm tài chính cần có logic chính xác, dữ liệu thống nhất và phải được test kỹ, chứ không chỉ cần concept tốt.

- **Leader cần hiểu toàn bộ flow, không chỉ chia việc**

  - Em nhận ra rằng vai trò leader không chỉ là phân công công việc cho từng thành viên.

  - Leader cần hiểu toàn bộ flow của sản phẩm để phát hiện điểm lệch giữa các module.

  - Khi một phần thay đổi, ví dụ scenario data, trading rule hoặc bias rule, các phần khác như app flow, scoring, dashboard và documentation cũng có thể bị ảnh hưởng.

  - Vì vậy, leader phải giữ được “bức tranh tổng thể” của sản phẩm.

- **Documentation là công cụ để thống nhất cách làm việc**

  - Qua việc set và rà soát **Key Common Variables** trong project plan, em học được rằng tài liệu không chỉ để nộp.

  - Các biến như cash, shares, trade size, portfolio value, return, bias score và rationality score cần được cả nhóm hiểu giống nhau.

  - Khi có một hệ biến chung, các thành viên dễ kết nối module của mình với các phần khác hơn.

  - Điều này giúp giảm sai lệch giữa code, dữ liệu, UI và tài liệu.

- **Bias detection cần rule rõ ràng và phải test nhiều lần**

  - Khi test bias detection logic, em học được rằng behavioral bias không thể chỉ đưa vào game bằng định nghĩa lý thuyết.

  - Mỗi bias phải được chuyển thành các điều kiện cụ thể và kiểm tra qua nhiều tình huống.

  - Ví dụ, hệ thống không thể kết luận người chơi bị herding chỉ vì họ Buy theo đám đông.

  - Cần xét thêm các yếu tố như crowd strength, fundamentals, trade size và bối cảnh scenario.

  - Điều này giúp kết quả bias detection hợp lý hơn và dễ giải thích hơn trong demo.

- **Làm việc nhóm hiệu quả cần hiểu sự liên kết giữa các phần**

  - Ban đầu, các thành viên chủ yếu hiểu phần mình phụ trách, nên khi tích hợp sản phẩm, nhóm mất thời gian để giải thích và sửa lỗi giữa các module.

  - Sau nhiều lần họp và trao đổi liên tục, mọi người bắt đầu hiểu rõ hơn phần việc của mình liên quan thế nào đến phần của người khác.

  - Khi cả nhóm nhìn vào flow chung thay vì chỉ nhìn từng phần riêng lẻ, việc xử lý lỗi trở nên nhanh hơn và hiệu quả hơn.

- **Quản lý thời gian cần tính cả debugging và testing**

  - Nhóm có lúc bị trễ so với kế hoạch ban đầu vì nhiều lỗi chỉ xuất hiện khi tích hợp hoặc khi test nhiều trường hợp khác nhau.

  - Từ đó, em học được rằng khi lập kế hoạch cho một dự án có code, không thể chỉ tính thời gian viết nội dung hoặc viết code raw.

  - Cần dành đủ thời gian cho debugging, testing, chỉnh sửa logic và cập nhật tài liệu.

  - Đây là bài học quan trọng giúp em hiểu rõ hơn cách quản lý một dự án sản phẩm từ ý tưởng đến bản demo cuối cùng.

### Khó khăn đã gặp và cách xử lý

- **hó khăn trong việc tích hợp các module**

- Khó khăn lớn nhất là ghép các phần do nhiều thành viên phụ trách thành một sản phẩm hoàn chỉnh.

- Ban đầu, mỗi thành viên hiểu rõ phần của mình hơn là toàn bộ game, nên khi tích hợp, nhóm gặp một số lỗi như:

  - code chưa kết nối mượt;

  - bias rule chưa detect đúng;

  - trading rule hiển thị nhầm return;

  - project plan chưa phản ánh đúng bản game cuối.

- Để xử lý, em cùng nhóm rà lại sản phẩm theo **user flow từ đầu đến cuối**, thay vì chỉ kiểm tra từng file riêng lẻ.

- **Khó khăn trong việc kiểm tra flow chơi**

- Khi game có nhiều bước như đọc scenario, chọn decision, trả lời checkpoint question, confirm decision, xử lý giao dịch và hiển thị kết quả, chỉ cần một bước sai là toàn bộ flow có thể bị lệch.

- Nhóm kiểm tra lại từng bước:

  - scenario có được đọc đúng không;

  - decision có được confirm sau checkpoint question không;

  - trading result có cập nhật đúng cash, shares và return không;

  - bias có được ghi nhận hợp lý không;

  - final dashboard có phản ánh đúng dữ liệu không.

- Cách làm này giúp nhóm phát hiện lỗi theo logic trải nghiệm người dùng, không chỉ theo từng file code.

- **Khó khăn do các thành viên chưa hiểu toàn bộ game ngay từ đầu**

- Ban đầu, mỗi người chủ yếu tập trung vào phần mình phụ trách như scenario, UI, trading logic, bias detection hoặc app flow.

- Vì vậy, khi một phần thay đổi, các phần khác đôi khi chưa được cập nhật theo.

- Để xử lý, nhóm họp và trao đổi nhiều lần hơn để thống nhất mối quan hệ giữa các module.

- Sau khi mọi người hiểu rõ hơn flow chung, việc sửa lỗi và hoàn thiện sản phẩm trở nên nhanh hơn.

- **Khó khăn trong việc xây dựng bias detection logic**

- Behavioral bias không dễ chuyển thành rule vì một hành động giống nhau có thể mang ý nghĩa khác nhau trong từng bối cảnh.

- Nếu rule quá đơn giản, hệ thống có thể detect sai; nếu rule quá phức tạp, nhóm khó giải thích trong buổi demo.

- Vì vậy, nhóm quyết định tập trung vào các bias phổ biến, dễ quan sát và có thể gắn với scenario rõ ràng.

- Nhóm cũng test bias logic qua nhiều tình huống để đảm bảo kết quả detect hợp lý hơn.

- **Khó khăn về quản lý thời gian**

- Nhóm có lúc bị trễ so với kế hoạch ban đầu vì nhiều lỗi chỉ xuất hiện ở giai đoạn tích hợp và testing.

- Để xử lý, nhóm ưu tiên ổn định **core flow** trước:

  - game phải chạy mượt;

  - trading logic phải đúng;

  - bias detection phải giải thích được;

  - documentation phải khớp với bản final.

- Sau khi các phần cốt lõi ổn định, nhóm mới tiếp tục chỉnh UI, dashboard và tài liệu nộp cuối.

### Lời nhắn cho sinh viên khóa sau

Nếu sinh viên khóa sau muốn tiếp tục hoặc học từ phần việc này, bạn muốn nhắn điều gì?

Nếu muốn tiếp tục phần việc này, các em hãy phát triển thêm nhiều scenario hơn, nhiều bias và rule hơn, cùng với đó cũng có thể phát triển các tính năng như multi-stock, multi-sector, cho phép short-selling, ...

Tuy nhiên, đừng cố làm sản phẩm quá phức tạp ngay từ đầu. Với một finance-based game, bản tốt nhất không phải là bản có nhiều tính năng nhất, mà là bản có flow rõ, logic đúng, dữ liệu sạch, và demo mượt. Khi core logic đã vững, việc mở rộng sẽ dễ hơn rất nhiều.

Một game muốn thành công thì phải test đi test lại rất nhiều lần. Hãy test nhiều lần nhất có thể vì bô logic đầu tiên luôn là bộ logic không hooàn hảo.

Cuối cùng, với vai trò của một leader, hãy đảm bảo tất cả các thành viên đều hiểu nhóm mình đang làm gì, mình kết nối với các thành viên khác ra sao. Đừng để thành viên nhóm chỉ biết làm việc của bản thân.
