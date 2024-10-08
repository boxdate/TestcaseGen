"""--------------------------------------------------------------------------------------------
Test Generation tool for PlantUML

Autor: boxdate
First Publish: 22th Aug 2024

Purpose this tool:
PlantUMLの各種ダイアグラムからテストケースを自動生成し、ソースコードのVerifyするための
テストケースの作成をソースコードを書き始める前から準備することが目的。
VerifyのTDDに使うためのテストケースの作成時間を短縮することで、ソースコードの開発に
時間と集中することを目指す。

Requiremetns for this tool:
Ver 0.00
・pythonでplantUMLのファイルを読み込むこと
・pythonで、plantUMLのアクティビティ図を解析すること
・pumlファイルをtextファイルに変換すること
・正規表現でtxtファイル内の条件を抽出しリスト化すること
・解析したアクティビティ図の条件分岐の条件を抽出すること
・条件分岐に使用されている比較演算子を抽出すること
・比較演算子を使用した条件の場合、同値分割、境界値分割のテスト技法を使用したテストケースを生成すること
・pytestで使用できる形式のテストコードを生成すること

※ソースコードはMicrosoft copilotの生成支援を受けて作成しています。

--------------------------------------------------------------------------------------------"""

"""--------------------------------------------------------------------------------------------
main.py

Autor: boxdate
First Publish: 21th Aug 2024

examination:
テストケース生成ツールの全体の処理フローをまとめ、テストケースを生成し、outputに保存する。
--------------------------------------------------------------------------------------------"""

from extract_conditions import ConditionExtractor
from generate_test_cases import TestCaseGenerator, TestCaseWriter
import puml_to_txt

def main():
    
    # input file .puml and output file .txt directory 
    puml_file_path = 'diagrams/activity_diagram.puml'  # .pumlファイルのパス
    activity_diagram_text_file_path = 'output/activity_diagram.txt'  # activity図を変換したtxtファイルのパス
    generate_test_cases_file_path = 'output/test_cases.py' # 生成したテストケースの.pyファイルのパス
    
    # convert .puml to .txt
    puml_to_txt.convert_puml_to_txt(puml_file_path, activity_diagram_text_file_path)
    
    # 正規表現で抽出したテスト条件を表示する
    extractor = ConditionExtractor(activity_diagram_text_file_path)
    conditions = extractor.extract_conditions()
    print("This activity diagram's test conditions: ", conditions)
    
    # pytestで使用するテストケースを生成する
    generator = TestCaseGenerator(conditions)
    test_cases = generator.generate_test_cases()
    print("This activitiy diagram's testcases: ", test_cases)
    
    # pytestで利用可能な.py形式のテストケースを生成する
    writer = TestCaseWriter(test_cases, generate_test_cases_file_path)
    writer.write_to_file()
    
    print(f"Test cases have been generated and saved to {generate_test_cases_file_path}")

if __name__ == "__main__":
    main()