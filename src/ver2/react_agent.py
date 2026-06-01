import os
from llama_cpp import Llama

from tools.skill_analyzer import analyze_skills
from tools.question_generator import build_prompt
from tools.report_writer import save_report


class ReActAgent:

    def __init__(self):

        model_path = os.getenv(
            "LOCAL_MODEL_PATH",
            "./models/Phi-3-mini-4k-instruct-q4.gguf"
        )

        self.llm = Llama(
            model_path=model_path,
            verbose=False
        )

    def run(self, role, skills_text):

        # Tool 1: Phân tích kỹ năng
        skills = analyze_skills(skills_text)

        # Tool 2: Tạo prompt
        prompt = build_prompt(role, skills)

        # Tool 3: Gọi LLM sinh câu hỏi + câu trả lời mẫu
        output = self.llm.create_chat_completion(
            messages=[
                {
                    "role": "user",
                    "content": f"""
{prompt}

Ngoài câu hỏi, hãy cung cấp đáp án mẫu ngắn gọn cho từng câu.

Định dạng:

Câu 1:
...

Đáp án:
...

Câu 2:
...

Đáp án:
...
"""
                }
            ],
            max_tokens=1024
        )

        result = output["choices"][0]["message"]["content"]

        # Tool 4: Lưu báo cáo
        filename = save_report(result)

        return {
            "result": result,
            "file": filename
        }