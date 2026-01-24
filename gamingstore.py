from colorama import Fore, Style, init


print(f"{Fore.CYAN}{Style.BRIGHT}✨ HELLO  Welcome to the  marryGen gaming store ✨")


print(f"\n{Fore.MAGENTA}{Style.BRIGHT}==========================================")
print(f"{Fore.MAGENTA}{Style.BRIGHT}║   🎧 earphone Instock list in here ⬇️ ⬇️ ║")
print(f"{Fore.MAGENTA}{Style.BRIGHT}==========================================")
instocktype=["gaming earphone","gaming headphone"]
for a in instocktype:
    print(a) 
userchoice =(input("which one do u want to choice?"))
if  userchoice=="gaming earphone":
    userchoicemodel=input(f"{Fore.GREEN}hyperx2,razerprov2,plextone21:{Fore.RESET}")
    if userchoicemodel=="hyperx2":
        useserchoicecolor=input("instock black color price230k - red color out of stock but when you want to buy preorder u can type red ").lower()
        if useserchoicecolor=="red":
            print(f"{Fore.YELLOW}Red color is current out of stock!{Fore.RESET}")
        preorder=input("do you want to buy perorder for red color?(yes/no):")
        if preorder.lower()=="yes":
            print(f"{Fore.CYAN}PRE order confirmed for Red color hypex10% off price 210k{Fore.RESET}")
        elif useserchoicecolor=="black":
            order=input("do you want to order black color?(yes/no):")
            if order.lower()=="yes":
                print(f"{Fore.CYAN}You order confirmed price 230k✅✅")    
    elif userchoicemodel.lower()=="razerprov2":
            print(f"{Fore.GREEN}IN stock razerprov2 price200k- COLOR GREEN🐍")
            order=input("do you want to order?(yes/no):")
            if order.lower()=="yes":
                print(f"{Fore.CYAN}You order confirmed✅✅")
    elif userchoicemodel.lower()=="plextone21":
            print(f"{Fore.GREEN}IN stock  price 120k plextone21s")
            order=input("do you want to order?(yes/no):")
            if order.lower()=="yes":
                 print(f"{Fore.CYAN}You order confirmed✅✅")
elif    userchoice=="gaming headphone":
            print(f"{Fore.GREEN}IN Stock FAZE gaming headphoneG40 price-300k")
            order=input("do u want to order?(yes/no):")
            if order.lower()=="yes":
                headphonetype=input(f"{Fore.GREEN}u can choice typec or 3.5mm same price(typec/3.5mm)")
                if headphonetype=="typec":
                    print(f"{Fore.CYAN}You order confirmed✅✅")
                elif  headphonetype=="3.5mm":
                 print(f"{Fore.CYAN}You order confirmed✅✅")
print(f"{Fore.CYAN}{Style.BRIGHT}please check your order list ✔️") 
items = {
    "hyperx2black": 230000,
    "hyperx2red": 210000,
    "razerprov2": 200000,
    "plextone21": 120000,
    "fazeheadphoneg40": 300000
}
total = 0
cart = []

print("\n--- Available Items ---")
for name, price in items.items():
    print(f"{name} : {price} MMK")

while True:
    choice = input("\nEnter item name (or type 'done' to finish): ").lower()

    if choice == "done":
        break

    if choice in items:
        total += items[choice]
        cart.append(choice)
        print(f"✅ Added {choice} ({items[choice]} MMK)")
    else:
        print("❌ Item not found, try again")

print("\n🛒 Your Order List")
for item in cart:
    print(f"- {item} : {items[item]} MMK")

print(f"\n💰 Total Amount = {total} MMK")
print("order completed")