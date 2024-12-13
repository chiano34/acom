import os

import matplotlib.pyplot as plt
import numpy as np
import Prewitt
import Roberts
import Scharr
import cv2
from matplotlib import pyplot as plt
import time

saving=False
def save_image(image, folder_path, file_name):
    cv2.imwrite(folder_path+file_name+".jpg", image)

def apply_canny(image_path, gaussian_size, thresholds, sigma):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    blurred = cv2.GaussianBlur(img, (gaussian_size, gaussian_size), sigma)
    edges = cv2.Canny(blurred, thresholds[0], thresholds[1])
    return edges

##### Оставляю здесь лучшие параметры для каждого из методов, чтобы проще в отчёт вносить
##### Канни с собелем: Ядро 5 сигма 2 нижний 50 верхний 150
##### Канни с собелем: Ядро 3 сигма 1 нижний 100 верхний 200 - оба хороши, выбирай сам
##### Канни с Прюиттом: Ядро 3 сигма 1 нижний 30 верхний 90
##### Канни с Робертсом: Ядро 3 сигма 1 нижний 30 верхний 90

##### Ядро общее для всех
gaussian_sizes = [(3,1), (5,2), (7,3)]# (3,1) 3 ядро гаусса и 1 параметр сигма

##ЗАДАНИЕ
## протестировать алгоритм Канни c 3 различными параметрами
## размытия Гаусса, на 3-5 изображениях, выделить оптимальный параметр,
## Ядро 5 сигма 2 вроде лучший результат

####ЭТОТ метод пусть будет, он является частью задания, но в целом, следующий метод включает эти примеры в себя
def visualize_canny_small():
    image_paths = ['1.jpg', '2.jpg', '3.jpg','4.jpg','5.jpg']
    for image_path in image_paths:
        for gaussian_size in gaussian_sizes:
            edges = apply_canny(image_path, gaussian_size[0], (50,150),gaussian_size[1])
            plt.imshow(edges, cmap='gray')
            plt.title(f'Gaussian Size: {gaussian_size[0]}, Sigma: {gaussian_size[1]}, Thresholds: 50,150')
            plt.axis('off')
            plt.show()

##ЗАДАНИЕ
##протестировать алгоритм Канни для каждого из параметров прошлого
##пункта, выбрав по 3 различных пары пороговых значений, итого 9 тестов для
##каждого изображения, выявить оптимальные параметры (размытие, пороги
##фильтрации) для выявления границ для каждого из изображений
def visualize_canny_sober():
    thresholds_list = [(50, 150), (100, 200),(150,250)]
    image_paths = ['1.jpg', '2.jpg', '3.jpg','4.jpg','5.jpg']
    for image_path in image_paths:
        for gaussian_size in gaussian_sizes:
            for thresholds in thresholds_list:
                edges = apply_canny(image_path, gaussian_size[0], thresholds, gaussian_size[1])
                global saving
                if saving:
                    save_image(edges,'output/canny/',f'canny size{gaussian_size[0]} sig{gaussian_size[1]} high{thresholds[0]} low{thresholds[1]}')
                plt.imshow(edges, cmap='gray')
                plt.title(f'Sobel operator \nGaussian Size: {gaussian_size[0]}, Sigma: {gaussian_size[1]}, Thresholds: low: {thresholds[0]} high: {thresholds[1]}')
                plt.axis('off')
                plt.show()

##ЗАДАНИЕ
##- протестировать алгоритм Канни, заменив оператор Собеля на любой
##другой оператор, провести 9 тестов на каждое изображение с новым
##оператором;

####ИСПОЛЬЗОВАННЫЙ ОПЕРАТОР - ОПЕРАТОР ПРЮИТТА, ЛУЧШИЕ ПАРАМЕТРЫ В СРЕДНЕМ ДЛЯ ИЗОБРАЖЕНИЙ
####РАЗМЕРА ЯДРА 5, СИГМА 2, НИЖНИЙ ПОРОГ 20, ВЕРХНИЙ 60

####Здесь почему-то возникает ошибка при обработке больше чем 2 картинок
####скорее всего графики переполняют память, хотя в прошлых случаех такого не было,
####очищай список image_paths от лишних картинок
def visualize_canny_prewitt():
    #image_paths2 = ['1.jpg', '2.jpg']
    #image_paths2 = ['3.jpg','4.jpg']
    image_paths2 = ['5.jpg']
    thresholds_list2 = [(10, 30), (20, 60), (30, 90)]
    image_paths2 = ['4.jpg', '3.jpg']
    for image_path in image_paths2:
        for gaussian_size in gaussian_sizes:
            for thresholds in thresholds_list2:
                prewitt=Prewitt.main(image_path,gaussian_size[0],gaussian_size[1],
                                               thresholds[0],thresholds[1])
                global saving
                if saving:
                    save_image(prewitt,'output/prewitt/',f'prewitt size{gaussian_size[0]} sig{gaussian_size[1]} high{thresholds[0]} low{thresholds[1]}')

                plt.imshow(prewitt, cmap='gray')
                plt.title(f'Prewitt operator \nGaussian Size: {gaussian_size[0]}, Sigma: {gaussian_size[1]}, Thresholds: low: {thresholds[0]} high: {thresholds[1]}')
                plt.axis('off')
                plt.show()


##ЗАДАНИЕ
##заменить оператор альтернативой, провести 9 тестов для каждого изображения;

######ИСПОЛЬЗОВАННЫЙ ОПЕРАТОР - ОПЕРАТОР РОБЕРТСА, ЛУЧШИЕ ПАРАМЕТРЫ В СРЕДНЕМ ДЛЯ ИЗОБРАЖЕНИЙ
######Здесь я не рисковал, тоже самое с изображениями что и в прошлом случае, может обработает за раз все 5
######Но лучше по частям
def visualize_canny_roberts():
    #image_paths2 = ['1.jpg', '2.jpg']
    #image_paths2 = ['3.jpg','4.jpg']
    #image_paths2 = ['5.jpg']
    thresholds_list3 = [(10, 30), (20, 60), (30, 90)]
    image_paths3 = ['1.jpg', '2.jpg']
    for image_path in image_paths3:
        for gaussian_size in gaussian_sizes:
            for thresholds in thresholds_list3:
                roberts=Roberts.main(image_path,gaussian_size[0],gaussian_size[1],
                                     thresholds[0],thresholds[1])
                global saving
                if saving:
                    save_image(roberts,'output/roberts/',f'robert size{gaussian_size[0]} sig{gaussian_size[1]} high{thresholds[0]} low{thresholds[1]}')
                plt.imshow(roberts, cmap='gray')
                plt.title(f'roberts operator \nGaussian Size: {gaussian_size[0]}, Sigma: {gaussian_size[1]}, Thresholds: low: {thresholds[0]} high: {thresholds[1]}')
                plt.axis('off')
                plt.show()

##ЗАДАНИЕ
## попробовать реализовать альтернативный способ выявления границ
## для изображений данноготипа,возможновоспользоваться
## готовыми библиотеками,протестировать на тех же изображениях,подобрать

###### ИСПОЛЬЗОВАННЫЙ МЕТОД - ОПЕРАТОРА ЩАРРА - простая свёртка изображения на оператора Щарра
###### как ни странно, очень неплохой результат хотя тут даже блюра нет
def visualize_canny_scharr():
    image = cv2.imread("1.jpg", cv2.IMREAD_GRAYSCALE)
    edges = Scharr.scharr_filter(image)
    save_image(edges,'output/scharr/',f'scharr filter')
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.title('Original Image')
    plt.imshow(image, cmap='gray')
    plt.subplot(1, 2, 2)
    plt.title('Edges Detected with Scharr Operator')
    plt.imshow(edges, cmap='gray')
    plt.show()

    #Читай описание методов перед запуском, много строчек всякого
def main():
    global saving
    #saving=True #Включение режима сохранения изображений на компьютер в папку output
    #visualize_canny_sober()
    #visualize_canny_prewitt()
    #visualize_canny_roberts()
    #visualize_canny_scharr()
    ##ЗАДАНИЕ
    ## провести сравнительный анализ примененного алгоритма с алгоритмом
    ## Канни с оптимальными параметрами, учесть не только качество выявления, но и скорость работы алгоритмов;
    ##### Поскольку отчёт делать не мне,так что сравнивать изображения не буду
    ##### запишу время работы каждого алгоритма на оптимальных параметрах
    image='1.jpg'
    start_sober=time.time()
    apply_canny(image,5,(50,150),2)
    end_sober=time.time()
    start_prewitt=time.time()
    Prewitt.main(image,3,1,30,90)
    end_prewitt=time.time()
    start_robert=time.time()
    Roberts.main(image,3,1,30,90)
    end_robert=time.time()
    img=cv2.imread(image)
    start_scharr=time.time()
    Scharr.scharr_filter(img)
    end_scharr=time.time()
    print(f"Результаты работы алгоритмов в секундах: "
          f"\nКанни с оператором Собеля:{end_sober-start_sober}\n"
          f"\nКанни с оператором Прюитта:{end_prewitt-start_prewitt}\n"
          f"\nКанни с оператором Роберста:{end_robert-start_robert}\n"
          f"\nОператор Щарра:{end_scharr-start_scharr}")

main()