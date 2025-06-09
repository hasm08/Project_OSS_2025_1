def to_roman(n: int) -> str:
    if not (0 < n < 4000):
        raise ValueError("1~3999 범위만 지원합니다")
    roman_map = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I'),
    ]
    result = ""
    for val, sym in roman_map:
        count, n = divmod(n, val)
        result += sym * count
    return result

def from_roman(s: str) -> int:
    roman_map = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I'),
    ]
    s = s.upper()
    i, total = 0, 0
    while i < len(s):
        matched = False
        for val, sym in roman_map:
            if s[i:i+len(sym)] == sym:
                total += val
                i += len(sym)
                matched = True
                break
        if not matched:
            raise ValueError(f"잘못된 로마 숫자: {s}")
    return total
