"""--------------------------------------------------------------------------------------------
puml_to_txt.py

Autor: boxdate
First Publish: 22th Aug 2024

examination:
pumlファイルをtxtファイルに変換する。
--------------------------------------------------------------------------------------------"""

def convert_puml_to_txt(puml_file, txt_file):
    with open(puml_file, 'r') as puml:
        content = puml.read()
    with open(txt_file, 'w') as txt:
        txt.write(content)
       
# Example usage
puml_file_path = 'diagrams/activity_diagram.puml'  # .pumlファイルのパス
output_file_path = 'output/activity_diagram.txt'  # 出力txtファイルのパス

convert_puml_to_txt(puml_file_path, output_file_path)