# src/ver2/tools/skill_analyzer.py

def analyze_skills(skills_text):
    return [s.strip() for s in skills_text.split(",") if s.strip()]