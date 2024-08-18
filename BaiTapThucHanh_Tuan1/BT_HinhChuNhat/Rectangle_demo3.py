import Rectangle as rect
menu_options = {
    1: ' Đọc dữ liệu từ file input.db',
    2: ' Thêm mới hình chữ nhật',
    3: ' Hiển thị danh sách hình chữ nhật',
    4: ' Lưu danh sách hình chữ nhật xuống file demmo4output,db',
    'Others':'Thoát chương trình'
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
#Kiểm tra các lựa chọn
    if userChoice == 1:
        #1 - Đọc dữ liệu từ file input.db
        fr = open('input.db', mode = 'r', encoding = 'utf-8')
        for line in fr:
            stripLine = line.strip('\n')
            ds = stripLine.split(',')
            cr = float(ds[0])
            cd = float(ds[1])
            hcn = rect.Rectangle(cr,cd)
            dsHCN.append(hcn)
        fr.close()
    elif userChoice == 2:
        #2 Thêm mới hình chữ nhật
        cr = float(input('Nhập chiều rộng: '))
        cd = float(input('Nhập chiều dai: '))
        hcn = rect.Rectangle(cr,cd)
        dsHCN.append(hcn)
    elif userChoice == 3:
        #3 Hiển thị danh sách hình chữ nhật
        if dsHCN.count == 0:
            print('Danh sách rỗng')
        else:
            for item in dsHCN:
                item.display()
    elif userChoice == 4:
        #4 Lưu danh sách hình chữ nhật xuống file demo3ouput,db
        fw = open('outpudemo4.db' , mode = 'w' , encoding = 'utf-8' )
        for item in dsHCN:
            fw.write(f'{item.width}-{item.length}-{item.perimeter()}-{item.area()}\n')
        fw.close()
    else:
        print('Kết thúc chương trình')
        break