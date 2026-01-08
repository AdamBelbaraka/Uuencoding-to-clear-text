import sys
import binascii

def uu_to_text(uu_text):
    lines = uu_text.splitlines()
    start = 0
    for i, l in enumerate(lines):
        if l.startswith('begin '):
            start = i + 1
            break
    out = bytearray()
    for l in lines[start:]:
        if l.strip() == 'end':
            break
        if not l:
            continue
        try:
            out.extend(binascii.a2b_uu(l))
        except Exception:
            continue
    return out.decode('utf-8', errors='replace')

def main():
    print("Paste uuencoded text, end with a line containing only 'end':")
    lines = []
    for line in sys.stdin:
        lines.append(line.rstrip('\n'))
        if line.strip() == 'end':
            break
    uu_text = "\n".join(lines) + "\n"
    if 'begin ' not in uu_text:
        uu_text = 'begin 644 file\n' + uu_text + '\nend\n'
    try:
        text = uu_to_text(uu_text)
    except Exception as e:
        print("Error decoding:", e)
        return
    print("Clear text :", text)

if __name__ == '__main__':
    main()
