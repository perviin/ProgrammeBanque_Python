def print_border():
    print("*********************")

def show_balance(balance):
    print_border()
    print(f"Votre balance est de ${balance:.2f}")
    print_border()

def deposit():
    return get_valid_amount("Montant à déposer: ")

def withdraw(balance):
    amount = get_valid_amount("Montant à retirer: ")
    if amount > balance:
        print("Fonds insuffisants.")
        return 0
    return amount

def get_valid_amount(prompt):
    while True:
        try:
            amount = float(input(prompt))
            if amount >= 0:
                return round(amount, 2)
            print("Montant invalide.")
        except ValueError:
            print("Entrée invalide.")

def main():
    name = input("Entrez votre prénom: ") + " " + input("Entrez votre nom: ")
    print_border()
    print(f"Bonjour, {name}")
    print_border()
    balance = 0.0
    
    while True:
        print("1. Voir Balance\n2. Déposer\n3. Retirer\n4. Quitter")
        choice = input("Que souhaitez-vous faire ? (1-4): ")
        
        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            print_border()
            print("Merci d'avoir utilisé notre programme")
            print_border()
            break
        else:
            print("Choix invalide.")

if __name__ == '__main__':
    main()
