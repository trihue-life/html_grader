#!/usr/bin/env python3
"""
HTML Grader Web App - Giao diện web để chấm điểm code HTML
Tác giả: Trí Huệ
Email: trihue.life@gmail.com
Version: 1.1.0
"""

from flask import Flask, request, jsonify, render_template_string
import json
import re
import sys
from pathlib import Path

app = Flask(__name__)

__author__ = "Trí Huệ"
__email__ = "trihue.life@gmail.com"
__version__ = "1.1.0"

# Load test cases
def load_test_cases():
    with open(Path(__file__).parent / 'test_cases.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    return {tc['id']: tc for tc in data}, data

TEST_CASES_DICT, TEST_CASES_LIST = load_test_cases()

# ─── Grader Logic ────────────────────────────────────────────────────────────

SELF_CLOSING_TAGS = {'img','br','hr','input','meta','link','area','base','col',
                     'embed','param','source','track','wbr'}

SCORES_MAX = {'structure': 2.5, 'required': 3.0, 'syntax': 2.5, 'format': 1.0, 'attributes': 1.0}

def grade_html(html_code, test_case):
    lines = html_code.split('\n')
    issues = []
    scores = {k: 0.0 for k in SCORES_MAX}

    # 1. Cấu trúc
    code_lower = html_code.lower()
    structure_checks = [
        (r'<!doctype\s+html', '<!DOCTYPE html>', 0.5),
        (r'<html[\s>].*</html>', '<html>...</html>', 0.5),
        (r'<head[\s>].*</head>', '<head>...</head>', 0.5),
        (r'<title[\s>].*</title>', '<title>...</title>', 0.5),
        (r'<body[\s>].*</body>', '<body>...</body>', 0.5),
    ]
    for pattern, tag_name, pts in structure_checks:
        if re.search(pattern, code_lower, re.DOTALL | re.IGNORECASE):
            scores['structure'] += pts
        else:
            issues.append({'type':'error','title':f'Thiếu {tag_name}',
                           'message':f'Thiếu {tag_name} — thành phần cơ bản của trang HTML.','line':None})

    # 2. Thẻ bắt buộc
    required_tags = test_case.get('required_tags', [])
    if not required_tags:
        scores['required'] = SCORES_MAX['required']
    else:
        pts_per = SCORES_MAX['required'] / len(required_tags)
        for tag in required_tags:
            pattern = r'<' + re.escape(tag.lower()) + r'[\s>/]'
            if re.search(pattern, code_lower, re.IGNORECASE):
                scores['required'] += pts_per
                line_num = next((i+1 for i,l in enumerate(lines) if re.search(pattern, l, re.IGNORECASE)), None)
                issues.append({'type':'success','title':f'Có thẻ <{tag}>',
                               'message':f'Thẻ <{tag}> được tìm thấy.','line':line_num})
            else:
                issues.append({'type':'error','title':f'Thiếu thẻ <{tag}>',
                               'message':f'Không tìm thấy <{tag}>. Bài tập yêu cầu thẻ này.','line':None})

    # 3. Cú pháp
    syntax_errors = 0
    tag_stack = []
    for i, line in enumerate(lines, 1):
        trimmed = line.strip()
        if not trimmed or trimmed.startswith('<!--'): continue
        for match in re.finditer(r'</?([a-zA-Z][a-zA-Z0-9]*)[^>]*/?>', trimmed):
            full_tag = match.group(0)
            tag_name = match.group(1).lower()
            is_closing = full_tag.startswith('</')
            is_self = full_tag.endswith('/>') or tag_name in SELF_CLOSING_TAGS
            if not is_closing and not is_self:
                tag_stack.append({'tag': tag_name, 'line': i})
            elif is_closing and tag_name not in SELF_CLOSING_TAGS:
                if tag_stack and tag_stack[-1]['tag'] == tag_name:
                    tag_stack.pop()
                else:
                    syntax_errors += 1
                    issues.append({'type':'error','title':f'Thẻ đóng không khớp </{tag_name}>',
                                   'message':f'Dòng {i}: </{tag_name}> không có thẻ mở tương ứng.','line':i})
        if trimmed.count('"') % 2 != 0:
            syntax_errors += 1
            issues.append({'type':'error','title':'Dấu nháy chưa đóng',
                           'message':f'Dòng {i}: Dấu nháy " chưa đóng đúng.','line':i})
    for ti in tag_stack:
        if ti['tag'] not in ['html','head','body']:
            syntax_errors += 1
            issues.append({'type':'error','title':f'Thẻ <{ti["tag"]}> chưa đóng',
                           'message':f'Dòng {ti["line"]}: <{ti["tag"]}> mở nhưng không có thẻ đóng.','line':ti['line']})
    has_html = bool(re.findall(r'<[a-zA-Z][a-zA-Z0-9]*[\s>/]', html_code))
    scores['syntax'] = max(0, SCORES_MAX['syntax'] - syntax_errors * 0.5) if has_html else 0

    # 4. Định dạng
    if not has_html:
        scores['format'] = 0
    else:
        fmt_ok = True
        for i, line in enumerate(lines, 1):
            if line.strip() and len(line) > 200:
                fmt_ok = False
                issues.append({'type':'info','title':'Dòng quá dài',
                               'message':f'Dòng {i}: {len(line)} ký tự. Nên xuống dòng.','line':i})
        has_indent = any(l.startswith('  ') or l.startswith('\t') for l in lines)
        if not has_indent and len(lines) > 5:
            fmt_ok = False
            issues.append({'type':'info','title':'Không có thụt lề',
                           'message':'Code không có thụt lề. Nên indent các thẻ lồng nhau.','line':None})
        scores['format'] = SCORES_MAX['format'] if fmt_ok else SCORES_MAX['format'] * 0.5

    # 5. Thuộc tính
    if not has_html:
        scores['attributes'] = 0
    else:
        attr_score = SCORES_MAX['attributes']
        for img in re.findall(r'<img[^>]*>', html_code, re.IGNORECASE):
            if not re.search(r'\balt\s*=', img, re.IGNORECASE):
                attr_score -= 0.25
                issues.append({'type':'warning','title':'<img> thiếu alt',
                               'message':'Thẻ <img> cần thuộc tính alt="" (tốt cho SEO).','line':None})
            if not re.search(r'\bsrc\s*=', img, re.IGNORECASE):
                attr_score -= 0.25
                issues.append({'type':'error','title':'<img> thiếu src',
                               'message':'Thẻ <img> phải có src="đường_dẫn_ảnh".','line':None})
        for a in re.findall(r'<a[^>]*>', html_code, re.IGNORECASE):
            if not re.search(r'\bhref\s*=', a, re.IGNORECASE):
                attr_score -= 0.2
                issues.append({'type':'warning','title':'<a> thiếu href',
                               'message':'Thẻ <a> nên có href="" để chỉ định liên kết.','line':None})
        scores['attributes'] = max(0, attr_score)

    total = round(sum(scores.values()), 1)
    return total, scores, issues


# ─── HTML Template ────────────────────────────────────────────────────────────

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>HTML Grader v{{ version }}</title>
  <style>
    :root {
      --bg: #0f1117;
      --surface: #1a1d27;
      --surface2: #22263a;
      --border: #2e3250;
      --accent: #6c63ff;
      --accent2: #a78bfa;
      --green: #22c55e;
      --red: #ef4444;
      --yellow: #f59e0b;
      --blue: #3b82f6;
      --text: #e2e8f0;
      --muted: #94a3b8;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body { background: var(--bg); color: var(--text); font-family: 'Segoe UI', system-ui, sans-serif; min-height: 100vh; }

    /* Header */
    header {
      background: linear-gradient(135deg, #1e1b4b 0%, #312e81 50%, #1e1b4b 100%);
      border-bottom: 1px solid var(--border);
      padding: 20px 32px;
      display: flex; align-items: center; justify-content: space-between;
    }
    .logo { display: flex; align-items: center; gap: 12px; }
    .logo-icon { font-size: 32px; }
    .logo-text h1 { font-size: 22px; font-weight: 700; color: #fff; }
    .logo-text p { font-size: 12px; color: var(--accent2); }
    .version-badge {
      background: var(--accent); color: #fff; padding: 4px 12px;
      border-radius: 20px; font-size: 12px; font-weight: 600;
    }

    /* Layout */
    .container { display: grid; grid-template-columns: 1fr 1fr; gap: 0; height: calc(100vh - 73px); }

    /* Left Panel */
    .left-panel { display: flex; flex-direction: column; border-right: 1px solid var(--border); }
    .panel-header {
      background: var(--surface); padding: 16px 20px;
      border-bottom: 1px solid var(--border);
      display: flex; align-items: center; gap: 12px; flex-wrap: wrap;
    }
    .panel-header h2 { font-size: 14px; font-weight: 600; color: var(--text); flex: 1; }

    select {
      background: var(--surface2); border: 1px solid var(--border);
      color: var(--text); padding: 8px 12px; border-radius: 8px;
      font-size: 13px; cursor: pointer; outline: none; flex: 1; min-width: 200px;
    }
    select:focus { border-color: var(--accent); }

    .exercise-desc {
      background: var(--surface2); border-bottom: 1px solid var(--border);
      padding: 12px 20px; font-size: 12px; color: var(--muted); line-height: 1.6;
      max-height: 80px; overflow-y: auto;
    }

    textarea {
      flex: 1; background: #0d1117; color: #e6edf3;
      border: none; padding: 16px 20px; font-family: 'Cascadia Code', 'Fira Code', monospace;
      font-size: 13px; line-height: 1.7; resize: none; outline: none;
      tab-size: 2;
    }
    textarea::placeholder { color: #3d4451; }

    .action-bar {
      background: var(--surface); border-top: 1px solid var(--border);
      padding: 12px 20px; display: flex; gap: 10px; align-items: center;
    }
    .btn-grade {
      background: linear-gradient(135deg, var(--accent), #8b5cf6);
      color: #fff; border: none; padding: 10px 28px;
      border-radius: 8px; font-size: 14px; font-weight: 600;
      cursor: pointer; transition: all 0.2s; flex: 1;
    }
    .btn-grade:hover { transform: translateY(-1px); box-shadow: 0 4px 20px rgba(108,99,255,0.4); }
    .btn-grade:active { transform: translateY(0); }
    .btn-clear {
      background: var(--surface2); color: var(--muted); border: 1px solid var(--border);
      padding: 10px 16px; border-radius: 8px; font-size: 13px; cursor: pointer;
    }
    .btn-clear:hover { color: var(--text); border-color: var(--muted); }

    /* Right Panel */
    .right-panel { display: flex; flex-direction: column; overflow-y: auto; }
    .result-placeholder {
      flex: 1; display: flex; flex-direction: column;
      align-items: center; justify-content: center; gap: 16px; color: var(--muted);
    }
    .result-placeholder .icon { font-size: 64px; opacity: 0.3; }
    .result-placeholder p { font-size: 14px; }

    /* Score Card */
    .score-card { padding: 24px; }
    .score-header { text-align: center; margin-bottom: 24px; }
    .score-circle {
      width: 120px; height: 120px; border-radius: 50%;
      display: flex; flex-direction: column; align-items: center; justify-content: center;
      margin: 0 auto 16px; border: 4px solid;
      background: var(--surface2);
    }
    .score-circle .score-num { font-size: 32px; font-weight: 800; }
    .score-circle .score-denom { font-size: 13px; color: var(--muted); }
    .score-label { font-size: 18px; font-weight: 700; margin-bottom: 4px; }
    .score-exercise { font-size: 12px; color: var(--muted); }

    /* Score Bars */
    .score-bars { margin-bottom: 20px; }
    .score-bar-item { margin-bottom: 12px; }
    .score-bar-label { display: flex; justify-content: space-between; font-size: 12px; margin-bottom: 4px; }
    .score-bar-label span:first-child { color: var(--muted); }
    .score-bar-label span:last-child { font-weight: 600; }
    .score-bar-track { background: var(--surface2); border-radius: 4px; height: 8px; overflow: hidden; }
    .score-bar-fill { height: 100%; border-radius: 4px; transition: width 0.6s ease; }

    /* Stats */
    .stats-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 8px; margin-bottom: 20px; }
    .stat-card { background: var(--surface2); border-radius: 10px; padding: 12px; text-align: center; border: 1px solid var(--border); }
    .stat-card .stat-num { font-size: 22px; font-weight: 700; }
    .stat-card .stat-label { font-size: 10px; color: var(--muted); margin-top: 2px; }

    /* Issues */
    .issues-section h3 { font-size: 13px; font-weight: 600; color: var(--muted); margin-bottom: 12px; text-transform: uppercase; letter-spacing: 0.5px; }
    .issue-item {
      background: var(--surface2); border-radius: 8px; padding: 10px 14px;
      margin-bottom: 8px; border-left: 3px solid; display: flex; gap: 10px;
    }
    .issue-icon { font-size: 14px; flex-shrink: 0; margin-top: 1px; }
    .issue-content .issue-title { font-size: 13px; font-weight: 600; margin-bottom: 2px; }
    .issue-content .issue-msg { font-size: 12px; color: var(--muted); line-height: 1.5; }
    .issue-content .issue-line { font-size: 11px; color: var(--accent2); margin-top: 2px; }

    .issue-error { border-color: var(--red); }
    .issue-warning { border-color: var(--yellow); }
    .issue-info { border-color: var(--blue); }
    .issue-success { border-color: var(--green); }

    /* Loading */
    .loading { display: none; text-align: center; padding: 40px; }
    .spinner { width: 40px; height: 40px; border: 3px solid var(--border); border-top-color: var(--accent); border-radius: 50%; animation: spin 0.8s linear infinite; margin: 0 auto 12px; }
    @keyframes spin { to { transform: rotate(360deg); } }

    /* Footer */
    .footer-info {
      background: var(--surface); border-top: 1px solid var(--border);
      padding: 10px 20px; font-size: 11px; color: var(--muted); text-align: center;
    }
    .footer-info a { color: var(--accent2); text-decoration: none; }

    /* Responsive */
    @media (max-width: 768px) {
      .container { grid-template-columns: 1fr; height: auto; }
      .left-panel { height: 60vh; }
    }
  </style>
</head>
<body>

<header>
  <div class="logo">
    <div class="logo-icon">🏷️</div>
    <div class="logo-text">
      <h1>HTML Grader</h1>
      <p>Công cụ chấm điểm code HTML tự động</p>
    </div>
  </div>
  <span class="version-badge">v{{ version }}</span>
</header>

<div class="container">
  <!-- Left: Editor -->
  <div class="left-panel">
    <div class="panel-header">
      <h2>📝 Chọn bài tập</h2>
      <select id="exerciseSelect" onchange="onExerciseChange()">
        {% for group_name, exercises in groups.items() %}
        <optgroup label="{{ group_name }}">
          {% for ex in exercises %}
          <option value="{{ ex.id }}">{{ ex.title }}</option>
          {% endfor %}
        </optgroup>
        {% endfor %}
      </select>
    </div>
    <div class="exercise-desc" id="exerciseDesc">Chọn bài tập để xem mô tả...</div>
    <textarea id="htmlCode" placeholder="Nhập code HTML của bạn vào đây...&#10;&#10;Ví dụ:&#10;&lt;!DOCTYPE html&gt;&#10;&lt;html&gt;&#10;  &lt;head&gt;&#10;    &lt;title&gt;Trang của tôi&lt;/title&gt;&#10;  &lt;/head&gt;&#10;  &lt;body&gt;&#10;    &lt;h1&gt;Xin chào!&lt;/h1&gt;&#10;  &lt;/body&gt;&#10;&lt;/html&gt;"></textarea>
    <div class="action-bar">
      <button class="btn-grade" onclick="gradeCode()">⚡ Chấm điểm</button>
      <button class="btn-clear" onclick="clearCode()">🗑 Xóa</button>
    </div>
  </div>

  <!-- Right: Results -->
  <div class="right-panel" id="rightPanel">
    <div class="result-placeholder" id="placeholder">
      <div class="icon">📊</div>
      <p>Nhập code HTML và nhấn <strong>Chấm điểm</strong></p>
    </div>
    <div class="loading" id="loading">
      <div class="spinner"></div>
      <p style="color:var(--muted);font-size:13px">Đang chấm điểm...</p>
    </div>
    <div id="resultArea" style="display:none"></div>
    <div class="footer-info">
      Tác giả: <strong>Trí Huệ</strong> &nbsp;|&nbsp;
      <a href="mailto:trihue.life@gmail.com">trihue.life@gmail.com</a> &nbsp;|&nbsp;
      <a href="https://github.com/TriHue-life/html_grader" target="_blank">GitHub</a>
    </div>
  </div>
</div>

<script>
const exercises = {{ exercises_json | safe }};
const exerciseMap = {};
exercises.forEach(e => exerciseMap[e.id] = e);

function onExerciseChange() {
  const id = document.getElementById('exerciseSelect').value;
  const ex = exerciseMap[id];
  if (ex) {
    document.getElementById('exerciseDesc').textContent = ex.description || 'Không có mô tả.';
    if (ex.initial_code) {
      document.getElementById('htmlCode').value = ex.initial_code;
    }
  }
}

function clearCode() {
  document.getElementById('htmlCode').value = '';
  document.getElementById('resultArea').style.display = 'none';
  document.getElementById('placeholder').style.display = 'flex';
}

async function gradeCode() {
  const code = document.getElementById('htmlCode').value.trim();
  const exerciseId = document.getElementById('exerciseSelect').value;
  if (!code) { alert('Vui lòng nhập code HTML!'); return; }

  document.getElementById('placeholder').style.display = 'none';
  document.getElementById('resultArea').style.display = 'none';
  document.getElementById('loading').style.display = 'block';

  try {
    const resp = await fetch('/grade', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({html_code: code, exercise_id: exerciseId})
    });
    const data = await resp.json();
    renderResult(data);
  } catch(e) {
    alert('Lỗi kết nối server!');
  } finally {
    document.getElementById('loading').style.display = 'none';
  }
}

function renderResult(data) {
  const { total_score, scores, issues, exercise_title } = data;

  const scoreColor = total_score >= 8.5 ? '#22c55e' : total_score >= 7 ? '#a78bfa' : total_score >= 5 ? '#f59e0b' : '#ef4444';
  const scoreLabel = total_score >= 8.5 ? '🏆 Xuất sắc!' : total_score >= 7 ? '👍 Khá tốt' : total_score >= 5 ? '⚠️ Trung bình' : '❌ Cần cải thiện';

  const errors = issues.filter(i => i.type === 'error');
  const warnings = issues.filter(i => i.type === 'warning');
  const infos = issues.filter(i => i.type === 'info');
  const successes = issues.filter(i => i.type === 'success');

  const barColor = (score, max) => {
    const pct = score / max;
    return pct >= 0.8 ? '#22c55e' : pct >= 0.5 ? '#f59e0b' : '#ef4444';
  };

  const renderIssues = (list) => list.map(issue => {
    const icons = {error:'✕', warning:'⚠', info:'ℹ', success:'✓'};
    const lineInfo = issue.line ? `<div class="issue-line">Dòng ${issue.line}</div>` : '';
    return `<div class="issue-item issue-${issue.type}">
      <div class="issue-icon">${icons[issue.type]}</div>
      <div class="issue-content">
        <div class="issue-title">${issue.title}</div>
        <div class="issue-msg">${issue.message}</div>
        ${lineInfo}
      </div>
    </div>`;
  }).join('');

  const nonSuccessIssues = issues.filter(i => i.type !== 'success');

  document.getElementById('resultArea').innerHTML = `
    <div class="score-card">
      <div class="score-header">
        <div class="score-circle" style="border-color:${scoreColor}">
          <span class="score-num" style="color:${scoreColor}">${total_score.toFixed(1)}</span>
          <span class="score-denom">/10</span>
        </div>
        <div class="score-label" style="color:${scoreColor}">${scoreLabel}</div>
        <div class="score-exercise">${exercise_title}</div>
      </div>

      <div class="score-bars">
        ${[
          ['Cấu trúc HTML', scores.structure, 2.5],
          ['Thẻ bắt buộc', scores.required, 3.0],
          ['Cú pháp thẻ', scores.syntax, 2.5],
          ['Định dạng', scores.format, 1.0],
          ['Thuộc tính', scores.attributes, 1.0],
        ].map(([label, score, max]) => `
          <div class="score-bar-item">
            <div class="score-bar-label">
              <span>${label}</span>
              <span style="color:${barColor(score,max)}">${score.toFixed(1)}/${max}</span>
            </div>
            <div class="score-bar-track">
              <div class="score-bar-fill" style="width:${(score/max*100).toFixed(0)}%;background:${barColor(score,max)}"></div>
            </div>
          </div>
        `).join('')}
      </div>

      <div class="stats-grid">
        <div class="stat-card">
          <div class="stat-num" style="color:#ef4444">${errors.length}</div>
          <div class="stat-label">Lỗi</div>
        </div>
        <div class="stat-card">
          <div class="stat-num" style="color:#f59e0b">${warnings.length}</div>
          <div class="stat-label">Cảnh báo</div>
        </div>
        <div class="stat-card">
          <div class="stat-num" style="color:#3b82f6">${infos.length}</div>
          <div class="stat-label">Gợi ý</div>
        </div>
        <div class="stat-card">
          <div class="stat-num" style="color:#22c55e">${successes.length}</div>
          <div class="stat-label">Đúng</div>
        </div>
      </div>

      ${nonSuccessIssues.length > 0 ? `
        <div class="issues-section">
          <h3>Chi tiết lỗi & cảnh báo</h3>
          ${renderIssues(nonSuccessIssues)}
        </div>
      ` : '<div style="text-align:center;color:#22c55e;padding:20px;font-size:14px">✅ Không có lỗi nào!</div>'}
    </div>
  `;
  document.getElementById('resultArea').style.display = 'block';
}

// Init
onExerciseChange();

// Tab key in textarea
document.getElementById('htmlCode').addEventListener('keydown', function(e) {
  if (e.key === 'Tab') {
    e.preventDefault();
    const start = this.selectionStart;
    const end = this.selectionEnd;
    this.value = this.value.substring(0, start) + '  ' + this.value.substring(end);
    this.selectionStart = this.selectionEnd = start + 2;
  }
});
</script>
</body>
</html>
"""

# ─── Routes ──────────────────────────────────────────────────────────────────

def group_exercises(exercises):
    groups = {}
    for ex in exercises:
        eid = ex['id']
        if eid.startswith('f1'): g = 'BÀI F1: HTML và Trang Web'
        elif eid.startswith('f2'): g = 'BÀI F2: Tạo và Định dạng'
        elif eid.startswith('f3'): g = 'BÀI F3: Bảng và Khung'
        elif eid.startswith('f4'): g = 'BÀI F4: Đa Phương Tiện'
        elif eid.startswith('f5'): g = 'BÀI F5: Biểu Mẫu'
        else: g = 'Bộ Tổng Hợp (F1–F5)'
        groups.setdefault(g, []).append(ex)
    return groups

@app.route('/')
def index():
    groups = group_exercises(TEST_CASES_LIST)
    return render_template_string(
        HTML_TEMPLATE,
        version=__version__,
        groups=groups,
        exercises_json=json.dumps(TEST_CASES_LIST, ensure_ascii=False)
    )

@app.route('/grade', methods=['POST'])
def grade():
    data = request.get_json()
    html_code = data.get('html_code', '')
    exercise_id = data.get('exercise_id', '')

    if exercise_id not in TEST_CASES_DICT:
        return jsonify({'error': 'Bài tập không tồn tại'}), 400

    test_case = TEST_CASES_DICT[exercise_id]
    total, scores, issues = grade_html(html_code, test_case)

    return jsonify({
        'exercise_id': exercise_id,
        'exercise_title': test_case['title'],
        'total_score': total,
        'scores': scores,
        'issues': issues
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
