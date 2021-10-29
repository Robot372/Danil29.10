print("Kivi,Paber,Käärid")
import random
while True: # обратите внимание на эту строку кода
    user_action = input("Tee valik — kivi, paber või käärid: ")
    possible_actions = ["kivi", "paber", "käärid"]
    computer_action = random.choice(possible_actions)
    print(f"\nTe valisite {user_action}, arvuti valis {computer_action}.\n")
    if user_action == computer_action:
        print(f"Mõlemad mängijad võitsid {user_action}. Viik!!")
    elif user_action == "kivi":
        if computer_action == "käärid":
            print("Kivi lööb kääre! Te võitsite!")
        else:
            print("Paber ümbritseb kivit! Te kaotasite.")
    elif user_action == "paber":
        if computer_action == "kivi":
            print("Paber ümbritseb kivit! Te võitsite!")
        else:
            print("Käärid lõikavad paberit! Te kaotasite.")
    elif user_action == "käärid":
        if computer_action == "paber":
            print("Käärid lõikavad paberit! Te võitsite!")
        else:
            print("Kivi lööb kääre! Te kaotasite.")
# Tähelepanu
    play_again = ""
    play_again = input("Mängime veel kord? (jah/ei): ")
    if play_again.lower() != "jah":
        break 
