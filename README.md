# Atividades-Engenharia

## 1. Single Responsibility Principle (SRP)
### O que é?
O SRP afirma que uma classe deve ter apenas uma responsabilidade.
### Para que serve?
Ele ajuda a manter o código modular, facilitando a manutenção, teste e reutilização.
### Exemplo em Python:

<a target="_blank" href="https://github.com/matheusa1/Atividades-Engenharia/blob/main/exemplos/S.py">Exemplo de código </a>

## 2. Open-Closed Principle (Princípio Aberto-Fechado)
### O que é?
O OCP afirma que uma classe deve ser aberta para extensão, mas fechada para modificação.
### Para que serve?
Isso permite que novos comportamentos sejam adicionados sem modificar o código existente.
### Exemplo em Python:
``` py
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

# Exemplo de uso
shapes = [Rectangle(5, 4), Circle(3)]
for shape in shapes:
    print(f"Área da forma: {shape.area()}")]
```
## 3. Liskov Substitution Principle (Princípio da substituição de Liskov)
### O que é?
O LSP afirma que os objetos de uma classe derivada devem poder substituir os objetos de sua classe base sem interromper o funcionamento do programa.
### Para que serve?
Isso garante que o código que usa as classes base continue funcionando corretamente quando objetos de subclasses são passados para ele.
### Exemplo em Python:
```py 
class Bird:
    def fly(self):
        return "Flying"

class Ostrich(Bird):
    def fly(self):
        return "Can't fly"

def bird_fly(bird):
    return bird.fly()

# Exemplo de uso
bird = Bird()
ostrich = Ostrich()

print(bird_fly(bird))   # Saída: "Flying"
print(bird_fly(ostrich))  # Saída: "Can't fly"

```
## 4. Dependency Inversion Principle (Princípio da inversão da dependência)
### O que é?
O DIP afirma que módulos de alto nível não devem depender de módulos de baixo nível. Ambos devem depender de abstrações.
### Para que serve?
Isso permite que os módulos de alto nível sejam independentes das implementações específicas dos módulos de baixo nível, facilitando a substituição e o teste.
### Exemplo em Python:

```py
class PaymentProcessor:
    def process_payment(self, payment_provider):
        return payment_provider.process()

class PaymentProvider:
    def process(self):
        pass

class CreditCardPaymentProvider(PaymentProvider):
    def process(self):
        return "Processing credit card payment"

class PayPalPaymentProvider(PaymentProvider):
    def process(self):
        return "Processing PayPal payment"

# Exemplo de uso
payment_processor = PaymentProcessor()
credit_card_provider = CreditCardPaymentProvider()
paypal_provider = PayPalPaymentProvider()

print(payment_processor.process_payment(credit_card_provider))
print(payment_processor.process_payment(paypal_provider))
```
