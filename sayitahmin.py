import random
while True:
    dogru = False
    print("--------------------------------")
    sayi=random.randint(1,10)
    print("Aklımdan 10 ile 1 arasında bir sayı tuttum.")
    a = int(input("Sayıyı tahmin et: "))
    if a==sayi:
        print("Tebrikler sayıyı bildiniz!")
        print("Bir daha denemeye ne dersin")
    elif 1<a<10 and a!=sayi:
        print("Maalesef bilemediniz.")
        if a<sayi:
            print("Sayıyı büyüt")
        if a>sayi:
            print("Sayıyı küçült")
        while dogru==False:
            a = int(input("Sayıyı tekrar tahmin et"))
            if a==sayi:
                print("Sayı doğru")
                dogru = True
    else:
        print("Tuttuğum sayı 1 ile 10 arasında")
        print("Bu sefer doğru aralığı tuttur")