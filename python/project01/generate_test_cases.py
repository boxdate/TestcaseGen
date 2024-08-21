"""--------------------------------------------------------------------------------------------
generate_test_cases.py

Autor: boxdate
First Publish: 21th Aug 2024

examination:
正規表現で抽出したテスト条件から、境界値テストのテストケースを生成する。
--------------------------------------------------------------------------------------------"""

def generate_test_cases(conditions):
    test_cases = []
    for condition in conditions:
        # 比較演算子に基づいてテストケースを生成
        if '>=' in condition:
            var, value = condition.split('>=')
            test_cases.append({'var': var.strip(), 'value': int(value.strip()) - 1, 'condition': '>='})  # 境界値
            test_cases.append({'var': var.strip(), 'value': int(value.strip()), 'condition': '>='})      # 同値分割
            test_cases.append({'var': var.strip(), 'value': int(value.strip()) + 1, 'condition': '>='})  # 境界値
        elif '>' in condition:
            var, value = condition.split('>')
            test_cases.append({'var': var.strip(), 'value': int(value.strip()) - 1, 'condition': '>'})  # 境界値
            test_cases.append({'var': var.strip(), 'value': int(value.strip()), 'condition': '>'})      # 同値分割
            test_cases.append({'var': var.strip(), 'value': int(value.strip()) + 1, 'condition': '>'})  # 境界値
        elif '<=' in condition:
            var, value = condition.split('<=')
            test_cases.append({'var': var.strip(), 'value': int(value.strip()) - 1, 'condition': '<='})  # 境界値
            test_cases.append({'var': var.strip(), 'value': int(value.strip()), 'condition': '<='})      # 同値分割
            test_cases.append({'var': var.strip(), 'value': int(value.strip()) + 1, 'condition': '<='})  # 境界値
        elif '<' in condition:
            var, value = condition.split('<')
            test_cases.append({'var': var.strip(), 'value': int(value.strip()) - 1, 'condition': '<'})  # 境界値
            test_cases.append({'var': var.strip(), 'value': int(value.strip()), 'condition': '<'})      # 同値分割
            test_cases.append({'var': var.strip(), 'value': int(value.strip()) + 1, 'condition': '<'})  # 境界値
    return test_cases

# 使用例
if __name__ == "__main__":
    from extract_conditions import extract_conditions
    activity_diagram_text_file_path = 'output/activity_diagram.txt'
    conditions = extract_conditions(activity_diagram_text_file_path)
    test_cases = generate_test_cases(conditions)
    print(test_cases)
    
    # テストケースをファイルに出力
    generate_test_cases_file_path = 'output/test_cases.py'
    with open(generate_test_cases_file_path, 'w') as f:
        f.write('import pytest\n\n')
        f.write('def test_generated_cases():\n')
        for i, case in enumerate(test_cases):
            f.write(f" assert {case['var']}{case['condition']}{case['value']}\n")