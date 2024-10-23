def bai_1 ():
    a = 8
    b= 9
    print ("a*b= " ,a*b)
    print("a+b= ", a+b)
    print("a-b=" , a-b)
    print("a/b= ", a/b)
    print("a**b=", a**b )
    print("a//b=", a//b)
    if a > b:
        print("a > b")
    elif a < b:
        print("a < b")
    else:
        print("a == b")
    print("a and b: " , a and b )
    print("a or b : ", a or b)
    print(f"a ^ b = {a ^ b}")
    print(f"NOT (a == b) = { not (a == b)}")
    print(f"a >> 5 = {a >> 5}")
    print(f"a << 6 = {a << 6}")

    br = bin(a)[2:][::-1]
    print(f"Hệ cơ số 2 đảo ngược của a: {br}")
def bai_2 ():
    string = input("nhap vao String : ")
    if  "hit" in string.lower() :
        print("TRUE")
    else :
        print("FALSE")
    if  "15" not in string  :
        print("TRUE")
    else :
        print("FALSE")

def bai_3 ():
    print("Chao mung den CLB Tin Hoc HIT")
    print('CLB Tin Hoc HIT truc thuoc Khoa CNTT  - “10 diem” ')
    string = "CLB Tin Hoc HIT truc thuoc Khoa CNTT"
    print("cac chu cai viet hoa: ")
    for x in string :
        if x.isupper() :
            print(x,end=" ")
    print()
    print("cac chu cai viet thuong: ")
    for x in string :
        if x.islower() :
            print(x,end=" ")
    s ="CLB Tin Hoc HIT truc thuoc Khoa CNTT "
    if ( "CNTT" in s ):
        print("yes")
    else :
        print("no")
    news=''
    print("sau khi thay doi: ")
    for x in s :
        if x.islower():
            news+=x.upper()
        elif x.isupper():
            news+=x.lower()
        else :
            news+=x
    print(news)
def bai_4():
    ho_ten = input("Nhap Ho va Ten: ")
    tuoi = int(input("Nhap Tuoi: "))
    gioi_tinh = input("Nhap Gioi tinh (Nam/Nu): ")
    tinh_trang_hon_nhan = input("Nhap Tinh trang hon nhan (Doc than/Da ket hon): ")

    print("\nThong tin nhan khau hoc cua cac ban HIT 15:")
    print(f"Ho va Ten: {ho_ten}")
    print(f"Tuoi: {tuoi}")
    print(f"Gioi tinh: {gioi_tinh}")
    print(f"Tinh trang hon nhan: {tinh_trang_hon_nhan}")

    if gioi_tinh.lower() == "nu" and tinh_trang_hon_nhan.lower() == "doc than" and tuoi >= 18:
        print(f"\nChuc mung Hung! {ho_ten} co the la nguoi yeu tiem nang!")
    else:
        print(f"\n{ho_ten} co the khong phu hop voi tieu chi tim nguoi yeu cua ban Hung, neu ban khong muon dap chau cuop hoa hoac yeu duoi 18 tuoi")
def bai_5 ():
    a = float(input("nhap vao so a"))
    c= oct(a)[2:]
    return len(c)*3
def bai_5_b (number):
    ocd = dir(number)
    for  x in ocd:
        print(x)
