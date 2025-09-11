import datetime

def tim_ngay_ke_tiep(ngay, thang, nam):
    try:
        ngay_hien_tai = datetime.date(nam, thang, ngay)
        ngay_ke_tiep = ngay_hien_tai + datetime.timedelta(days=1)
        return ngay_ke_tiep.strftime("%d/%m/%Y")
    except ValueError:
        return "Ngày không hợp lệ!"
ngay = int(input("Nhập ngày: "))
thang = int(input("Nhập tháng: "))
nam = int(input("Nhập năm: "))

print("Ngày kế tiếp là:", tim_ngay_ke_tiep(ngay, thang, nam))