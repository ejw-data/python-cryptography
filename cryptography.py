# http://www.crypto-it.net/eng/simple/caesar-cipher.html
import getpass
import random

def encrypt(text, KEY = 3):
  '''
  Function for encrypting text
  '''

  encrypted = ""
  for ch in text:
    if ord(ch) >= ord('a') and ord(ch) <= ord('z'):
      newCode = ord(ch) + (KEY % 26)
      if (newCode > ord('z')):
        newCode -= 26
      encrypted += chr(newCode)
    elif ord(ch) >= ord('A') and ord(ch) <= ord('Z'):
      newCode = ord(ch) + (KEY % 26)
      if (newCode > ord('Z')):
        newCode -= 26
      encrypted += chr(newCode)
    else:
      encrypted += " "
  return encrypted

def decrypt(text, KEY = 3):
  '''
  Function for decrypting text.
  '''

  decrypted = ""
  for ch in text:
    if ord(ch) >= ord('a') and ord(ch) <= ord('z'):
      newCode = ord(ch) - (KEY % 26)
      if (newCode < ord('a')):
        newCode += 26
      decrypted += chr(newCode)
    elif ord(ch) >= ord('A') and ord(ch) <= ord('Z'):
      newCode = ord(ch) - (KEY % 26)
      if (newCode < ord('A')):
        newCode += 26
      decrypted += chr(newCode)
    else:
      decrypted += " "
  return decrypted

def encrypted_messages():
  '''
  Used to send and receive encrypted messages.
  '''

  key_public_a = random.randrange(10,100,1)
  key_private_a = random.randrange(10,100,1)
  print(f"\nYour Public Key is:  {key_public_a}")
  print(f"Your Private Key is hidden")

  
  key_public_b = int(input("\nAsk Person B for their public key, Enter here: "))
  key_part_a = (key_public_a**key_private_a) % key_public_b

  print(f"\nSend them your key part:  {key_part_a}")

  # key_part_b = int(input("Ask Person B for their Key Part, Enter here: "))
  key_part_b = int(getpass.getpass("Ask Person B for their Key Part.\n\
You will not see the text when typing.  Enter here: "))
  key_full_a = (key_part_b**key_private_a) % key_public_b

  print(f"\nSender/Receiver Key Matches")

  allowed_invalid_reponses = 3
  auto_exit = 0

  menu = 4
  while menu != 3:
      menu = int(input(f"\nWhat would you like to do now.  Select from these options:\n \
(1) Encrypt message\n \
(2) Decrypt message\n \
(3) End Program\n \
Enter only the number here:  "))

      if (menu == 1):
          message = input(f"\n Enter message here:\n ")
          encrypted = encrypt(message, KEY = key_full_a)
          print(f"\n Send this encrypted message to them:\n {encrypted}")
          auto_exit = 0
      elif (menu == 2):
          message = input(f"\n Enter the encrypted message here:\n ")
          decrypted = decrypt(message, KEY = key_full_a)
          print(f"\n The decrypted message reads:\n {decrypted}")
          auto_exit = 0
      elif (menu ==3):
          print(f"\n Closing Program.  A new public key and key part will need to be shared next time.\n")
      else:
          auto_exit += 1
          if (auto_exit == allowed_invalid_reponses):
              print(f"{allowed_invalid_reponses} invalid responses.  Program exiting now.")
              menu = 3
          elif (auto_exit > 1):
              print(f"Warning:  Invalid Response.  Only enter 1,2,3.  You have {allowed_invalid_reponses - auto_exit} \
                tries left before program automatically closes.")
          else:
              print(f"I'm sorry but your response is unclear.  You can enter 1,2, or 3 only. Try again.")
        


def logic_test():
  '''
  Used for inputing different values to test the functionality of the code.
  '''
  key_public_a = 20
  key_private_a = 26
  key_public_b = 13
  key_private_b = 17

  allowed_invalid_reponses = 3
  auto_exit = 0
  continue_test = True

  while continue_test:

      print(f"\nThese are the values that have been entered:\n")
      print(f"Public Key A:  {key_public_a}")
      print(f"Private Key A:  {key_private_a}")
      print(f"Public Key B:  {key_public_b}")
      print(f"Private Key B:  {key_private_b}")

      key_part_a = (key_public_a**key_private_a) % key_public_b
      key_part_b = (key_public_a**key_private_b) % key_public_b

      print(f"Partial Key for A is {key_part_a} and Partial Key for B is {key_part_b}.")

      key_full_a = (key_part_b**key_private_a) % key_public_b
      key_full_b = (key_part_a**key_private_b) % key_public_b

      print(f"Full Key for A is {key_full_a} and Full Key for B is {key_full_b}.")

      menu = input(f"\nDo you want to enter your own values to test? (y/n): ")
      menu_valid = menu.upper()
      if (menu_valid == "Y" or menu_valid == "YES" or menu_valid == "1"):
          key_public_a = int(input(f"Submit a public key number ( <100 ) for person A:  "))
          key_private_a = int(input(f"Submit a private key number ( <100 ) for person A:  "))
          key_public_b = int(input(f"Submit a public key number ( <100 ) for person B:  "))
          key_private_b = int(input(f"Submit a private key number ( <100 ) for person B:  "))
          auto_exit = 0

      elif (menu_valid =="N" or menu_valid == "NO" or menu_valid == "0"):
          print(f"\nClosing program.\n")
          continue_test = False

      else:
        auto_exit += 1
        if (auto_exit == allowed_invalid_reponses):
            print(f"{allowed_invalid_reponses} invalid responses.  Program exiting now.")
            continue_test = False
        elif (auto_exit > 1):
            print(f"Warning:  Invalid Response.  Only enter 1,2,3.  You have {allowed_invalid_reponses - auto_exit} \
              tries left before program automatically closes.")
        else:
            print(f"I'm sorry but your response is unclear.  You can enter 'y' or 'n'. Try again.")
          
print(f"\n\nSelect which program to run:\n")
choice = int(input(f"(1) Add Person A and B Keys for Testing\n\
(2) Share Code with a Friend and Practice Sending Messages\n\
(3) End Program\n\
Enter Selection (1,2,3):  ") )

if (choice == 1):
  logic_test()
elif (choice == 2):
  encrypted_messages()
else:
  print("\nProgram Closing...\n")
