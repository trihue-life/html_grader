#!/usr/bin/env python3
"""
HTML Grader - Công cụ chấm điểm code HTML tự động
Phân tích HTML code của học sinh và đưa ra điểm số cùng phản hồi chi tiết.
"""

import json
import argparse
import re
import sys

__author__ = "Trí Huệ"
__email__ = "trihue.life@gmail.com"
__version__ = "1.1.0"
from pathlib import Path
from html.parser import HTMLParser
from typing import List, Dict, Tuple, Optional


class HTMLAnalyzer(HTMLParser):
    """Phân tích cấu trúc HTML và trích xuất thông tin."""
    
    def __init__(self):
        super().__init__()
        self.tags_found = set()  # Các thẻ được tìm thấy
        self.tag_stack = []  # Stack để theo dõi thẻ mở/đóng
        self.line_number = 1
        self.tag_positions = {}  # Vị trí (dòng) của các thẻ
        self.errors = []  # Danh sách lỗi phát hiện
        
    def handle_starttag(self, tag, attrs):
        self.tags_found.add(tag.lower())
        self.tag_stack.append(tag.lower())
        if tag.lower() not in self.tag_positions:
            self.tag_positions[tag.lower()] = self.line_number
    
    def handle_endtag(self, tag):
        if self.tag_stack and self.tag_stack[-1] == tag.lower():
            self.tag_stack.pop()
    
    def handle_data(self, data):
        self.line_number += data.count('\n')


class HTMLGrader:
    """Công cụ chấm điểm HTML."""
    
    # Các thẻ tự đóng
    SELF_CLOSING_TAGS = {'img', 'br', 'hr', 'input', 'meta', 'link', 'area', 
                         'base', 'col', 'embed', 'param', 'source', 'track', 'wbr'}
    
    # Thang điểm
    SCORES = {
        'structure': 2.5,      # Cấu trúc HTML chuẩn
        'required': 3.0,       # Thẻ bắt buộc
        'syntax': 2.5,         # Cú pháp thẻ
        'format': 1.0,         # Thụt lề / định dạng
        'attributes': 1.0,     # Thuộc tính hợp lệ
    }
    
    def __init__(self, html_code: str, test_case: Dict):
        self.html_code = html_code
        self.test_case = test_case
        self.lines = html_code.split('\n')
        self.issues = []
        self.scores = {k: 0 for k in self.SCORES.keys()}
        
    def grade(self) -> Tuple[float, Dict, List]:
        """Chấm điểm HTML code và trả về điểm, chi tiết điểm, và danh sách lỗi."""
        
        # 1. Kiểm tra cấu trúc HTML chuẩn
        self._check_structure()
        
        # 2. Kiểm tra thẻ bắt buộc
        self._check_required_tags()
        
        # 3. Kiểm tra cú pháp
        self._check_syntax()
        
        # 4. Kiểm tra định dạng
        self._check_format()
        
        # 5. Kiểm tra thuộc tính
        self._check_attributes()
        
        # Tính tổng điểm
        total_score = sum(self.scores.values())
        
        return total_score, self.scores, self.issues
    
    def _check_structure(self):
        """Kiểm tra cấu trúc HTML chuẩn."""
        code_lower = self.html_code.lower()
        
        checks = [
            (r'<!doctype\s+html', '<!DOCTYPE html>', 0.5),
            (r'<html[\s>].*</html>', '<html>...</html>', 0.5),
            (r'<head[\s>].*</head>', '<head>...</head>', 0.5),
            (r'<title[\s>].*</title>', '<title>...</title>', 0.5),
            (r'<body[\s>].*</body>', '<body>...</body>', 0.5),
        ]
        
        for pattern, tag_name, points in checks:
            if re.search(pattern, code_lower, re.DOTALL | re.IGNORECASE):
                self.scores['structure'] += points
            else:
                self.issues.append({
                    'type': 'error',
                    'line': None,
                    'title': 'Thiếu cấu trúc bắt buộc',
                    'message': f'Thiếu {tag_name} — đây là thành phần cơ bản của trang HTML.',
                    'code': None
                })
    
    def _check_required_tags(self):
        """Kiểm tra các thẻ bắt buộc."""
        required_tags = self.test_case.get('required_tags', [])
        
        if not required_tags:
            self.scores['required'] = self.SCORES['required']
            return
        
        points_per_tag = self.SCORES['required'] / len(required_tags)
        code_lower = self.html_code.lower()
        
        for tag in required_tags:
            tag_lower = tag.lower()
            # Tìm thẻ mở: <tag hoặc <tag>
            pattern = r'<' + re.escape(tag_lower) + r'[\s>/]'
            
            if re.search(pattern, code_lower, re.IGNORECASE):
                self.scores['required'] += points_per_tag
                line_num = self._find_tag_line(tag_lower)
                self.issues.append({
                    'type': 'success',
                    'line': line_num,
                    'title': f'Có thẻ <{tag}>',
                    'message': f'Thẻ <{tag}> được tìm thấy trong code.',
                    'code': None
                })
            else:
                self.issues.append({
                    'type': 'error',
                    'line': None,
                    'title': f'Thiếu thẻ <{tag}>',
                    'message': f'Không tìm thấy thẻ <{tag}>. Yêu cầu bài tập yêu cầu phải có thẻ này.',
                    'code': f'<!-- Ví dụ: <{tag}>...</{tag}> -->'
                })
    
    def _check_syntax(self):
        """Kiểm tra cú pháp thẻ HTML."""
        syntax_errors = 0
        tag_stack = []
        
        for line_num, line in enumerate(self.lines, 1):
            trimmed = line.strip()
            
            # Bỏ qua dòng trống và comment
            if not trimmed or trimmed.startswith('<!--'):
                continue
            
            # Tìm tất cả các thẻ trong dòng
            tag_pattern = r'</?([a-zA-Z][a-zA-Z0-9]*)[^>]*/?>'
            
            for match in re.finditer(tag_pattern, trimmed):
                full_tag = match.group(0)
                tag_name = match.group(1).lower()
                is_closing = full_tag.startswith('</')
                is_self_closing = full_tag.endswith('/>') or tag_name in self.SELF_CLOSING_TAGS
                
                if not is_closing and not is_self_closing:
                    tag_stack.append({'tag': tag_name, 'line': line_num})
                elif is_closing and tag_name not in self.SELF_CLOSING_TAGS:
                    if tag_stack and tag_stack[-1]['tag'] == tag_name:
                        tag_stack.pop()
                    else:
                        # Thẻ đóng không khớp
                        syntax_errors += 1
                        self.issues.append({
                            'type': 'error',
                            'line': line_num,
                            'title': f'Thẻ đóng không khớp </{tag_name}>',
                            'message': f'Dòng {line_num}: Thẻ </{tag_name}> không có thẻ mở tương ứng.',
                            'code': trimmed
                        })
            
            # Kiểm tra dấu nháy không đóng
            quote_count = trimmed.count('"')
            if quote_count % 2 != 0:
                syntax_errors += 1
                self.issues.append({
                    'type': 'error',
                    'line': line_num,
                    'title': 'Dấu nháy chưa đóng',
                    'message': f'Dòng {line_num}: Thuộc tính có dấu nháy " chưa được đóng đúng cách.',
                    'code': trimmed
                })
        
        # Kiểm tra các thẻ chưa đóng
        for tag_info in tag_stack:
            if tag_info['tag'] not in ['html', 'head', 'body']:
                syntax_errors += 1
                self.issues.append({
                    'type': 'error',
                    'line': tag_info['line'],
                    'title': f'Thẻ <{tag_info["tag"]}> chưa đóng',
                    'message': f'Dòng {tag_info["line"]}: Thẻ <{tag_info["tag"]}> mở nhưng không có thẻ đóng </{tag_info["tag"]}>.',
                    'code': None
                })
        
        # Kiểm tra xem có nội dung HTML thực sự không
        has_html_content = len(re.findall(r'<[a-zA-Z][a-zA-Z0-9]*[\s>/]', self.html_code)) > 0
        
        if has_html_content:
            self.scores['syntax'] = max(0, self.SCORES['syntax'] - syntax_errors * 0.5)
        else:
            self.scores['syntax'] = 0
    
    def _check_format(self):
        """Kiểm tra định dạng và thụt lề."""
        has_html_content = len(re.findall(r'<[a-zA-Z][a-zA-Z0-9]*[\s>/]', self.html_code)) > 0
        
        if not has_html_content:
            self.scores['format'] = 0
            return
        
        format_ok = True
        
        # Kiểm tra độ dài dòng
        for line_num, line in enumerate(self.lines, 1):
            if line.strip() and len(line) > 200:
                format_ok = False
                self.issues.append({
                    'type': 'info',
                    'line': line_num,
                    'title': 'Dòng quá dài',
                    'message': f'Dòng {line_num}: Dòng dài {len(line)} ký tự. Nên xuống dòng để dễ đọc.',
                    'code': None
                })
        
        # Kiểm tra thụt lề
        has_indent = any(line.startswith('  ') or line.startswith('\t') for line in self.lines)
        if not has_indent and len(self.lines) > 5:
            format_ok = False
            self.issues.append({
                'type': 'info',
                'line': None,
                'title': 'Không có thụt lề',
                'message': 'Code không có thụt lề (indent). Nên thụt lề các thẻ lồng nhau để dễ đọc hơn.',
                'code': None
            })
        
        self.scores['format'] = self.SCORES['format'] if format_ok else self.SCORES['format'] * 0.5
    
    def _check_attributes(self):
        """Kiểm tra thuộc tính HTML."""
        has_html_content = len(re.findall(r'<[a-zA-Z][a-zA-Z0-9]*[\s>/]', self.html_code)) > 0
        
        if not has_html_content:
            self.scores['attributes'] = 0
            return
        
        attr_score = self.SCORES['attributes']
        
        # Kiểm tra thẻ <img>
        img_tags = re.findall(r'<img[^>]*>', self.html_code, re.IGNORECASE)
        for img_tag in img_tags:
            if not re.search(r'\balt\s*=', img_tag, re.IGNORECASE):
                attr_score -= 0.25
                line_num = self._find_line_of_text(img_tag)
                self.issues.append({
                    'type': 'warning',
                    'line': line_num,
                    'title': 'Thẻ <img> thiếu thuộc tính alt',
                    'message': 'Thẻ <img> cần có thuộc tính alt="" để mô tả hình ảnh (tốt cho SEO và accessibility).',
                    'code': img_tag
                })
            
            if not re.search(r'\bsrc\s*=', img_tag, re.IGNORECASE):
                attr_score -= 0.25
                line_num = self._find_line_of_text(img_tag)
                self.issues.append({
                    'type': 'error',
                    'line': line_num,
                    'title': 'Thẻ <img> thiếu thuộc tính src',
                    'message': 'Thẻ <img> phải có thuộc tính src="đường_dẫn_ảnh".',
                    'code': img_tag
                })
        
        # Kiểm tra thẻ <a>
        a_tags = re.findall(r'<a[^>]*>', self.html_code, re.IGNORECASE)
        for a_tag in a_tags:
            if not re.search(r'\bhref\s*=', a_tag, re.IGNORECASE):
                attr_score -= 0.2
                line_num = self._find_line_of_text(a_tag)
                self.issues.append({
                    'type': 'warning',
                    'line': line_num,
                    'title': 'Thẻ <a> thiếu thuộc tính href',
                    'message': 'Thẻ <a> nên có thuộc tính href="" để chỉ định liên kết.',
                    'code': a_tag
                })
        
        self.scores['attributes'] = max(0, attr_score)
    
    def _find_tag_line(self, tag_name: str) -> Optional[int]:
        """Tìm số dòng của thẻ."""
        pattern = r'<' + re.escape(tag_name) + r'[\s>/]'
        for line_num, line in enumerate(self.lines, 1):
            if re.search(pattern, line, re.IGNORECASE):
                return line_num
        return None
    
    def _find_line_of_text(self, text: str) -> Optional[int]:
        """Tìm số dòng chứa text."""
        for line_num, line in enumerate(self.lines, 1):
            if text in line:
                return line_num
        return None


def load_test_cases(test_cases_file: str) -> Dict:
    """Tải dữ liệu bài tập từ file JSON."""
    with open(test_cases_file, 'r', encoding='utf-8') as f:
        test_cases_list = json.load(f)
    
    return {tc['id']: tc for tc in test_cases_list}


def format_output(total_score: float, scores: Dict, issues: List, exercise_title: str):
    """In kết quả chấm điểm ra màn hình."""
    
    print("\n" + "="*70)
    print(f"  HTML GRADER - KẾT QUẢ CHẤM ĐIỂM")
    print("="*70)
    print(f"\n📝 Bài tập: {exercise_title}")
    print(f"\n{'─'*70}")
    
    # Tổng điểm
    if total_score >= 8.5:
        emoji = "🏆"
        label = "Xuất sắc!"
    elif total_score >= 7.0:
        emoji = "👍"
        label = "Khá tốt"
    elif total_score >= 5.0:
        emoji = "⚠️"
        label = "Trung bình"
    else:
        emoji = "❌"
        label = "Cần cải thiện"
    
    print(f"\n{emoji} TỔNG ĐIỂM: {total_score:.1f}/10 ({label})")
    print(f"\n{'─'*70}")
    
    # Chi tiết điểm
    print("\n📊 CHI TIẾT ĐIỂM:")
    print(f"  • Cấu trúc HTML:      {scores['structure']:.1f}/2.5")
    print(f"  • Thẻ bắt buộc:       {scores['required']:.1f}/3.0")
    print(f"  • Cú pháp thẻ:        {scores['syntax']:.1f}/2.5")
    print(f"  • Định dạng:          {scores['format']:.1f}/1.0")
    print(f"  • Thuộc tính:         {scores['attributes']:.1f}/1.0")
    
    # Lỗi và cảnh báo
    errors = [i for i in issues if i['type'] == 'error']
    warnings = [i for i in issues if i['type'] == 'warning']
    infos = [i for i in issues if i['type'] == 'info']
    success = [i for i in issues if i['type'] == 'success']
    
    print(f"\n{'─'*70}")
    print(f"\n📋 PHÂN TÍCH:")
    print(f"  • ✕ Lỗi:        {len(errors)}")
    print(f"  • ⚠ Cảnh báo:    {len(warnings)}")
    print(f"  • ℹ Gợi ý:      {len(infos)}")
    print(f"  • ✓ Đúng:       {len(success)}")
    
    if errors or warnings or infos:
        print(f"\n{'─'*70}")
        print("\n🔍 CHI TIẾT LỖI & CẢNH BÁO:\n")
        
        # Sắp xếp theo loại và dòng
        sorted_issues = sorted(
            [i for i in issues if i['type'] != 'success'],
            key=lambda x: (x['type'] != 'error', x['line'] or 999)
        )
        
        for issue in sorted_issues:
            type_emoji = {'error': '✕', 'warning': '⚠', 'info': 'ℹ'}[issue['type']]
            line_info = f"(Dòng {issue['line']})" if issue['line'] else "(Toàn bộ file)"
            
            print(f"{type_emoji} {issue['title']} {line_info}")
            print(f"   {issue['message']}")
            if issue['code']:
                print(f"   Code: {issue['code']}")
            print()
    
    print("="*70 + "\n")


def main():
    parser = argparse.ArgumentParser(
        description='HTML Grader - Công cụ chấm điểm code HTML tự động',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ví dụ sử dụng:
  python3 grader.py student_code/exercise1.html --exercise f1_apply1
  python3 grader.py code.html --exercise f2_apply2 --test-cases test_cases.json
        """
    )
    
    parser.add_argument('html_file', help='Đường dẫn đến file HTML cần chấm')
    parser.add_argument('--exercise', '-e', required=True, help='ID của bài tập (vd: f1_apply1)')
    parser.add_argument('--test-cases', '-t', default='test_cases.json', 
                       help='Đường dẫn đến file test_cases.json (mặc định: test_cases.json)')
    parser.add_argument('--json', '-j', action='store_true', help='In kết quả dưới dạng JSON')
    parser.add_argument('--version', '-v', action='version', version=f'%(prog)s {__version__}')
    
    args = parser.parse_args()
    
    # Kiểm tra file HTML
    if not Path(args.html_file).exists():
        print(f"❌ Lỗi: File '{args.html_file}' không tồn tại.", file=sys.stderr)
        sys.exit(1)
    
    # Kiểm tra file test_cases.json
    if not Path(args.test_cases).exists():
        print(f"❌ Lỗi: File '{args.test_cases}' không tồn tại.", file=sys.stderr)
        sys.exit(1)
    
    # Đọc HTML code
    with open(args.html_file, 'r', encoding='utf-8') as f:
        html_code = f.read()
    
    # Tải test cases
    test_cases = load_test_cases(args.test_cases)
    
    if args.exercise not in test_cases:
        print(f"❌ Lỗi: Bài tập '{args.exercise}' không tồn tại trong test_cases.json", file=sys.stderr)
        print(f"   Các bài tập có sẵn: {', '.join(test_cases.keys())}", file=sys.stderr)
        sys.exit(1)
    
    test_case = test_cases[args.exercise]
    
    # Chấm điểm
    grader = HTMLGrader(html_code, test_case)
    total_score, scores, issues = grader.grade()
    
    # In kết quả
    if args.json:
        result = {
            'exercise_id': args.exercise,
            'exercise_title': test_case['title'],
            'total_score': total_score,
            'scores': scores,
            'issues': issues
        }
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        format_output(total_score, scores, issues, test_case['title'])


if __name__ == '__main__':
    main()
