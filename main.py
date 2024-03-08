'''
Se determina un punct de pe o curba Bezier de grad oarecare, folosind algoritmul lui De Casteljau, precum si derivata
se de ordinul intai 
'''
class Punctele:
    def __init__(self, x, y, z):
        self.__x = x
        self.__y = y
        self.__z = z

    def __str__(self):
        return f"({self.__x}, {self.__y}, {self.__z})"

    def __add__(self, p):
        return Punctele(self.__x + p.__x, self.__y + p.__y, self.__z + p.__z)

    def __sub__(self, p):
        return Punctele(self.__x - p.__x, self.__y - p.__y, self.__z - p.__z)

    def multiply(self, scalar):
        return Punctele(scalar * self.__x, scalar * self.__y, scalar * self.__z)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def z(self):
        return self.__z


def main():
    grad = int(input("Dati gradul curbei: "))
    puncte_control = grad + 1
    lista = []
    print("Punctele de control: ")
    for i in range(0, puncte_control):
        x = int(input("x: "))
        y = int(input("y: "))
        z = int(input("z: "))
        lista.append(Punctele(x, y, z))
    t = float(input("Dati t-ul: (sa fie din[0,1]) "))
    nr = puncte_control
    lista_noua = []
    lista_copie = lista

#dividem segementele in raportul t/(1-t) si obtinem astfel, alte n puncte. Iteram pana cand raman doar doua puncte.
#Punctul r(t) de pe curba va fi punctul care divide segmentul format din ultimele doua puncte ramase in raportul t/(1-t)

# pentru r(t)
    for i in range(nr - 1):
        for j in range(nr - 1):
            lista_noua.append(lista[j].multiply(1 - t) + lista[j + 1].multiply(t))
        lista = lista_noua
        lista_noua = []
        nr = nr - 1

    print(f"r ({t}) = ", lista[0])

# pentru r'(t)

    lista1 = []
    for i in range(len(lista_copie) - 1):
        lista1.append((lista_copie[i + 1] - lista_copie[i]).multiply(grad))

    nr = len(lista_copie)
    for i in range(len(lista_copie) - 2):
        for j in range(nr - 2):
            lista_noua.append(lista1[j].multiply(1 - t) + lista1[j + 1].multiply(t))
        lista1 = lista_noua
        lista_noua = []

        nr = nr - 1

    print(f"r' ({t}) = ", lista1[0])


if __name__ == '__main__':
    main()
