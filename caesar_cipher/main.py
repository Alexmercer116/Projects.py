from art import logo
print(logo)
from caesar import ceaser
caesar_cipher=True
while(caesar_cipher):
   action = input("Use Caesar Cipher for[encode/decode]: ")
   msg = input("Type your message:\n")
   key = int(input("Enter key:\n"))
   caesar_text= ceaser(msg,key,action)
   print(f"Your {action}d text is {caesar_text}.")
   try_again=input("Want to try again[Y/N]?")
   if(try_again in 'nN'):caesar_cipher=False


