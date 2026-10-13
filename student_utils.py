def parse_student(line):
    """将一行记录解析为字典, 校验字段数量、姓名和成绩范围"""
    fields = line.split(",")
    if len(fields) != 2:
        raise ValueError(f"字段数量错误, 期望 2, 收到 {len(fields)}")
    name, score_str = fields
    name = name.strip()
    if not name:
        raise ValueError("姓名为空")
    score = int(score_str)
    if score < 0 or score > 100:
        raise ValueError(f"成绩 {score} 超出 0~100 范围")
    return {"name": name, "score": score}
