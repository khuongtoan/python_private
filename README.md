git add README.md   

Câu 1: Python có thể làm được gì?
Python là một ngôn ngữ lập trình đa năng, có thể được sử dụng cho nhiều mục đích khác nhau:

Phát triển ứng dụng web: Sử dụng các framework như Django, Flask.
Phân tích dữ liệu và khoa học dữ liệu: Các thư viện như Pandas, NumPy, Matplotlib, Scikit-learn giúp xử lý dữ liệu, phân tích và machine learning.
Trí tuệ nhân tạo (AI) và Machine Learning (ML): Các thư viện như TensorFlow, PyTorch, Keras hỗ trợ các mô hình AI và ML.
Tự động hóa: Python có thể dùng để tự động hóa các tác vụ hệ thống, tạo script tự động.
Phát triển game: Sử dụng Pygame để phát triển các trò chơi cơ bản.
Phát triển ứng dụng desktop: Sử dụng Tkinter hoặc PyQt.
IoT và lập trình nhúng: Có thể sử dụng MicroPython hoặc CircuitPython để lập trình cho thiết bị nhỏ như Raspberry Pi.


Câu 2: So sánh đặc điểm của Python với C++
Loại ngôn ngữ: Python là ngôn ngữ thông dịch, nghĩa là mã nguồn Python được thực thi trực tiếp bởi trình thông dịch mà không cần biên dịch trước. C++ là ngôn ngữ biên dịch, nghĩa là mã nguồn C++ cần phải được biên dịch thành mã máy trước khi có thể chạy.

Cú pháp: Python có cú pháp đơn giản và dễ học, không yêu cầu dấu chấm phẩy (;) hay khai báo kiểu dữ liệu cho biến, giúp mã nguồn gọn gàng và dễ đọc. Ngược lại, C++ có cú pháp phức tạp hơn, yêu cầu khai báo kiểu dữ liệu cho mỗi biến và dấu chấm phẩy ở cuối các lệnh, làm cho mã nguồn có thể dài và khó đọc hơn với người mới học.

Tốc độ thực thi: Python chậm hơn so với C++ vì Python là ngôn ngữ thông dịch và mã nguồn được dịch trong thời gian thực. C++ nhanh hơn nhiều vì mã nguồn đã được biên dịch thành mã máy, sẵn sàng để CPU thực thi.

Quản lý bộ nhớ: Python sử dụng cơ chế quản lý bộ nhớ tự động thông qua hệ thống thu gom rác (Garbage Collection), giúp người lập trình không phải quản lý bộ nhớ trực tiếp. Trong C++, lập trình viên phải quản lý bộ nhớ thủ công, thông qua con trỏ và các hàm cấp phát như new và delete, điều này cung cấp sự linh hoạt nhưng cũng đòi hỏi kiến thức quản lý bộ nhớ tốt để tránh rò rỉ bộ nhớ (memory leak).

Mức độ ứng dụng: Python thích hợp với các ứng dụng cần phát triển nhanh, chẳng hạn như web, khoa học dữ liệu, trí tuệ nhân tạo, và các tác vụ tự động hóa. Trong khi đó, C++ thường được sử dụng cho các ứng dụng yêu cầu hiệu suất cao, như lập trình hệ thống, phát triển game, và các ứng dụng nhúng.


Câu 3: Python là ngôn ngữ biên dịch hay thông dịch? Vì sao?
Python là ngôn ngữ thông dịch. Điều này có nghĩa là mã Python được chạy trực tiếp bởi trình thông dịch (interpreter) thay vì được biên dịch thành mã máy trước khi thực thi.     Cụ thể:
Python code được chuyển thành mã bytecode và sau đó trình thông dịch Python (CPython, PyPy, Jython, ...) sẽ thực thi mã bytecode này.
Quá trình thông dịch cho phép Python linh hoạt, dễ sửa lỗi, và chạy mà không cần phải biên dịch toàn bộ chương trình, giúp quá trình phát triển nhanh chóng hơn