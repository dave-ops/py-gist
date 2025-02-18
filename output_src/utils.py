import re

def json_safe(s):
    if isinstance(s, str):
        # Escape special characters
        s = s.replace('\\', '\\\\')  # Backslash
        s = s.replace('\n', '\\n')   # Newline
        s = s.replace('\r', '\\r')   # Carriage return
        s = s.replace('\t', '\\t')   # Tab
        s = s.replace('\b', '\\b')   # Backspace
        s = s.replace('\f', '\\f')   # Form feed
        s = s.replace('"', '\\"')    # Double quote
        # Handle non-ASCII characters
        return s.encode('utf-8').decode('unicode_escape')
    return s

def make_content_json_safe(content):
    if isinstance(content, dict):
        return {json_safe(k): make_content_json_safe(v) for k, v in content.items()}
    elif isinstance(content, list):
        return [make_content_json_safe(item) for item in content]
    elif isinstance(content, str):
        return json_safe(content)
    else:
        return content

def sanitize_filename(filename):
    return re.sub(r'[^\w_.]', '_', filename)