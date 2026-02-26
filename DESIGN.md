# Thiết kế HTML Grader

## 1. Tổng quan

HTML Grader là một công cụ dòng lệnh (CLI) viết bằng Python để chấm điểm các bài tập HTML một cách tự động. Công cụ này sẽ phân tích code HTML của học sinh, so sánh với các tiêu chí được định sẵn trong một file test case, và đưa ra điểm số cùng với các phản hồi chi tiết.

Logic chấm điểm được mô phỏng dựa trên file `ÔnluyệnHTML(2).html`.

## 2. Cấu trúc dự án

```
/home/ubuntu/html_grader/
├── grader.py         # Script Python chính để chấm điểm
├── test_cases.json   # File JSON chứa các bài tập và tiêu chí
├── student_code/     # Thư mục chứa các file HTML của học sinh cần chấm
│   └── exercise1.html
└── README.md         # Hướng dẫn sử dụng
```

## 3. Cấu trúc file `test_cases.json`

File này sẽ là một mảng các đối tượng JSON, mỗi đối tượng đại diện cho một bài tập.

```json
[
  {
    "id": "f1_apply1",
    "title": "F1 - Vận dụng 1: Trang thông tin cá nhân",
    "description": "Tạo một trang web đơn giản hiển thị thông tin cá nhân của bạn, bao gồm họ tên, lớp, và một bức ảnh.",
    "required_tags": ["h1", "p", "img"],
    "initial_code": "<!DOCTYPE html>\n<html>\n<head>\n  <title>Thông tin cá nhân</title>\n</head>\n<body>\n  \n</body>\n</html>"
  }
  // ... các bài tập khác
]
```

## 4. Logic chấm điểm trong `grader.py`

Script sẽ đọc một file HTML đầu vào, nhận một `exercise_id` để biết cần áp dụng bộ tiêu chí nào từ `test_cases.json`.

**Thang điểm (Tổng: 10.0):**

1.  **Cấu trúc HTML chuẩn (2.5 điểm):**
    - `<!DOCTYPE html>`: 0.5đ
    - `<html>...</html>`: 0.5đ
    - `<head>...</head>`: 0.5đ
    - `<title>...</title>`: 0.5đ
    - `<body>...</body>`: 0.5đ

2.  **Thẻ bắt buộc (3.0 điểm):**
    - Điểm được chia đều cho các thẻ trong `required_tags` của test case.
    - Ví dụ: nếu có 3 thẻ bắt buộc, mỗi thẻ sẽ là 1.0đ.

3.  **Cú pháp thẻ hợp lệ (2.5 điểm):**
    - Điểm ban đầu là 2.5.
    - Mỗi lỗi cú pháp (thẻ không đóng, thẻ đóng sai,...) sẽ trừ 0.5đ.
    - Các lỗi bao gồm:
        - Thẻ mở nhưng không có thẻ đóng tương ứng.
        - Thẻ đóng không có thẻ mở.
        - Thuộc tính có dấu nháy `"` không được đóng.

4.  **Thụt lề / Định dạng (1.0 điểm):**
    - Điểm ban đầu là 1.0.
    - Nếu không có thụt lề nào được phát hiện (cho file dài hơn 5 dòng): 0.5đ.
    - Nếu có dòng dài hơn 200 ký tự: 0.5đ.
    - Nếu không có code HTML thực sự: 0đ.

5.  **Thuộc tính hợp lệ (1.0 điểm):**
    - Điểm ban đầu là 1.0.
    - Mỗi lỗi thuộc tính sẽ trừ điểm:
        - `<img>` thiếu `alt`: -0.25đ
        - `<img>` thiếu `src`: -0.25đ
        - `<a>` thiếu `href`: -0.2đ

**Thư viện Python:**
- `json` để đọc `test_cases.json`.
- `argparse` để xử lý tham số dòng lệnh.
- `BeautifulSoup4` (sẽ được cài đặt) để phân tích (parse) và duyệt cây HTML một cách hiệu quả, thay vì dùng regex phức tạp.

## 5. Luồng hoạt động

1. Người dùng chạy lệnh:
   `python3 grader.py student_code/exercise1.html --exercise f1_apply1`
2. `grader.py` đọc nội dung file `student_code/exercise1.html`.
3. Script tải `test_cases.json` và tìm test case có `id` là `f1_apply1`.
4. Sử dụng `BeautifulSoup` để phân tích code HTML.
5. Áp dụng các quy tắc chấm điểm đã nêu ở trên.
6. In kết quả ra màn hình theo định dạng rõ ràng, bao gồm:
   - Tổng điểm.
   - Điểm thành phần.
   - Danh sách các lỗi và cảnh báo cụ thể (kèm số dòng nếu có thể).
