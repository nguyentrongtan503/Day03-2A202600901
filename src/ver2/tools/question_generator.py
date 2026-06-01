# src/ver2/tools/question_generator.py

def build_prompt(role, skills):

    skill_text = ", ".join(skills)

    return f"""
Bạn là chuyên gia tuyển dụng.

Tạo 5 câu hỏi phỏng vấn cho vị trí {role}.

Kỹ năng cần đánh giá:
{skill_text}

Yêu cầu:
- Từ dễ đến khó
- Có câu hỏi thực tế
- Đánh giá đúng kỹ năng
"""