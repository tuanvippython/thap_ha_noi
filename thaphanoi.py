# n là số đĩa
def thap_ha_noi(n,cot1,cot2,cot3):
    # Kiếm tra nếu số đĩa bằng 1 thì in ra thông báo chuyển đĩa từ cột 1 sang cột 3
    if n==1:
        print("chuyển đĩa",cot1,"sang",cot3)
    else:
    # Kiếm tra nếu số đĩa lớn hơn 1 thì sẽ chuyển đĩa ở cột 1 sang cột 3 thông qua cột 2
        thap_ha_noi(n-1,cot1,cot3,cot2)
        print("chuyển đĩa",cot1,"sang",cot3)
        thap_ha_noi(n-1,cot2,cot1,cot3)

n = int(input("Nhập n: "))
thap_ha_noi(n,"A","B","C")