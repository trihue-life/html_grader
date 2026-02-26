# HTML Grader

**HTML Grader** là một công cụ dòng lệnh (CLI) viết bằng Python để chấm điểm các bài tập HTML một cách tự động. Công cụ này phân tích code HTML của học sinh, so sánh với các tiêu chí được định sẵn, và đưa ra điểm số cùng với các phản hồi chi tiết.

## Tính năng

- ✅ **Kiểm tra cấu trúc HTML chuẩn** (DOCTYPE, html, head, title, body)
- ✅ **Kiểm tra thẻ bắt buộc** được chỉ định trong bài tập
- ✅ **Kiểm tra cú pháp** (thẻ mở/đóng, dấu nháy)
- ✅ **Kiểm tra định dạng** (thụt lề, độ dài dòng)
- ✅ **Kiểm tra thuộc tính** (alt cho img, href cho a, src cho img)
- ✅ **Hệ thống điểm 10 điểm** với phân bổ chi tiết
- ✅ **Báo cáo chi tiết** với danh sách lỗi, cảnh báo và gợi ý
- ✅ **Xuất kết quả JSON** để tích hợp với các hệ thống khác

## Tác giả

- **Tên:** Trí Huệ
- **Email:** trihue.life@gmail.com
- **GitHub:** [TriHue-life](https://github.com/TriHue-life)

## Phiên bản

- **Version:** 1.1.0

## Cài đặt

### Yêu cầu

- Python 3.6+
- Không cần thư viện bên ngoài (chỉ sử dụng thư viện chuẩn của Python)

### Hướng dẫn

1. Clone hoặc tải xuống dự án:

```bash
git clone https://github.com/TriHue-life/html_grader.git
cd html_grader
```

2. Cấp quyền thực thi cho script (tùy chọn):

```bash
chmod +x grader.py
```

## Sử dụng

### Cú pháp cơ bản

```bash
python3 grader.py <file_html> --exercise <exercise_id>
```

### Ví dụ

1. **Chấm điểm bài tập F1 - Vận dụng 1:**

```bash
python3 grader.py student_code/exercise1.html --exercise f1_apply1
```

2. **Chấm điểm với file test_cases tùy chỉnh:**

```bash
python3 grader.py code.html --exercise f2_apply2 --test-cases my_test_cases.json
```

3. **Xuất kết quả dưới dạng JSON:**

```bash
python3 grader.py code.html --exercise f1_apply1 --json
```

### Tùy chọn dòng lệnh

| Tùy chọn | Mô tả | Bắt buộc |
|----------|-------|---------|
| `html_file` | Đường dẫn đến file HTML cần chấm | ✅ Có |
| `--exercise`, `-e` | ID của bài tập (vd: f1_apply1) | ✅ Có |
| `--test-cases`, `-t` | Đường dẫn đến file test_cases.json (mặc định: test_cases.json) | ❌ Không |
| `--json`, `-j` | In kết quả dưới dạng JSON | ❌ Không |

## Cấu trúc thang điểm

HTML Grader sử dụng thang điểm 10 điểm, phân bổ như sau:

| Tiêu chí | Điểm | Mô tả |
|----------|------|-------|
| **Cấu trúc HTML** | 2.5 | Kiểm tra DOCTYPE, html, head, title, body |
| **Thẻ bắt buộc** | 3.0 | Kiểm tra các thẻ được chỉ định trong bài tập |
| **Cú pháp thẻ** | 2.5 | Kiểm tra thẻ mở/đóng khớp, dấu nháy |
| **Định dạng** | 1.0 | Kiểm tra thụt lề, độ dài dòng |
| **Thuộc tính** | 1.0 | Kiểm tra thuộc tính bắt buộc (alt, href, src) |
| **TỔNG** | **10.0** | |

### Phân loại kết quả

- 🏆 **8.5 - 10.0**: Xuất sắc!
- 👍 **7.0 - 8.4**: Khá tốt
- ⚠️ **5.0 - 6.9**: Trung bình
- ❌ **0 - 4.9**: Cần cải thiện

## Cấu trúc dự án

```
html_grader/
├── grader.py              # Script Python chính để chấm điểm
├── test_cases.json        # File JSON chứa các bài tập và tiêu chí
├── student_code/          # Thư mục chứa các file HTML mẫu
│   ├── example_good.html  # Ví dụ HTML tốt (10/10 điểm)
│   └── example_bad.html   # Ví dụ HTML có lỗi (7.8/10 điểm)
├── README.md              # Tài liệu này
└── DESIGN.md              # Tài liệu thiết kế chi tiết
```

## Định dạng file test_cases.json

File `test_cases.json` là một mảng JSON chứa các bài tập. Mỗi bài tập có cấu trúc sau:

```json
[
  {
    "id": "f1_apply1",
    "title": "F1 - Vận dụng 1: Trang thông tin cá nhân",
    "description": "Viết mã HTML hoàn chỉnh tạo trang web có tiêu đề là 'Thông tin cá nhân'...",
    "required_tags": ["html", "head", "title", "body", "h1", "p"],
    "initial_code": ""
  },
  // ... các bài tập khác
]
```

### Các trường

- **id** (string): Định danh duy nhất của bài tập (vd: f1_apply1)
- **title** (string): Tiêu đề bài tập
- **description** (string): Mô tả chi tiết yêu cầu bài tập
- **required_tags** (array): Danh sách các thẻ HTML bắt buộc phải có
- **initial_code** (string): Code mẫu ban đầu (tùy chọn)

## Danh sách bài tập

HTML Grader bao gồm 22 bài tập được phân thành 5 nhóm chính:

### BÀI F1: HTML VÀ TRANG WEB

- `f1_apply1`: Trang thông tin cá nhân
- `f1_apply2`: Trang có ô nhập số điện thoại
- `f1_apply3`: Lí lịch trích ngang (có `<hr>`)
- `f1_analyze1`: Sửa lỗi cú pháp thuộc tính

### BÀI F2: TẠO VÀ ĐỊNH DẠNG

- `f2_apply1`: Danh sách môn học yêu thích (in đậm)
- `f2_apply2`: Trang thành viên lớp + liên kết
- `f2_apply3`: Portfolio — Sở thích & Hoạt động

### BÀI F3: BẢNG VÀ KHUNG

- `f3_apply1`: Bảng danh sách điểm thi
- `f3_apply2`: Bố cục trang web (Header-Menu-Nội dung-Footer)
- `f3_apply3`: Nhúng video YouTube (iframe)

### BÀI F4: ĐA PHƯƠNG TIỆN

- `f4_apply1`: Video tự động phát, tắt tiếng
- `f4_apply2`: Trang nhạc + lời bài hát
- `f4_apply3`: Portfolio hoàn chỉnh (ảnh + video + audio)

### BÀI F5: BIỂU MẪU

- `f5_apply1`: Biểu mẫu tìm kiếm
- `f5_apply2`: Đăng ký nhận tin (email bắt buộc)
- `f5_apply3`: Khảo sát ý kiến
- `f5_apply4`: Trang đăng nhập hệ thống
- `f5_apply5`: Đăng ký câu lạc bộ

### BỘ TỔNG HỢP (F1–F5)

- `tong1`: Hồ sơ cá nhân tổng hợp
- `tong2`: Thời khóa biểu phức tạp
- `tong3`: Đăng ký câu lạc bộ đầy đủ

## Ví dụ kết quả

### Kết quả tốt (10/10)

```
======================================================================
  HTML GRADER - KẾT QUẢ CHẤM ĐIỂM
======================================================================
📝 Bài tập: F1 - Vận dụng 1: Trang thông tin cá nhân
──────────────────────────────────────────────────────────────────────
🏆 TỔNG ĐIỂM: 10.0/10 (Xuất sắc!)
──────────────────────────────────────────────────────────────────────
📊 CHI TIẾT ĐIỂM:
  • Cấu trúc HTML:      2.5/2.5
  • Thẻ bắt buộc:       3.0/3.0
  • Cú pháp thẻ:        2.5/2.5
  • Định dạng:          1.0/1.0
  • Thuộc tính:         1.0/1.0
──────────────────────────────────────────────────────────────────────
📋 PHÂN TÍCH:
  • ✕ Lỗi:        0
  • ⚠ Cảnh báo:    0
  • ℹ Gợi ý:      0
  • ✓ Đúng:       6
======================================================================
```

### Kết quả có lỗi (7.8/10)

```
======================================================================
  HTML GRADER - KẾT QUẢ CHẤM ĐIỂM
======================================================================
📝 Bài tập: F1 - Vận dụng 1: Trang thông tin cá nhân
──────────────────────────────────────────────────────────────────────
👍 TỔNG ĐIỂM: 7.8/10 (Khá tốt)
──────────────────────────────────────────────────────────────────────
📊 CHI TIẾT ĐIỂM:
  • Cấu trúc HTML:      2.5/2.5
  • Thẻ bắt buộc:       3.0/3.0
  • Cú pháp thẻ:        1.0/2.5
  • Định dạng:          0.5/1.0
  • Thuộc tính:         0.8/1.0
──────────────────────────────────────────────────────────────────────
📋 PHÂN TÍCH:
  • ✕ Lỗi:        3
  • ⚠ Cảnh báo:    1
  • ℹ Gợi ý:      1
  • ✓ Đúng:       6
──────────────────────────────────────────────────────────────────────
🔍 CHI TIẾT LỖI & CẢNH BÁO:

✕ Thẻ <h1> chưa đóng (Dòng 7)
   Dòng 7: Thẻ <h1> mở nhưng không có thẻ đóng </h1>.
✕ Thẻ đóng không khớp </body> (Dòng 10)
   Dòng 10: Thẻ </body> không có thẻ mở tương ứng.
   Code: </body>
⚠ Thẻ <img> thiếu thuộc tính alt (Dòng 9)
   Thẻ <img> cần có thuộc tính alt="" để mô tả hình ảnh...
   Code: <img src="avatar.jpg">
ℹ Không có thụt lề (Toàn bộ file)
   Code không có thụt lề (indent). Nên thụt lề các thẻ lồng nhau...

======================================================================
```

## Xuất kết quả JSON

Sử dụng tùy chọn `--json` để xuất kết quả dưới dạng JSON:

```bash
python3 grader.py code.html --exercise f1_apply1 --json
```

Kết quả:

```json
{
  "exercise_id": "f1_apply1",
  "exercise_title": "F1 - Vận dụng 1: Trang thông tin cá nhân",
  "total_score": 10.0,
  "scores": {
    "structure": 2.5,
    "required": 3.0,
    "syntax": 2.5,
    "format": 1.0,
    "attributes": 1.0
  },
  "issues": [
    {
      "type": "success",
      "line": 2,
      "title": "Có thẻ <html>",
      "message": "Thẻ <html> được tìm thấy trong code.",
      "code": null
    }
    // ... các issue khác
  ]
}
```

## Tích hợp với các hệ thống khác

HTML Grader có thể được tích hợp với các hệ thống quản lý học tập (LMS) hoặc các công cụ tự động hóa khác thông qua:

1. **Gọi từ dòng lệnh**: Các script bash hoặc Python khác có thể gọi `grader.py` và xử lý kết quả
2. **Xuất JSON**: Sử dụng tùy chọn `--json` để nhận dữ liệu có cấu trúc
3. **Tùy chỉnh test_cases.json**: Tạo các bài tập tùy chỉnh cho lớp học của bạn

## Phát triển thêm

### Các tính năng có thể thêm trong tương lai

- [ ] Hỗ trợ CSS checking
- [ ] Hỗ trợ JavaScript checking
- [ ] Kiểm tra accessibility (WCAG)
- [ ] Kiểm tra SEO
- [ ] Giao diện web (Flask/Django)
- [ ] Tích hợp GitHub Classroom
- [ ] Báo cáo chi tiết PDF

## Đóng góp

Chúng tôi hoan nghênh các đóng góp! Vui lòng:

1. Fork dự án
2. Tạo branch cho tính năng mới (`git checkout -b feature/AmazingFeature`)
3. Commit các thay đổi (`git commit -m 'Add some AmazingFeature'`)
4. Push đến branch (`git push origin feature/AmazingFeature`)
5. Mở Pull Request

## Giấy phép

Dự án này được cấp phép dưới giấy phép MIT. Xem file [LICENSE](LICENSE) để biết chi tiết.

## Liên hệ

- **Tác giả**: Trí Huệ
- **Email**: 
- **GitHub**: [html_grader](https://github.com/yourusername/html_grader)

## Lịch sử phiên bản

### v1.0.0 (2026-02-26)

- ✅ Phát hành phiên bản đầu tiên
- ✅ Hỗ trợ 22 bài tập HTML
- ✅ Chấm điểm tự động với 5 tiêu chí
- ✅ Báo cáo chi tiết với danh sách lỗi
- ✅ Xuất kết quả JSON

---

**Chúc bạn sử dụng HTML Grader vui vẻ! 🎉**
