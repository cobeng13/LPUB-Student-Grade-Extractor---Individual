Grade Extractor – Individual Reports
====================================

This Python script processes multiple student HTML grade reports and exports each student's grades to a separate Excel file.

Features:
- Extracts the student’s name, course codes, and grades from HTML.
- Generates one Excel file per student.
- Uses course codes as column headers and places grades in a single row.
- Output Excel file is named after the student.

Folder Structure:
-----------------
📂 Raw HTML/             → Place all student HTML files here  
📂 Output/               → Excel files will be saved here  
📄 Grade Extractor Individual.py

Requirements:
-------------
- Python 3.7+
- Packages:
  beautifulsoup4, pandas, openpyxl

Install via pip:
----------------
pip install beautifulsoup4 pandas openpyxl

How to Use:
-----------
1. Open Grade Extractor Individual.py.
2. Edit the paths in the main() function:
   input_folder = r"C:\Path\To\Raw HTML"
   output_folder = r"C:\Path\To\Output"
3. Run the script:
   python Grade Extractor Individual.py

Output Format:
--------------
Each Excel file will be named:
STUDENT_NAME.xlsx

It will contain:
| PHAR_1 | GEC-RPH | PHAR_CHEM_1 | ... |
|--------|---------|--------------|-----|
| 1.75   | 2.00    | 2.25         | ... |

License:
--------
MIT License
