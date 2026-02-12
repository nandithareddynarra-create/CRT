def Student_Grade_System(name: str, n1: int, n2: int, n3: int) -> str:
    avg = (n1 + n2 + n3) / 3

    avg = int(avg * 100) / 100
    avg_str = format(avg, ".2f")
    if avg_str.endswith("00"):
        avg_str = avg_str[:-1]

    if avg >= 40:
        status = "Pass"
    else:
        status = "fail"

    return f"Average grade: {avg_str}, Status: {status}"