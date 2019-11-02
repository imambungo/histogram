from matplotlib import pyplot

def histogram(R, G, B):
    "menampilkan histogram berdasarkan kemunculan setiap intensitas RGB"
    intensitas = list(range(11))
    lebar_bar = 0.27
    intensitas = [i-lebar_bar for i in intensitas]
    pyplot.bar(intensitas, R, width=lebar_bar, color='r')
    intensitas = [i+lebar_bar for i in intensitas]
    pyplot.bar(intensitas, G, width=lebar_bar, color='g')
    intensitas = [i+lebar_bar for i in intensitas]
    pyplot.bar(intensitas, B, width=lebar_bar, color='b')
    pyplot.title('Histogram')
    pyplot.xlabel('Intensitas')
    pyplot.ylabel('Kemunculan')
    pyplot.legend(['R', 'G', 'B'])
    pyplot.show()


R = [1, 4, 9, 4, 5, 8, 6, 7, 8, 9, 10]
G = [10, 5, 2, 4, 5, 7, 6, 7, 8, 9, 10]
B = [10, 5, 2, 4, 5, 7, 6, 7, 8, 9, 10]

histogram(R, G, B)
