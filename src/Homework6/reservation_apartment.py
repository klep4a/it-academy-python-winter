"""Создайте  модель из жизни. Это может быть бронирование комнаты
 в отеле, покупка билета в транспортной компании, или простая РПГ.
  Создайте несколько объектов классов, которые описывают ситуацию
   Объекты должны содержать как атрибуты так и методы класса для
    симуляции различных действий. Программа должна инстанцировать
     объекты и эмулировать какую-либо ситуацию - вызывать методы,
      взаимодействие объектов и т.д.
"""

import datetime
from datetime import date


class Apartment(object):
    def __init__(self, adress):
        self.adress = adress
        self.print_welcome(guest.get_first_name())
        self.clean(reservation.get_checkin_date(),
                   reservation.get_checkout_date())
        self.set_agent('Natali')

    def set_agent(self, agent):
        self.agent = agent
        print(f"{agent} will be on call for Apartment {self.adress}")

    def clean(self, checkin_date, checkout_date):
        print(f"Apartment {self.adress} will be cleaned on"
              f" {checkin_date} and {checkout_date}")

    def print_welcome(self, first_name):
        print(f"Welcome at the Apartment {self.adress}, "
              f"{first_name} good stay!")


class Guest(object):
    def __init__(self, first_name, last_name, num_adults, num_children):
        self.first_name = first_name
        self.last_name = last_name
        self.num_adults = num_adults
        self.num_children = num_children

    def get_first_name(self):
        return self.first_name

    def __repr__(self):
        return f'Guest: {self.first_name} {self.last_name} '\
            f'with {self.num_adults - 1 + self.num_children} person'


class Reservation(object):
    def __init__(self, checkin_date, day_stay, adress):
        self.checkin_date = checkin_date
        self.day_stay = day_stay
        self.adress = adress
        self.checkout_date = checkin_date + datetime.timedelta(days=day_stay)

    def get_adress(self):
        return self.adress

    def get_checkin_date(self):
        return self.checkin_date

    def get_checkout_date(self):
        return self.checkout_date

    def __repr__(self):
        return f'Reservation: ({self.checkin_date} ~ {self.checkout_date}, '\
            f'{self.adress})'


class Firma(object):
    apartments = ['Kolasa-9-24', 'Geroev-12-124']
    guest_list = []
    reservation_list = []

    def __init__(self):
        print("Firma Minsk Apartments!")

    def set_guest(self, guest):
        self.guest_list.append(guest)

    def set_reservation(self, reservation):
        if self.apartments:
            for adr in self.apartments:
                if adr.startswith(reservation.adress):
                    self.reservation_list.append(reservation)
                    self.apartments.remove(adr)
        else:
            print('Sorry, no free apartments')

    def print_lists(self):
        print(f"\tThe guest list is: {self.guest_list}")
        print(f"\tThe reservation list is: {self.reservation_list}")
        print(f"\tThe free apartments list is: {self.apartments}")


if __name__ == '__main__':
    firma = Firma()
    # Guest 1
    guest = Guest('Guido', 'Van Rossum', 2, 0)
    firma.set_guest(guest)
    reservation = Reservation(date(2020, 3, 8), 3, 'Kolasa')
    firma.set_reservation(reservation)
    apartment_res = Apartment(reservation.get_adress())
    firma.print_lists()
    # Guest 2
    guest = Guest('Edsger Wybe', 'Dijkstra', 2, 1)
    firma.set_guest(guest)
    reservation = Reservation(date(2020, 3, 8), 5, 'Geroev')
    firma.set_reservation(reservation)
    apartment_res = Apartment(reservation.get_adress())
    firma.print_lists()
