#  **Group Footprint**

## **Tên sản phẩm**

FOMOPOLY

## **Mã nhóm**

G07

## **Link repo**

https://github.com/FTU-Legacy-62/G07

## **Link demo**

[bit.ly/3RR5kJQ](https://bit.ly/3RR5kJQ)

## **Vấn đề nhóm muốn giải quyết** 

Nhóm muốn giải quyết vấn đề: sinh viên học tài chính thường được học nhiều lý thuyết về đầu tư, nhưng lại có ít cơ hội thực hành ra quyết định đầu tư trong một môi trường thực tế. Vì thế, các sinh viên có thể sẽ tham gia vào thị trường chứng khoán khi chưa nhận thức rõ các yếu tố như cảm xúc cá nhân, thông tin thị trường, biến động giá và hành vi đám đông có thể tác động đến quyết định của mình ra sao. Điều này dễ dẫn đến những lựa chọn đầu tư sai lệch và hiệu suất kém.

Vì vậy, nhóm xây dựng **Fomopoly** như một game mô phỏng đầu tư để người dùng có thể luyện tập ra quyết định trong môi trường không có rủi ro tài chính thật. Người chơi giao dịch bằng tài khoản ảo, đi qua các tình huống thị trường được thiết kế trước, và nhận phản hồi về cả kết quả danh mục lẫn các thiên kiến hành vi có thể xuất hiện trong quá trình chơi.

Điểm nhóm muốn nhấn mạnh là sản phẩm không chỉ trả lời câu hỏi “người chơi lời hay lỗ”, mà còn giúp người chơi hiểu “vì sao mình ra quyết định như vậy”. Đây là phần quan trọng vì trong đầu tư, chất lượng quyết định không chỉ nằm ở kết quả cuối cùng, mà còn nằm ở cách người chơi xử lý thông tin, kiểm soát cảm xúc và phản ứng với rủi ro.

## **Người dùng mục tiêu** 

Người dùng chính của sản phẩm là sinh viên năm 1,2 thuộc các ngành tài chính, ngân hàng, kinh tế. Đây là nhóm người đã có hoặc đang xây dựng nền tảng kiến thức về tài chính, nhưng vẫn cần một công cụ trực quan hơn để hiểu cách các quyết định đầu tư bị ảnh hưởng bởi tâm lý và thông tin thị trường.

Nhóm người dùng này cần một sản phẩm đơn giản, dễ sử dụng, nhưng vẫn phản ánh được logic cơ bản của một tình huống đầu tư. Sau khi chơi, họ cần một phần kết quả giúp giải thích quyết định của mình có thể liên quan đến những bias nào, thay vì chỉ biết mình lời hay lỗ.

Người dùng sẽ dùng sản phẩm trong bối cảnh học tập, demo nhóm, thảo luận trên lớp.

Ví dụ: trong một buổi học về finance-based application, giảng viên hoặc nhóm sinh viên có thể dùng game này để minh họa rằng cùng một thông tin thị trường nhưng mỗi người chơi có thể phản ứng khác nhau. Một người có thể bán quá sớm khi có lãi nhỏ, một người có thể giữ quá lâu khi đang lỗ, một người khác có thể mua theo đám đông.

## **Sản phẩm hiện làm được gì** 

Sản phẩm hiện tại đã làm được các chức năng chính sau:

- **Mô phỏng một game đầu tư cơ bản**

<!-- -->

    + Game cho người chơi đầu tư vào một cổ phiếu giả lập tên là **STEELSTOX**.
    + Người chơi bắt đầu với tài khoản ảo **100,000 USD**.
    + Mục tiêu không chỉ là tạo lợi nhuận, mà còn giúp người chơi hiểu cách mình ra quyết định trong từng tình huống thị trường.

<!-- -->

- **Cung cấp các scenario thị trường cho từng round**

<!-- -->

    + Mỗi round có một scenario mô tả bối cảnh thị trường, giá cổ phiếu, tín hiệu liên quan và thông tin đám đông.

    + Các scenario được thiết kế để tạo ra tình huống đầu tư có thể ảnh hưởng đến tâm lý và hành vi của người chơi.

<!-- -->

- **Randomize thứ tự các rounds trong mỗi lượt chơi**

<!-- -->

    + Các scenario rounds không xuất hiện theo một thứ tự cố định.

    + Ở mỗi lượt chơi, hệ thống sẽ trộn thứ tự các rounds để tạo trải nghiệm khác nhau.

<!-- -->

- **Cho phép người chơi ra quyết định đầu tư**

<!-- -->

    + Ở mỗi round, người chơi chọn một trong ba hành động: **Buy, Sell hoặc Hold.**

    + Nếu chọn Buy hoặc Sell, người chơi nhập **trade size** để xác định mức độ giao dịch.

<!-- -->

- **Có câu hỏi ngắn sau mỗi round**

<!-- -->

    + Sau mỗi round, game hiển thị 3 câu hỏi liên quan đến scenario

    + Phần này giúp xác nhận người chơi đã thực sự đọc qua scenario.

<!-- -->

- **Xử lý giao dịch và cập nhật danh mục**

<!-- -->

    + Hệ thống xử lý giao dịch dựa trên số tiền mặt hiện có, số cổ phiếu đang nắm giữ và giá cổ phiếu hiện tại.

    + Giao dịch được thực hiện theo **số cổ phiếu nguyên và làm tròn xuống**, thay vì cho phép mua bán cổ phiếu thập phân.

    + Sau mỗi quyết định, hệ thống cập nhật các chỉ số chính như: *cash, shares, portfolio value, round return, total return.*

<!-- -->

- **Ghi nhận và phát hiện behavioral biases**

<!-- -->

    + Ngoài kết quả tài chính, game còn phân tích quyết định của người chơi để phát hiện các bias hành vi.

    + Hệ thống sử dụng decision, trade size, trạng thái danh mục, bối cảnh scenario và decision history để ghi nhận bias.

    + Các bias được xét gồm: ***loss aversion, Disposition effect, herding, overconfidence, Framing bias, Availability bias***

<!-- -->

- **Tạo final dashboard cuối game**

<!-- -->

    + Khi hoàn thành các rounds, người chơi nhận được bảng kết quả cuối cùng.

    + Final dashboard hiển thị:

        kết quả danh mục;

        tổng lợi nhuận;

        bias summary;

        score;

        feedback ngắn.

    + Phần này giúp người chơi không chỉ biết mình lời hay lỗ, mà còn hiểu rõ hơn về hành vi đầu tư của mình trong quá trình chơi.

## **Input** 

Sản phẩm tiếp nhận các input chính từ người chơi trong quá trình chơi game:

- **Tên hoặc biệt danh người chơi**

<!-- -->

    + Người chơi nhập tên khi bắt đầu game.

    + Thông tin này được dùng để ghi nhận kết quả và hiển thị trên leaderboard nếu cần.

<!-- -->

- **Quyết định đầu tư trong từng round**

<!-- -->

    + Sau khi đọc scenario và xem thông tin thị trường, người chơi chọn một trong ba hành động:

        Buy;

        Sell;

        Hold.
    + Đây là input chính thể hiện cách người chơi phản ứng với tình huống thị trường.

<!-- -->

- **Trade size khi Buy hoặc Sell**

<!-- -->

    + Nếu chọn Buy hoặc Sell, người chơi chọn thêm khối lượng giao dịch: 25%, 50%, 75%, 100%

    + Với Buy, tỷ lệ này áp dụng trên cash hiện có.

    + Với Sell, tỷ lệ này áp dụng trên số cổ phiếu đang nắm giữ.

<!-- -->

- **Câu trả lời checkpoint**

<!-- -->

    + Sau khi chọn quyết định, người chơi trả lời một câu hỏi ngắn liên quan đến scenario hoặc kiến thức tài chính.

    + Câu trả lời này giúp xác nhận decision trước khi hệ thống xử lý kết quả round.

<!-- -->

- **Chuỗi input trong 8 rounds**

<!-- -->
    + Hệ thống ghi lại toàn bộ tên người chơi, quyết định Buy/Sell/Hold, trade size và câu trả lời checkpoint.

    + Các dữ liệu này được dùng để xử lý giao dịch, cập nhật danh mục, phát hiện bias và tạo kết quả cuối game.

## **Logic hoặc quy tắc xử lý** 

Sản phẩm xử lý input của người chơi theo một quy trình lặp qua từng round: **nhận quyết định giao dịch → kiểm tra giao dịch → cập nhật danh mục → kiểm tra bias → lưu kết quả**.

**1. Nhận input từ người chơi**

<!-- -->

    Ở mỗi round, hệ thống hiển thị scenario, giá hiện tại của cổ phiếu STEELSTOX, tín hiệu thị trường, thông tin đám đông và trạng thái danh mục hiện tại. Sau đó, người chơi chọn:

       + Hành động: **Buy, Sell hoặc Hold**;

       + Trade size: **25%, 50%, 75% hoặc 100%** nếu có giao dịch

    Trước khi quyết định được xác nhận, người chơi phải trả lời một câu hỏi ngắn liên quan đến scenario hoặc kiến thức tài chính. Sau khi trả lời, hệ thống mới confirm decision và xử lý round.

<!-- -->

**2. Kiểm tra và xử lý giao dịch**
<!-- -->

    Nếu người chơi chọn Buy, hệ thống dùng một phần cash để mua cổ phiếu:
          target_cash = cash_before × size_pct  
          shares_bought = floor(target_cash / price_now)  
          cash_after = cash_before - (shares_bought × price_now)

    Nếu người chơi mua thêm cổ phiếu, hệ thống cập nhật giá vốn bình quân  
        new_avg_cost = ((shares_before × avg_cost_before) + (shares_bought × price_now)) / (shares_before + shares_bought)

    Nếu người chơi chọn Sell, hệ thống bán một phần số cổ phiếu đang nắm giữ
        shares_sold = floor(shares_before × size_pct)

    Nếu người chơi bán toàn bộ vị thế, hệ thống đặt shares_sold = shares_before và đưa avg_cost = 0.0 để tránh lỗi tính toán ở các round sau.

    Nếu người chơi chọn Hold, hệ thống không thay đổi cash và shares.
<!-- -->

**3. Cập nhật danh mục đầu tư**

<!-- -->

    Sau khi xử lý giao dịch, hệ thống cập nhật các biến chính như: **cash, shares, avg_cost, portfolio_value, round_return, total_return và unrealized_return**.

      Giá trị danh mục được tính bằng: 
        portfolio_value = cash_after + (shares_after × price_now)

      Tổng lợi nhuận được tính bằng: 
        total_return = (portfolio_value - initial_capital) / initial_capital
  
      Lợi nhuận của vị thế cổ phiếu đang nắm giữ được tính bằng:
        unrealized_return = (price_now - avg_cost_before) / avg_cost_before

<!-- -->

**4. Kiểm tra bias**

<!-- -->

    Sau khi cập nhật danh mục, hệ thống dùng quyết định của người chơi, trade size, trạng thái lãi/lỗ, scenario context, crowd signal và decision history để kiểm tra các bias.  
      Ví dụ, hệ thống có thể ghi nhận:

      **Herding** nếu người chơi đi theo đám đông khi tín hiệu cơ bản chưa đủ mạnh;

      **Loss aversion** nếu người chơi tiếp tục giữ hoặc mua thêm khi đang lỗ trong bối cảnh tín hiệu xấu;

      **Disposition effect** nếu người chơi bán vị thế đang lời quá sớm hoặc giữ vị thế đang lỗ quá lâu;

       **Overconfidence** nếu người chơi giao dịch quá mạnh sau kết quả tốt hoặc trong bối cảnh rủi ro.

    Để tránh tính điểm trùng, hệ thống dùng cơ chế **anti-double-counting**: các rule có ý nghĩa giống nhau được gom vào cùng một cụm và mỗi cụm chỉ được tính một lần trong một round.

<!-- -->

**5. Lưu kết quả và tính điểm cuối game**

<!-- -->

    Sau mỗi round, hệ thống lưu decision history, trading result và bias signals vào session state. Sau 8 rounds, hệ thống tổng hợp điểm bias và tính Rationality Score:  
      Rationality_Score = max(0, round(100 × (1 - total_bias_score / MAX_BIAS)))  
    Cuối game, người chơi nhận được final dashboard gồm portfolio result, total return, bias summary, rationality score và feedback ngắn.

<!-- -->

## **User flow** 

1.  Người dùng mở game và bắt đầu với tài khoản ảo **100,000 USD**.

2.  Hệ thống tải các scenario của cổ phiếu **STEELSTOX** và **trộn ngẫu nhiên thứ tự các rounds** cho lượt chơi hiện tại.

3.  Người dùng đọc scenario của round hiện tại và xem trạng thái danh mục.

4.  Người dùng chọn quyết định đầu tư: **Buy, Sell hoặc Hold**. Nếu chọn Buy hoặc Sell, người dùng nhập thêm **trade size**.

5.  Trước khi quyết định được xác nhận, người dùng phải trả lời một câu hỏi ngắn liên quan đến scenario hoặc kiến thức tài chính của round đó.

6.  Sau khi người dùng trả lời câu hỏi, hệ thống mới **confirm decision**, xử lý giao dịch và hiển thị kết quả của round vừa rồi.

7.  Hệ thống cập nhật **cash, shares, portfolio value, round return và total return**.

8.  Hệ thống lưu decision history và kiểm tra các behavioral biases dựa trên decision, trade size, portfolio state và scenario context.

9.  Người dùng tiếp tục các rounds tiếp theo theo cùng quy trình.

10. Khi hoàn thành game, người dùng xem final dashboard gồm portfolio result, total return, bias summary, score và feedback.

Người dùng có thể chơi lại; do thứ tự rounds được randomize, trải nghiệm ở lần chơi sau có thể khác lần trước.

## **Output** 

Sản phẩm tạo ra các output chính theo trình tự trải nghiệm của người chơi:

- **Màn hình bắt đầu**

<!-- -->

- Giới thiệu game, bối cảnh mô phỏng và cho phép người chơi nhập tên để bắt đầu.

<!-- -->

- **Màn hình round chơi**

<!-- -->

- Hiển thị thông tin của từng round, gồm giá cổ phiếu STEELSTOX, bối cảnh thị trường, tin tức, fundamentals, tín hiệu đám đông và biểu đồ giá.

- Hiển thị trạng thái danh mục hiện tại như cash, số cổ phiếu, portfolio value và return.

<!-- -->

- **Giao diện ra quyết định**

<!-- -->

- Cho phép người chơi chọn Buy, Sell hoặc Hold.

- Nếu chọn Buy hoặc Sell, người chơi chọn thêm khối lượng giao dịch.

- Sau đó, hệ thống hiển thị Decision Checkpoint để tóm tắt quyết định và yêu cầu người chơi trả lời câu hỏi ngắn trước khi xác nhận.

<!-- -->

- **Kết quả sau mỗi round**

<!-- -->

- Sau khi quyết định được xác nhận, hệ thống mô phỏng biến động thị trường và hiển thị kết quả round.

- Kết quả gồm giá cổ phiếu sau biến động, Week P&L, portfolio value mới và giải thích ngắn về diễn biến thị trường.

<!-- -->

- **Lịch sử quyết định**

<!-- -->

- Sản phẩm lưu lại các quyết định của người chơi qua từng round, gồm hành động, trade size, giá, số cổ phiếu, cash, portfolio value và return.

- Phần này giúp người chơi nhìn lại quá trình ra quyết định của mình.

<!-- -->

- **Final dashboard**

<!-- -->

- Sau 8 rounds, hệ thống hiển thị kết quả cuối game, gồm final portfolio value, total return, total bias score và rationality score.

- Sản phẩm cũng hiển thị biểu đồ tổng kết như portfolio chart, bias chart và leaderboard.

<!-- -->

- **Phân tích behavioral biases**

<!-- -->

- Hệ thống tổng hợp các bias xuất hiện trong quá trình chơi, ví dụ Overconfidence, Herding, Availability Bias, Framing Bias, Loss Aversion và Disposition Effect.

- Mỗi bias được phân loại theo mức độ từ None đến Very Strong, kèm giải thích ngắn, bằng chứng từ các round và gợi ý cải thiện.

## **Các lựa chọn thiết kế quan trọng** 

Nhóm có một số lựa chọn thiết kế quan trọng khi xây dựng sản phẩm:

- **Chọn một cổ phiếu giả lập**

<!-- -->

- Nhóm chọn một cổ phiếu duy nhất thay vì nhiều tài sản để giữ game đơn giản và dễ kiểm soát, giúp người chơi tập trung vào quá trình ra quyết định, thay vì bị phân tán bởi quá nhiều mã cổ phiếu hoặc nhiều loại tài sản khác nhau.

- Cách làm này cũng phù hợp với phạm vi môn học và thời gian phát triển sản phẩm.

<!-- -->

- **Sử dụng pre-designed scenario rounds thay vì dữ liệu thị trường real-time**

<!-- -->

- Các scenario được chuẩn bị trước để nhóm có thể kiểm soát nội dung, bối cảnh và mục tiêu học tập của từng round.

- Điều này giúp hệ thống dễ test hơn và giúp bias detection hoạt động rõ ràng hơn.

- Nếu dùng dữ liệu real-time, game có thể thực tế hơn nhưng sẽ khó kiểm soát, khó giải thích và khó đảm bảo mỗi tình huống đều phục vụ đúng mục tiêu phát hiện bias.

<!-- -->

- **Randomize thứ tự các rounds trong mỗi lượt chơi**

<!-- -->

- Nhóm không để các scenario xuất hiện theo thứ tự cố định.

- Ở mỗi lượt chơi, hệ thống trộn ngẫu nhiên thứ tự các rounds.

- Lựa chọn này giúp game có tính replay cao hơn, vì người chơi có thể chơi lại mà không gặp đúng cùng một trình tự tình huống.

- Điều này cũng giảm khả năng người chơi học thuộc thứ tự round và làm cho trải nghiệm chơi lại tự nhiên hơn.

<!-- -->

- **Thêm trade size vào quyết định giao dịch**

<!-- -->

- Người chơi không chỉ chọn Buy hoặc Sell, mà còn phải chọn mức độ giao dịch.

- Trade size giúp thể hiện mức độ rủi ro mà người chơi sẵn sàng chấp nhận.

- Hai người có thể cùng chọn Buy, nhưng một người mua ít và một người mua gần như toàn bộ cash sẽ phản ánh mức độ phản ứng khác nhau trước cùng một scenario.

<!-- -->

- **Sử dụng rule-based bias detection thay vì AI. modek**

<!-- -->

- Nhóm chọn rule-based logic thay vì mô hình AI phức tạp.

- Cách này phù hợp với mục tiêu vì logic dễ hiểu, dễ kiểm tra và dễ giải thích

- Mỗi bias được gắn với một số điều kiện cụ thể, giúp nhóm có thể giải thích vì sao hệ thống ghi nhận bias đó ở người chơi.

<!-- -->

- **Chọn Python/Streamlit để xây dựng demo**

<!-- -->

- Python/Streamlit đủ đơn giản để nhóm phát triển sản phẩm trong phạm vi môn học.

- Công cụ này vẫn cho phép nhóm kết nối các phần quan trọng như scenario data, Data Manager, app flow, trading logic, bias rules, scoring và final dashboard.

- Nhờ đó, nhóm có thể tạo ra một bản demo chạy được, dễ trình bày và dễ kiểm tra.

## **Điểm nhóm thấy làm tốt)**

1.  **Mô phỏng cơ chế khớp lệnh sát thực tế và quản lý tốt sai số**

> **N**hóm đã xử lý khá tốt bài toán sai số thập phân (floating-point inaccuracy) thường gặp. Thay vì nhân tỷ lệ % đơn thuần, thuật toán áp dụng làm tròn xuống (math.floor) để mô phỏng giao dịch **cổ phiếu nguyên lô**. Điều này giúp hạn chế tối đa rủi ro tiền thực mua vượt quá số dư thực tế, duy trì sự ổn định cho các phép tính tài chính của game.

2.  Hệ thống scoring không đánh giá bias chỉ dựa trên lựa chọn đơn giản như **Buy / Sell / Hold**,

> Nhóm đã tính đến bối cảnh ra quyết định của người chơi. Cụ thể, game xét thêm các yếu tố như **fundamentals, news tone, crowd signal, trade size, trạng thái lãi/lỗ và mức độ phù hợp giữa hành động với thông tin thị trường**.

3.  **Hệ thống anti-double-counting trong bias scoring được thiết kế rất chặt**

> Mỗi cluster có ID riêng và chỉ fire tối đa một lần mỗi vòng. Amplifier chỉ được tính khi đã có supporting cluster trước đó — ví dụ OC_HIGH_SIZE_AMPLIFIER không thể fire nếu chỉ có core OC_WARNING_IGNORED. Điều này ngăn việc một hành động bị tính điểm bias nhiều lần chỉ vì nó thỏa mãn nhiều điều kiện cùng lúc.

4.  **UI trực quan và dễ theo dõi**

> Nhóm đã thiết kế giao diện theo đúng trình tự người chơi cần sử dụng: bắt đầu game, đọc scenario, xem danh mục, đưa ra quyết định, xác nhận quyết định, xem kết quả round và cuối cùng xem final dashboard.
>
> Các thông tin quan trọng như giá cổ phiếu, portfolio value, cash, shares, return và tín hiệu thị trường được đặt ở những vị trí dễ nhìn, giúp người chơi không bị rối khi ra quyết định.

5.  **Flow chơi mượt và có logic rõ ràng**

> Game có luồng chơi khép kín qua từng round: scenario → decision → checkpoint question → market movement → outcome revealed → next round.
>
> Người chơi không bị chuyển màn hình đột ngột, mà luôn biết mình đang ở bước nào và cần làm gì tiếp theo. Việc yêu cầu trả lời câu hỏi ngắn trước khi confirm decision cũng giúp flow có tính học tập hơn, vì người chơi phải đọc hiểu scenario trước khi hệ thống xử lý kết quả.

**6 Scenario design tốt và hỗ trợ đúng mục tiêu**

Nhóm thiết kế các scenario có bối cảnh thị trường rõ ràng, kết hợp giá cổ phiếu, tin tức, fundamentals và tín hiệu đám đông để người chơi phải cân nhắc trước khi ra quyết định. Các scenario cũng được liên kết với những bias chính của game, giúp phần bias detection có cơ sở rõ hơn. Ngoài ra, việc randomize thứ tự rounds làm trải nghiệm chơi lại bớt lặp và tự nhiên hơn.

## **Hạn chế hiện tại** 

1.  **Giới hạn ở một mã tài sản:** Lõi Trading xử lý luồng tiền rất tốt nhưng hiện tại mới thiết lập cho 1 mã cổ phiếu duy nhất (STEELSTOX). Do đó, sản phẩm chưa đo lường được các lỗi tâm lý liên quan đến việc Tái cơ cấu tỷ trọng tài sản hay Đa dạng hóa danh mục (Diversification).

2.  **Thiếu cơ chế Thuế, Phí giao dịch và Trượt giá:** Thuật toán hiện tại đang cho phép giao dịch miễn phí hoàn toàn. Trong thực tế, các lỗi tâm lý như "Giao dịch quá mức" (Overconfidence/Overtrading) sẽ bào mòn tài khoản rất nhanh do phí môi giới và thuế.

3.  **Hệ thống chấm điểm thiên kiến hiện vẫn dựa trên các quy tắc định sẵn**. Cách này phù hợp với phạm vi dự án, nhưng chưa thể bao quát toàn bộ sự phức tạp trong tâm lý đầu tư thực tế. Một hành vi của người chơi đôi khi có thể đến từ nhiều nguyên nhân khác nhau, không chỉ từ một thiên kiến cụ thể.’

4.  **Dự án dùng scenario dựng sẵn,** kết quả phù hợp để phản ánh hành vi trong môi trường mô phỏng, chưa nên xem là kết luận chắc chắn về hành vi đầu tư ngoài đời thực. Tiền tệ trong game chỉ là tiền ảo nên người chơi có thể sẽ có hành vi risk taking mạnh hơn so với việc dùng tiền thật.

## **Điều nhóm học được** 

- **Hiểu vấn đề và người dùng rõ hơn**

<!-- -->

- Người dùng mục tiêu là sinh viên mới học tài chính, nên sản phẩm phải đủ đơn giản để dễ chơi, nhưng vẫn phải đủ logic để thể hiện được các bias.Và các bias nên là những bias mà sinh viên dễ mắc phải

- Ban đầu, nhóm dự định đưa nhiều behavioral biases hơn vào game để sản phẩm có vẻ đầy đủ hơn về mặt lý thuyết.

- Tuy nhiên, sau nhiều lần trao đổi và cân nhắc, nhóm nhận ra rằng nếu đưa quá nhiều bias, game sẽ khó thiết kế scenario, khó viết rule rõ ràng và khó giải thích kết quả cho người chơi.

- Vì vậy, nhóm quyết định tập trung vào các bias phổ biến và dễ quan sát trong hành vi đầu tư của người mới, Đây cũng là những bias mà bản thân các thành viên trong nhóm từng gặp

<!-- -->

- **Học cách thiết kế sản phẩm theo một flow rõ ràng**

<!-- -->

- Nhóm học được rằng một game tài chính cần có flow mạch lạc để người chơi hiểu mình đang làm gì ở từng bước.

- Flow cuối cùng được xây dựng theo hướng: người chơi đọc scenario, xem danh mục, chọn Buy/Sell/Hold, trả lời câu hỏi để confirm decision, sau đó hệ thống mới xử lý giao dịch và hiển thị kết quả của round.

- Nhóm cũng học được rằng việc randomize thứ tự các rounds giúp game có tính replay cao hơn và tránh cảm giác mỗi lượt chơi đều giống nhau.

<!-- -->

- **Học cách chuyển lý thuyết tài chính thành logic cụ thể**

<!-- -->

- Một bài học lớn là các khái niệm trong behavioral finance khi đưa thành các bộ rule thì cần rất cẩn thận.

- Khi đưa vào sản phẩm, mỗi bias phải được chuyển thành điều kiện rõ ràng, ví dụ khi nào được xem là lỗ lớn, khi nào hành động Hold có thể liên quan đến loss aversion, hoặc khi nào việc Sell một khoản lời nhỏ có thể liên quan đến disposition effect.

- Vì vậy, việc xây dựng logic cần có rule rõ ràng, biến rõ ràng và phải được test nhiều lần qua nhiều trường hợp khác nhau.

<!-- -->

- **Học được tầm quan trọng của testing**

<!-- -->

- Trong quá trình làm, nhóm nhiều lần bị chậm hơn kế hoạch ban đầu vì code lỗi hoặc rule chưa hoạt động đúng.

- Có lúc bias rule chưa detect được bias như dự kiến, hoặc trading rule hiển thị nhầm return, khiến kết quả không phản ánh đúng quyết định của người chơi.

- Những lỗi này giúp nhóm nhận ra rằng một sản phẩm chạy được chưa chắc đã đúng..

<!-- -->

- **Học cách làm việc nhóm hiệu quả hơn**

<!-- -->

- Ban đầu, các thành viên chưa thực sự hiểu toàn bộ game. Mỗi người chủ yếu hiểu phần mình phụ trách, ví dụ scenario, UI, trading logic, bias detection hoặc app flow.

- Điều này làm cho việc tích hợp ban đầu khá khó, vì một module thay đổi có thể ảnh hưởng đến module khác.

- Sau nhiều lần họp nhóm và trao đổi liên tục, các thành viên bắt đầu hiểu rõ hơn mối quan hệ giữa phần việc của mình và phần việc của người khác.

- Khi mọi người hiểu được game như một hệ thống chung, việc sửa lỗi và hoàn thiện sản phẩm trở nên nhanh hơn.

- Nhóm học được rằng làm việc nhóm không chỉ là chia việc, mà còn là đảm bảo mọi người hiểu cách phần việc của mình kết nối với sản phẩm cuối.

## **Gợi ý cho khóa sau - Cả nhóm (1-2 idea)**

Nếu sinh viên khóa sau muốn tiếp tục hoặc học từ sản phẩm này, nhóm muốn nhắn gì?

1.  **Nên bổ sung thêm biến số Phí Giao Dịch:** Khóa sau nên bắt đầu nâng cấp bằng cách thêm một hằng số nhỏ (Ví dụ: TRANSACTION_FEE = 0.0015) vào hàm execute_buy và execute_sell để trừ thẳng vào tiền mặt người chơi, giúp game cọ xát với thực tế khốc liệt của thị trường chứng khoán hơn.

2.  **Có thể thêm nhiều loại tài sản khác ngoài một cổ phiếu duy nhất**, ví dụ cổ phiếu ngành khác, trái phiếu hoặc crypto giả lập, để người chơi học cách so sánh rủi ro giữa các lựa chọn.

3.  **Tuy nhiên,** phải ưu tiên core logic trước khi thêm tính năng. Đừng cố thêm quá nhiều tính năng khi phần cốt lõi chưa ổn định.Khi core logic đã vững, việc mở rộng thêm nhiều scenario, nhiều tài sản, biểu đồ hoặc feedback cá nhân hóa sẽ dễ hơn nhiều.

4.  **Cập nhật plan song song với code.** Nếu code đã thay đổi nhưng tài liệu vẫn mô tả bản cũ, nhóm sẽ khó giải thích sản phẩm trong buổi demo. Documentation tốt giúp nhóm hiểu sản phẩm rõ hơn và cũng giúp người khác dễ tiếp tục phát triển sản phẩm.
