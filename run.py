from game import *
from colorama import Fore


def main() -> None:
    """Main function to start the game
    """

    logo = [
        # Game logo
        """
        Welcome To :
              __            _        ___                            
             /__\ ___   ___| | __   / _ \__ _ _ __  _ __   ___ _ __ 
            / \/// _ \ / __| |/ /  / /_)/ _` | '_ \| '_ \ / _ \ '__|
           / _  \ (_) | (__|   <  / ___/ (_| | |_) | |_) |  __/ |   
           \/ \_/\___/ \___|_|\_\ \/    \__,_| .__/| .__/ \___|_|   
                                             |_|   |_|              
          __                                  __ _                  _ 
         / _\ ___ ___  ___ ___  ___  _ __    / /(_)______ _ _ __ __| |
         \ \ / __/ _ \/ __/ __|/ _ \| '__|  / / | |_  / _` | '__/ _` |
         _\ \ (_|  __/\__ \__ \ (_) | |    / /__| |/ / (_| | | | (_| |
         \__/\___\___||___/___/\___/|_|    \____/_/___\__,_|_|  \__,_|
                                                                      
                            __                  _    
                           / _\_ __   ___   ___| | __
                           \ \| '_ \ / _ \ / __| |/ /
                           _\ \ |_) | (_) | (__|   < 
                           \__/ .__/ \___/ \___|_|\_\
                              
                              |_|    
   
        """
    ]

    print(f"{Fore.BLUE}{logo[0]}")

    user_name = Game.get_user_name()
    game = Game(user_name)

    print(Fore.YELLOW + '\n       ---Game Rules---\n')
    print(Fore.YELLOW + ' -Scissors decapitate Lizard.\n')
    print(Fore.YELLOW + ' -Scissors cuts paper.\n')
    print(Fore.YELLOW + ' -Paper covers rock.\n')
    print(Fore.YELLOW + ' -Rock crushes lizard.\n')
    print(Fore.YELLOW + ' -Lizard poisons Spock.\n')
    print(Fore.YELLOW + ' -Spock smashes scissors.\n')
    print(Fore.YELLOW + ' -Scissors decapitates lizard.\n')
    print(Fore.YELLOW + ' -Lizard eats paper.\n')
    print(Fore.YELLOW + ' -Paper disproves Spock.\n')
    print(Fore.YELLOW + ' -Spock vaporizes rock.\n')
    print(Fore.YELLOW + ' -Rock crushes scissors.\n')
    print(Fore.BLUE + '------You will play 5 Rounds------\n')
    print(Fore.WHITE + "Press [Enter] to start:")
    _ = input()
    game.play()
    print(Fore.YELLOW + '+++++++++++++The End++++++++++++\n')
    game.restart()


if __name__ == '__main__':
    main()
