# Üçgenin doğruluğunu belirleyen program

# Doğruluğu kontrol edecek fonksiyonun tanımlanması
def is_valid_triangle(a,b,c):
    if a+b>=c and b+c>=a and c+a>=b:
        return True
    else:
        return False

# Üçgenin hangi tür olduğunu belirleyen fonksiyon tanımlanması
def type_of_triangle(a,b,c):
    if a==b and b==c:
        print('Ucgen eskenar ucgendir.')
    elif a==b or b==c or a==c:
        print('Ucgen ikizkenar ucgendir.')
    else:
        print('Ucgen cesitkenar ucgendir.')

# Listeyi oluşturma ve listeden veriyi çekme
list = []
for n in range(3)
  side = float(input("Ucgenlerin kenar uzunluklarini giriniz: "))
  list.append(side)
side_a = list[0]
side_b = list[1]
side_c = list[2]
 
# Fonksiyonu çağırma ve işlemi gerçekleştirme
if is_valid_triangle(side_a, side_b, side_c):
    type_of_triangle(side_a, side_b, side_c)
else:
    print('Bu kenarlarla ucgen cizmek mumkun degildir.')
