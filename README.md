# модуль для решения квадратных уравнений

## модуль quadratic_equation.py вычисляет корни квадратного уравнения

### как использовать:

+ При импортировании модуля *quadratic_equation.py* используйте функцию *get_ruts(a,b,c)* 
+ если *discriminant блоьше 0* функция вернет два решения, 
+ если *discriminant равен 0* функция возвращает одно решение и объект None, 
+ если *discriminant меньше 0* функция вернет два обьекта None

### особенности кода:

+ функции вычисляют корни уравнения при обращении к ним

```python
root1(a, b, discriminant)
root2(a, b, discriminant)
```
---

#### импорт функции:

```python
from quadratic_equation import get_roots
```
#### пример использования функции:

```python
get_roots(1, -2, 1)
```
---

## Как запустить

+ Интерпретатора Python 3.5

+ Запуск на Linux:

```bash
python tests.py # может понадобиться вызов python3 вместо python, зависит от настроек операционной системы
```

+ Запуск на Windows происходит аналогично.

# Цели проекта

+ Код создан в учебных целях. В рамках учебного курса по веб-разработке ― [DEVMAN.org](https://devman.org)
