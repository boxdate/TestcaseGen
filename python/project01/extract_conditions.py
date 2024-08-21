"""--------------------------------------------------------------------------------------------
extract_conditions.py

Autor: boxdate
First Publish: 21th Aug 2024

examination:
txtファイルから正規表現で、アクティビティ図の条件を抽出する。
--------------------------------------------------------------------------------------------"""

import re

def extract_conditions(txt_file):
    with open(txt_file, 'r') as file:
        content = file.read()
        
    #if分の条件を正規表現で抽出
    conditions = re.findall(r'if\s\((.*?)\)', content)
    return conditions

if __name__ == "__main__":
    activity_diagram_text_file_path = 'output/activity_diagram.txt'  # 出力txtファイルのパス
    conditions = extract_conditions(activity_diagram_text_file_path)
    print(conditions)
