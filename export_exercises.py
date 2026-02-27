#!/usr/bin/env python3
import json

def struct_criteria(points=2.5):
    per = round(points / 5, 2)
    return {
        "name": "1. Cấu trúc HTML cơ bản",
        "points": points,
        "checks": [
            {"type": "has_doctype", "points": per, "label": "Có <!DOCTYPE html>", "hint": "Thêm <!DOCTYPE html> vào dòng đầu tiên"},
            {"type": "has_tag", "tag": "html", "points": per, "label": "Có thẻ <html>", "hint": "Bọc toàn bộ nội dung trong <html>...</html>"},
            {"type": "has_tag", "tag": "head", "points": per, "label": "Có thẻ <head>", "hint": "Thêm <head>...</head> bên trong <html>"},
            {"type": "has_tag", "tag": "title", "points": per, "label": "Có thẻ <title>", "hint": "Thêm <title>Tiêu đề</title> vào trong <head>"},
            {"type": "has_tag", "tag": "body", "points": per, "label": "Có thẻ <body>", "hint": "Thêm <body>...</body> bên trong <html>"},
        ]
    }

def syntax_criteria(points=1.5):
    return {
        "name": "4. Cú pháp & Định dạng",
        "points": round(points, 2),
        "checks": [
            {"type": "no_syntax_error", "points": round(points * 0.7, 2), "label": "Không có lỗi thẻ đóng/mở", "hint": "Mỗi thẻ mở phải có thẻ đóng tương ứng"},
            {"type": "no_quote_error", "points": round(points * 0.3, 2), "label": "Thuộc tính có dấu nháy kép", "hint": "Dùng dấu nháy kép: attr=\"value\""},
        ]
    }

EXERCISES = [
    # F1
    {
        "id": "f1_apply1", "group": "F1 — Thẻ cơ bản",
        "title": "F1 - Vận dụng 1: Trang giới thiệu bản thân",
        "description": "Tạo trang giới thiệu bản thân với <code>&lt;h1&gt;</code> tên, <code>&lt;h2&gt;</code> tiêu đề phụ, <code>&lt;p&gt;</code> đoạn văn giới thiệu, <code>&lt;ul&gt;</code> danh sách sở thích.",
        "required_tags": ["h1","h2","p","ul","li"],
        "criteria": [
            struct_criteria(2.5),
            {"name":"2. Thẻ nội dung bắt buộc","points":5.5,"checks":[
                {"type":"has_tag","tag":"h1","points":1.0,"label":"Có thẻ <h1> tên","hint":"Thêm <h1>Tên của bạn</h1>"},
                {"type":"has_tag","tag":"h2","points":1.0,"label":"Có thẻ <h2> tiêu đề phụ","hint":"Thêm <h2>Giới thiệu</h2>"},
                {"type":"has_tag","tag":"p","points":1.0,"label":"Có thẻ <p> đoạn văn","hint":"Thêm <p>Nội dung giới thiệu</p>"},
                {"type":"has_tag","tag":"ul","points":1.0,"label":"Có thẻ <ul> danh sách","hint":"Thêm <ul>...</ul>"},
                {"type":"tag_count","tag":"li","min":3,"points":1.5,"label":"Có ít nhất 3 <li> sở thích","hint":"Thêm ít nhất 3 <li>Sở thích</li> vào <ul>"},
            ]},
            syntax_criteria(2.0),
        ]
    },
    {
        "id": "f1_apply2", "group": "F1 — Thẻ cơ bản",
        "title": "F1 - Vận dụng 2: Bài thơ / Bài hát yêu thích",
        "description": "Tạo trang hiển thị bài thơ/bài hát với <code>&lt;h1&gt;</code> tên bài, <code>&lt;h2&gt;</code> tác giả, <code>&lt;p&gt;</code> các đoạn thơ.",
        "required_tags": ["h1","h2","p"],
        "criteria": [
            struct_criteria(2.5),
            {"name":"2. Thẻ nội dung bắt buộc","points":5.5,"checks":[
                {"type":"has_tag","tag":"h1","points":1.5,"label":"Có thẻ <h1> tên bài thơ/bài hát","hint":"Thêm <h1>Tên bài</h1>"},
                {"type":"has_tag","tag":"h2","points":1.5,"label":"Có thẻ <h2> tên tác giả","hint":"Thêm <h2>Tác giả: ...</h2>"},
                {"type":"tag_count","tag":"p","min":2,"points":2.5,"label":"Có ít nhất 2 thẻ <p> đoạn thơ","hint":"Thêm ít nhất 2 <p>Đoạn thơ</p>"},
            ]},
            syntax_criteria(2.0),
        ]
    },
    {
        "id": "f1_apply3", "group": "F1 — Thẻ cơ bản",
        "title": "F1 - Vận dụng 3: Thực đơn nhà hàng",
        "description": "Tạo thực đơn nhà hàng với <code>&lt;h1&gt;</code> tên nhà hàng, <code>&lt;h2&gt;</code> danh mục, <code>&lt;ol&gt;</code> danh sách món ăn có thứ tự.",
        "required_tags": ["h1","h2","ol","li"],
        "criteria": [
            struct_criteria(2.5),
            {"name":"2. Thẻ nội dung bắt buộc","points":5.5,"checks":[
                {"type":"has_tag","tag":"h1","points":1.0,"label":"Có thẻ <h1> tên nhà hàng","hint":"Thêm <h1>Tên nhà hàng</h1>"},
                {"type":"has_tag","tag":"h2","points":1.0,"label":"Có thẻ <h2> danh mục","hint":"Thêm <h2>Danh mục món ăn</h2>"},
                {"type":"has_tag","tag":"ol","points":1.5,"label":"Có thẻ <ol> danh sách có thứ tự","hint":"Thêm <ol>...</ol> cho danh sách món"},
                {"type":"tag_count","tag":"li","min":3,"points":2.0,"label":"Có ít nhất 3 <li> món ăn","hint":"Thêm ít nhất 3 <li>Tên món</li> vào <ol>"},
            ]},
            syntax_criteria(2.0),
        ]
    },
    # F2
    {
        "id": "f2_apply1", "group": "F2 — Liên kết & Hình ảnh",
        "title": "F2 - Vận dụng 1: Trang ảnh du lịch",
        "description": "Tạo trang ảnh du lịch với <code>&lt;h1&gt;</code> tiêu đề, ít nhất 3 <code>&lt;img&gt;</code> có <code>src</code> và <code>alt</code>, <code>&lt;p&gt;</code> mô tả.",
        "required_tags": ["h1","img","p"],
        "criteria": [
            struct_criteria(2.5),
            {"name":"2. Thẻ ảnh bắt buộc","points":5.0,"checks":[
                {"type":"has_tag","tag":"h1","points":0.5,"label":"Có thẻ <h1> tiêu đề","hint":"Thêm <h1>Album du lịch</h1>"},
                {"type":"tag_count","tag":"img","min":3,"points":2.0,"label":"Có ít nhất 3 thẻ <img>","hint":"Thêm ít nhất 3 <img src=\"...\" alt=\"...\">"},
                {"type":"has_attr","tag":"img","attr":"src","points":1.5,"label":"Tất cả <img> có src","hint":"Thêm src=\"đường_dẫn_ảnh\" vào <img>"},
                {"type":"has_attr","tag":"img","attr":"alt","points":1.0,"label":"Tất cả <img> có alt","hint":"Thêm alt=\"mô tả ảnh\" vào <img>"},
            ]},
            {"name":"3. Mô tả ảnh","points":1.0,"checks":[
                {"type":"tag_count","tag":"p","min":2,"points":1.0,"label":"Có ít nhất 2 <p> mô tả","hint":"Thêm <p>Mô tả ảnh</p> dưới mỗi ảnh"},
            ]},
            syntax_criteria(1.5),
        ]
    },
    {
        "id": "f2_apply2", "group": "F2 — Liên kết & Hình ảnh",
        "title": "F2 - Vận dụng 2: Trang liên kết mạng xã hội",
        "description": "Tạo trang liên kết với <code>&lt;h1&gt;</code> tiêu đề, ít nhất 3 <code>&lt;a&gt;</code> có <code>href</code> và <code>target=\"_blank\"</code>.",
        "required_tags": ["h1","a","img"],
        "criteria": [
            struct_criteria(2.5),
            {"name":"2. Thẻ liên kết bắt buộc","points":5.5,"checks":[
                {"type":"has_tag","tag":"h1","points":0.5,"label":"Có thẻ <h1> tiêu đề","hint":"Thêm <h1>Mạng xã hội của tôi</h1>"},
                {"type":"tag_count","tag":"a","min":3,"points":2.0,"label":"Có ít nhất 3 thẻ <a>","hint":"Thêm ít nhất 3 <a href=\"...\">...</a>"},
                {"type":"has_attr","tag":"a","attr":"href","points":1.5,"label":"Tất cả <a> có href","hint":"Thêm href=\"https://...\" vào <a>"},
                {"type":"attr_value","tag":"a","attr":"target","value":"_blank","points":1.5,"label":"<a> có target=\"_blank\"","hint":"Thêm target=\"_blank\" vào <a> để mở tab mới"},
            ]},
            syntax_criteria(2.0),
        ]
    },
    {
        "id": "f2_apply3", "group": "F2 — Liên kết & Hình ảnh",
        "title": "F2 - Vận dụng 3: Trang web có ảnh liên kết",
        "description": "Tạo trang với ảnh bọc trong liên kết: <code>&lt;a href=\"...\"&gt;&lt;img src=\"...\" alt=\"...\"&gt;&lt;/a&gt;</code>.",
        "required_tags": ["a","img"],
        "criteria": [
            struct_criteria(2.5),
            {"name":"2. Ảnh liên kết bắt buộc","points":5.5,"checks":[
                {"type":"has_tag","tag":"a","points":1.5,"label":"Có thẻ <a> liên kết","hint":"Thêm <a href=\"...\">...</a>"},
                {"type":"has_tag","tag":"img","points":1.5,"label":"Có thẻ <img> bên trong <a>","hint":"Đặt <img> bên trong <a>: <a><img></a>"},
                {"type":"has_attr","tag":"a","attr":"href","points":1.5,"label":"<a> có href","hint":"Thêm href=\"https://...\" vào <a>"},
                {"type":"has_attr","tag":"img","attr":"alt","points":1.0,"label":"<img> có alt","hint":"Thêm alt=\"mô tả\" vào <img>"},
            ]},
            syntax_criteria(2.0),
        ]
    },
    # F3
    {
        "id": "f3_apply1", "group": "F3 — Bảng & Bố cục",
        "title": "F3 - Vận dụng 1: Bảng thời khóa biểu",
        "description": "Tạo bảng thời khóa biểu với <code>&lt;table border&gt;</code>, <code>&lt;thead&gt;</code> dùng <code>&lt;th&gt;</code>, ít nhất 5 hàng trong <code>&lt;tbody&gt;</code>.",
        "required_tags": ["table","thead","tbody","tr","th","td"],
        "criteria": [
            struct_criteria(2.0),
            {"name":"2. Cấu trúc bảng","points":5.5,"checks":[
                {"type":"has_tag","tag":"table","points":1.0,"label":"Có thẻ <table>","hint":"Thêm <table>...</table>"},
                {"type":"has_tag","tag":"thead","points":1.0,"label":"Có thẻ <thead> tiêu đề bảng","hint":"Thêm <thead>...</thead> trong <table>"},
                {"type":"has_tag","tag":"tbody","points":1.0,"label":"Có thẻ <tbody> thân bảng","hint":"Thêm <tbody>...</tbody> trong <table>"},
                {"type":"has_tag","tag":"th","points":1.0,"label":"Có thẻ <th> tiêu đề cột","hint":"Dùng <th> trong <thead> thay vì <td>"},
                {"type":"tag_count","tag":"tr","min":6,"points":1.5,"label":"Có ít nhất 6 hàng <tr>","hint":"Thêm ít nhất 5 hàng <tr> vào <tbody>"},
            ]},
            {"name":"3. Thuộc tính bảng","points":1.0,"checks":[
                {"type":"has_attr","tag":"table","attr":"border","points":1.0,"label":"<table> có border","hint":"Thêm border=\"1\" vào <table>"},
            ]},
            syntax_criteria(1.5),
        ]
    },
    {
        "id": "f3_apply2", "group": "F3 — Bảng & Bố cục",
        "title": "F3 - Vận dụng 2: Bố cục trang web (Header-Menu-Nội dung-Footer)",
        "description": "Tạo bố cục trang web với thẻ ngữ nghĩa: <code>&lt;header&gt;</code>, <code>&lt;nav&gt;</code>, <code>&lt;main&gt;</code>, <code>&lt;footer&gt;</code>.",
        "required_tags": ["header","nav","main","footer"],
        "criteria": [
            struct_criteria(2.0),
            {"name":"2. Thẻ ngữ nghĩa bắt buộc","points":6.0,"checks":[
                {"type":"has_tag","tag":"header","points":1.5,"label":"Có thẻ <header>","hint":"Thêm <header>Tiêu đề trang</header>"},
                {"type":"has_tag","tag":"nav","points":1.5,"label":"Có thẻ <nav> menu điều hướng","hint":"Thêm <nav>...</nav> chứa menu"},
                {"type":"has_tag","tag":"main","points":1.5,"label":"Có thẻ <main> nội dung chính","hint":"Thêm <main>Nội dung chính</main>"},
                {"type":"has_tag","tag":"footer","points":1.5,"label":"Có thẻ <footer>","hint":"Thêm <footer>Thông tin cuối trang</footer>"},
            ]},
            syntax_criteria(2.0),
        ]
    },
    {
        "id": "f3_apply3", "group": "F3 — Bảng & Bố cục",
        "title": "F3 - Vận dụng 3: Nhúng video YouTube (iframe)",
        "description": "Nhúng video YouTube bằng <code>&lt;iframe&gt;</code> có <code>src</code> URL YouTube, <code>width</code>, <code>height</code>, <code>allowfullscreen</code>.",
        "required_tags": ["iframe"],
        "criteria": [
            struct_criteria(2.5),
            {"name":"2. Thẻ iframe bắt buộc","points":5.5,"checks":[
                {"type":"has_tag","tag":"iframe","points":2.0,"label":"Có thẻ <iframe>","hint":"Thêm <iframe src=\"...\"></iframe>"},
                {"type":"has_attr","tag":"iframe","attr":"src","points":1.5,"label":"<iframe> có src","hint":"Thêm src=\"https://www.youtube.com/embed/...\" vào <iframe>"},
                {"type":"has_attr","tag":"iframe","attr":"width","points":0.5,"label":"<iframe> có width","hint":"Thêm width=\"560\" vào <iframe>"},
                {"type":"has_attr","tag":"iframe","attr":"height","points":0.5,"label":"<iframe> có height","hint":"Thêm height=\"315\" vào <iframe>"},
                {"type":"has_bool_attr","tag":"iframe","attr":"allowfullscreen","points":1.0,"label":"<iframe> có allowfullscreen","hint":"Thêm allowfullscreen vào <iframe>"},
            ]},
            syntax_criteria(2.0),
        ]
    },
    # F4
    {
        "id": "f4_apply1", "group": "F4 — Đa phương tiện",
        "title": "F4 - Vận dụng 1: Video tự động phát, tắt tiếng",
        "description": "Nhúng video với <code>&lt;video autoplay muted controls&gt;</code> và <code>&lt;source&gt;</code> chỉ định file video.",
        "required_tags": ["video","source"],
        "criteria": [
            struct_criteria(2.0),
            {"name":"2. Thẻ video bắt buộc","points":6.5,"checks":[
                {"type":"has_tag","tag":"video","points":1.5,"label":"Có thẻ <video>","hint":"Thêm <video>...</video>"},
                {"type":"has_tag","tag":"source","points":1.0,"label":"Có <source> bên trong <video>","hint":"Thêm <source src=\"video.mp4\" type=\"video/mp4\"> vào <video>"},
                {"type":"has_bool_attr","tag":"video","attr":"autoplay","points":1.5,"label":"<video> có autoplay","hint":"Thêm autoplay vào <video>"},
                {"type":"has_bool_attr","tag":"video","attr":"muted","points":1.5,"label":"<video> có muted","hint":"Thêm muted vào <video>"},
                {"type":"has_bool_attr","tag":"video","attr":"controls","points":1.0,"label":"<video> có controls","hint":"Thêm controls vào <video>"},
            ]},
            syntax_criteria(1.5),
        ]
    },
    {
        "id": "f4_apply2", "group": "F4 — Đa phương tiện",
        "title": "F4 - Vận dụng 2: Trang nhạc + lời bài hát",
        "description": "Tạo trang nhạc với <code>&lt;audio controls&gt;</code>, <code>&lt;source&gt;</code>, <code>&lt;h2&gt;</code> tên bài và lời trong <code>&lt;p&gt;</code>.",
        "required_tags": ["audio","source","h2"],
        "criteria": [
            struct_criteria(2.0),
            {"name":"2. Thẻ audio bắt buộc","points":5.5,"checks":[
                {"type":"has_tag","tag":"audio","points":2.0,"label":"Có thẻ <audio>","hint":"Thêm <audio>...</audio>"},
                {"type":"has_tag","tag":"source","points":1.0,"label":"Có <source> bên trong <audio>","hint":"Thêm <source src=\"nhac.mp3\" type=\"audio/mpeg\"> vào <audio>"},
                {"type":"has_bool_attr","tag":"audio","attr":"controls","points":1.5,"label":"<audio> có controls","hint":"Thêm controls vào <audio>"},
                {"type":"has_tag","tag":"h2","points":1.0,"label":"Có <h2> tên bài hát","hint":"Thêm <h2>Tên bài hát</h2>"},
            ]},
            {"name":"3. Lời bài hát","points":1.0,"checks":[
                {"type":"tag_count","tag":"p","min":2,"points":1.0,"label":"Có ít nhất 2 <p> lời bài hát","hint":"Thêm <p>Lời bài hát...</p>"},
            ]},
            syntax_criteria(1.5),
        ]
    },
    {
        "id": "f4_apply3", "group": "F4 — Đa phương tiện",
        "title": "F4 - Vận dụng 3: Portfolio hoàn chỉnh (ảnh + video + audio)",
        "description": "Tạo Portfolio với <code>&lt;img alt&gt;</code> ảnh đại diện, <code>&lt;video&gt;</code> giới thiệu, <code>&lt;audio&gt;</code> nhạc nền, <code>&lt;h1&gt;</code> tiêu đề.",
        "required_tags": ["img","video","audio","h1"],
        "criteria": [
            struct_criteria(2.0),
            {"name":"2. Thẻ media đầy đủ","points":6.5,"checks":[
                {"type":"has_tag","tag":"h1","points":0.5,"label":"Có <h1> tiêu đề","hint":"Thêm <h1>Portfolio của tôi</h1>"},
                {"type":"has_tag","tag":"img","points":1.5,"label":"Có <img> ảnh đại diện","hint":"Thêm <img src=\"anh.jpg\" alt=\"Ảnh đại diện\">"},
                {"type":"has_attr","tag":"img","attr":"alt","points":1.0,"label":"<img> có alt","hint":"Thêm alt=\"mô tả ảnh\" vào <img>"},
                {"type":"has_tag","tag":"video","points":2.0,"label":"Có thẻ <video>","hint":"Thêm <video controls>...</video>"},
                {"type":"has_tag","tag":"audio","points":1.5,"label":"Có thẻ <audio>","hint":"Thêm <audio controls>...</audio>"},
            ]},
            syntax_criteria(1.5),
        ]
    },
    # F5
    {
        "id": "f5_apply1", "group": "F5 — Biểu mẫu",
        "title": "F5 - Vận dụng 1: Biểu mẫu tìm kiếm",
        "description": "Tạo form tìm kiếm với <code>&lt;form&gt;</code>, <code>&lt;input type=\"text\"&gt;</code> có <code>placeholder</code>, <code>&lt;button type=\"submit\"&gt;</code>.",
        "required_tags": ["form","input","button"],
        "criteria": [
            struct_criteria(2.0),
            {"name":"2. Thẻ form bắt buộc","points":5.5,"checks":[
                {"type":"has_tag","tag":"form","points":2.0,"label":"Có thẻ <form>","hint":"Thêm <form>...</form>"},
                {"type":"has_tag","tag":"input","points":1.5,"label":"Có thẻ <input>","hint":"Thêm <input type=\"text\" placeholder=\"Tìm kiếm...\">"},
                {"type":"attr_value","tag":"input","attr":"type","value":"text","points":1.0,"label":"<input> có type=\"text\"","hint":"Thêm type=\"text\" vào <input>"},
                {"type":"has_tag","tag":"button","points":1.0,"label":"Có thẻ <button>","hint":"Thêm <button type=\"submit\">Tìm kiếm</button>"},
            ]},
            {"name":"3. Thuộc tính form","points":1.0,"checks":[
                {"type":"has_attr","tag":"input","attr":"placeholder","points":1.0,"label":"<input> có placeholder","hint":"Thêm placeholder=\"Nhập từ khóa...\" vào <input>"},
            ]},
            syntax_criteria(1.5),
        ]
    },
    {
        "id": "f5_apply2", "group": "F5 — Biểu mẫu",
        "title": "F5 - Vận dụng 2: Đăng ký nhận tin (email bắt buộc)",
        "description": "Tạo form đăng ký với <code>&lt;input type=\"email\" required&gt;</code>, <code>&lt;label&gt;</code>, nút submit.",
        "required_tags": ["form","input","label","button"],
        "criteria": [
            struct_criteria(2.0),
            {"name":"2. Thẻ form bắt buộc","points":5.5,"checks":[
                {"type":"has_tag","tag":"form","points":1.5,"label":"Có thẻ <form>","hint":"Thêm <form>...</form>"},
                {"type":"has_tag","tag":"label","points":1.0,"label":"Có thẻ <label>","hint":"Thêm <label for=\"email\">Email:</label>"},
                {"type":"has_tag","tag":"input","points":1.0,"label":"Có thẻ <input>","hint":"Thêm <input type=\"email\" required>"},
                {"type":"attr_value","tag":"input","attr":"type","value":"email","points":1.0,"label":"<input> có type=\"email\"","hint":"Thêm type=\"email\" vào <input>"},
                {"type":"has_bool_attr","tag":"input","attr":"required","points":1.0,"label":"<input> có required","hint":"Thêm required vào <input type=\"email\">"},
            ]},
            {"name":"3. Nút submit","points":1.0,"checks":[
                {"type":"has_tag","tag":"button","points":1.0,"label":"Có nút <button> submit","hint":"Thêm <button type=\"submit\">Đăng ký</button>"},
            ]},
            syntax_criteria(1.5),
        ]
    },
    {
        "id": "f5_apply3", "group": "F5 — Biểu mẫu",
        "title": "F5 - Vận dụng 3: Khảo sát ý kiến",
        "description": "Tạo form khảo sát với <code>&lt;input type=\"radio\"&gt;</code>, <code>&lt;input type=\"checkbox\"&gt;</code>, <code>&lt;textarea&gt;</code> nhận xét.",
        "required_tags": ["form","input","textarea"],
        "criteria": [
            struct_criteria(2.0),
            {"name":"2. Thẻ form bắt buộc","points":6.0,"checks":[
                {"type":"has_tag","tag":"form","points":1.5,"label":"Có thẻ <form>","hint":"Thêm <form>...</form>"},
                {"type":"attr_value","tag":"input","attr":"type","value":"radio","points":1.5,"label":"Có <input type=\"radio\">","hint":"Thêm <input type=\"radio\" name=\"...\" value=\"...\">"},
                {"type":"attr_value","tag":"input","attr":"type","value":"checkbox","points":1.5,"label":"Có <input type=\"checkbox\">","hint":"Thêm <input type=\"checkbox\" name=\"...\" value=\"...\">"},
                {"type":"has_tag","tag":"textarea","points":1.5,"label":"Có <textarea> nhận xét","hint":"Thêm <textarea rows=\"4\">...</textarea>"},
            ]},
            {"name":"3. Nút submit","points":0.5,"checks":[
                {"type":"has_tag","tag":"button","points":0.5,"label":"Có nút submit","hint":"Thêm <button type=\"submit\">Gửi</button>"},
            ]},
            syntax_criteria(1.5),
        ]
    },
    {
        "id": "f5_apply4", "group": "F5 — Biểu mẫu",
        "title": "F5 - Thực hành: Trang đăng nhập hệ thống",
        "description": "Tạo trang đăng nhập với <code>&lt;input type=\"text\"&gt;</code> tên đăng nhập, <code>&lt;input type=\"password\"&gt;</code> mật khẩu, <code>&lt;label&gt;</code>, nút đăng nhập.",
        "required_tags": ["form","input","label","button"],
        "criteria": [
            struct_criteria(2.0),
            {"name":"2. Thẻ form đăng nhập","points":6.0,"checks":[
                {"type":"has_tag","tag":"form","points":1.5,"label":"Có thẻ <form>","hint":"Thêm <form>...</form>"},
                {"type":"has_tag","tag":"label","points":1.0,"label":"Có thẻ <label>","hint":"Thêm <label> cho mỗi input"},
                {"type":"attr_value","tag":"input","attr":"type","value":"text","points":1.5,"label":"Có <input type=\"text\"> tên đăng nhập","hint":"Thêm <input type=\"text\" name=\"username\">"},
                {"type":"attr_value","tag":"input","attr":"type","value":"password","points":1.5,"label":"Có <input type=\"password\"> mật khẩu","hint":"Thêm <input type=\"password\" name=\"password\">"},
                {"type":"has_tag","tag":"button","points":0.5,"label":"Có nút đăng nhập","hint":"Thêm <button type=\"submit\">Đăng nhập</button>"},
            ]},
            {"name":"3. Thuộc tính bảo mật","points":0.5,"checks":[
                {"type":"has_bool_attr","tag":"input","attr":"required","points":0.5,"label":"Input có required","hint":"Thêm required vào các <input>"},
            ]},
            syntax_criteria(1.5),
        ]
    },
    {
        "id": "f5_apply5", "group": "F5 — Biểu mẫu",
        "title": "F5 - Vận dụng: Đăng ký câu lạc bộ",
        "description": "Tạo form đăng ký câu lạc bộ với <code>&lt;select&gt;</code> (ít nhất 3 <code>&lt;option&gt;</code>), <code>&lt;input type=\"email\"&gt;</code>, nút submit.",
        "required_tags": ["form","select","option","input","button"],
        "criteria": [
            struct_criteria(2.0),
            {"name":"2. Thẻ form bắt buộc","points":6.0,"checks":[
                {"type":"has_tag","tag":"form","points":1.5,"label":"Có thẻ <form>","hint":"Thêm <form>...</form>"},
                {"type":"has_tag","tag":"select","points":1.5,"label":"Có <select> chọn câu lạc bộ","hint":"Thêm <select name=\"club\">...</select>"},
                {"type":"tag_count","tag":"option","min":3,"points":1.5,"label":"Có ít nhất 3 <option>","hint":"Thêm ít nhất 3 <option value=\"...\">Tên CLB</option>"},
                {"type":"attr_value","tag":"input","attr":"type","value":"email","points":1.5,"label":"Có <input type=\"email\">","hint":"Thêm <input type=\"email\" required>"},
            ]},
            {"name":"3. Nút submit","points":0.5,"checks":[
                {"type":"has_tag","tag":"button","points":0.5,"label":"Có nút <button> submit","hint":"Thêm <button type=\"submit\">Đăng ký</button>"},
            ]},
            syntax_criteria(1.5),
        ]
    },
    # TỔNG HỢP
    {
        "id": "tong1", "group": "Tổng hợp",
        "title": "Tổng hợp - Vận dụng 1: Hồ sơ cá nhân (F1+F2+F4)",
        "description": "Tạo trang Hồ sơ cá nhân: <code>&lt;h1&gt;</code> tên, <code>&lt;img alt&gt;</code> ảnh đại diện, <code>&lt;ul&gt;</code> sở thích, <code>&lt;a&gt;</code> liên kết, <code>&lt;audio&gt;</code> hoặc <code>&lt;video&gt;</code>.",
        "required_tags": ["h1","img","ul","li","a"],
        "criteria": [
            struct_criteria(2.0),
            {"name":"2. Thẻ nội dung (F1+F2)","points":4.5,"checks":[
                {"type":"has_tag","tag":"h1","points":1.0,"label":"Có <h1> tên cá nhân","hint":"Thêm <h1>Họ và tên</h1>"},
                {"type":"has_tag","tag":"img","points":1.0,"label":"Có <img> ảnh đại diện","hint":"Thêm <img src=\"anh.jpg\" alt=\"Ảnh đại diện\">"},
                {"type":"has_attr","tag":"img","attr":"alt","points":0.5,"label":"<img> có alt","hint":"Thêm alt=\"mô tả\" vào <img>"},
                {"type":"has_tag","tag":"ul","points":0.5,"label":"Có <ul> danh sách sở thích","hint":"Thêm <ul>...</ul>"},
                {"type":"tag_count","tag":"li","min":3,"points":0.5,"label":"Có ít nhất 3 <li>","hint":"Thêm ít nhất 3 <li>Sở thích</li>"},
                {"type":"has_tag","tag":"a","points":1.0,"label":"Có <a> liên kết","hint":"Thêm <a href=\"...\">Liên kết</a>"},
            ]},
            {"name":"3. Media (F4)","points":2.0,"checks":[
                {"type":"has_tag_any","tags":["audio","video"],"points":2.0,"label":"Có <audio> hoặc <video>","hint":"Thêm <audio controls>...</audio> hoặc <video controls>...</video>"},
            ]},
            syntax_criteria(1.5),
        ]
    },
    {
        "id": "tong2", "group": "Tổng hợp",
        "title": "Tổng hợp - Vận dụng 2: Thời khóa biểu phức tạp (F3)",
        "description": "Tạo bảng thời khóa biểu: <code>&lt;table border&gt;</code>, <code>&lt;thead&gt;</code>, ít nhất 5 hàng <code>&lt;tbody&gt;</code>, dùng <code>colspan</code> hoặc <code>rowspan</code>.",
        "required_tags": ["table","thead","tbody","tr","th","td"],
        "criteria": [
            struct_criteria(2.0),
            {"name":"2. Cấu trúc bảng đầy đủ","points":5.0,"checks":[
                {"type":"has_tag","tag":"table","points":1.0,"label":"Có <table>","hint":"Thêm <table border=\"1\">...</table>"},
                {"type":"has_tag","tag":"thead","points":1.0,"label":"Có <thead>","hint":"Thêm <thead>...</thead>"},
                {"type":"has_tag","tag":"tbody","points":1.0,"label":"Có <tbody>","hint":"Thêm <tbody>...</tbody>"},
                {"type":"has_tag","tag":"th","points":1.0,"label":"Có <th> trong thead","hint":"Dùng <th> trong <thead>"},
                {"type":"tag_count","tag":"tr","min":6,"points":1.0,"label":"Có ít nhất 6 hàng <tr>","hint":"Thêm ít nhất 5 hàng dữ liệu vào <tbody>"},
            ]},
            {"name":"3. Thuộc tính nâng cao","points":1.5,"checks":[
                {"type":"has_attr","tag":"table","attr":"border","points":0.5,"label":"<table> có border","hint":"Thêm border=\"1\" vào <table>"},
                {"type":"has_attr_any","tags":["td","th"],"attr":"colspan","points":0.5,"label":"Có colspan","hint":"Thêm colspan vào ô cần gộp cột"},
                {"type":"has_attr_any","tags":["td","th"],"attr":"rowspan","points":0.5,"label":"Có rowspan","hint":"Thêm rowspan vào ô cần gộp hàng"},
            ]},
            syntax_criteria(1.5),
        ]
    },
    {
        "id": "tong3", "group": "Tổng hợp",
        "title": "Tổng hợp - Vận dụng 3: Đăng ký câu lạc bộ đầy đủ (F5)",
        "description": "Tạo form đăng ký đầy đủ: họ tên, email (<code>required</code>), <code>&lt;select&gt;</code> câu lạc bộ, <code>&lt;input type=\"radio\"&gt;</code> giới tính, <code>&lt;textarea&gt;</code> lý do.",
        "required_tags": ["form","input","select","textarea","button"],
        "criteria": [
            struct_criteria(2.0),
            {"name":"2. Thẻ form đầy đủ","points":6.5,"checks":[
                {"type":"has_tag","tag":"form","points":1.0,"label":"Có <form>","hint":"Thêm <form>...</form>"},
                {"type":"attr_value","tag":"input","attr":"type","value":"email","points":1.5,"label":"Có <input type=\"email\">","hint":"Thêm <input type=\"email\" required>"},
                {"type":"has_bool_attr","tag":"input","attr":"required","points":1.0,"label":"Email có required","hint":"Thêm required vào <input type=\"email\">"},
                {"type":"has_tag","tag":"select","points":1.0,"label":"Có <select> câu lạc bộ","hint":"Thêm <select>...</select>"},
                {"type":"attr_value","tag":"input","attr":"type","value":"radio","points":1.0,"label":"Có <input type=\"radio\"> giới tính","hint":"Thêm <input type=\"radio\" name=\"gender\">"},
                {"type":"has_tag","tag":"textarea","points":1.0,"label":"Có <textarea> lý do","hint":"Thêm <textarea>...</textarea>"},
            ]},
            {"name":"3. Nút submit","points":0.0,"checks":[
                {"type":"has_tag","tag":"button","points":0.0,"label":"Có nút <button> submit","hint":"Thêm <button type=\"submit\">Đăng ký</button>"},
            ]},
            syntax_criteria(1.5),
        ]
    },
]

# Validate
errors = []
for ex in EXERCISES:
    total = sum(c['points'] for c in ex['criteria'])
    check_total = sum(ch['points'] for c in ex['criteria'] for ch in c['checks'])
    if abs(total - 10.0) > 0.01:
        errors.append(f"ERROR {ex['id']}: criteria_total={total}")
    if abs(check_total - 10.0) > 0.01:
        errors.append(f"ERROR {ex['id']}: checks_total={check_total}")

if errors:
    for e in errors:
        print(e)
else:
    print(f"OK: All {len(EXERCISES)} exercises validated, total=10.0")
    print(json.dumps(EXERCISES, ensure_ascii=False, separators=(',',':')))
