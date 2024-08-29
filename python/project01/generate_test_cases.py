"""--------------------------------------------------------------------------------------------
generate_test_cases.py

Autor: boxdate
First Publish: 22th Aug 2024

examination:
正規表現で抽出したテスト条件から、境界値テストのテストケースを生成する。
--------------------------------------------------------------------------------------------"""

# 境界値テスト生成クラス
class BoundaryValueTestCaseGenerator:
    def generate(self, var, value, condition):
        return [
            {'var': var, 'value': int(value) - 1, 'condition': condition},  # 境界値
            {'var': var, 'value': int(value) + 1, 'condition': condition}   # 境界値
        ]
    
# 同値分割テスト生成クラス    
class EquivalencePartitioningTestCaseGenerator:
    def generate(self, var, value, condition):
        return [
            {'var': var, 'value': int(value), 'condition': condition}  # 同値分割
        ]

# テストケース生成クラス
class TestCaseGenerator:
    def __init__(self, conditions):
        self.conditions = conditions
        self.test_cases = []
        self.boundary_value_generator = BoundaryValueTestCaseGenerator()
        self.equivalence_partitioning_generator = EquivalencePartitioningTestCaseGenerator()

    def generate_test_cases(self):
        for condition in self.conditions:
            if '>=' in condition:
                var, value = condition.split('>=')
                self.test_cases.extend(self.boundary_value_generator.generate(var.strip(), value.strip(), '>='))
                self.test_cases.extend(self.equivalence_partitioning_generator.generate(var.strip(), value.strip(), '>='))
            elif '>' in condition:
                var, value = condition.split('>')
                self.test_cases.extend(self.boundary_value_generator.generate(var.strip(), value.strip(), '>'))
                self.test_cases.extend(self.equivalence_partitioning_generator.generate(var.strip(), value.strip(), '>'))
            elif '<=' in condition:
                var, value = condition.split('<=')
                self.test_cases.extend(self.boundary_value_generator.generate(var.strip(), value.strip(), '<='))
                self.test_cases.extend(self.equivalence_partitioning_generator.generate(var.strip(), value.strip(), '<='))
            elif '<' in condition:
                var, value = condition.split('<')
                self.test_cases.extend(self.boundary_value_generator.generate(var.strip(), value.strip(), '<'))
                self.test_cases.extend(self.equivalence_partitioning_generator.generate(var.strip(), value.strip(), '<'))
        return self.test_cases

# テストケース出力クラス
class TestCaseWriter:
    def __init__(self, test_cases, file_path):
        self.test_cases = test_cases
        self.file_path = file_path

    def write_to_file(self):
        with open(self.file_path, 'w') as f:
            f.write('import pytest\n\n')
            f.write('def test_generated_cases():\n')
            for i, case in enumerate(self.test_cases):
                f.write(f" assert {case['var']}{case['condition']}{case['value']}\n")


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