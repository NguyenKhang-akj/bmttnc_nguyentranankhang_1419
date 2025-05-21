from Quanlisinhvien import Quanlisinhvien

qlsv = Quanlisinhvien()

while (1):
    print("CHƯƠNG TRÌNH QUẢN LÝ SINH VIÊN")
    print("*************MENU*************")
    print("1. Thêm sinh viên")
    print("2. Cập nhật thông tin sinh viên bởi ID")
    print("3. Xoá sinh vien boi ID")
    print("4. Tìm sinh viên theo tên")
    print("5. Sắp xếp sinh viên theo điểm trung bình")
    print("6. Sắp xếp sinh viên theo chuyen ngành")
    print("7. Hiển thị sinh viên ")
    print("0. Thoát")
    print("*******************************")

    key = int(input("Nhập tùy chọn: "))
    if (key == 1):
        print("1. Thêm sinh viên")
        qlsv.nhapSinhvien()
        print("Thêm sinh viên thành công!")
        
    elif (key == 2):
        if (qlsv.soLuongSinhvien() > 0):
            print("\n2. Cập nhật thông tin sinh viên.")
            print("\nNhập ID: ")
            ID = int(input())
            qlsv.updateSinhVien(ID)
        else:
            print("\nDanh sách sinh viên trống!")

    elif (key == 3):
        if (qlsv.soLuongSinhvien() > 0):
            print("\n3. Xóa sinh viên.")
            print("\nNhập ID: ")
            ID = int(input())
            if (qlsv.deleteById(ID)):
                print("\nSinh viên có id =", ID, "đã bị xóa.")
            else:
                print("\nSinh viên có id =", ID, "không tồn tại.")
        else:
            print("\nDanh sách sinh viên trống!")

    elif (key == 4):
        if (qlsv.soLuongSinhvien() > 0):
            print("\n4. Tìm kiếm sinh viên theo tên.")
            print("\nNhập tên để tìm kiếm: ")
            name = input()
            searchResult = qlsv.findByName(name)
            qlsv.showSinhVien(searchResult)
        else:
            print("\nDanh sách sinh viên trống!")

    elif (key == 5):
        if (qlsv.soLuongSinhvien() > 0):
            print("\n5. Sắp xếp sinh viên theo điểm trung bình (GPA).")
            qlsv.sortByDiemTB()
            qlsv.showSinhvien(qlsv.getListSinhvien())
        else:
            print("\nDanh sách sinh viên trống!")
    elif (key == 6):
        if (qlsv.soLuongSinhvien() > 0):
            print("\n6. Sap xep sinh vien theo ten.")
            qlsv.sortByName()
            qlsv.showSinhvien(qlsv.getListSinhvien())
        else:
            print("\nDanh sach sinh vien trong!")
    elif (key == 7):
        if (qlsv.soLuongSinhvien() > 0):
            print("\n7. Hien thi danh sach sinh vien.")
            qlsv.showSinhvien(qlsv.getListSinhvien())
        else:
            print("\nDanh sach sinh vien trong!")
    elif (key == 0):
        print("\nBan da chon thoat chuong trinh!")
        break
    else:
        print("\nKhong co chuc nang nay!")
        print("\nHay chon chuc nang trong hop menu.")
        