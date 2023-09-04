def ceaser(msg,key,action):
  final_txt=""
  if(action.lower()=='decode'):
      key*=-1
  for i in msg:
    if(i.isalpha()):
      if(i.isupper()):base=ord('A')
      else:base=ord('a')
      final_txt+=chr((ord(i)-base+key)%26+base)
    else:final_txt+=i
  return final_txt
