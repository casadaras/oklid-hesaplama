Merhaba, bu proje Kodluyoruz: IBM SkillsBuild Cyberstart programı 2.hafta Python kodlama ödevidir.

Bu proje öklid mesafesini hesaplar.
Öklid mesafesi nedir? Öklid uzayındaki iki nokta arasındaki "sıradan" düz çizgi mesafesidir. 
Bu formül ile, düzlemde veya üç boyutlu uzayda iki nokta arasındaki mesafeyi bulabiliyoruz.


Not: Projede "min" fonksiyonunu kullandım. "min" fonksiyonu kullanılmadan "for" döngüsüyle;
```py
points = [(1, 5), (5, 8), (8, 1), (9, 5)]
def euclideanDistance(kordinat1, kordinat2):
    return pow(pow(kordinat1[0] - kordinat2[0], 2) + pow(kordinat1[1] - kordinat2[1], 2), 0.5)
distances = []
min_distances = float("inf")
for _ in range(len(points) -1):
    for i in range(_ + 1, len(points)):
        distances = euclideanDistance(points[_], points[i])
        if distances < min_distances:
            min_distances = distances        
print("Minimum mesafe:", min_distances)
```

şeklinde kodlanabilir.
