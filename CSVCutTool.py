import pandas as pd
import os

def create_example_file(file_path):
    # 获取文件的目录、文件名和扩展名
    dir_name, base_name = os.path.split(file_path)
    file_name, ext = os.path.splitext(base_name)
    
    # 读取文件内容
    if ext == '.csv':
        data = pd.read_csv(file_path)
    elif ext in ['.xls', '.xlsx']:
        data = pd.read_excel(file_path)
    else:
        raise ValueError('Unsupported file type. Please provide a CSV or Excel file.')
    
    # 截取前25行数据
    data_example = data.head(25)
    
    # 构造新文件名
    new_file_name = f"{file_name}_example{ext}"
    new_file_path = os.path.join(dir_name, new_file_name)
    
    # 保存截取的数据到新文件
    if ext == '.csv':
        data_example.to_csv(new_file_path, index=False)
    else:
        data_example.to_excel(new_file_path, index=False)
    
    print(f"Example file saved to: {new_file_path}")

# 获取用户输入的文件路径
file_path = input("Enter the path of the CSV or Excel file: ")
create_example_file(file_path)
