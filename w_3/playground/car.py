import sys
import csv
import os.path


class BaseCar:
    # Indexes in csv
    car_type_idx = 0
    brand_idx = 1
    passenger_seats_count_idx = 2
    photo_file_name_idx = 3
    body_whl_idx = 4
    carrying_idx = 5
    extra_idx = 6

    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = float(carrying)

    def get_photo_file_ext(self):
        photo, ext = os.path.splitext(self.photo_file_name)
        return ext


class Car(BaseCar):

    car_type = 'car'

    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.passenger_seats_count = int(passenger_seats_count)

    @classmethod
    def instance(cls, row):
        return cls(
            row[cls.brand_idx],
            row[cls.photo_file_name_idx],
            row[cls.carrying_idx],
            row[cls.passenger_seats_count_idx],
        )


class Truck(BaseCar):

    car_type = 'truck'

    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)

        try:
            length, width, height = (float(i) for i in body_whl.split('x', 2))
        except ValueError:
            length, width, height = .0, .0, .0

        self.body_length = length
        self.body_width = width
        self.body_height = height

    def get_body_volume(self):
        return self.body_width * self.body_height * self.body_length

    @classmethod
    def instance(cls, row):
        return cls(
            row[cls.brand_idx],
            row[cls.photo_file_name_idx],
            row[cls.carrying_idx],
            row[cls.body_whl_idx],
        )


class SpecMachine(BaseCar):

    car_type = 'spec_machine'

    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.extra = extra

    @classmethod
    def instance(cls, row):
        return cls(
            row[cls.brand_idx],
            row[cls.photo_file_name_idx],
            row[cls.carrying_idx],
            row[cls.extra_idx],
        )


def get_car_list(csv_filename):
    with open(csv_filename) as table:
        reader = csv.reader(table, delimiter=';')

    # skip titles
        next(reader)

        car_list = []

        car_dict = {
            car_class.car_type: car_class for car_class in (Car, Truck, SpecMachine)
        }

        for row in reader:
            try:
                car_type = row[BaseCar.car_type_idx]
            except IndexError:
                continue

            try:
                car_class = car_dict[car_type]
            except KeyError:
                continue

            try:
                car_list.append(car_class.instance(row))
            except (ValueError, IndexError):
                pass

    return car_list


if __name__ == '__main__':
    print(get_car_list(sys.argv[1]))
