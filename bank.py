class Bank:
    def __init__(self):
        self.akun = {"user1": {"password": "apaaja", "saldo": 50000},
                        "user2": {"password": "katakata", "saldo": 100000}}

    def login(self, username, password):
        if username in self.akun and password == self.akun[username]["password"]:
            return True
        else:
            return False

    def transfer(self, sender, recipient, amount):
        if sender in self.akun and recipient in self.akun:
            if self.akun[sender]["saldo"] >= amount:
                self.akun[sender]["saldo"] -= amount
                self.akun[recipient]["saldo"] += amount
                print("Transfer sukses. Saldo akhir:", self.akun[sender]["saldo"])
            else:
                print("Insufficient funds.")
        else:
            print("Invalid account(s).")

    def tarikTunai(self, username, amount):
        if username in self.akun:
            if self.akun[username]["saldo"] >= amount:
                self.akun[username]["saldo"] -= amount
                print("Tarik tunai sukses. Saldo akhir:", self.akun[username]["saldo"])
            else:
                print("Insufficient funds.")
        else:
            print("Invalid account.")

    def Tabungan(self, username, amount):
        if username in self.akun:
            self.akun[username]["saldo"] += amount
            print("Tabungan sukses. Saldo akhir:", self.akun[username]["saldo"])
        else:
            print("Invalid account.")


def main():
    bank = Bank()
    attempts = 3

    while attempts > 0:
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")

        if bank.login(username, password):
            print("Login sukses. ")
            break
        else:
            attempts -= 1
            print(f"Invalid credentials. {attempts} attempts left.")

    if attempts == 0:
        print("Too many unsuccessful login attempts. Exiting program.")
    else:
        while True:
            print("\nOptions:")
            print("1. Transfer")
            print("2. Tarik tunai")
            print("3. Menabung")
            print("4. Exit")

            choice = input("Enter your choice (1-4): ")

            if choice == "1":
                sender = username
                recipient = input("Masukkan username penerima: ")
                amount = float(input("Masukkan saldo: "))
                bank.transfer(sender, recipient, amount)
            elif choice == "2":
                amount = float(input("Masukkan saldo tarik: "))
                bank.tarikTunai(username, amount)
            elif choice == "3":
                amount = float(input("Masukkan saldo tabungan: "))
                bank.Tabungan(username, amount)
            elif choice == "4":
                print("Exiting program.")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()
