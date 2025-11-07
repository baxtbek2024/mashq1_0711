#1-misol
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

son = int(input("Son kiriting: "))
print("Faktorial =", factorial(son))

#2-misol
def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]

satr = input("So‘z kiriting: ")
print("Palindrom:", is_palindrome(satr))

#3-misol
def max_min(royxat):
    return max(royxat), min(royxat)

r = [int(x) for x in input("Sonlarni kiriting (bo‘shliq bilan): ").split()]
katta, kichik = max_min(r)
print("Eng katta:", katta, "Eng kichik:", kichik)


#4-misol
def unli_soni(satr):
    unlilar = "aeiouAEIOU"
    return sum(1 for harf in satr if harf in unlilar)

matn = input("Satr kiriting: ")
print("Unli harflar soni:", unli_soni(matn))


#5-misol
def tubmi(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

son = int(input("Son kiriting: "))
print("Tub son:", tubmi(son))

