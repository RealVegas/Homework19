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


class Zookeeper:
    @classmethod
    def feed_animal(cls, animal: Animal) -> None:
        print(f'Сотрудник накормил: {animal.name}')


class Vet:
    @classmethod
    def heal_animal(cls, animal: Animal) -> None:
        print(f'Ветеринар лечит: {animal.name}')


class Zoo:
    def __init__(self,) -> None:
        self.animals = []
        self.staff = []

    def add_animal(self, animal: Animal) -> None:
        self.animals.append(animal)
        print(f'Животное {animal.name} добавлено в зоопарк')

    def get_animals(self) -> list[Animal]:
        return self.animals

    def add_staff(self, staffer) -> None:
        self.staff.append(staffer)
        print(f'В зоопарк устроился новый сотрудник {staffer.__class__.__name__}')


bird = Bird('Обычная кукушка')
mammal = Mammal('Милая киска')
reptile = Reptile('Маленькая змейка')

zoo = Zoo()

veterinarian = Vet()
keeper = Zookeeper()

zoo.add_animal(bird)
zoo.add_animal(mammal)
zoo.add_animal(reptile)
print()
zoo.add_staff(veterinarian)
zoo.add_staff(keeper)
print()


def animal_noise(animal_list: list[Animal]) -> None:
    for animal in animal_list:
        print(animal.name, end=' - ')
        animal.make_sound()


animal_noise(zoo.animals)
print()
keeper.feed_animal(mammal)
veterinarian.heal_animal(reptile)