## Уравнения Татаринова для треугольной платформы на рояльных колесах

### Описание 

#### Уравнениния:

![main_eq](imgs/tatarinov.gif)
 
где:
 
 -  ![1](imgs/poisson_bracket.gif)
 -  ![2](imgs/description1.gif)
 -  ![3](imgs/description2.gif) 
 
[Описание уравнение](http://elibrary.udsu.ru/xmlui/bitstream/handle/123456789/9494/Zobova.pdf) (Александра Александровна Зобова)

### Установка

Склонировать репозиторий:
```shell script
git clone https://github.com/git-alice/tatarinov_equation.git
```

Установить зависимости
```shell script
pip install -r requirements.txt
```

Установить локально в режиме editable:
```shell script
pip install -e .
```

###  TODO:
Так как в пакете `sympy` есть встроенный модуль [mechanics](https://docs.sympy.org/latest/modules/physics/mechanics/index.html), о котором я поздно узнал, то классы и логику в какой-то степени можно переписать используя данные возможности.
 