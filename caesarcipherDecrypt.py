def di(ch) :
 d=("A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z")
 n=3
 ch2=""
 for i in ch :
     if i=='A' or i=='a':
        ch2+='x'
     elif i=='B' or i=='b':
         ch2+='Y'
     elif i=='C' or i=='c':
       ch2+='Z'
     else: 
      for j in range(3,26) :
        if d[j]==i or d[j].casefold()==i:
         ch2+=d[j-n]
 return ch2