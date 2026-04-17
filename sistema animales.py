class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print("Este animal hace un sonido.")

class Perro(Animal):
    def hablar(self):
        print(f"{self.nombre} dice: ¡Guau!")

class Gato(Animal):
    def hablar(self):
        print(f"{self.nombre} dice: ¡Miau!")

class Gallina(Animal):
    def hablar(self):
        print(f"{self.nombre} dice: ¡Co Co ro Co!")

# Instanciamos y llamamos al mismo método
animales = [Perro("Rex"), Gato("Mishi"), Gallina("Turuleca")]
for animal in animales:
    animal.hablar()
