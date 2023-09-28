import csv

file_path = "C:\\Users\\ACER\\Desktop\\csgo_player_stats.csv"
count = 0
with open(file_path, newline='') as csvfile:
    # Tạo một đối tượng đọc CSV
    csv_reader = csv.DictReader(csvfile)
    # Lặp qua từng hàng trong tệp CSV
    for row in csv_reader:
        # Truy cập giá trị của cột "KAST" và "Impact" cho mỗi hàng
        kast_value = row["KAST"]
        impact_value = row["Impact"]
        isTrue = row["Rating 2.0"]
        namePlayer = row["Name"]
        a = (float(kast_value) + float(impact_value) -0.8)*0.96 +0.04
        count+=1
        # Thực hiện các thao tác bạn muốn với các giá trị này
        if (a == float(isTrue)):{
            print(str(count) + " " + namePlayer + " true\n")
        }
        else : print(str(count) + " " + namePlayer + " false\n")
            

