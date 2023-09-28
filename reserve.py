import pandas as pd
import numpy as np

# Đọc tệp CSV vào DataFrame
file_path = "C:\\Users\\ACER\\Desktop\\a.csv"
df = pd.read_csv(file_path)

# Đảo ngược thứ tự các hàng
#df_reversed = df.iloc[::-1]
# Đảo ngược thứ tự các hàng 1 cách ngẫu nhiên
df_randomized = df.sample(frac=1, random_state=0)
# Lưu DataFrame mới vào tệp CSV
output_file = "C:\\Users\\ACER\\Desktop\\b.csv"
df_randomized.to_csv(output_file, index=False, encoding='utf-8')

print("Done:", output_file.encode('utf-8').decode('cp1252', 'ignore'))
