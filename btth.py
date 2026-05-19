patient = input("Nhập tên bệnh nhân:")
sex = input("Nhập giới tính:")
year_of_birth = input("Nhập năm sinh:")
phone_number = input("Nhập số điện thoại:")
email = input("nhập Email:")
symptom = input("Nhập triệu chứng ban đầu:")
examination = input("Nhập chi phí khám:")

year_of_birth = int(new_year)
examination = float(new_examination)

import random
#tạo số ngẫu nhiên có 3 chữ số
random_number = random.randint(100, 999)
# tạo mã bênh nhân
code = "BN" + str(year_of_birth) + str(random_number)
print("-- THẺ BỆNH NHÂN --")
print("MÃ BN:",code)
print("Tên:",patient)
print("Giới tính:",sex)
print("Năm sinh:",new_year)
print("Điện thoại:",phone_number)
print("Email:",email)
print("Triệu chứng:",symptom)
print("Chi phí:",new_examination)
