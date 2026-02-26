import re
import json

# Read the HTML file
with open("/home/ubuntu/upload/ÔnluyệnHTML(2).html", "r", encoding="utf-8") as f:
    html_content = f.read()

# Find the PRESETS object using regex
match = re.search(r"const PRESETS = ({.*?});", html_content, re.DOTALL)

if not match:
    print("Error: Could not find the PRESETS object in the HTML file.")
    exit()

js_object_string = match.group(1)

# Convert the JavaScript object to a JSON-compatible string
# 1. Add quotes to keys
json_string = re.sub(r"([a-zA-Z0-9_]+):", r'"\1":', js_object_string)

# 2. Replace single quotes with double quotes, being careful not to replace escaped single quotes
# This is tricky because of the mixed content. A simpler way is to load it as a dictionary.
# Let's try a different approach using a library that can handle JS objects, or do more careful regex.

# A more robust way to handle the conversion:
# The main issue is that keys are not quoted, and strings use single quotes.

# Let's try to make it a valid python dictionary string and use ast.literal_eval
import ast

# The structure is like a Python dictionary if we replace single quotes in values carefully
# and quote the keys.

# The keys are valid identifiers, so we can use a regex to quote them.
# Regex to find keys (identifiers before a colon)
processed_string = re.sub(r'(\s*)([a-zA-Z0-9_]+)(\s*):', r'\1"\2"\3:', js_object_string)

# Replace single quotes with double quotes for string literals.
# This is complex due to escaped quotes. Let's try a simpler regex that assumes no escaped single quotes inside strings.
processed_string = processed_string.replace("'", '"')

# It seems the description contains HTML with double quotes, which will break the JSON parsing.
# The original file uses single quotes for JS strings.

# Let's go back to the source and do a more careful replacement.
js_object_string = match.group(1)

# 1. Quote the keys
json_string = re.sub(r'([a-zA-Z0-9_]+): ',
                     r'"\1": ',
                     js_object_string)

# 2. Replace single-quoted strings with double-quoted strings
def replace_quotes(match):
    return '"' + match.group(1).replace('"', '\\"') + '"'

# The regex needs to capture content inside single quotes
#json_string = re.sub(r"'(.*?)'", replace_quotes, json_string, flags=re.DOTALL)
# The above is too greedy and complex.

# Let's try a simpler approach again. The structure is very regular.
# The main problem is converting JS object literal to JSON.

# Let's manually create the JSON from the extracted text, which is more reliable.

presets_raw = match.group(1)

# Remove comments
presets_raw = re.sub(r"//.*", "", presets_raw)

# Split into individual preset entries
entries = re.findall(r'([a-zA-Z0-9_]+):\s*({.*?})\s*,', presets_raw, re.DOTALL)

all_exercises = []
for key, data_str in entries:
    title_match = re.search(r"title:\s*'(.*?)'", data_str)
    desc_match = re.search(r"desc:\s*'(.*?)'", data_str, re.DOTALL)
    tags_match = re.search(r"tags:\s*'(.*?)'", data_str)

    if title_match and desc_match and tags_match:
        exercise = {
            "id": key,
            "title": title_match.group(1),
            "description": desc_match.group(1).replace('\\n', '\n').replace('<br>', '\n'),
            "required_tags": [tag.strip() for tag in tags_match.group(1).split(',') if tag.strip()],
            "initial_code": "" # This can be added later if needed
        }
        all_exercises.append(exercise)

# Write to JSON file
with open("/home/ubuntu/html_grader/test_cases.json", "w", encoding="utf-8") as f:
    json.dump(all_exercises, f, ensure_ascii=False, indent=2)

print("Successfully extracted and saved test cases to test_cases.json")
