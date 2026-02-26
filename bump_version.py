#!/usr/bin/env python3
"""
bump_version.py — Tự động tăng patch version cho HTML Grader
Cách dùng:
  python3 bump_version.py          # tăng patch: 1.2.3 → 1.2.4
  python3 bump_version.py minor    # tăng minor: 1.2.3 → 1.3.0
  python3 bump_version.py major    # tăng major: 1.2.3 → 2.0.0
  python3 bump_version.py set 1.5.0  # đặt version cụ thể
"""

import re
import sys
import os
from datetime import datetime

FILES = [
    os.path.join(os.path.dirname(__file__), 'index.html'),
    os.path.join(os.path.dirname(__file__), 'html_grader_offline.html'),
]

VERSION_PATTERN = re.compile(r"const VERSION = '(\d+)\.(\d+)\.(\d+)';")

def read_version(filepath):
    """Đọc version hiện tại từ file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    m = VERSION_PATTERN.search(content)
    if not m:
        raise ValueError(f"Không tìm thấy VERSION trong {filepath}")
    return int(m.group(1)), int(m.group(2)), int(m.group(3))

def write_version(filepath, major, minor, patch):
    """Ghi version mới vào file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    new_content = VERSION_PATTERN.sub(
        f"const VERSION = '{major}.{minor}.{patch}';",
        content
    )
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

def bump(major, minor, patch, bump_type='patch'):
    if bump_type == 'major':
        return major + 1, 0, 0
    elif bump_type == 'minor':
        return major, minor + 1, 0
    else:  # patch
        return major, minor, patch + 1

def main():
    args = sys.argv[1:]

    # Đọc version hiện tại từ file đầu tiên
    try:
        major, minor, patch = read_version(FILES[0])
    except (FileNotFoundError, ValueError) as e:
        print(f"❌ Lỗi: {e}")
        sys.exit(1)

    old_version = f"{major}.{minor}.{patch}"

    # Xác định loại bump
    if args and args[0] == 'set' and len(args) == 2:
        parts = args[1].split('.')
        if len(parts) != 3 or not all(p.isdigit() for p in parts):
            print("❌ Định dạng version không hợp lệ. Dùng: X.Y.Z")
            sys.exit(1)
        new_major, new_minor, new_patch = int(parts[0]), int(parts[1]), int(parts[2])
    elif args and args[0] in ('major', 'minor', 'patch'):
        new_major, new_minor, new_patch = bump(major, minor, patch, args[0])
    else:
        new_major, new_minor, new_patch = bump(major, minor, patch, 'patch')

    new_version = f"{new_major}.{new_minor}.{new_patch}"

    # Ghi version mới vào tất cả file
    updated = []
    for filepath in FILES:
        if os.path.exists(filepath):
            try:
                write_version(filepath, new_major, new_minor, new_patch)
                updated.append(os.path.basename(filepath))
            except Exception as e:
                print(f"⚠️  Không thể cập nhật {filepath}: {e}")

    # In kết quả
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"✅ Version: {old_version} → {new_version}  [{timestamp}]")
    print(f"   Đã cập nhật: {', '.join(updated)}")

    # Ghi vào VERSION file để theo dõi lịch sử
    version_log = os.path.join(os.path.dirname(__file__), 'VERSION')
    with open(version_log, 'w', encoding='utf-8') as f:
        f.write(f"{new_version}\n")

    return new_version

if __name__ == '__main__':
    main()
