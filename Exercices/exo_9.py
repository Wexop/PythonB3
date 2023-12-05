import cmath

print("Entrez une équation du second degré sous la forme ax^2 + bx + c = 0")

try:
    a = float(input("Entrez la valeur de a : "))
    b = float(input("Entrez la valeur de b : "))
    c = float(input("Entrez la valeur de c : "))
except ValueError:
    print("Veuillez entrer des nombres valides.")

delta = b ** 2 - 4 * a * c

if delta < 0:
    print("L'équation n'a pas de solution réelle (delta < 0).")
else:
    # Utilisation de la bibliothèque cmath pour prendre en charge les solutions complexes
    solution1 = (-b + cmath.sqrt(delta)) / (2 * a)
    solution2 = (-b - cmath.sqrt(delta)) / (2 * a)

    print(f"Solutions de l'équation :")
    print(f"Solution 1 : {solution1}")
    print(f"Solution 2 : {solution2}")
