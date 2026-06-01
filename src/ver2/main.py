from react_agent import ReActAgent

if __name__ == "__main__":

    agent = ReActAgent()

    role = input("Nhập vị trí tuyển dụng: ")
    skills = input("Nhập kỹ năng: ")

    response = agent.run(role, skills)

    print("\n=== KẾT QUẢ ===\n")
    print(response["result"])

    print(f"\nĐã lưu báo cáo: {response['file']}")