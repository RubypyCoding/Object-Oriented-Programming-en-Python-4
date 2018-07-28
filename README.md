## Herencia

Cuando una clase hereda un comportamiento desde otra clase se denomina `herencia`. La clase que está heredando comportamiento se le denomina `subclase` y la clase que le hereda ese comportamiento se llama `superclase`. 

#### Ventajas de la herencia

La posibilidad de crear una nueva clase a partir de una o más clases existentes, heredando de ellas sus atributos y métodos que podrán utilizarse como si estuvieran definidos en la clase hija.

Las clases que en una jerarquía están en un nivel inferior, heredan las características de las clases de niveles superiores; y además, pueden añadir sus propias características.

#### Declarando una subclase

Las clases derivadas se declaran como cualquier clase, después del nombre entre paréntesis se incluye el nombre de la clase superior `(superclase)`.

Por ejemplo, todos los `conejos` y `ratones` son mamíferos. Si todos los mamíferos respiran, la clase `conejo` y la clase `raton` heredan de la clase mamífero esta característica de respirar...

```python
class Mammal:
  def breath(self):
      return 'inspirar, espirar'
 
# la superclase incluida dentro de paréntesis indica que 'Mouse' es una subclase de 'Mammal'
 
class Mouse(Mammal):
  def who_am_i(self):
      return 'Soy un ratón'

# la superclase incluida dentro de paréntesis indica indica que 'Rabbit' es una subclase de 'Mammal'

class Rabbit(Mammal):
  def who_am_i(self):
      return 'Soy un conejo'

 
ratty = Mouse()
robby = Rabbit()
print(ratty.breath())
print(ratty.who_am_i())
print(robby.breath())
print(robby.who_am_i())
```

#### Extracción de comportamientos

En el ejemplo anterior fue posible extraer el comportamiento `breath`, desde clases que comparten ese comportamiento `Mouse` y `Rabbit`, de esta manera es posible moverlo a la superclase `Mammal`. Esta es una manera de mantener la lógica en un sólo lugar.

## Herencia múltiple

Este tipo de herencia se refiere a la posibilidad de crear una clase a partir de múltiples clases superiores `superclases`.

```python
class Phone:
    """Phone class"""
    def __init__(self):
        pass
    def call(self):
        return 'calling'
    def hang_up(self):
        return 'hanging up'        

class Cam:
    """Cam class"""
    def __init__(self):
        pass
    def photograph(self):
        return 'photographing'       

class Play:
    "Mp3 class"
    def __init__(self):
        pass
    def play_mp3(self):
        return 'playing mp3'                 
    def play_video(self):
        return 'playing video'                 

class Movil(Phone, Cam, Play):
	
	#método destructor que se ejecuta al suprimir un objeto
    def __del__(self):
        print('Movil is shutting down...')

movil_1 = Movil()

print(movil_1.play_mp3())
print(movil_1.call())
print(movil_1.photograph())
del movil_1
print(movil_1.play_mp3())
```

## Funciones issubclass() e isinstance()

La función `issubclass(SubClase, ClaseSup)` se utiliza para comprobar si una clase `SubClase` es hija de otra superior `ClaseSup`, retornando `True` o `False`.

```python
print(issubclass(Movil, Phone))
#>> True
print(issubclass(Movil, Play))
#>> True
``` 

La función `isinstance(Objeto, Clase)` se usa para comprobar si un objeto pertenece a una clase o superclase.

```python
print(isinstance(movil_1, Movil))
print(isinstance(movil_1, Phone))
```

## Polimorfismo: Overriding (sobrecarga) de métodos

El `overriding` se refiere a la posibilidad de que una subclase cuente con métodos con el mismo nombre que los de la superclase pero que definan comportamientos diferentes.

En el ejemplo anterior utilizaremos `overriding` para los métodos `__init__` y `play_mp3`.

```python
class Phone:
    """Phone class"""
    def __init__(self):
        pass
    def call(self):
        return 'calling'
    def hang_up(self):
        return 'hanging up'        

class Cam:
    """Cam class"""
    def __init__(self):
        pass
    def photograph(self):
        return 'photographing'       

class Play:
    "Mp3 class"
    def __init__(self):
        pass
    def play_mp3(self):
        return 'playing mp3'                 
    def play_video(self):
        return 'playing video'                 

class Movil(Phone, Cam, Play):
	#overriding __init__ method
	def __init__(self):
		print("Movil is Turning On...")
    
    #overriding play_mp3 method
	def play_mp3(self):
		return 'playing mp3 list now...'

	def __del__(self):
		print('Movil is shutting down...')

movil_1 = Movil()

print(movil_1.play_mp3())
print(movil_1.call())
print(movil_1.photograph())
del movil_1
print(movil_1.play_mp3())

```

## Polimorfismo: Overloading (sobrecarga) de operadores

Trata de los mismo que la sobrecarga de métodos pero pertenece al ámbito de los operadores aritméticos, binarios, de comparación y lógicos.

```python
class Coordinate:
    def __init__(self,x = 0,y = 0):
        self.x = x
        self.y = y

    #overloading operator
    def __add__(self, other_object):
        x = self.x + other_object.x
        y = self.y + other_object.y
        return x, y

punto1 = Coordinate(4, 6)
punto2 = Coordinate(1, -2)
print(punto1 + punto2)
```

## Orden de resolución de métodos (MRO) - Atributo __mro__

Es el orden en que son llamados los métodos de un objeto o instancia. Es importante conocer cómo funciona la herencia en Python cuando existe una jerarquía con varios niveles de clases que pueden tener definidos métodos que usan el mismo nombre.

Un ejemplo con varios niveles de clases:

```python
class A():
    def metodo_1(self):
        print("Clase_A.metodo1()")
        
    def metodo_3(self):
        print("Clase_A.metodo3()")
        
    def metodo_4(self):
        print("Clase_A.metodo4()")

class A1(A):
    def metodo_1(self):
        print("Clase_A1.metodo1()")

    def metodo_2(self):
        print("Clase_A1.metodo2()")

class A2(A):
    def metodo_1(self):
        print("Clase_A2.metodo1()")

    def metodo_3(self):
        print("Clase_A2.metodo3()")

class X(A1, A2):
    def metodo_1(self):
        print("Clase_X.metodo1()")
```

Para calcular el orden de resolución Python utiliza el método MRO (Method Resolution Order) basado en un algoritmo llamado C3. 

El cálculo realizado se puede consultar accediendo al atributo especial __mro__, que devuelve una tupla con las clases por su orden de resolución de métodos (MRO).

```python
print(X.__mro__) 

(<class '__main__.X'>, <class '__main__.A1'>, <class '__main__.A2'>, <class '__main__.A'>, <class 'object'>)
```

De esta manera podemos conocer el orden en que serán ejecutados los métodos:

```python
class A():
    def metodo_1(self):
        print("Clase_A.metodo1()")
        
    def metodo_3(self):
        print("Clase_A.metodo3()")
        
    def metodo_4(self):
        print("Clase_A.metodo4()")

class A1(A):
    def metodo_1(self):
        print("Clase_A1.metodo1()")

    def metodo_2(self):
        print("Clase_A1.metodo2()")

class A2(A):
    def metodo_1(self):
        print("Clase_A2.metodo1()")

    def metodo_3(self):
        print("Clase_A2.metodo3()")

class X(A1, A2):
    def metodo_1(self):
        print("Clase_X.metodo1()")

# Creación de una instancia (objeto) de Clase_X
objeto_1 = X()


objeto_1.metodo_1()
#>> Clase_X.metodo1()
objeto_1.metodo_2()
#>> Clase_A1.metodo2()
objeto_1.metodo_3()
#>> Clase_A2.metodo3()
objeto_1.metodo_4()
#>> Clase_A.metodo4()
```

Podemos observar que el orden en que fueron llamados los métodos desde las clases de las que se heredan esos comportamientos va de acuerdo al orden obtenido a através del atributo `__mro__`.

```python
(<class '__main__.X'>, <class '__main__.A1'>, <class '__main__.A2'>, <class '__main__.A'>, <class 'object'>)
```

## Super

La función super() se utiliza para llamar a métodos definidos en alguna de las clases de las que se hereda sin nombrarla(s) explícitamente, teniendo en cuenta el orden de resolución de métodos (MRO). 

```python
class Computer:
  def __init__(self):
  	pass

  def greeting(self):
    return "Hi, I'm a Computer..."

class Ipad:
  def __init__(self):
  	pass

  def greeting(self):
    return "Hi, I'm an Ipad..."


class Mac(Ipad, Computer):
  def __init__(self):
      pass

  def greeting(self):
    return super().greeting() + " of Mac mark"


macbook_air = Mac()
print(macbook_air.greeting() == "Hi, I'm an Ipad... of Mac mark")      
#=> True

#Verificamos si el orden de resolución es el correcto 

print(Mac.__mro__)

"""Podemos observar que la primera clase superior es Ipad, de la cual va a ejecutar el método 'greeting'"""

```

## Ejercicio - Herencia

Crea las siguientes clases y relaciona con herencia: `Animal`, `Dog`, `SeaTurtle`, `Macaw`, `Fish`, `Dolphin`, `Reptile`, `Cat`, `Whale`, `Snake`, `Mammal`, `Bird` y `Sea`. Es importante usar herencia múltiple.

Define el comportamiento común `sight` que puede ser heredado a todas las clases. Asimismo, revisa el uso de `super` y la jerarquía de herencia para que cada subclase tenga el comportamiento `who_am_i` que heradará de la superclase y regresará un string tal y como se muestra en el ejemplo de código.

Desarrolla el código basado en las pruebas `specs` correspondientes. 


```python
class Animal:
  def __init__(self):
      pass

  def who_am_i(self):
      return "I'm an animal and"

class Sea:
  def __init__(self):
      pass

  def where_i_live(self):
      pass

class Mammal:
  pass   

class Reptile:
  pass

class Bird:
  pass

class SeaTurtle:
  pass

class Dog:
  pass

class Macaw:
  pass

class Fish:
  pass

class Dolphin:
  pass

class Cat:
  pass

class Whale:
  pass

class Snake:
  pass
```

```ruby
#Ejemplo de objeto y salida

macaw = Macaw()
print(macaw.sight())
#>> "I'm seeing..."
print(macaw.who_am_i())   
#>> "I'm an animal and I'm a Bird. I'm a Macaw too."
```

```ruby
#Test Driven Development - TDD
$ test_herencia.py
```

