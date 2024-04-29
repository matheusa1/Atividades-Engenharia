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

# neste caso, uma subclasse Ostrich é passada como parâmetro sendo que o parâmetro Bird era o esperado, e ainda funciona
