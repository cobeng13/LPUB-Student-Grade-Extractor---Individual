import os
from bs4 import BeautifulSoup
import pandas as pd

def extract_student_data(html_path):
    with open(html_path, encoding="utf-8") as file:
        soup = BeautifulSoup(file, "html.parser")

    # Extract student name
    student_tag = soup.find("span", id="spnStudentName")
    student_name = student_tag.get_text(strip=True).replace(",", "").replace(" ", "_") if student_tag else "Unknown_Student"

    # Extract course codes and grades
    grade_table = soup.find("table", class_="user_data")
    course_codes, grades = [], []

    if grade_table:
        for row in grade_table.find_all("tr"):
            cells = row.find_all("td")
            if len(cells) >= 2:
                code = cells[0].text.strip()
                grade = cells[1].text.strip()
                if code and grade and not code.lower().startswith("total") and "GWA" not in grade:
                    course_codes.append(code)
                    grades.append(grade)
    
    return student_name, course_codes, grades

def process_html_folder(folder_path, output_folder):
    os.makedirs(output_folder, exist_ok=True)
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(".html"):
            html_path = os.path.join(folder_path, filename)
            student_name, codes, grades = extract_student_data(html_path)

            df = pd.DataFrame([grades], columns=codes)
            output_path = os.path.join(output_folder, f"{student_name}.xlsx")
            df.to_excel(output_path, index=False)
            print(f"✅ Saved: {output_path}")

def main():
    # ✏️ EDIT THESE PATHS ONLY
    input_folder = r"C:\Users\aaron\Desktop\Grade Extractor\Raw HTML"
    output_folder = r"C:\Users\aaron\Desktop\Grade Extractor\Output"

    process_html_folder(input_folder, output_folder)

if __name__ == "__main__":
    main()
