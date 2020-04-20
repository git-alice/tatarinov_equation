## Уравнения Татаринова для треугольной платформы на рояльных колесах

### Описание 

#### Уравнениния:
<img src="https://latex.codecogs.com/gif.latex?\frac{d}{dt} \frac{\partial L*}{\partial \omega_{\alpha}} + \{P_{\alpha}, L*\} = \{P_{\alpha}, \sum_{\mu}{\omega_{\mu} P_{\mu}} \} + \sum_{i}{Q_i \frac{\partial v_i}{ \partial \omega_{\alpha}}}"/> 
где 
 - <img src="https://latex.codecogs.com/gif.latex?\{f, g\} = \sum_{i=1}^{N} \left( \frac{\partial f}{\partial q_{i}} \frac{\partial g}{\partial p_{i}} - \frac{\partial f}{\partial p_i} \frac{\partial g}{\partial q_i}\right)"/>
 -  <img src="https://latex.codecogs.com/gif.latex?\sum_{\alpha}{P_{\alpha} \omega_{\alpha}} = \sum_i{p_iv_i}"/>
 -  <img src="https://latex.codecogs.com/gif.latex?v_i = \dot{q}"/>
[Описание уравнение (А.А. Зобова)](http://elibrary.udsu.ru/xmlui/bitstream/handle/123456789/9494/Zobova.pdf)

### Установка

Склонировать репозиторий:
```shell script
git clone https://github.com/git-alice/tatarinov_equation.git
```

Установить 
```shell script
pip install -r requirements.txt
```

Установить локально в режиме editable:
```shell script
pip install -e .
```

###  TODO:
Так как в пакете `sympy` есть встроенный модуль mechanics, о котором я поздно узнал, то классы и логику в какой-то степени можно переписать используя данные возможности.
 