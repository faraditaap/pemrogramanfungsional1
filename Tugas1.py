#NO.1
print("Program Returning Function")
list_integer = [1, 2, 3]
print('sum_square',(list_integer))

def sum_squares (x, y, z):
    return (x**2 + y**2 + z**2)

print ('Hasil = ', sum_squares(1,2,3))

#NO.2
print('\nprogram triangular')
def triangular(n):
    if n==1:
        return(1)
    else:
        return (n + triangular(n-1))
jumlah = triangular(5)
print("triangular ke-5 = ",jumlah)

#NO.3
print('\nprogram pangkat')
def pangkat(a):
    return (a**2)

print('Pangkat (3,2)')
print("Hasil = ", pangkat(3))

#NO.4
print("\nProgram Mengecek Kata Palindrom atau Bukan Palindrom")
print()

kata = input("Input Kata : ")
temp = ""

for i in range(len(kata)-1, -1, -1): 
    temp+=kata[i]
print("Hasil : ", end="")

if(kata == temp):
    print("True")
else:
    print("False")