def rectangle_area(w, l):
    return round(w * l, 2)

def circle_area(ra):
    return round(3.1416 * ra**2, 2)

def rectangular_prism_volume(w, l, hi):
    return round(w * l * hi, 2)

def sphere_volume(ra):
    return round(4/3 * 3.1416 * ra**3, 2)

while True:
    print("เลือกเมนู:")
    print("1. พื้นที่สี่เหลี่ยม")
    print("2. พื้นที่วงกลม")
    print("3. ปริมาตรทรงสี่เหลี่ยม")
    print("4. ปริมาตรทรงกลม")
    print("0. ออกจากโปรแกรม")

    selec = input("เลือกเมนู: ")

    if selec == '0':
        print("โปรแกรมจบการทำงาน")
        break
    elif selec in ('1', '2', '3', '4'):
        if selec == '1':
            w = float(input("ป้อนความกว้าง: "))
            l = float(input("ป้อนความยาว: "))
            result = rectangle_area(w, l)
            print(f"พื้นที่สี่เหลี่ยม: {result}")
        elif selec == '2':
            ra = float(input("ป้อนรัศมี: "))
            result = circle_area(ra)
            print(f"พื้นที่วงกลม: {result}")
        elif selec == '3':
            w = float(input("ป้อนความกว้าง: "))
            l = float(input("ป้อนความยาว: "))
            hi = float(input("ป้อนความสูง: "))
            result = rectangular_prism_volume(w, l, hi)
            print(f"ปริมาตรทรงสี่เหลี่ยม: {result}")
        elif selec == '4':
            ra = float(input("ป้อนรัศมี: "))
            result = sphere_volume(ra)
            print(f"ปริมาตรทรงกลม: {result}")
    else:
        print("กรุณาเลือกเมนู 1, 2, 3, 4 หรือ 0 เท่านั้น")