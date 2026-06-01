# src/ver1/chatbot_llm.py
import os
import datetime
from llama_cpp import Llama

class InterviewChatbotLLM:
    def __init__(self):
        model_path = os.getenv("LOCAL_MODEL_PATH", "./models/Phi-3-mini-4k-instruct-q4.gguf")
        self.llm = Llama(model_path=model_path, verbose=False)

    def generate_questions(self, role, skills):
        prompt = f"Tạo 5 câu hỏi phỏng vấn cho vị trí {role}, tập trung vào kỹ năng {skills}."
        # Gọi chat completion
        output = self.llm.create_chat_completion(
            messages=[{"role": "user", "content": prompt}],
            max_tokens=256
        )

        if "choices" in output and len(output["choices"]) > 0:
            text = output["choices"][0]["message"]["content"]
        else:
            text = "Không có kết quả từ mô hình."

        clean_text = (
            text.replace("<br>", "\n")
                .replace("<b>", "")
                .replace("</b>", "")
                .strip()
        )
        return clean_text

    def chat(self):
        print("Xin chào! Tôi là chatbot hỗ trợ tạo phỏng vấn AI (LLM).")

        role = input("Bạn muốn tạo phỏng vấn cho vị trí nào: ")
        skills = input("Kỹ năng chính bạn muốn đánh giá là gì: ")

        questions = self.generate_questions(role, skills)

        print("\n--- Câu hỏi phỏng vấn ---")
        print(questions)

        # Tạo thư mục nếu chưa có
        os.makedirs("report/individual_reports", exist_ok=True)

        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

        filename = f"report/individual_reports/chat_{timestamp}.txt"

        with open(filename, "w", encoding="utf-8") as f:
            f.write(questions)

        print(f"\n✅ Đã lưu vào {filename}")