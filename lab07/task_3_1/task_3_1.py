# Інтерфейс TypeCCharger
class TypeCCharger:
    def get_output_voltage(self):
        raise NotImplementedError()

    def get_output_amperage(self):
        raise NotImplementedError()


# Пристрій FastCharge (Type-C зарядний пристрій)
class FastCharge(TypeCCharger):
    def get_output_voltage(self):
        return 20

    def get_output_amperage(self):
        return 3


# Інтерфейс MicroUsbCharger
class MicroUsbCharger:
    def get_output_voltage(self):
        raise NotImplementedError()

    def get_output_amperage(self):
        raise NotImplementedError()


# Адаптер MicroUSB → Type-C (через агрегацію)
class AdapterMicroUsbToTypeC(TypeCCharger):
    def __init__(self, micro_usb_charger):
        self.micro_usb_charger = micro_usb_charger

    def get_output_voltage(self):
        return self.micro_usb_charger.get_output_voltage()

    def get_output_amperage(self):
        return self.micro_usb_charger.get_output_amperage()


# Адаптер Type-C → MicroUSB (через агрегацію)
class AdapterTypeCToMicroUsb(MicroUsbCharger):
    def __init__(self, type_c_charger):
        self.type_c_charger = type_c_charger

    def get_output_voltage(self):
        return self.type_c_charger.get_output_voltage()

    def get_output_amperage(self):
        return self.type_c_charger.get_output_amperage()


# Телефон SamsungS, який підтримує Type-C
class SamsungS:
    def charge(self, charger: TypeCCharger):
        voltage = charger.get_output_voltage()
        amperage = charger.get_output_amperage()
        print(f"SamsungS is charging with {voltage}V / {amperage}A")


# Телефон старого зразка, який очікує MicroUSB
class MobilePhone:
    def charge(self, charger: MicroUsbCharger):
        voltage = charger.get_output_voltage()
        amperage = charger.get_output_amperage()
        print(f"Old phone is charging with {voltage}V / {amperage}A")


# Тестування
if __name__ == "__main__":
    fast = FastCharge()
    samsung = SamsungS()
    samsung.charge(fast)  # напряму через Type-C

    # Адаптер Type-C до MicroUSB для старого телефону
    adapter_to_micro = AdapterTypeCToMicroUsb(fast)
    old_phone = MobilePhone()
    old_phone.charge(adapter_to_micro)
