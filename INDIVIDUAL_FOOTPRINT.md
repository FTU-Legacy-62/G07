# Individual Footprint

Individual footprint là phần ghi lại đóng góp của từng thành viên.

Mỗi thành viên cần viết rõ mình đã làm gì, phần đó liên quan thế nào đến sản phẩm cuối cùng và có bằng chứng gì để kiểm tra.

Footprint không chỉ là danh sách công việc.

Footprint cũng cần nói rõ bạn học được gì trong quá trình làm phần việc của mình.

Trong buổi thi cuối kỳ, mỗi thành viên cần có thể giải thích phần việc của mình.

Nhóm cần nộp bản cứng của individual footprint.

Mỗi thành viên cần có một mục riêng theo mẫu dưới đây.

## Thành viên 1: Vương Huy Hoàng
### Vai trò trong dự án

- **Team leader**
<!-- -->
    Điều phối công việc chung của nhóm.

    Theo dõi tiến độ và đảm bảo các phần của sản phẩm được phát triển theo cùng một định hướng.

    Giữ vai trò kết nối giữa các thành viên để sản phẩm cuối không bị rời rạc giữa các module.
<!-- -->
- **App backbone và module integration**
<!-- -->
      Phụ trách xây dựng và kiểm soát luồng chính của game.

      Đảm bảo các bước trong game được kết nối mạch lạc, Kết nối các phần như scenario data, UI, trading logic, bias detection, scoring và dashboard thành một game hoàn chỉnh.
<!-- -->
- **Data Manager module**
<!-- -->
      Phụ trách phần quản lý dữ liệu scenario.

      Đảm bảo dữ liệu được đọc, xử lý và đưa vào từng round đúng cách.

      Hỗ trợ việc randomize thứ tự các rounds và đảm bảo scenario data khớp với app flow.
<!-- -->
- **Testing logic của game**
<!-- -->
      Tham gia kiểm tra logic của sản phẩm, đặc biệt là **bias detection logic**.
<!-- -->
- **Lập Project plan**
<!-- -->
      Hỗ trợ cập nhật và theo dõi tiến độ của nhóm.

      Đặc biệt phụ trách chuẩn hóa phần **Key Common Variables** trong Project Plan.

      Đảm bảo các biến quan trọng trong code, dữ liệu và tài liệu được sử dụng thống nhất, giúp sản phẩm dễ hiểu và dễ demo hơn..
<!-- -->
### Dấu ấn cá nhân trong sản phẩm

    Dấu ấn cá nhân rõ nhất của em thể hiện ở ba phần chính:

- **Kết nối các module thành một flow chơi hoàn chỉnh**
<!-- -->
      Tham gia kết nối các phần riêng lẻ như scenario data, UI, trading logic, bias rules, scoring và final dashboard. Thay vì để các module hoạt động rời rạc, em giúp sắp xếp chúng theo một flow thống nhất để game có thể chạy từ đầu đến cuối.

      Điều này giúp sản phẩm cuối hoạt động như một game hoàn chỉnh, không chỉ là tập hợp các file code riêng lẻ.
<!-- -->
- **Thiết lập Key Common Variables để thống nhất logic giữa các thành viên**
<!-- -->
      Lập và rà soát các Key Common Variables trong project plan để cả nhóm dùng chung một hệ biến. Việc này giúp giảm sai lệch khi ghép các module lại với nhau, đặc biệt giữa trading logic, bias detection, scoring và UI.
<!-- -->
- **Xây dựng flow chính của game**
<!-- -->
        Đóng góp vào việc thiết kế luồng chơi chính:

            người chơi đọc scenario;

            đưa ra quyết định Buy/Sell/Hold;
            
            trả lời checkpoint question để xác nhận quyết định;
            
            hệ thống xử lý giao dịch;
            
            kết quả của round được hiển thị;
            
            người chơi tiếp tục sang round tiếp theo hoặc xem final dashboard.

            Flow này giúp trải nghiệm chơi rõ ràng hơn và giúp người chơi hiểu mình đang ở bước nào trong quá trình ra quyết định.
<!-- -->
- **Phụ trách Data Manager module**
<!-- -->
      Data Manager module là một dấu ấn quan trọng của em trong sản phẩm.

      Module này giúp quản lý cách scenario data được đọc, xử lý và đưa vào từng round. Nó cũng hỗ trợ randomize thứ tự các rounds, giúp mỗi lượt chơi có trình tự scenario khác nhau.

  Nhờ đó, dữ liệu scenario được sử dụng đúng trong app flow và kết nối tốt hơn với các phần như bias detection, checkpoint question và final dashboard
.<!-- -->

### Những việc đã thực sự làm

- Điều phối nhóm, chia đầu việc và theo dõi tiến độ hoàn thiện sản phẩm.

- Xây dựng và chỉnh sửa app backbone để game có thể chạy theo từng round.

- Phụ trách Data Manager module để đọc, quản lý và cung cấp scenario data cho game.

- Kết hợp các module chính gồm scenario data, trading logic, bias detection, scoring và UI.

- Test bias detection logic để kiểm tra hệ thống có ghi nhận bias hợp lý theo decision, trade size, portfolio state, scenario context và decision history hay không.

- Lập project plan để giúp cả nhóm thống nhất logic sản phẩm, đảm bảo code, dữ liệu và tài liệu khớp với nhau, Lập ra các Key Common Variables trong project plan để thống nhất code

### File, tính năng, dữ liệu, logic, giao diện, tài liệu hoặc phần demo đã đóng góp

- File **app.py**, thể hiện app backbone và luồng chính của game.
- File **data_manager.py**, thể hiện phần quản lý dữ liệu scenario do em phụ trách.

- File **config.py** Đây là file giúp các module trong game dùng chung một bộ cấu hình thống nhất, tránh việc mỗi file tự định nghĩa biến riêng và gây lệch logic giữa app flow, trading logic, bias detection, scoring và project plan.

- **Project plan** , đặc biệt là phần **Key Common Variables**,
- Logic test cho phần bias detection rule

### Bằng chứng đóng góp

- File **app.py** .

- File **data_manager.py**

- File **config.py**

- Project plan, đặc biệt các sheet “key common variable”, “team task”, “flow”, “python module”

- Bản game chạy được theo flow: nhập tên → đọc scenario → chọn Buy/Sell/Hold → trả lời checkpoint question → confirm decision → xem kết quả round → chơi round tiếp theo → xem final dashboard.

- Ảnh màn hình thể hiện phần việc test logic

### Phần đóng góp đó kết nối thế nào với sản phẩm cuối cùng

- Phần em làm giúp sản phẩm cuối cùng hoạt động như một game hoàn chỉnh thay vì chỉ là các module rời rạc. App backbone giữ vai trò kết nối các phần chính: scenario data, UI, trading logic, bias detection, scoring và final dashboard.

- Data Manager module giúp game lấy dữ liệu scenario từ file dữ liệu và đưa vào từng round một cách có tổ chức. Đây là phần quan trọng vì scenario là input chính của sản phẩm. Nếu dữ liệu không được quản lý tốt, game sẽ khó randomize rounds, khó hiển thị đúng scenario và khó kết nối với bias detection.

- Ngoài ra, việc chuẩn hóa Key Common Variables trong project plan và file config.py giúp cả nhóm dùng chung một hệ biến thống nhất. Điều này làm cho code, dữ liệu, tài liệu và phần demo khớp với nhau hơn, giúp sản phẩm dễ hiểu và dễ bảo vệ trong buổi thi.

### Điều cá nhân học được

Qua dự án này, em học được nhiều bài học trực tiếp từ những khó khăn mà nhóm gặp phải trong quá trình xây dựng sản phẩm:

- **Một sản phẩm tài chính không chỉ cần ý tưởng hay, mà cần logic rõ ràng**
<!-- -->
       Ban đầu, nhóm có định hướng khá rõ về việc xây dựng một behavioral investing simulation game.
    
       Tuy nhiên, khi triển khai thành game thật, nhóm gặp nhiều lỗi như code chưa kết nối mượt, bias rule không detect đúng, trading rule hiển thị nhầm return hoặc tài liệu chưa khớp với bản game cuối.
    
       Từ đó, em học được rằng một sản phẩm tài chính cần có logic chính xác, dữ liệu thống nhất và phải được test kỹ, chứ không chỉ cần concept tốt.
<!-- -->
- **Leader cần hiểu toàn bộ flow, không chỉ chia việc**
<!-- -->
       Em nhận ra rằng vai trò leader không chỉ là phân công công việc cho từng thành viên.
    
       Leader cần hiểu toàn bộ flow của sản phẩm để phát hiện điểm lệch giữa các module.
    
       Khi một phần thay đổi, ví dụ scenario data, trading rule hoặc bias rule, các phần khác như app flow, scoring, dashboard và documentation cũng có thể bị ảnh hưởng.
    
       Vì vậy, leader phải giữ được “bức tranh tổng thể” của sản phẩm.
<!-- -->
- **Documentation là công cụ để thống nhất cách làm việc**
<!-- -->
      Qua việc set và rà soát **Key Common Variables** trong project plan, em học được rằng tài liệu không chỉ để nộp.
    
      Các biến như cash, shares, trade size, portfolio value, return, bias score và rationality score cần được cả nhóm hiểu giống nhau.
    
      Khi có một hệ biến chung, các thành viên dễ kết nối module của mình với các phần khác hơn.
    
      Điều này giúp giảm sai lệch giữa code, dữ liệu, UI và tài liệu.
<!-- -->
- **Bias detection cần rule rõ ràng và phải test nhiều lần**
<!-- -->
      Khi test bias detection logic, em học được rằng behavioral bias không thể chỉ đưa vào game bằng định nghĩa lý thuyết.
    
      Mỗi bias phải được chuyển thành các điều kiện cụ thể và kiểm tra qua nhiều tình huống.
    
      Ví dụ, hệ thống không thể kết luận người chơi bị herding chỉ vì họ Buy theo đám đông.
    
      Cần xét thêm các yếu tố như crowd strength, fundamentals, trade size và bối cảnh scenario.
    
      Điều này giúp kết quả bias detection hợp lý hơn và dễ giải thích hơn trong demo.
<!-- -->
- **Làm việc nhóm hiệu quả cần hiểu sự liên kết giữa các phần**
<!-- -->
      Ban đầu, các thành viên chủ yếu hiểu phần mình phụ trách, nên khi tích hợp sản phẩm, nhóm mất thời gian để giải thích và sửa lỗi giữa các module.
    
      Sau nhiều lần họp và trao đổi liên tục, mọi người bắt đầu hiểu rõ hơn phần việc của mình liên quan thế nào đến phần của người khác.
    
      Khi cả nhóm nhìn vào flow chung thay vì chỉ nhìn từng phần riêng lẻ, việc xử lý lỗi trở nên nhanh hơn và hiệu quả hơn.
<!-- -->
- **Quản lý thời gian cần tính cả debugging và testing**
<!-- -->
      Nhóm có lúc bị trễ so với kế hoạch ban đầu vì nhiều lỗi chỉ xuất hiện khi tích hợp hoặc khi test nhiều trường hợp khác nhau.
    
      Từ đó, em học được rằng khi lập kế hoạch cho một dự án có code, không thể chỉ tính thời gian viết nội dung hoặc viết code raw.
    
      Cần dành đủ thời gian cho debugging, testing, chỉnh sửa logic và cập nhật tài liệu.
    
      Đây là bài học quan trọng giúp em hiểu rõ hơn cách quản lý một dự án sản phẩm từ ý tưởng đến bản demo cuối cùng.
<!-- -->
### Khó khăn đã gặp và cách xử lý

- **Khó khăn trong việc tích hợp các module**
<!-- -->
          Khó khăn lớn nhất là ghép các phần do nhiều thành viên phụ trách thành một sản phẩm hoàn chỉnh.
    
          Ban đầu, mỗi thành viên hiểu rõ phần của mình hơn là toàn bộ game, nên khi tích hợp, nhóm gặp một số lỗi như:
    
              code chưa kết nối mượt;
    
              bias rule chưa detect đúng;
    
              trading rule hiển thị nhầm return;
    
              project plan chưa phản ánh đúng bản game cuối.
    
          Để xử lý, em cùng nhóm rà lại sản phẩm theo **user flow từ đầu đến cuối**, thay vì chỉ kiểm tra từng file riêng lẻ.
<!-- -->
- **Khó khăn trong việc kiểm tra flow chơi**
<!-- -->
        Khi game có nhiều bước như đọc scenario, chọn decision, trả lời checkpoint question, confirm decision, xử lý giao dịch và hiển thị kết quả, chỉ cần một bước sai là toàn bộ flow có thể bị lệch.
    
          Nhóm kiểm tra lại từng bước:
    
              scenario có được đọc đúng không;
    
              decision có được confirm sau checkpoint question không;
    
              trading result có cập nhật đúng cash, shares và return không;
    
              bias có được ghi nhận hợp lý không;
    
              final dashboard có phản ánh đúng dữ liệu không.
    
          Cách làm này giúp nhóm phát hiện lỗi theo logic trải nghiệm người dùng, không chỉ theo từng file code.
<!-- -->
- **Khó khăn do các thành viên chưa hiểu toàn bộ game ngay từ đầu**
<!-- -->
          Ban đầu, mỗi người chủ yếu tập trung vào phần mình phụ trách như scenario, UI, trading logic, bias detection hoặc app flow.
    
          Vì vậy, khi một phần thay đổi, các phần khác đôi khi chưa được cập nhật theo.
    
          Để xử lý, nhóm họp và trao đổi nhiều lần hơn để thống nhất mối quan hệ giữa các module.
    
          Sau khi mọi người hiểu rõ hơn flow chung, việc sửa lỗi và hoàn thiện sản phẩm trở nên nhanh hơn.
<!-- -->
- **Khó khăn về quản lý thời gian**
<!-- -->
          Nhóm có lúc bị trễ so với kế hoạch ban đầu vì nhiều lỗi chỉ xuất hiện ở giai đoạn tích hợp và testing.
    
          Để xử lý, nhóm ưu tiên ổn định **core flow** trước:
    
              game phải chạy mượt;
    
              trading logic phải đúng;
    
              bias detection phải giải thích được;
    
              documentation phải khớp với bản final.
    
          Sau khi các phần cốt lõi ổn định, nhóm mới tiếp tục chỉnh UI, dashboard và tài liệu nộp cuối.
<!-- -->
### Lời nhắn cho sinh viên khóa sau

Nếu sinh viên khóa sau muốn tiếp tục hoặc học từ phần việc này, bạn muốn nhắn điều gì?

- Nếu muốn tiếp tục phần việc này, các em hãy phát triển thêm nhiều scenario hơn, nhiều bias và rule hơn, cùng với đó cũng có thể phát triển các tính năng như multi-stock, multi-sector, cho phép short-selling, ...

- Tuy nhiên, đừng cố làm sản phẩm quá phức tạp ngay từ đầu. Với một finance-based game, bản tốt nhất không phải là bản có nhiều tính năng nhất, mà là bản có flow rõ, logic đúng, dữ liệu sạch, và demo mượt. Khi core logic đã vững, việc mở rộng sẽ dễ hơn rất nhiều.

- Một game muốn thành công thì phải test đi test lại rất nhiều lần. Hãy test nhiều lần nhất có thể vì bô logic đầu tiên luôn là bộ logic không hooàn hảo.

- Cuối cùng, với vai trò của một leader, hãy đảm bảo tất cả các thành viên đều hiểu nhóm mình đang làm gì, mình kết nối với các thành viên khác ra sao. Đừng để thành viên nhóm chỉ biết làm việc của bản thân.

## Thành viên 2: Trần Trung Hiếu - 2312380009

## Vai trò trong dự án

Phụ trách chính phần thiết kế bias, hỗ trợ xây dựng rule chấm điểm và hoàn thiện trải nghiệm người dùng cuối cùng. Công việc bao gồm thiết kế logic cho các bias như herding, overconfidence, availability bias, loss aversion và disposition effect; đồng thời chuyển các khái niệm hành vi này thành hệ thống rule và khung điểm có thể áp dụng trực tiếp trong game.

## Dấu ấn cá nhân trong sản phẩm

Dấu ấn nổi bật nhất nằm ở phần lượng hóa các bias thành cơ chế chấm điểm theo bối cảnh. Hệ thống không chỉ đánh giá người chơi dựa trên hành động Buy/Sell/Hold, mà còn xét toàn bộ bối cảnh thị trường như news sentiment, fundamentals, crowd signal, trade size và trạng thái lãi/lỗ của vị thế. Nhờ đó, game có thể phân biệt tốt hơn giữa một quyết định đầu tư hợp lý và một hành vi bị ảnh hưởng bởi thiên kiến.

Bên cạnh đó, quy tắc tính portfolio return và stockholding return cũng được chỉnh sửa để phục vụ việc xác định bias chính xác hơn, đặc biệt với loss aversion và disposition effect. Portfolio return phản ánh hiệu quả tổng thể của danh mục, trong khi stockholding return giúp đánh giá trạng thái lãi/lỗ của vị thế đang nắm giữ.

Ở giai đoạn cuối, phần UI được refine và final touch để sản phẩm hoàn thiện hơn. Giao diện được chỉnh sửa theo hướng informative và comprehensive hơn, đồng thời các chart trong UI được hoàn thiện để kết quả game trực quan, chỉn chu và dễ theo dõi hơn đối với người chơi.

### Những việc đã thực sự làm

1. **Logic tài chính và portfolio**

        - Đổi toàn bộ đơn vị tiền sang USD.
        
        - Game bắt đầu với 100,000 USD.
        
        - Shares được chuyển sang số nguyên, không còn mua ra số thập phân.
        
        - Khi Buy 100% mà còn dư cash nhỏ không đủ mua 1 cổ phiếu, hệ thống sẽ không cho chọn Buy tiếp.
        
        - Tách rõ 2 loại return:
        
        - unrealized_return: return của cổ phiếu đang nắm giữ.
        
        - portfolio_return: return tổng của toàn bộ portfolio.
        
        - unrealized_return được dùng cho các bias như Loss Aversion và Disposition Effect để chính xác hơn.

2. **Bias detection**

        - Loss Aversion và Disposition Effect được chỉnh về ngưỡng lỗ 7%.
        
        - Loss Aversion giờ trigger khi người chơi giữ vị thế đang lỗ trên 7%.
        
        - Disposition Effect giờ nhận diện tốt hơn các hành vi:
        
        - bán winner nhỏ quá sớm,
        
        - giữ loser quá lâu,
        
        - bán winner khi signal vẫn còn tốt.
        
        - Sửa false positive: nếu bán winner nhỏ nhưng fundamental/news đang xấu thật thì không tính là Disposition.
        
        - Herding được kiểm lại để chỉ trigger khi:
        
        - crowd signal mạnh,
        
        - người chơi đi theo crowd,
        
        - fundamental không support rõ ràng.
        
        - Availability, Framing, Overconfidence cũng được kiểm tra lại qua log để đảm bảo trigger hợp lý hơn.

3. **Scenario content**

        - Xóa các mô tả liên quan đến “Vietnam” để scenario trung tính hơn.
        
        - Cập nhật nhiều phần news, fundamentals, forum/crowd sentiment, outcome.
        
        - Round 2 được chỉnh lại để có:
        
        - crowd_direction = sell,
        
        - crowd_strength = 4,
        
        - news_sentiment = positive,
        
        - fundamental_signal = good.
        
        - Herding scenario G2 được set đúng biến:
        
        - positive news,
        
        - neutral fundamentals,
        
        - crowd buy rất mạnh,
        
        - outcome giảm.
        
        - Các scenario giờ có độ mâu thuẫn tốt hơn giữa news, fundamentals, crowd và outcome.

4. **UI và chart**

        - Chart được làm lại theo hướng giống TradingView hơn:
        
        - candlestick rõ hơn,
        
        - nền trắng,
        
        - trục giá bên phải,
        
        - có pan/zoom,
        
        - bỏ moving averages,
        
        - bỏ dòng OHLC và “Random Walk Simulation”.
        
        - Mỗi round có 7 candlestick đại diện cho 7 ngày.
        
        - Đổi tên chart từ VN-STOCK - HOSE thành STEELSTOX - FOMOPOLY.
        
        - Portfolio panel được thiết kế lại thành 3 box chính:
        
        - Cash,
        
        - Stock Value / Total Cost,
        
        - Portfolio Value.
        
        - Unrealized return và Portfolio return được đưa thành dòng nhỏ dưới box liên quan.
        
        - Thêm tooltip chữ i để giải thích cách tính các chỉ số.
        
        - Sửa QnA box thành nền trắng, text rõ trên Streamlit Cloud.
        
        - Bỏ box Portfolio Return dư ở outcome.

5. **Scoring và grading**

        - Rationality Score được làm lại để không còn trường hợp full hold/cash vẫn được 80 điểm.
        
        - Thêm participation logic: người chơi cần thật sự tham gia quyết định, không thể né game.
        
        - Full hold toàn game bị cap điểm thấp hơn.
        
        - Nếu vừa lỗ vừa có bias score cao thì bị phạt thêm.
        
        - Scale Rationality Score hiện dùng tiếng Anh:
        
        - Poor: dưới 65,
        
        - Average: 65-79,
        
        - Good: từ 80 trở lên.
        
        - Thêm thanh màu đỏ/vàng/xanh cho Rationality Score.

### File, tính năng, dữ liệu, logic, giao diện, tài liệu hoặc phần demo đã đóng góp

        Đóng góp lớn (<80%):
        
        bias _rule.py
        
        Đóng góp mang tính hỗ trợ (<20%):
        
        scoring.py
        
        ui_components.py
        
        app.py
        
        charts.py
        
        config.py
        
        trading_logic.py

### Bằng chứng đóng góp

Link: https://drive.google.com/drive/folders/1oL7r5BR6nKeN11EkHl3SMxl5pDjSYRbP?usp=sharing

### Phần đóng góp đó kết nối thế nào với sản phẩm cuối cùng

Trước hết, phần logic tài chính đã rõ ràng hơn: tách unrealized return và portfolio return giúp game đo bias chính xác hơn. Đặc biệt Loss Aversion và Disposition Effect cần nhìn vào lãi/lỗ của vị thế đang nắm giữ, không phải chỉ tổng tài sản. Việc chuyển shares sang số nguyên, dùng USD, starting capital 100,000 USD, và chặn Buy khi không đủ tiền mua 1 cổ phiếu cũng làm gameplay thực tế hơn. Trước khi có thay đổi về return, người chơi chỉ nhìn thấy có unrealized return cho nên sẽ dễ bị nhầm đó là portfolio return hoặc bị hiểu là game đang tính sai. Việc có thêm 2 loại return cũng khiến cho game thực tế hơn vì có thể phản ánh được xu hướng extra risk taking của người chơi khi đang lãi, có thể chịu lỗ nhiều hơn và từ đó dễ bắt được xu hướng loss aversion hơn.

Phần UI/chart giúp sản phẩm chuyên nghiệp hơn nhiều: chart giống TradingView, candlestick theo ngày trong từng tuần, có pan/zoom, bỏ moving average/OHLC không cần thiết, panel portfolio gọn hơn, QnA rõ hơn, tooltip giải thích cách tính return. Những thứ này làm người chơi hiểu trạng thái tài khoản nhanh hơn và ít bị rối.

Phần scenario content tốt hơn vì các tin tức, fundamentals, forum sentiment giờ có mâu thuẫn và độ nhiễu giống thị trường thật hơn. Điều này giúp người chơi không chỉ bấm theo outcome, mà phải cân nhắc giữa news, fundamentals, crowd và price action. Đây là thứ làm game có giá trị học behavioral finance.

### Điều cá nhân học được

Bias detection cần ngữ cảnh, không thể chỉ dùng một điều kiện đơn giản

Ví dụ Disposition Effect không phải cứ bán khi đang lời là bias. Nếu news xấu và fundamental yếu thì bán có thể là quyết định hợp lý. Tương tự Herding không phải cứ hành động giống crowd là herding. Phải xem crowd có mạnh không, fundamental có support không, người chơi có đang bị kéo theo đám đông không.

Quy trình test sản phẩm

Khi test sản phẩm thì phải trực tiếp trải nghiệm, rồi kiểm log để xem action, signal, return, bias rule, đọc dữ liệu, xác định nguyên nhân, sửa rule, rồi test lại.

### Khó khăn đã gặp và cách xử lý

Khó khăn lớn nhất gặp phải là lượng hóa các thiên kiến hành vi thành điểm số cụ thể. Các bias như herding, overconfidence hay loss aversion là khái niệm tâm lý, nên nếu chỉ chấm dựa trên hành động Buy/Sell/Hold thì rất dễ đánh giá sai.

Xử lý bằng cách xây dựng logic chấm điểm theo hướng context-aware scoring. Nghĩa là hệ thống không chỉ nhìn vào hành động của người chơi, mà còn xét thêm bối cảnh như news sentiment, fundamentals, crowd signal, trade size và trạng thái lãi/lỗ. Ví dụ, mua theo đám đông chỉ bị tính là herding khi tín hiệu đám đông mạnh nhưng yếu tố cơ bản không đủ hỗ trợ.

Cơ chế anti-double-counting cũng được thêm để tránh một hành vi bị cộng điểm bias nhiều lần. Nhờ vậy, kết quả scoring phản ánh hành vi người chơi hợp lý hơn và giảm nguy cơ diễn giải sai quyết định đầu tư.

### Lời nhắn cho sinh viên khóa sau

Khi tiếp tục phát triển dự án, nên tập trung trước vào logic sản phẩm thay vì chỉ viết code cho chạy được. Với game mô phỏng đầu tư, phần quan trọng nhất là cách lượng hóa bias và chấm điểm hành vi người chơi trong đúng bối cảnh thị trường.

Hãy kiểm tra kỹ các rule, tránh chấm điểm chỉ dựa trên Buy/Sell/Hold và tránh double-counting giữa các bias. Ngoài ra, nên tiếp tục refine UI, chart và feedback để người chơi hiểu rõ kết quả của mình hơn.

Dự án sẽ có giá trị hơn nếu được phát triển như một sản phẩm học tập hoàn chỉnh, không chỉ là một bài code.

---

## Individual Footprint

## Thành viên 3: Nguyễn Hoàng Thiều Trang - 2313380037

### Vai trò trong dự án

- Phụ trách code Trading Logic.

- Kiểm thử hệ thống (QA/Tester) và xử lý lỗi giao diện (UI/UX Bug Fixer).

- Triển khai chạy thử nghiệm game (GitHub & Streamlit Testing Server).

### Dấu ấn cá nhân trong sản phẩm

Đóng góp lớn nhất của em là đảm bảo hệ thống chạy ổn định từ backend (thuật toán tài chính) ra đến frontend trên môi trường web thực tế. Ở backend, em code logic khớp lệnh, kiểm soát sai số của luồng tiền để game không bị crash. Ở khâu triển khai, em chủ động đưa source code lên GitHub và deploy thử nghiệm trên Streamlit Cloud để giả lập môi trường chạy thực tế, từ đó phát hiện sớm các bug phát sinh khi chạy online (vốn không xuất hiện ở localhost) và trực tiếp can thiệp bằng code để fix.

### Những việc đã thực sự làm

- Trading Logic: Code hàm xử lý lệnh Buy / Sell / Hold. Thiết lập cơ chế ép mua cổ phiếu nguyên lô, tính toán số tiền giao dịch thực tế, cập nhật tự động số dư Tiền mặt (cash), Số dư cổ phiếu (shares) và Giá vốn bình quân (avg_cost).

- Deployment & Testing : Đưa dự án lên chạy thử trên server của Streamlit Cloud để giả lập môi trường người dùng cuối, test toàn bộ flow của game từ đầu đến cuối.

- Fix Bug UI: Trong quá trình test trên web live, phát hiện bug hiển thị màu sắc (chữ ở thanh Slider và nút bị chìm vào nền, không thể đọc được do cơ chế auto-theme của Streamlit). Trực tiếp can thiệp bằng cách viết mã CSS đè lên file giao diện mặc định để vá lỗi hiển thị.

### File, tính năng, dữ liệu, logic, giao diện, tài liệu hoặc phần demo đã đóng góp

File code: trading_logic.py

Tính năng & Logic: Tính năng ép khớp lệnh cổ phiếu nguyên lô (cắt đuôi thập phân), dọn rác bộ nhớ giá vốn khi bán sạch danh mục.

Giao diện: Bản vá lỗi màu chữ tại các khu vực tương tác chính (nút Radio chọn hành động Buy/Sell/Hold và thanh Slider chọn khối lượng).

Tài liệu: Phần công thức toán học tính luồng tiền tại Sheet "Trading logic" trong Plan.

### Bằng chứng đóng góp

- Link source code: trading_logic.py

- Link game trên Streamlit: https://finalfomopoly.streamlit.app/

- Plan project phần Trading logic

- Link repo Github: https://github.com/CocoDuckie?tab=repositories

- Lịch sử Commit: https://github.com/CocoDuckie/final-/commit/cbe9a18d6f117309181c87437c2cddb5808cbd34

- Ảnh chụp màn hình

### Phần đóng góp đó kết nối thế nào với sản phẩm cuối cùng

- Logic thuật toán tài chính chuẩn xác là nền tảng để game tính ra được số dư Tiền, Cổ phiếu và Lãi/Lỗ đúng thực tế, từ đó render lên UI Dashboard sau mỗi vòng.

- Việc chủ động test trên server và fix lỗi hiển thị màu đóng vai trò như một chốt chặn an toàn cuối cùng. Nếu không có bước này, sản phẩm mang đi demo sẽ gặp lỗi tàng hình chữ, khiến người chơi không thể đọc được câu hỏi Quiz hay các lựa chọn Buy/Sell/Hold, ảnh hưởng tới trải nghiệm của người sử dụng.

### Điều cá nhân học được

Nắm vững cách handle các rủi ro của kiểu dữ liệu float trong Python để tránh sai số vi phân khi lập trình hệ thống tài chính.

Hiểu rõ khoảng cách giữa việc "code chạy tốt trên máy cá nhân (localhost)" và "code chạy trên server". Môi trường server luôn phát sinh những bug runtime hoặc lỗi UI bất ngờ.

### Khó khăn đã gặp và cách xử lý

Khó khăn 1: Sai số float và lỗi ZeroDivisionError. Khi trade theo %, kết quả hay ra số lẻ, dễ làm tiền mặt bị âm vi phân hỏng luồng điều kiện. Khi người chơi bán sạch (shares == 0), công thức tính giá vốn (DCA) sẽ bị lỗi chia cho 0 làm sập game.

- Cách xử lý: Dùng math.floor() để ép khớp lệnh nguyên lô ngay từ đầu. Khi bán sạch danh mục, chủ động hard-code gán biến portfolio.avg_cost = 0.0 để dọn sạch rác bộ nhớ, giúp game an toàn tiến vào vòng tiếp theo.

Khó khăn 2: Server từ chối build và Lỗi tàng hình chữ khi chạy online.

Khi đưa code lên Cloud, server báo lỗi không cài được thư viện do file requirements.txt dính ký tự tiếng Việt và đường dẫn sai. Khi chạy được game, UI lại tự động đổi độ tương phản theo theme của máy người test làm chữ bị chìm mất.

- Cách xử lý: Dọn sạch rác trong requirements.txt và sửa toàn bộ code thành đường dẫn tương đối (relative path). Với bug UI, dùng lệnh st.markdown("<style>...") bọc thẻ div lại và gắn !important để ép màu chữ xám đen vĩnh viễn, giải quyết triệt để vấn đề trên mọi thiết bị.

Lời nhắn cho sinh viên khóa sau

Trong làm sản phẩm phần mềm, code chạy được trên máy mình mới chỉ là thành công 50%. Hãy tập thói quen push code lên GitHub và tạo một server deploy thử nghiệm (Staging) càng sớm càng tốt. Môi trường server thực tế có thể xuất hiện những lỗi runtime về đường dẫn hoặc xung đột UI. Việc test trực tiếp trên link live từ sớm sẽ hạn chế những lỗi sai không đáng có.

---

## Thành viên: Đào Minh Quang - 2312380030

### Vai trò trong dự án

Trong quá trình phát triển sản phẩm game FOMOpoly, tôi đảm nhận công việc thiết kế kịch bản của toàn bộ 8 vòng chơi. Nhờ óc sáng tạo cùng sự am hiểu sâu sắc các thiên kiến của nhà đầu tư, tôi đã được cả nhóm tin tưởng giao cho trọng trách này. Bản thân là một nhà đầu tư theo trường phái giao dịch cổ phiếu ngắn hạn, tôi hiểu rất rõ những quyết định mua bán bị điều khiển bởi cảm xúc, dẫn đến kết quả thua lỗ cho các nhà đầu tư. Vì vậy, dựa trên kinh nghiệm thực chiến trên thị trường chứng khoán, tôi đã dành thời gian thiết kế ra những bối cảnh, tình huống, tin tức mà người chơi sẽ phải đối diện trong quá trình tham gia đầu tư ảo trên FOMOpoly.

### Dấu ấn cá nhân trong sản phẩm

Tôi là người đứng sau toàn bộ cốt truyện của trò chơi, những gì mà người chơi trực tiếp tiếp xúc và tương tác khi chơi. Những câu chữ xuất hiện trên giao diện trong cả 8 vòng chơi đều được tôi viết ra, chọn lọc và trau chuốt kĩ lưỡng. Thật vậy, từng tình huống đều phải được nghiên cứu rất tỉ mẩn để đảm bảo việc dẫn dắt cảm xúc của người chơi trở nên hiệu quả. Cụ thể, để thiết kế nên 8 kịch bản ứng với 8 vòng đấu, tôi đã:

- Phải hiểu rõ về các thiên kiến mà trò chơi được xây dựng xoay quanh. Tôi phải dành thời gian đọc và nghiên cứu khái niệm, xem qua các ví dụ và hậu quả của từng thiên kiến đó đối với nhà đầu tư. Việc này không chỉ dừng lại ở việc hiểu định nghĩa, mà còn phải hiểu thiên kiến đó thường xuất hiện trong hoàn cảnh nào trên thị trường. Ví dụ, với những thiên kiến liên quan đến tâm lý bầy đàn, quá tự tin hay sợ thua lỗ, tôi phải tự đặt câu hỏi rằng nhà đầu tư thường nhìn thấy thông tin gì, bị tác động bởi cảm xúc gì và vì sao họ lại đưa ra quyết định thiếu lý trí. Từ đó, tôi mới có thể biến các khái niệm lý thuyết thành những tình huống chơi cụ thể và tự nhiên hơn.

- Vẽ ra trong đầu những ý tưởng về bối cảnh thị trường, những thông tin vĩ mô, vi mô, những tín hiệu từ đám đông nhà đầu tư ảo. Những ý tưởng đó đều phải được gắn với một thiên kiến nhất định. Sau khi phác thảo, tôi đã phải suy xét rất kĩ xem những kịch bản đó đã đủ sức khiến nhà đầu tư để lộ ra thiên kiến hay chưa. Để thỏa mãn được điều này, cốt truyện phải có khả năng đánh vào cảm xúc người chơi, đồng nghĩa với việc nó phải thật sự lôi cuốn, có những tình tiết giật gân và mang những màu sắc khác nhau.

- Biến những suy nghĩ, ý tưởng đó thành những câu từ được chọn lọc kĩ lưỡng. Tôi phải áp dụng những kinh nghiệm trong quá trình đầu tư, giao dịch cổ phiếu ngắn hạn để hiểu rõ khía cạnh tâm lý của người chơi trước những tình huống trên thị trường. Từ đó, tôi đảm bảo những thông tin do mình viết ra phải đủ sức nặng để có thể đánh vào tâm lý họ. Phần tin tức phải nổi bật, sát với thực tế và đa dạng. Phần biến động giá phải khó lường nhưng vẫn rất logic. Tôi không muốn các tin tức trong game chỉ giống như những dòng mô tả khô khan, mà muốn chúng tạo ra cảm giác giống những thông tin mà nhà đầu tư thật sự có thể bắt gặp khi theo dõi thị trường. Đồng thời, tôi muốn người chơi cảm nhận được sự hưng phấn, sợ hãi hoặc hoang mang của đám đông. Vì vậy, tôi phải điều chỉnh độ dài, cách dùng từ và mức độ nhấn mạnh của từng câu. Tôi cũng cố gắng tạo cho mỗi vòng chơi một sắc thái riêng, tránh việc các vòng bị lặp lại về cảm giác.

Nhìn chung, phần kịch bản là đóng góp thể hiện rõ nhất vai trò cá nhân của tôi trong FOMOpoly. Công việc của tôi không chỉ là viết nội dung, mà còn là biến những khái niệm về hành vi tài chính thành những tình huống cụ thể để người chơi có thể trải nghiệm. Tôi phải kết nối giữa lý thuyết về thiên kiến, bối cảnh thị trường và cảm xúc của nhà đầu tư để tạo ra các vòng chơi có ý nghĩa. Đây cũng là phần khiến tôi cảm thấy mình đóng góp nhiều nhất cho sản phẩm, bởi những gì tôi viết ra là thứ người chơi trực tiếp đọc, cảm nhận và dựa vào đó để đưa ra quyết định trong suốt quá trình chơi.

### File, tính năng, dữ liệu, logic, giao diện, tài liệu hoặc phần demo đã đóng góp

Trong quá trình phát triển FOMOpoly, tôi đã đóng góp chủ yếu vào phần nội dung, kịch bản và logic trải nghiệm của người chơi. Cụ thể, phần việc của tôi không chỉ dừng lại ở việc viết chữ cho trò chơi, mà còn bao gồm quá trình nghiên cứu, xây dựng bối cảnh, thiết kế tình huống và đảm bảo các thông tin trong từng vòng chơi có thể tác động đến tâm lý người chơi theo đúng mục tiêu ban đầu.

Các phần cụ thể tôi đã thực hiện bao gồm:

- Kịch bản cho 8 vòng chơi của FOMOpoly: Tôi là người xây dựng toàn bộ nội dung cốt truyện mà người chơi trực tiếp đọc và tương tác trong quá trình chơi. Mỗi vòng chơi đều được thiết kế xoay quanh một thiên kiến nhất định, với các tình huống thị trường khác nhau nhằm khiến người chơi phải đưa ra quyết định mua, bán hoặc nắm giữ cổ phiếu.

- Phần news: Tôi viết các phần tin tức xuất hiện trong từng vòng chơi. Các tin tức này bao gồm cả yếu tố vĩ mô như chiến tranh, biến động giá nguyên liệu đầu vào, chính sách đầu tư công, lẫn yếu tố vi mô như doanh nghiệp kí hợp tác phát triển bền vững hay doanh nghiệp thuộc diện thanh tra. Mục tiêu là tạo ra những thông tin đủ chân thực, đủ hấp dẫn và có khả năng tác động đến cảm xúc của người chơi.

- Phần fundamentals: Tôi tham gia xây dựng các đoạn thông tin liên quan đến nền tảng doanh nghiệp, giúp người chơi có thêm dữ liệu để cân nhắc trước khi ra quyết định. Dù trò chơi không tập trung quá sâu vào phân tích tài chính, phần fundamentals vẫn cần được viết sao cho hợp lý, có liên kết với tin tức chính và phù hợp với bối cảnh thị trường của từng vòng.

- Phần crowd signal: Tôi xây dựng các tín hiệu thể hiện phản ứng của đám đông nhà đầu tư ảo. Đây là phần quan trọng để mô phỏng áp lực tâm lý trên thị trường chứng khoán, chẳng hạn như sự hưng phấn, sợ hãi, hoang mang hoặc tâm lý chạy theo đám đông. Phần này được thiết kế nhằm khiến người chơi cảm nhận được sức ép từ thị trường, nhưng vẫn phải đủ tinh tế để không làm lộ rõ ý đồ của người phát triển trò chơi.

- Hệ thống câu hỏi MCQ sau mỗi vòng chơi: Tôi xây dựng nội dung các câu hỏi trắc nghiệm xuất hiện sau mỗi vòng chơi nhằm giúp người chơi ghi nhớ những thông tin quan trọng vừa được cung cấp. Các câu hỏi được thiết kế dựa trên nội dung news, fundamentals, crowd signal và thiên kiến của vòng chơi, giúp người chơi ôn lại các dữ kiện chính và nhận diện những tín hiệu quan trọng đã xuất hiện.

### Bằng chứng đóng góp

Toàn bộ dữ kiện về kịch bản của FOMOpoly được trình bày theo từng vòng chơi trong link này: https://docs.google.com/document/d/18wUtN8joJE32GfxBYlLIQnhVaf6PoUBjWOs0mroCMK0/edit?tab=t.0#heading=h.qtpohqca0fks

### Phần đóng góp đó kết nối thế nào với sản phẩm cuối cùng

Nếu những dòng code là xương sống, trading logic và hệ thống chấm điểm là bộ não, giao diện UI là ngoại hình thì sản phẩm đầu ra của tôi sẽ là cả năm giác quan của dự án. Năm giác quan này sẽ truyền đến cho người chơi những thông tin người chơi cần phải nắm được, bằng những cử chỉ, ngôn ngữ, giọng điệu khác nhau theo từng vòng chơi, để từ đó người chơi sẽ đưa ra những quyết định cho mình. Đồng thời, năm giác quan này cũng sẽ trực tiếp dẫn dắt và nhận các dữ liệu đầu vào của người chơi. Để rồi từ đó, những dữ liệu này sẽ được xử lý, và sản phẩm đầu ra cuối cùng sẽ đến tay người chơi.

### Điều cá nhân học được

Trong quá trình thiết kế kịch bản trò chơi FOMOpoly, tôi đã tiếp thu thêm nhiều kiến thức và kinh nghiệm quý giá. Về phần mình, đây là lần đầu tiên tôi được tham gia phát triển một sản phẩm công nghệ. Việc được tiếp xúc và tự tay viết những dòng code đầu tiên bằng Python đã giúp tôi tự tin hơn và không còn ngại những công việc máy tính phức tạp nữa. Trước đây, tôi thường nghĩ rằng việc lập trình là điều khá xa lạ và khó tiếp cận. Tuy nhiên, khi thật sự bắt tay vào làm, tôi nhận ra rằng nếu kiên trì tìm hiểu từng phần nhỏ và không ngại sửa lỗi, tôi vẫn có thể hiểu được cách một sản phẩm vận hành. Đây là một trải nghiệm rất mới, giúp tôi có thêm sự chủ động khi làm việc với công nghệ.

Những giá trị mang lại cho tôi từ việc phát triển trò chơi này nghiễm nhiên không chỉ gói gọn trong lĩnh vực công nghệ. Để có thể thiết kế nên kịch bản của FOMOpoly, như đã đề cập, tôi đã dành rất nhiều thời gian đọc và nghiên cứu sâu các thiên kiến mà nhà đầu tư mắc phải trong quá trình chinh chiến trên thị trường chứng khoán. Từ đó, tôi hiểu được tường tận hơn khía cạnh tâm lý của người chơi, vốn là một lĩnh vực tôi không hề hay biết mình sẽ khám phá ra trước khi bắt tay vào làm công việc này. Việc nghiên cứu những thiên kiến này cũng giúp tôi nhìn lại chính cách mình từng phản ứng trước thị trường, qua đó hiểu rằng kiểm soát cảm xúc là một phần rất quan trọng của quá trình ra quyết định.

Hơn nữa, việc tự mình phác thảo ý tưởng và biến nó thành cốt truyện của FOMOpoly cũng giúp tôi rèn luyện sự sáng tạo. Trong lĩnh vực tài chính khô khan, cơ hội để não bộ được trui rèn khả năng suy nghĩ vượt ra ngoài những khuôn khổ thông thường không hề nhiều. Bởi vậy, quá trình phát triển các tình huống trong trò chơi thực sự vô cùng quý giá. Tôi không chỉ phải nghĩ ra một tin tức nghe có vẻ hợp lý, mà còn phải làm sao để tin tức đó có cảm xúc, có bối cảnh và có khả năng khiến người chơi phải phân vân trước khi ra quyết định. Điều này buộc tôi phải kết hợp giữa kiến thức tài chính, khả năng quan sát thị trường và năng lực viết nội dung. Qua đó, tôi học được rằng sáng tạo không nhất thiết phải tách rời khỏi tính logic.

### Khó khăn đã gặp và cách xử lý

Công việc thiết kế cốt truyện của FOMOpoly nghiễm nhiên không hề dễ dàng. Các kịch bản không chỉ đòi hỏi sự đa dạng, để nhắm đến nhiều thiên kiến, mà còn cần phải sâu, có sức thao túng, để người chơi bộc lộ ra những thiên kiến này. Điều này yêu cầu tôi phải tập trung cao độ và sáng tạo ở mức tối đa. Ở một số thiên kiến, rất khó để vẽ ra một kịch bản mà có thể thật sự tác động đến tâm lý người chơi. Lấy ví dụ như câu chuyện về tâm lý bầy đàn, tôi đã phải suy nghĩ rất nhiều về cách dùng từ để làm sao cho người chơi nhìn ra được là đám đông đang phản ứng ra sao. Bởi lẽ, chỉ qua việc miêu tả suông, người chơi rất khó hình dung được cụ thể tình huống trông như thế nào. Đối với tôi, chìa khóa ở đây là sự sáng tạo và kiên trì. Tôi phải sẵn sàng đập đi xây lại một kịch bản nếu nó không đủ sâu, không đủ mạnh mẽ. Việc này có thể rất tốn thời gian, song nó đảm bảo kết quả công việc sẽ được như ý muốn.

Bên cạnh đó, tôi cũng phải đối mặt với một vấn đề, đó là không có công cụ nào có thể hỗ trợ tôi làm công việc này một cách triệt để. Trong quá trình thực hiện, AI có thể giúp tôi gợi ý một số ý tưởng ban đầu, chỉnh câu chữ hoặc mở rộng một vài hướng triển khai. Tuy nhiên, AI không thể đủ sáng tạo để thay thế hoàn toàn vai trò của người viết kịch bản. Đặc biệt, AI cũng không thể thật sự hiểu được tâm lý con người nói chung và tâm lý nhà đầu tư nói riêng một cách sâu sắc như người trực tiếp quan sát, trải nghiệm và suy nghĩ về thị trường. Vì vậy, cách xử lý của tôi là không phụ thuộc hoàn toàn vào công cụ hỗ trợ, mà chỉ xem chúng như một phương tiện tham khảo. Phần cốt lõi của kịch bản vẫn phải đến từ khả năng suy nghĩ, quan sát, sáng tạo và kinh nghiệm cá nhân của tôi trong quá trình tiếp xúc với thị trường chứng khoán.

Đồng thời, tôi phải đảm nhận nhiều phần việc khác nhau, đòi hỏi những kĩ năng khác nhau cùng một lúc. Trong quá trình xây dựng FOMOpoly, tôi không chỉ đơn thuần viết nội dung cho trò chơi, mà còn phải mày mò viết code, hiểu cách trò chơi vận hành, đọc hiểu tâm lý nhà đầu tư, nghiền ngẫm tin tức thị trường và sáng tạo nên những tình huống đủ hấp dẫn. Mỗi đầu việc lại yêu cầu một kiểu tư duy khác nhau. Khi viết code, tôi cần sự logic, chính xác và kiên nhẫn để sửa lỗi. Khi viết kịch bản, tôi lại cần sự sáng tạo, khả năng dùng từ và khả năng đặt mình vào vị trí của người chơi. Khi nghiên cứu tin tức thị trường, tôi phải hiểu được sự kiện nào có thể tác động đến cổ phiếu và sự kiện nào chỉ tạo ra nhiễu thông tin. Việc phải liên tục chuyển đổi giữa nhiều vai trò như vậy khiến tôi đôi lúc cảm thấy quá tải. Để xử lý khó khăn này, tôi đã cố gắng chia nhỏ công việc, làm từng phần một và ưu tiên hoàn thiện những phần quan trọng nhất trước. Chính quá trình này giúp tôi hiểu ra rằng việc tạo ra một trò chơi không chỉ cần ý tưởng, mà còn cần rất nhiều sự bền bỉ, kiên trì và tính tổ chức tốt.

### Lời nhắn cho sinh viên khóa sau

Nếu sinh viên khóa sau muốn tiếp tục hoặc học từ phần việc này, tôi muốn nhấn mạnh rằng việc thiết kế kịch bản trò chơi không chỉ là viết ra vài tình huống cho người chơi đọc. Trước hết, các bạn cần hiểu thật rõ mục tiêu của trò chơi và những thiên kiến mà mình muốn người chơi bộc lộ. Sau đó, hãy đầu tư thời gian nghiên cứu các thiên kiến này. Đồng thời, mình cần phải hiểu thị trường, quan sát tâm lý nhà đầu tư để rồi viết kịch bản sao cho có cảm xúc. Trong quá trình làm, đừng ngại sửa nhiều lần, vì một kịch bản tốt phải vừa logic, vừa hấp dẫn, vừa đủ sức thao túng tâm lý người chơi. Chúc các bạn thành công với dự án mình lựa chọn!

---

## Thành viên 5: Nguyễn Hạnh Trang - 2312380038

### Vai trò trong dự án

Trong dự án này, em phụ trách chính phần thiết kế giao diện người dùng và trực quan hóa trải nghiệm cho Behavioral Investing Simulation Game. Vai trò của em tập trung vào việc xây dựng lớp giao diện của ứng dụng Streamlit, thiết kế bố cục các màn hình chính, tổ chức luồng tương tác của người chơi và trình bày các thông tin tài chính – hành vi theo cách dễ hiểu, trực quan và phù hợp với mục tiêu giáo dục.

Cụ thể, em tham gia thiết kế giao diện mở đầu, màn hình từng vòng chơi, các bảng thông tin thị trường, khu vực hiển thị danh mục đầu tư, giao diện ra quyết định, phần hiển thị kết quả sau mỗi vòng, thẻ phân tích thiên kiến hành vi và các phần biểu đồ phục vụ theo dõi diễn biến giá, hiệu quả danh mục và kết quả cuối cùng.

### Dấu ấn cá nhân trong sản phẩm

Dấu ấn rõ nhất của em trong sản phẩm là lớp giao diện trực quan và tương tác của trò chơi. Em đã góp phần chuyển đổi mô phỏng từ một ứng dụng xử lý dữ liệu đơn giản thành một trải nghiệm giao dịch mang tính giáo dục, có cấu trúc rõ ràng và dễ theo dõi hơn.

Phần đóng góp của em thể hiện qua giao diện Streamlit được tùy chỉnh, màn hình mở đầu, thanh tiến trình vòng chơi, các thẻ thông tin thị trường, bảng danh mục đầu tư, khu vực ra quyết định, phần câu hỏi kiểm tra, khu vực công bố kết quả, thẻ kết quả thiên kiến và các biểu đồ trực quan.

Nhờ phần giao diện và trực quan hóa này, sản phẩm trở nên hoàn thiện hơn và có cảm giác giống một trò chơi giáo dục hơn. Người dùng có thể theo dõi toàn bộ luồng mô phỏng một cách trực quan: đọc thông tin thị trường, đưa ra quyết định giao dịch, quan sát biến động giá, xem lại thay đổi trong danh mục đầu tư và diễn giải phản hồi về thiên kiến hành vi.

### Những việc đã thực sự làm

- Thiết kế hệ thống giao diện tổng thể cho ứng dụng Streamlit, bao gồm bố cục, màu sắc, typography, card layout, panel thông tin, button style và responsive layout.

- Xây dựng các thành phần UI tái sử dụng trong ui_components.py, như opening screen, hero banner, round progress banner, market information cards, portfolio dashboard, decision panel, quiz checkpoint, outcome section và bias result cards.

- Tổ chức lại luồng trải nghiệm người chơi theo trình tự rõ ràng: đọc thông tin thị trường, xem trạng thái danh mục, đưa ra quyết định, theo dõi biến động giá, nhận kết quả và xem phản hồi thiên kiến.

- Thiết kế cách trình bày thông tin thị trường thành các khu vực riêng biệt như market context, news, fundamentals và crowd sentiment để người chơi dễ đọc và dễ so sánh.

- Trình bày portfolio dashboard dưới dạng các metric cards để các chỉ số như cash, stock value, total cost, portfolio value và return dễ theo dõi hơn.

- Đóng góp vào phần trình bày trực quan trong charts.py, gồm chart container, candlestick chart, portfolio value chart, bias score chart và leaderboard chart ở góc độ hiển thị và trải nghiệm người dùng.

### File, tính năng, dữ liệu, logic, giao diện, tài liệu hoặc phần demo đã đóng góp

- ui_components.py: chứa hệ thống giao diện Streamlit, custom CSS, các thành phần giao diện tái sử dụng, opening screen, round banner, market information cards, portfolio dashboard, decision panel, quiz panel, outcome section, bias result card và responsive layout.

- charts.py: chứa các thành phần trực quan hóa như candlestick chart, portfolio value chart, bias score chart và leaderboard chart.

### Bằng chứng đóng góp

2312380038 - Nguyễn Hạnh Trang - Contribution Evidence

### Phần đóng góp đó kết nối thế nào với sản phẩm cuối cùng

Đóng góp của em kết nối trực tiếp với sản phẩm cuối cùng vì giao diện là lớp mà người dùng tương tác trong toàn bộ quá trình chơi. Các phần logic phía sau có thể xử lý giao dịch, tính toán danh mục và phát hiện thiên kiến, nhưng nếu không có giao diện rõ ràng thì người chơi sẽ khó hiểu thông tin thị trường, khó đưa ra quyết định và khó diễn giải kết quả cuối cùng.

Phần UI giúp sản phẩm hoạt động như một trải nghiệm học tập hoàn chỉnh. Người chơi không chỉ nhập lệnh giao dịch, mà đi qua một luồng có cấu trúc: đọc bối cảnh, xem tín hiệu thị trường, đánh giá danh mục, đưa ra quyết định, quan sát kết quả và nhận phản hồi về thiên kiến hành vi.

Bên cạnh đó, các dashboard và biểu đồ giúp chuyển những dữ liệu tài chính phức tạp thành thông tin trực quan. Điều này đặc biệt quan trọng trong một game giáo dục về behavioral finance, vì người chơi cần nhìn thấy mối liên hệ giữa hành vi đầu tư, biến động thị trường, hiệu quả danh mục và kết quả bias.

Phần giao diện cũng góp phần nâng cao chất lượng demo của sản phẩm. Khi trình bày trước người xem, sản phẩm có bố cục rõ ràng, hình ảnh thống nhất và luồng trải nghiệm dễ theo dõi hơn, từ đó thể hiện tốt hơn giá trị của dự án.

### Điều cá nhân học được

Thông qua phần việc này, em học được rằng UI trong một sản phẩm giáo dục không chỉ có vai trò làm đẹp giao diện, mà còn là một phần của cách người dùng học và ra quyết định. Nếu thông tin được trình bày lộn xộn, người chơi có thể hiểu sai bối cảnh hoặc đưa ra quyết định mà không nắm được lý do. Ngược lại, một giao diện rõ ràng có thể giúp người chơi đọc dữ liệu tốt hơn và phản ánh hành vi của mình hiệu quả hơn.

Em cũng học được cách sử dụng Streamlit kết hợp với HTML/CSS tùy chỉnh để vượt qua giới hạn của các component mặc định. Việc xây dựng các UI block tái sử dụng giúp em hiểu hơn về tính nhất quán trong thiết kế sản phẩm và tầm quan trọng của việc duy trì một visual system xuyên suốt.

Ngoài ra, em hiểu rõ hơn vai trò của data visualization trong tài chính hành vi. Một biểu đồ hoặc dashboard không chỉ hiển thị số liệu, mà còn giúp người dùng nhận ra xu hướng, so sánh kết quả và hiểu tác động của quyết định đầu tư đối với danh mục của mình.

### Khó khăn đã gặp và cách xử lý

Khó khăn đầu tiên là Streamlit có nhiều giới hạn về bố cục và giao diện mặc định, khiến sản phẩm dễ trông đơn giản nếu chỉ dùng component có sẵn. Để xử lý, em sử dụng custom CSS, HTML blocks, card layout, grid layout, shadow, spacing và các class giao diện riêng để tạo cảm giác hoàn thiện hơn cho sản phẩm.

Khó khăn thứ hai là mỗi vòng chơi có nhiều loại thông tin khác nhau, bao gồm bối cảnh thị trường, tin tức, fundamentals, crowd sentiment, giá cổ phiếu, trạng thái danh mục, quyết định giao dịch, câu hỏi kiểm tra và kết quả sau vòng. Nếu đưa tất cả thông tin lên màn hình cùng lúc mà không phân cấp, người chơi sẽ dễ bị rối. Em giải quyết bằng cách chia giao diện thành các khu vực riêng, dùng tiêu đề rõ ràng, màu sắc nhất quán và thứ tự hiển thị hợp lý.

Khó khăn thứ ba là làm sao để giao diện vừa có tính game-like, vừa không làm mất đi tính nghiêm túc của một sản phẩm giáo dục tài chính. Em xử lý bằng cách dùng phong cách trading-themed nhưng vẫn giữ bố cục rõ ràng, chữ dễ đọc và các dashboard có mục đích cụ thể.

Khó khăn cuối cùng là đảm bảo các biểu đồ và dashboard không chỉ đẹp mà còn hỗ trợ người chơi hiểu kết quả. Vì vậy, em chú trọng vào cách đặt chart trong luồng chơi, cách hiển thị metric, cách chia outcome section và cách trình bày bias result để người chơi có thể liên hệ giữa quyết định, kết quả tài chính và hành vi của mình.

### Lời nhắn cho sinh viên khóa sau

Với các nhóm tiếp tục phát triển dự án, em nghĩ nên xem UI là một phần quan trọng của logic học tập, không chỉ là phần trang trí. Trong một game mô phỏng đầu tư, người chơi cần hiểu rõ họ đang thấy thông tin gì, thông tin đó ảnh hưởng thế nào đến quyết định và kết quả phản ánh điều gì về hành vi của họ.

Các bạn nên duy trì sự nhất quán giữa logic game và giao diện. Mỗi card, chart, dashboard hoặc feedback section nên có một mục đích rõ ràng: giúp người chơi đọc thông tin, đưa ra quyết định, hiểu kết quả hoặc phản tư về thiên kiến hành vi.

Trong tương lai, sản phẩm có thể được cải thiện thêm bằng cách tối ưu mobile layout, thêm biểu tượng hoặc minh họa cho scenario, cải thiện accessibility, tăng tính trực quan của phần feedback và kiểm thử giao diện với người dùng thật. Khi UI được thiết kế tốt, sản phẩm không chỉ dễ dùng hơn mà còn truyền tải bài học về behavioral finance hiệu quả hơn.
