import Rectangle as rect

menu_options = {
    1: 'Thêm một hình chữ nhât',
    2: 'Hiển thị danh sách hình chữ nhật',
    3: 'Tính tổng diện tích các hình chữ nhật',
    4: 'Tính tổng chu vi các hình chữ nhật',
    5: 'Hiển thị các hình chữ nhật có chu vi nhỏ nhất',
    'Others': 'Thoát chương trình'
}
def print_menu():
    for key in menu_options.keys():
        print ( key, '--', menu_options[key] )
# Khai báo biến lưu trữ những hình chữ nhật
dsHCN = []

while(True):
    print_menu()
    userChoice = ''
    try:
        userChoice = int(input('Nhập tùy chon: '))
    except:
        print('Nhập sai đinh dạng, hãy nhập lại.....')
        continue
    #Check what choice was entered and act accordingly
    if userChoice == 1:
        cr = float(input('Nhập chiều rộng: '))
        cd = float(input('Nhập chiều dai: '))
        hcn = rect.Rectangle(cr,cd)
        dsHCN.append(hcn)
    elif userChoice == 2:
        for item in dsHCN:
            item.display()
    elif userChoice == 3:
        dientich = 0.0
        for item in dsHCN:
            dientich = dientich + item.area()
        print(f'Tổng diện tích là : {dientich}')
    elif userChoice == 4:
        chuvi = 0.0
        for item in dsHCN:
            chuvi = chuvi +item.perimeter()
        print(f'Tổng chu vi là : {chuvi}')
    elif userChoice == 5:
        if dsHCN.count == 0:
            print('Danh sách rỗng')
        else:
            chuvinn = dsHCN[0].perimeter()
            for item in dsHCN:
                if chuvinn > item.perimeter():
                    chuvinn = item.perimeter()
            #print(f'chu vi nhỏ nhất là : {chuvinn}')
            for item in dsHCN:
                if item.perimeter() == chuvinn:
                    item.display() # In ra hiển thị các hình chữ nhật có chu vi nhỏ nhất
         
            
    else:
        print('Thoat chuong trinh BYE BYE')
        break