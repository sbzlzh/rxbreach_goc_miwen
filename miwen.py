def caesar_decode(cipher: str, shift: int = 3) -> str:
    result = []
    for ch in cipher.upper():
        if 'A' <= ch <= 'Z':
            pos = (ord(ch) - ord('A') - shift) % 26
            result.append(chr(pos + ord('A')))
        else:
            result.append(ch)
    return ''.join(result)

if __name__ == "__main__":
    while True:
        text = input("请输入密文（空格分隔，输入 q 退出）: ").strip()
        if text.lower() == "q":
            break
        words = text.split()
        decoded = [caesar_decode(w) for w in words]
        print("解密结果:", " ".join(decoded))
