"""--------------------------------------------------------------------------------------------
extract_conditions.py

Autor: boxdate
First Publish: 22th Aug 2024

examination:
txtファイルから正規表現で、アクティビティ図の条件を抽出する。
--------------------------------------------------------------------------------------------"""

import re

class ConditionExtractor:
    def __init__(self, file_path):
        self.file_path = file_path
    
    def extract_conditions(self):
        with open(self.file_path, 'r') as file:
            content = file.read()
            
        #if分の条件を正規表現で抽出
        #複数条件の抽出ができるように変更
        conditions = re.findall(r'if\s*\(([^)]+)\)', content)
        return conditions
    
    def split_conditions(self, condition):
        # 論理演算子で条件を分割する
        return re.split(r'\s*&&\s*\|\s*\|\|\s', condition)
    
    def extract_coparisons(self, sub_condition):
        # 各条件を分割して解析する
        return re.findall(r'(\w+)\s*([><]=?)\s*(\d+)', sub_condition)
    
# 使用例
if __name__ == "__main__":
    activity_diagram_text_file_path = 'output/activity_diagram.txt'  # 出力txtファイルのパス
    conditions = extract_conditions(activity_diagram_text_file_path)
    print(conditions)
