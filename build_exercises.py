#!/usr/bin/env python3
"""Script tạo EXERCISES data với tiêu chí chi tiết cho từng bài"""
import json

EXERCISES = [
  # ─── F1 ───────────────────────────────────────────────────────────
  {
    "id": "f1_apply1",
    "title": "F1 - Vận dụng 1: Trang thông tin cá nhân",
    "description": "Tạo trang HTML giới thiệu bản thân gồm: <code>&lt;h1&gt;</code> tên, <code>&lt;p&gt;</code> giới thiệu, thuộc tính <code>bgcolor</code> hoặc <code>style</code> cho <code>&lt;body&gt;</code>, và thẻ <code>&lt;title&gt;</code> đặt tên trang.",
    "required_tags": ["h1", "p"],
    "criteria": [
      {
        "name": "1. Cấu trúc HTML cơ bản",
        "points": 2.5,
        "items": [
          "✅ Dòng đầu tiên là <!DOCTYPE html>",
          "✅ Có thẻ <html lang=\"vi\"> hoặc <html>",
          "✅ Có thẻ <head> chứa <title>",
          "✅ Có thẻ <body> chứa nội dung"
        ]
      },
      {
        "name": "2. Thẻ nội dung bắt buộc",
        "points": 3.0,
        "items": [
          "✅ Có thẻ <h1> chứa tên của bạn",
          "✅ Có ít nhất 1 thẻ <p> giới thiệu bản thân",
          "✅ <title> có nội dung (không để trống)"
        ]
      },
      {
        "name": "3. Nội dung & Thuộc tính",
        "points": 3.0,
        "items": [
          "✅ <body> có thuộc tính bgcolor hoặc style",
          "✅ <h1> có nội dung (tên thực sự)",
          "✅ <p> có nội dung mô tả bản thân"
        ]
      },
      {
        "name": "4. Cú pháp & Định dạng",
        "points": 1.5,
        "items": [
          "✅ Tất cả thẻ mở đều có thẻ đóng tương ứng",
          "✅ Thuộc tính được bọc trong dấu nháy kép",
          "✅ Thụt lề code đúng (2 hoặc 4 dấu cách)"
        ]
      }
    ],
    "test_cases": [
      {"type": "tag_exist", "tags": ["h1", "p"], "error": "Thiếu thẻ <{tag}>", "hint": "Thêm thẻ <{tag}> vào <body>"},
      {"type": "attr_value", "tag": "body", "attr": "bgcolor", "value": None, "optional": True, "error": "Nên có bgcolor hoặc style trên <body>", "hint": "Thêm bgcolor=\"#ffffff\" hoặc style=\"background:...\" vào <body>"},
      {"type": "title_contains", "value": "", "error": "<title> không được để trống", "hint": "Thêm nội dung vào <title>Tên trang</title>"}
    ]
  },
  {
    "id": "f1_apply2",
    "title": "F1 - Vận dụng 2: Trang có ô nhập số điện thoại",
    "description": "Tạo trang HTML có: <code>&lt;label&gt;</code> nhãn, <code>&lt;input type=\"tel\"&gt;</code> nhập số điện thoại, và <code>&lt;button&gt;</code> xác nhận.",
    "required_tags": ["label", "input", "button"],
    "criteria": [
      {
        "name": "1. Cấu trúc HTML cơ bản",
        "points": 2.5,
        "items": [
          "✅ Có <!DOCTYPE html>",
          "✅ Có <html>, <head>, <title>, <body>"
        ]
      },
      {
        "name": "2. Thẻ form bắt buộc",
        "points": 4.0,
        "items": [
          "✅ Có thẻ <label> với nội dung nhãn",
          "✅ Có thẻ <input> nhập dữ liệu",
          "✅ Có thẻ <button> hoặc <input type=\"submit\">",
          "✅ <input> có type=\"tel\" hoặc type=\"text\""
        ]
      },
      {
        "name": "3. Nội dung & Thuộc tính",
        "points": 2.0,
        "items": [
          "✅ <input> có thuộc tính type",
          "✅ <button> có nội dung (ví dụ: \"Xác nhận\")"
        ]
      },
      {
        "name": "4. Cú pháp & Định dạng",
        "points": 1.5,
        "items": [
          "✅ Thẻ đóng đúng (trừ self-closing tags)",
          "✅ Thuộc tính có dấu nháy kép",
          "✅ Thụt lề hợp lý"
        ]
      }
    ],
    "test_cases": [
      {"type": "tag_exist", "tags": ["label", "input", "button"], "error": "Thiếu thẻ <{tag}>", "hint": "Thêm thẻ <{tag}> vào trang"},
      {"type": "attr_value", "tag": "input", "attr": "type", "value": "tel", "optional": True, "error": "<input> nên có type=\"tel\" cho số điện thoại", "hint": "Đổi thành <input type=\"tel\">"}
    ]
  },
  {
    "id": "f1_apply3",
    "title": "F1 - Vận dụng 3: Lí lịch trích ngang (có <hr>)",
    "description": "Tạo trang lí lịch trích ngang gồm: <code>&lt;h1&gt;</code> họ tên, <code>&lt;hr&gt;</code> đường kẻ ngang, ít nhất 3 thẻ <code>&lt;p&gt;</code> thông tin (ngày sinh, địa chỉ, nghề nghiệp).",
    "required_tags": ["h1", "hr", "p"],
    "criteria": [
      {
        "name": "1. Cấu trúc HTML cơ bản",
        "points": 2.5,
        "items": [
          "✅ Có <!DOCTYPE html>",
          "✅ Có <html>, <head>, <title>, <body>"
        ]
      },
      {
        "name": "2. Thẻ nội dung bắt buộc",
        "points": 4.0,
        "items": [
          "✅ Có thẻ <h1> chứa họ tên",
          "✅ Có thẻ <hr> (đường kẻ ngang)",
          "✅ Có ít nhất 3 thẻ <p> thông tin cá nhân",
          "✅ Thông tin đa dạng (ngày sinh, địa chỉ, v.v.)"
        ]
      },
      {
        "name": "3. Nội dung",
        "points": 2.0,
        "items": [
          "✅ <h1> chứa tên thực",
          "✅ Các <p> có nội dung thông tin thực tế"
        ]
      },
      {
        "name": "4. Cú pháp & Định dạng",
        "points": 1.5,
        "items": [
          "✅ Thẻ đóng đúng",
          "✅ Thụt lề hợp lý"
        ]
      }
    ],
    "test_cases": [
      {"type": "tag_exist", "tags": ["h1", "hr", "p"], "error": "Thiếu thẻ <{tag}>", "hint": "Thêm thẻ <{tag}> vào trang"},
      {"type": "tag_count", "tag": "p", "min": 3, "error": "Cần ít nhất 3 thẻ <p> thông tin cá nhân", "hint": "Thêm các <p> cho ngày sinh, địa chỉ, nghề nghiệp..."}
    ]
  },
  {
    "id": "f1_analyze1",
    "title": "F1 - Phân tích: Sửa lỗi cú pháp thuộc tính",
    "description": "Sửa đoạn code HTML có lỗi: thêm <code>&lt;h2&gt;</code> tiêu đề, <code>&lt;p&gt;</code> nội dung, <code>&lt;a href=\"...\"&gt;</code> liên kết hợp lệ. Đảm bảo tất cả thuộc tính có dấu nháy kép.",
    "required_tags": ["h2", "p", "a"],
    "criteria": [
      {
        "name": "1. Cấu trúc HTML cơ bản",
        "points": 2.5,
        "items": [
          "✅ Có <!DOCTYPE html>",
          "✅ Có <html>, <head>, <title>, <body>"
        ]
      },
      {
        "name": "2. Thẻ nội dung bắt buộc",
        "points": 3.5,
        "items": [
          "✅ Có thẻ <h2> tiêu đề",
          "✅ Có thẻ <p> nội dung",
          "✅ Có thẻ <a> liên kết"
        ]
      },
      {
        "name": "3. Cú pháp đúng",
        "points": 2.5,
        "items": [
          "✅ <a> có thuộc tính href hợp lệ",
          "✅ Tất cả thuộc tính có dấu nháy kép",
          "✅ Không có thẻ đóng thừa hoặc thiếu"
        ]
      },
      {
        "name": "4. Định dạng",
        "points": 1.5,
        "items": [
          "✅ Thụt lề đúng",
          "✅ Không có dòng quá 120 ký tự"
        ]
      }
    ],
    "test_cases": [
      {"type": "tag_exist", "tags": ["h2", "p", "a"], "error": "Thiếu thẻ <{tag}>", "hint": "Thêm thẻ <{tag}>"},
      {"type": "attr_exist", "tag": "a", "attr": "href", "error": "<a> phải có thuộc tính href", "hint": "Thêm href=\"https://...\" vào thẻ <a>"}
    ]
  },

  # ─── F2 ───────────────────────────────────────────────────────────
  {
    "id": "f2_apply1",
    "title": "F2 - Vận dụng 1: Danh sách môn học yêu thích (in đậm)",
    "description": "Tạo trang có: <code>&lt;h2&gt;</code> tiêu đề, danh sách không thứ tự <code>&lt;ul&gt;</code> với ít nhất 3 <code>&lt;li&gt;</code>, dùng <code>&lt;strong&gt;</code> in đậm tên môn học.",
    "required_tags": ["h2", "ul", "li", "strong"],
    "criteria": [
      {
        "name": "1. Cấu trúc HTML cơ bản",
        "points": 2.0,
        "items": [
          "✅ Có <!DOCTYPE html>",
          "✅ Có <html>, <head>, <title>, <body>"
        ]
      },
      {
        "name": "2. Thẻ danh sách bắt buộc",
        "points": 4.5,
        "items": [
          "✅ Có thẻ <h2> tiêu đề danh sách",
          "✅ Có thẻ <ul> (danh sách không thứ tự)",
          "✅ Có ít nhất 3 thẻ <li> trong <ul>",
          "✅ Có thẻ <strong> in đậm tên môn học"
        ]
      },
      {
        "name": "3. Nội dung",
        "points": 2.0,
        "items": [
          "✅ Mỗi <li> chứa tên môn học thực tế",
          "✅ <strong> bao quanh tên môn học"
        ]
      },
      {
        "name": "4. Cú pháp",
        "points": 1.5,
        "items": [
          "✅ <li> phải nằm trong <ul>",
          "✅ Thẻ đóng đúng"
        ]
      }
    ],
    "test_cases": [
      {"type": "tag_exist", "tags": ["h2", "ul", "li", "strong"], "error": "Thiếu thẻ <{tag}>", "hint": "Thêm thẻ <{tag}>"},
      {"type": "tag_count", "tag": "li", "min": 3, "error": "Cần ít nhất 3 thẻ <li> trong danh sách", "hint": "Thêm ít nhất 3 mục <li> vào <ul>"}
    ]
  },
  {
    "id": "f2_apply2",
    "title": "F2 - Vận dụng 2: Trang thành viên lớp + liên kết",
    "description": "Tạo trang danh sách thành viên lớp: <code>&lt;ol&gt;</code> danh sách có thứ tự, ít nhất 3 <code>&lt;li&gt;</code>, mỗi thành viên có <code>&lt;a href&gt;</code> liên kết Facebook/email, và <code>&lt;p&gt;</code> mô tả.",
    "required_tags": ["ol", "li", "a", "p"],
    "criteria": [
      {
        "name": "1. Cấu trúc HTML cơ bản",
        "points": 2.0,
        "items": [
          "✅ Có <!DOCTYPE html>",
          "✅ Có <html>, <head>, <title>, <body>"
        ]
      },
      {
        "name": "2. Thẻ danh sách & liên kết",
        "points": 4.5,
        "items": [
          "✅ Có thẻ <ol> (danh sách có thứ tự)",
          "✅ Có ít nhất 3 thẻ <li> trong <ol>",
          "✅ Có thẻ <a> liên kết",
          "✅ Có thẻ <p> mô tả"
        ]
      },
      {
        "name": "3. Thuộc tính liên kết",
        "points": 2.0,
        "items": [
          "✅ <a> có href hợp lệ (https:// hoặc mailto:)",
          "✅ <a> có nội dung (tên thành viên)"
        ]
      },
      {
        "name": "4. Cú pháp",
        "points": 1.5,
        "items": [
          "✅ <li> nằm trong <ol>",
          "✅ Thẻ đóng đúng"
        ]
      }
    ],
    "test_cases": [
      {"type": "tag_exist", "tags": ["ol", "li", "a", "p"], "error": "Thiếu thẻ <{tag}>", "hint": "Thêm thẻ <{tag}>"},
      {"type": "attr_exist", "tag": "a", "attr": "href", "error": "<a> phải có thuộc tính href", "hint": "Thêm href=\"https://...\" vào <a>"}
    ]
  },
  {
    "id": "f2_apply3",
    "title": "F2 - Vận dụng 3: Portfolio — Sở thích & Hoạt động",
    "description": "Tạo trang Portfolio cá nhân gồm: <code>&lt;h1&gt;</code> tên, <code>&lt;ul&gt;</code> danh sách sở thích, <code>&lt;ol&gt;</code> danh sách hoạt động (có thứ tự), và <code>&lt;a&gt;</code> liên kết mạng xã hội.",
    "required_tags": ["h1", "ul", "ol", "li", "a"],
    "criteria": [
      {
        "name": "1. Cấu trúc HTML cơ bản",
        "points": 2.0,
        "items": [
          "✅ Có <!DOCTYPE html>",
          "✅ Có <html>, <head>, <title>, <body>"
        ]
      },
      {
        "name": "2. Thẻ nội dung bắt buộc",
        "points": 4.5,
        "items": [
          "✅ Có <h1> tên cá nhân",
          "✅ Có <ul> danh sách sở thích",
          "✅ Có <ol> danh sách hoạt động",
          "✅ Có ít nhất 3 <li> trong mỗi danh sách",
          "✅ Có <a> liên kết mạng xã hội"
        ]
      },
      {
        "name": "3. Nội dung",
        "points": 2.0,
        "items": [
          "✅ <li> có nội dung thực tế",
          "✅ <a> có href hợp lệ"
        ]
      },
      {
        "name": "4. Cú pháp",
        "points": 1.5,
        "items": [
          "✅ Thẻ đóng đúng",
          "✅ Thụt lề hợp lý"
        ]
      }
    ],
    "test_cases": [
      {"type": "tag_exist", "tags": ["h1", "ul", "ol", "li", "a"], "error": "Thiếu thẻ <{tag}>", "hint": "Thêm thẻ <{tag}>"},
      {"type": "tag_count", "tag": "li", "min": 3, "error": "Cần ít nhất 3 thẻ <li>", "hint": "Thêm ít nhất 3 mục <li>"}
    ]
  },

  # ─── F3 ───────────────────────────────────────────────────────────
  {
    "id": "f3_apply1",
    "title": "F3 - Vận dụng 1: Bảng danh sách điểm thi",
    "description": "Tạo bảng điểm thi gồm: <code>&lt;table&gt;</code> có <code>border</code>, <code>&lt;thead&gt;</code> hàng tiêu đề với <code>&lt;th&gt;</code>, <code>&lt;tbody&gt;</code> ít nhất 3 hàng dữ liệu <code>&lt;tr&gt;&lt;td&gt;</code>.",
    "required_tags": ["table", "thead", "tbody", "tr", "th", "td"],
    "criteria": [
      {
        "name": "1. Cấu trúc HTML cơ bản",
        "points": 2.0,
        "items": [
          "✅ Có <!DOCTYPE html>",
          "✅ Có <html>, <head>, <title>, <body>"
        ]
      },
      {
        "name": "2. Cấu trúc bảng đầy đủ",
        "points": 5.0,
        "items": [
          "✅ Có <table> (bảng chính)",
          "✅ Có <thead> (phần tiêu đề bảng)",
          "✅ Có <tbody> (phần dữ liệu bảng)",
          "✅ Có <th> trong <thead> (tiêu đề cột)",
          "✅ Có ít nhất 3 hàng <tr> trong <tbody>",
          "✅ Mỗi hàng có <td> dữ liệu"
        ]
      },
      {
        "name": "3. Nội dung",
        "points": 1.5,
        "items": [
          "✅ <th> có tên cột (STT, Họ tên, Điểm...)",
          "✅ <td> có dữ liệu điểm thực tế"
        ]
      },
      {
        "name": "4. Cú pháp",
        "points": 1.5,
        "items": [
          "✅ <td>/<th> nằm trong <tr>",
          "✅ <tr> nằm trong <thead>/<tbody>",
          "✅ Thẻ đóng đúng"
        ]
      }
    ],
    "test_cases": [
      {"type": "tag_exist", "tags": ["table", "thead", "tbody", "tr", "th", "td"], "error": "Thiếu thẻ <{tag}>", "hint": "Thêm thẻ <{tag}> vào bảng"},
      {"type": "tag_count", "tag": "tr", "min": 4, "error": "Cần ít nhất 4 hàng <tr> (1 tiêu đề + 3 dữ liệu)", "hint": "Thêm hàng <tr> vào <tbody>"}
    ]
  },
  {
    "id": "f3_apply2",
    "title": "F3 - Vận dụng 2: Bố cục trang web (Header-Menu-Nội dung-Footer)",
    "description": "Tạo bố cục trang web ngữ nghĩa gồm: <code>&lt;header&gt;</code> tiêu đề, <code>&lt;nav&gt;</code> menu điều hướng, <code>&lt;main&gt;</code> nội dung chính, <code>&lt;footer&gt;</code> chân trang.",
    "required_tags": ["header", "nav", "main", "footer"],
    "criteria": [
      {
        "name": "1. Cấu trúc HTML cơ bản",
        "points": 2.0,
        "items": [
          "✅ Có <!DOCTYPE html>",
          "✅ Có <html>, <head>, <title>, <body>"
        ]
      },
      {
        "name": "2. Thẻ ngữ nghĩa bắt buộc",
        "points": 5.0,
        "items": [
          "✅ Có <header> (phần đầu trang)",
          "✅ Có <nav> (menu điều hướng)",
          "✅ Có <main> (nội dung chính)",
          "✅ Có <footer> (chân trang)",
          "✅ Thứ tự đúng: header → nav → main → footer"
        ]
      },
      {
        "name": "3. Nội dung",
        "points": 1.5,
        "items": [
          "✅ <header> có tiêu đề trang",
          "✅ <nav> có danh sách liên kết",
          "✅ <footer> có thông tin liên hệ"
        ]
      },
      {
        "name": "4. Cú pháp",
        "points": 1.5,
        "items": [
          "✅ Thẻ đóng đúng",
          "✅ Thụt lề hợp lý"
        ]
      }
    ],
    "test_cases": [
      {"type": "tag_exist", "tags": ["header", "nav", "main", "footer"], "error": "Thiếu thẻ <{tag}>", "hint": "Thêm thẻ <{tag}> vào bố cục trang"}
    ]
  },
  {
    "id": "f3_apply3",
    "title": "F3 - Vận dụng 3: Nhúng video YouTube (iframe)",
    "description": "Nhúng video YouTube vào trang web bằng <code>&lt;iframe&gt;</code> có <code>src</code> URL YouTube, <code>width</code> và <code>height</code> kích thước, <code>allowfullscreen</code>.",
    "required_tags": ["iframe"],
    "criteria": [
      {
        "name": "1. Cấu trúc HTML cơ bản",
        "points": 2.5,
        "items": [
          "✅ Có <!DOCTYPE html>",
          "✅ Có <html>, <head>, <title>, <body>"
        ]
      },
      {
        "name": "2. Thẻ iframe bắt buộc",
        "points": 4.5,
        "items": [
          "✅ Có thẻ <iframe>",
          "✅ <iframe> có thuộc tính src",
          "✅ src chứa URL YouTube (youtube.com/embed/...)",
          "✅ <iframe> có width và height",
          "✅ <iframe> có allowfullscreen"
        ]
      },
      {
        "name": "3. Nội dung",
        "points": 1.5,
        "items": [
          "✅ Có tiêu đề <h2> hoặc <h3> mô tả video",
          "✅ URL YouTube hợp lệ"
        ]
      },
      {
        "name": "4. Cú pháp",
        "points": 1.5,
        "items": [
          "✅ Thuộc tính có dấu nháy kép",
          "✅ Thẻ đóng đúng"
        ]
      }
    ],
    "test_cases": [
      {"type": "tag_exist", "tags": ["iframe"], "error": "Thiếu thẻ <iframe>", "hint": "Thêm <iframe src=\"https://www.youtube.com/embed/VIDEO_ID\">"},
      {"type": "attr_exist", "tag": "iframe", "attr": "src", "error": "<iframe> phải có thuộc tính src", "hint": "Thêm src=\"https://www.youtube.com/embed/VIDEO_ID\""},
      {"type": "attr_exist", "tag": "iframe", "attr": "allowfullscreen", "error": "<iframe> nên có allowfullscreen", "hint": "Thêm allowfullscreen vào <iframe>"}
    ]
  },

  # ─── F4 ───────────────────────────────────────────────────────────
  {
    "id": "f4_apply1",
    "title": "F4 - Vận dụng 1: Video tự động phát, tắt tiếng",
    "description": "Nhúng video vào trang bằng <code>&lt;video&gt;</code> với <code>&lt;source&gt;</code>, có các thuộc tính: <code>autoplay</code>, <code>muted</code>, <code>controls</code>.",
    "required_tags": ["video", "source"],
    "criteria": [
      {
        "name": "1. Cấu trúc HTML cơ bản",
        "points": 2.0,
        "items": [
          "✅ Có <!DOCTYPE html>",
          "✅ Có <html>, <head>, <title>, <body>"
        ]
      },
      {
        "name": "2. Thẻ video bắt buộc",
        "points": 5.0,
        "items": [
          "✅ Có thẻ <video>",
          "✅ Có thẻ <source> bên trong <video>",
          "✅ <source> có thuộc tính src (đường dẫn video)",
          "✅ <video> có thuộc tính autoplay",
          "✅ <video> có thuộc tính muted",
          "✅ <video> có thuộc tính controls"
        ]
      },
      {
        "name": "3. Nội dung",
        "points": 1.5,
        "items": [
          "✅ <source> có type (video/mp4)",
          "✅ Có tiêu đề mô tả video"
        ]
      },
      {
        "name": "4. Cú pháp",
        "points": 1.5,
        "items": [
          "✅ <source> là self-closing tag",
          "✅ Thẻ đóng đúng"
        ]
      }
    ],
    "test_cases": [
      {"type": "tag_exist", "tags": ["video", "source"], "error": "Thiếu thẻ <{tag}>", "hint": "Thêm <video><source src=\"video.mp4\"></video>"},
      {"type": "bool_attr", "tag": "video", "attr": "autoplay", "error": "<video> phải có thuộc tính autoplay", "hint": "Thêm autoplay vào <video autoplay muted controls>"},
      {"type": "bool_attr", "tag": "video", "attr": "muted", "error": "<video> phải có thuộc tính muted", "hint": "Thêm muted vào <video autoplay muted controls>"},
      {"type": "bool_attr", "tag": "video", "attr": "controls", "error": "<video> phải có thuộc tính controls", "hint": "Thêm controls vào <video autoplay muted controls>"}
    ]
  },
  {
    "id": "f4_apply2",
    "title": "F4 - Vận dụng 2: Trang nhạc + lời bài hát",
    "description": "Tạo trang nhạc gồm: <code>&lt;h2&gt;</code> tên bài hát, <code>&lt;audio&gt;</code> với <code>&lt;source&gt;</code> và <code>controls</code>, và <code>&lt;p&gt;</code> hoặc <code>&lt;pre&gt;</code> chứa lời bài hát.",
    "required_tags": ["audio", "source", "h2"],
    "criteria": [
      {
        "name": "1. Cấu trúc HTML cơ bản",
        "points": 2.0,
        "items": [
          "✅ Có <!DOCTYPE html>",
          "✅ Có <html>, <head>, <title>, <body>"
        ]
      },
      {
        "name": "2. Thẻ audio bắt buộc",
        "points": 4.5,
        "items": [
          "✅ Có thẻ <audio>",
          "✅ Có <source> bên trong <audio>",
          "✅ <source> có src (đường dẫn file nhạc)",
          "✅ <audio> có thuộc tính controls",
          "✅ Có <h2> tên bài hát"
        ]
      },
      {
        "name": "3. Nội dung lời bài hát",
        "points": 2.0,
        "items": [
          "✅ Có <p> hoặc <pre> chứa lời bài hát",
          "✅ Lời bài hát có nội dung thực tế"
        ]
      },
      {
        "name": "4. Cú pháp",
        "points": 1.5,
        "items": [
          "✅ Thẻ đóng đúng",
          "✅ Thuộc tính có dấu nháy kép"
        ]
      }
    ],
    "test_cases": [
      {"type": "tag_exist", "tags": ["audio", "source", "h2"], "error": "Thiếu thẻ <{tag}>", "hint": "Thêm thẻ <{tag}>"},
      {"type": "bool_attr", "tag": "audio", "attr": "controls", "error": "<audio> phải có thuộc tính controls", "hint": "Thêm controls vào <audio controls>"}
    ]
  },
  {
    "id": "f4_apply3",
    "title": "F4 - Vận dụng 3: Portfolio hoàn chỉnh (ảnh + video + audio)",
    "description": "Tạo trang Portfolio đa phương tiện gồm: <code>&lt;img&gt;</code> ảnh đại diện (có <code>alt</code>), <code>&lt;video&gt;</code> giới thiệu, <code>&lt;audio&gt;</code> nhạc nền, <code>&lt;h1&gt;</code> tên, <code>&lt;p&gt;</code> mô tả.",
    "required_tags": ["img", "video", "audio", "h1", "p"],
    "criteria": [
      {
        "name": "1. Cấu trúc HTML cơ bản",
        "points": 2.0,
        "items": [
          "✅ Có <!DOCTYPE html>",
          "✅ Có <html>, <head>, <title>, <body>"
        ]
      },
      {
        "name": "2. Thẻ media đầy đủ",
        "points": 4.5,
        "items": [
          "✅ Có <img> ảnh đại diện",
          "✅ <img> có thuộc tính alt",
          "✅ Có <video> (hoặc <source> trong video)",
          "✅ Có <audio> (hoặc <source> trong audio)",
          "✅ Có <h1> tên cá nhân"
        ]
      },
      {
        "name": "3. Nội dung",
        "points": 2.0,
        "items": [
          "✅ <img alt> có mô tả thực tế",
          "✅ <p> có nội dung giới thiệu"
        ]
      },
      {
        "name": "4. Cú pháp",
        "points": 1.5,
        "items": [
          "✅ Thẻ đóng đúng",
          "✅ Thuộc tính có dấu nháy kép"
        ]
      }
    ],
    "test_cases": [
      {"type": "tag_exist", "tags": ["img", "video", "audio", "h1", "p"], "error": "Thiếu thẻ <{tag}>", "hint": "Thêm thẻ <{tag}>"},
      {"type": "attr_exist", "tag": "img", "attr": "alt", "error": "<img> phải có thuộc tính alt", "hint": "Thêm alt=\"mô tả ảnh\" vào <img>"}
    ]
  },

  # ─── F5 ───────────────────────────────────────────────────────────
  {
    "id": "f5_apply1",
    "title": "F5 - Vận dụng 1: Biểu mẫu tìm kiếm",
    "description": "Tạo form tìm kiếm gồm: <code>&lt;form&gt;</code>, <code>&lt;input type=\"search\"&gt;</code> hoặc <code>type=\"text\"</code>, <code>&lt;button type=\"submit\"&gt;</code>.",
    "required_tags": ["form", "input", "button"],
    "criteria": [
      {
        "name": "1. Cấu trúc HTML cơ bản",
        "points": 2.0,
        "items": [
          "✅ Có <!DOCTYPE html>",
          "✅ Có <html>, <head>, <title>, <body>"
        ]
      },
      {
        "name": "2. Thẻ form bắt buộc",
        "points": 4.5,
        "items": [
          "✅ Có thẻ <form>",
          "✅ Có <input> ô nhập tìm kiếm",
          "✅ <input> có type=\"search\" hoặc type=\"text\"",
          "✅ Có <button> hoặc <input type=\"submit\">",
          "✅ Có <label> hoặc placeholder mô tả"
        ]
      },
      {
        "name": "3. Thuộc tính",
        "points": 2.0,
        "items": [
          "✅ <form> có action hoặc method",
          "✅ <input> có name hoặc placeholder"
        ]
      },
      {
        "name": "4. Cú pháp",
        "points": 1.5,
        "items": [
          "✅ <input> là self-closing tag",
          "✅ Thẻ đóng đúng"
        ]
      }
    ],
    "test_cases": [
      {"type": "tag_exist", "tags": ["form", "input", "button"], "error": "Thiếu thẻ <{tag}>", "hint": "Thêm thẻ <{tag}> vào form"},
      {"type": "attr_value", "tag": "input", "attr": "type", "value": "search", "optional": True, "error": "<input> nên có type=\"search\" cho form tìm kiếm", "hint": "Thêm type=\"search\" vào <input>"}
    ]
  },
  {
    "id": "f5_apply2",
    "title": "F5 - Vận dụng 2: Đăng ký nhận tin (email bắt buộc)",
    "description": "Tạo form đăng ký nhận tin gồm: <code>&lt;input type=\"email\"&gt;</code> bắt buộc (<code>required</code>), <code>&lt;label&gt;</code> nhãn, <code>&lt;button&gt;</code> gửi.",
    "required_tags": ["form", "input", "label", "button"],
    "criteria": [
      {
        "name": "1. Cấu trúc HTML cơ bản",
        "points": 2.0,
        "items": [
          "✅ Có <!DOCTYPE html>",
          "✅ Có <html>, <head>, <title>, <body>"
        ]
      },
      {
        "name": "2. Thẻ form bắt buộc",
        "points": 4.5,
        "items": [
          "✅ Có thẻ <form>",
          "✅ Có <input type=\"email\">",
          "✅ <input> có thuộc tính required",
          "✅ Có <label> nhãn mô tả",
          "✅ Có <button> gửi form"
        ]
      },
      {
        "name": "3. Thuộc tính",
        "points": 2.0,
        "items": [
          "✅ <input type=\"email\"> — đúng kiểu dữ liệu",
          "✅ required — bắt buộc nhập email"
        ]
      },
      {
        "name": "4. Cú pháp",
        "points": 1.5,
        "items": [
          "✅ Thẻ đóng đúng",
          "✅ Thuộc tính có dấu nháy kép"
        ]
      }
    ],
    "test_cases": [
      {"type": "attr_value", "tag": "input", "attr": "type", "value": "email", "error": "Thiếu <input type=\"email\">", "hint": "Thêm <input type=\"email\" required>"},
      {"type": "bool_attr", "tag": "input", "attr": "required", "error": "<input> phải có thuộc tính required", "hint": "Thêm required vào <input type=\"email\" required>"}
    ]
  },
  {
    "id": "f5_apply3",
    "title": "F5 - Vận dụng 3: Khảo sát ý kiến",
    "description": "Tạo form khảo sát gồm: <code>&lt;input type=\"radio\"&gt;</code> câu hỏi trắc nghiệm, <code>&lt;input type=\"checkbox\"&gt;</code> chọn nhiều, và <code>&lt;textarea&gt;</code> ý kiến tự do.",
    "required_tags": ["form", "input", "textarea"],
    "criteria": [
      {
        "name": "1. Cấu trúc HTML cơ bản",
        "points": 2.0,
        "items": [
          "✅ Có <!DOCTYPE html>",
          "✅ Có <html>, <head>, <title>, <body>"
        ]
      },
      {
        "name": "2. Thẻ form bắt buộc",
        "points": 4.5,
        "items": [
          "✅ Có thẻ <form>",
          "✅ Có <input type=\"radio\"> câu hỏi trắc nghiệm",
          "✅ Có <input type=\"checkbox\"> chọn nhiều",
          "✅ Có <textarea> ý kiến tự do",
          "✅ Có <button> gửi form"
        ]
      },
      {
        "name": "3. Thuộc tính",
        "points": 2.0,
        "items": [
          "✅ <input type=\"radio\"> có name (cùng nhóm)",
          "✅ <textarea> có rows hoặc cols"
        ]
      },
      {
        "name": "4. Cú pháp",
        "points": 1.5,
        "items": [
          "✅ Thẻ đóng đúng",
          "✅ Thuộc tính có dấu nháy kép"
        ]
      }
    ],
    "test_cases": [
      {"type": "attr_value", "tag": "input", "attr": "type", "value": "radio", "error": "Thiếu <input type=\"radio\">", "hint": "Thêm <input type=\"radio\" name=\"q1\">"},
      {"type": "attr_value", "tag": "input", "attr": "type", "value": "checkbox", "error": "Thiếu <input type=\"checkbox\">", "hint": "Thêm <input type=\"checkbox\">"},
      {"type": "tag_exist", "tags": ["textarea"], "error": "Thiếu thẻ <textarea>", "hint": "Thêm <textarea rows=\"4\"></textarea>"}
    ]
  },
  {
    "id": "f5_apply4",
    "title": "F5 - Thực hành: Trang đăng nhập hệ thống",
    "description": "Tạo form đăng nhập gồm: <code>&lt;input type=\"text\"&gt;</code> tên đăng nhập, <code>&lt;input type=\"password\"&gt;</code> mật khẩu (có <code>required</code>), <code>&lt;label&gt;</code> cho mỗi input, và <code>&lt;button&gt;</code> đăng nhập.",
    "required_tags": ["form", "input", "label", "button"],
    "criteria": [
      {
        "name": "1. Cấu trúc HTML cơ bản",
        "points": 2.0,
        "items": [
          "✅ Có <!DOCTYPE html>",
          "✅ Có <html>, <head>, <title>, <body>"
        ]
      },
      {
        "name": "2. Thẻ form đăng nhập",
        "points": 4.5,
        "items": [
          "✅ Có thẻ <form>",
          "✅ Có <input type=\"text\"> tên đăng nhập",
          "✅ Có <input type=\"password\"> mật khẩu",
          "✅ Có <label> cho mỗi input",
          "✅ Có <button> Đăng nhập"
        ]
      },
      {
        "name": "3. Thuộc tính bảo mật",
        "points": 2.0,
        "items": [
          "✅ <input> có required (bắt buộc nhập)",
          "✅ <label> có for khớp với id của input"
        ]
      },
      {
        "name": "4. Cú pháp",
        "points": 1.5,
        "items": [
          "✅ Thẻ đóng đúng",
          "✅ Thuộc tính có dấu nháy kép"
        ]
      }
    ],
    "test_cases": [
      {"type": "attr_value", "tag": "input", "attr": "type", "value": "password", "error": "Thiếu <input type=\"password\">", "hint": "Thêm <input type=\"password\" required>"},
      {"type": "bool_attr", "tag": "input", "attr": "required", "error": "Input phải có required", "hint": "Thêm required vào các <input>"}
    ]
  },
  {
    "id": "f5_apply5",
    "title": "F5 - Vận dụng: Đăng ký câu lạc bộ",
    "description": "Tạo form đăng ký câu lạc bộ có: <code>&lt;select&gt;</code> chọn câu lạc bộ (ít nhất 3 <code>&lt;option&gt;</code>), <code>&lt;input type=\"text\"&gt;</code> họ tên, <code>&lt;input type=\"email\"&gt;</code>, và nút submit.",
    "required_tags": ["form", "select", "option", "input", "button"],
    "criteria": [
      {
        "name": "1. Cấu trúc HTML cơ bản",
        "points": 2.0,
        "items": [
          "✅ Có <!DOCTYPE html>",
          "✅ Có <html>, <head>, <title>, <body>"
        ]
      },
      {
        "name": "2. Thẻ form đăng ký",
        "points": 4.5,
        "items": [
          "✅ Có thẻ <form>",
          "✅ Có <select> chọn câu lạc bộ",
          "✅ Có ít nhất 3 <option> trong <select>",
          "✅ Có <input type=\"email\">",
          "✅ Có <button> submit"
        ]
      },
      {
        "name": "3. Nội dung",
        "points": 2.0,
        "items": [
          "✅ <option> có nội dung tên câu lạc bộ",
          "✅ <input type=\"text\"> họ tên"
        ]
      },
      {
        "name": "4. Cú pháp",
        "points": 1.5,
        "items": [
          "✅ Thẻ đóng đúng",
          "✅ Thuộc tính có dấu nháy kép"
        ]
      }
    ],
    "test_cases": [
      {"type": "tag_exist", "tags": ["select", "option"], "error": "Thiếu thẻ <{tag}>", "hint": "Thêm <select><option>...</option></select>"},
      {"type": "tag_count", "tag": "option", "min": 3, "error": "Cần ít nhất 3 <option>", "hint": "Thêm các <option> vào <select>"}
    ]
  },

  # ─── Tổng hợp ─────────────────────────────────────────────────────
  {
    "id": "tong1",
    "title": "Tổng hợp - Vận dụng 1: Hồ sơ cá nhân tổng hợp (F1+F2+F4)",
    "description": "Tạo trang Hồ sơ cá nhân tổng hợp gồm: <code>&lt;h1&gt;</code> tên, <code>&lt;img&gt;</code> ảnh đại diện (có alt), danh sách <code>&lt;ul&gt;</code> sở thích, liên kết <code>&lt;a&gt;</code>, và nhúng <code>&lt;audio&gt;</code> hoặc <code>&lt;video&gt;</code>.",
    "required_tags": ["h1", "img", "ul", "li", "a"],
    "criteria": [
      {
        "name": "1. Cấu trúc HTML cơ bản",
        "points": 2.0,
        "items": [
          "✅ Có <!DOCTYPE html>",
          "✅ Có <html>, <head>, <title>, <body>"
        ]
      },
      {
        "name": "2. Thẻ nội dung bắt buộc (F1+F2)",
        "points": 4.5,
        "items": [
          "✅ Có <h1> tên cá nhân",
          "✅ Có <img> ảnh đại diện với alt",
          "✅ Có <ul> danh sách sở thích",
          "✅ Có ít nhất 3 <li>",
          "✅ Có <a> liên kết mạng xã hội"
        ]
      },
      {
        "name": "3. Media (F4)",
        "points": 2.0,
        "items": [
          "✅ Có <audio> hoặc <video>",
          "✅ Media có controls"
        ]
      },
      {
        "name": "4. Cú pháp",
        "points": 1.5,
        "items": [
          "✅ Thẻ đóng đúng",
          "✅ Thuộc tính có dấu nháy kép"
        ]
      }
    ],
    "test_cases": [
      {"type": "tag_exist", "tags": ["h1", "img", "ul", "li", "a"], "error": "Thiếu thẻ <{tag}>", "hint": "Thêm thẻ <{tag}>"},
      {"type": "attr_exist", "tag": "img", "attr": "alt", "error": "<img> phải có thuộc tính alt", "hint": "Thêm alt=\"mô tả ảnh\" vào <img>"}
    ]
  },
  {
    "id": "tong2",
    "title": "Tổng hợp - Vận dụng 2: Thời khóa biểu phức tạp (F3)",
    "description": "Tạo bảng thời khóa biểu: <code>&lt;table&gt;</code> với <code>border</code>, hàng tiêu đề <code>&lt;thead&gt;</code>, ít nhất 5 hàng dữ liệu <code>&lt;tbody&gt;</code>, dùng <code>colspan</code> hoặc <code>rowspan</code>.",
    "required_tags": ["table", "thead", "tbody", "tr", "th", "td"],
    "criteria": [
      {
        "name": "1. Cấu trúc HTML cơ bản",
        "points": 2.0,
        "items": [
          "✅ Có <!DOCTYPE html>",
          "✅ Có <html>, <head>, <title>, <body>"
        ]
      },
      {
        "name": "2. Cấu trúc bảng đầy đủ",
        "points": 4.5,
        "items": [
          "✅ Có <table>",
          "✅ Có <thead> và <tbody>",
          "✅ Có <th> trong thead",
          "✅ Có ít nhất 5 hàng <tr> trong tbody"
        ]
      },
      {
        "name": "3. Thuộc tính nâng cao",
        "points": 2.0,
        "items": [
          "✅ <table> có border",
          "✅ Dùng colspan hoặc rowspan"
        ]
      },
      {
        "name": "4. Cú pháp",
        "points": 1.5,
        "items": [
          "✅ Thẻ đóng đúng",
          "✅ Thụt lề hợp lý"
        ]
      }
    ],
    "test_cases": [
      {"type": "tag_exist", "tags": ["table", "thead", "tbody", "tr", "th", "td"], "error": "Thiếu thẻ <{tag}>", "hint": "Thêm thẻ <{tag}>"},
      {"type": "tag_count", "tag": "tr", "min": 6, "error": "Cần ít nhất 6 hàng <tr> (1 tiêu đề + 5 dữ liệu)", "hint": "Thêm hàng <tr> vào <tbody>"}
    ]
  },
  {
    "id": "tong3",
    "title": "Tổng hợp - Vận dụng 3: Đăng ký câu lạc bộ đầy đủ (F5)",
    "description": "Tạo form đăng ký câu lạc bộ đầy đủ: họ tên, email (<code>required</code>), <code>&lt;select&gt;</code> câu lạc bộ, <code>&lt;input type=\"radio\"&gt;</code> giới tính, <code>&lt;textarea&gt;</code> lý do, nút submit.",
    "required_tags": ["form", "input", "select", "textarea", "button"],
    "criteria": [
      {
        "name": "1. Cấu trúc HTML cơ bản",
        "points": 2.0,
        "items": [
          "✅ Có <!DOCTYPE html>",
          "✅ Có <html>, <head>, <title>, <body>"
        ]
      },
      {
        "name": "2. Thẻ form đầy đủ",
        "points": 4.5,
        "items": [
          "✅ Có <form>",
          "✅ Có <input type=\"email\" required>",
          "✅ Có <select> câu lạc bộ",
          "✅ Có <input type=\"radio\"> giới tính",
          "✅ Có <textarea> lý do",
          "✅ Có <button> submit"
        ]
      },
      {
        "name": "3. Thuộc tính",
        "points": 2.0,
        "items": [
          "✅ required trên email",
          "✅ <select> có ít nhất 3 <option>"
        ]
      },
      {
        "name": "4. Cú pháp",
        "points": 1.5,
        "items": [
          "✅ Thẻ đóng đúng",
          "✅ Thuộc tính có dấu nháy kép"
        ]
      }
    ],
    "test_cases": [
      {"type": "tag_exist", "tags": ["form", "select", "textarea", "button"], "error": "Thiếu thẻ <{tag}>", "hint": "Thêm thẻ <{tag}>"},
      {"type": "attr_value", "tag": "input", "attr": "type", "value": "email", "error": "Thiếu <input type=\"email\">", "hint": "Thêm <input type=\"email\" required>"},
      {"type": "bool_attr", "tag": "input", "attr": "required", "error": "Email phải có required", "hint": "Thêm required vào <input type=\"email\">"}
    ]
  }
]

# Xuất JSON
print(json.dumps(EXERCISES, ensure_ascii=False, indent=2))
