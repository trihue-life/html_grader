# Changelog — HTML Grader

Tất cả thay đổi đáng chú ý của dự án được ghi lại tại đây.
Định dạng theo [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

---

## [1.2.1] — 2026-02-26
### Added
- Thêm tab **📝 Đề bài** và **📋 Tiêu chí** trên panel trái
- Hiển thị rõ trên mobile dọc và ngang
- Script `bump_version.py` tự động tăng version
- Git pre-commit hook tự động bump patch version khi commit

### Fixed
- Sửa lỗi đề bài và tiêu chí không hiển thị trên mobile landscape
- Cải thiện layout grid cho left-panel

---

## [1.2.0] — 2026-02-26
### Added
- Hệ thống chấm điểm v1.2.0 với 21 bài tập đầy đủ
- Tiêu chí chấm điểm công khai cho từng bài
- Test case chi tiết cho mỗi bài tập
- Báo lỗi chính xác với gợi ý sửa cụ thể
- Nút **▶ Run** để xem preview output HTML
- Responsive mobile (dọc và ngang)
- Badge phiên bản hiển thị trên mobile

---

## [1.1.0] — 2026-02-26
### Added
- Thêm thông tin tác giả: Trí Huệ, trihue.life@gmail.com
- Thêm tham số `--version` cho CLI
- File `html_grader_offline.html` chạy không cần internet
- GitHub Pages: https://trihue-life.github.io/html_grader/

---

## [1.0.0] — 2026-02-26
### Added
- Phiên bản đầu tiên của HTML Grader
- Script `grader.py` chấm điểm HTML từ dòng lệnh
- 22 bài tập HTML từ F1 đến F5
- File `test_cases.json` với dữ liệu bài tập
- README.md hướng dẫn sử dụng
