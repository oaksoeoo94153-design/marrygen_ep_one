oflash_items = ["GAMING EARPHONES", "GAMING HEADPHONES"]

for item in flash_items:
    for _ in range(3):
        os.system('clear') # Screen 
        print("\n\n") #
        print(f"{Fore.RED}{Style.BRIGHT}{item}".center(50))
        time.sleep(0.5) #
        
        os.system('clear') # Screen 
        time.sleep(0.3) # 

print(f"{Fore.CYAN}{Style.BRIGHT}--- ALL ITEMS 
