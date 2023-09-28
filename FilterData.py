<<<<<<< HEAD
# Đường dẫn đến tệp văn bản
input_file = 'C:\\Users\\ACER\\Desktop\\a.txt'
output_file = 'C:\\Users\\ACER\\Desktop\\b.txt'

# Đọc nội dung từ tệp
with open(input_file, 'r') as file:
    lines = file.readlines()

# Xóa các dòng có ít hơn 8 kí tự (bao gồm chữ và số)
filtered_lines = [line.strip() for line in lines if len(line.strip()) >= 8]

# Ghi dữ liệu đã lọc vào tệp
with open(output_file, 'w') as file:
    for line in filtered_lines:
        file.write(line + '\n')

print("SS", output_file)
=======
# Đường dẫn đến tệp văn bản
input_file = 'C:\\Users\\ACER\\Desktop\\a.txt'
output_file = 'C:\\Users\\ACER\\Desktop\\b.txt'

# Đọc nội dung từ tệp
with open(input_file, 'r') as file:
    lines = file.readlines()

# Xóa các dòng có ít hơn 8 kí tự (bao gồm chữ và số)
filtered_lines = [line.strip() for line in lines if len(line.strip()) >= 8]

# Ghi dữ liệu đã lọc vào tệp
with open(output_file, 'w') as file:
    for line in filtered_lines:
        file.write(line + '\n')

print("SS", output_file)
>>>>>>> dc076e8357095f791f7a1af698241833ec617e8e
