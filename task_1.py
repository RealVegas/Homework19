class Animal:

    def __init__(self, name: str, age: int | None = None) -> None:
        self.name = name
        self.age = age

    def _eat_someone(self) -> None:
        print(f'{self.name} кого-то съел')

    def make_sound(self) -> None:
        pass


class Bird(Animal):
    def make_sound(self) -> None:
        print('Чик-чирик')


class Mammal(Animal):
    def make_sound(self) -> None:
        print('Myр-мур')


class Reptile(Animal):
    def make_sound(self) -> None:
        print('Шшш-шшш')


def animal_noise(animal_list: list[Animal]) -> None:
    for animal in animal_list:
        print(animal.name, end=' - ')
        animal.make_sound()


animals = [Bird('Птичка'), Mammal('Киска'), Reptile('Змейка')]
animal_noise(animals)