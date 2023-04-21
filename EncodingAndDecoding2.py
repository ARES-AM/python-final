print('''                Welcome Agent''')
x=int(input("Enter encoding or decoding code"))


try:
    if x==1 or x==0 or x==2:
        if x==1:
                # encode
                x=input("Enter your message")
                y=x[::-1]
                z=y.split(" ")
                a='skdjfk'
                b='sdff'
                for i in range(0,len(z)):
                    if i%2==0:
                        z.insert(i,"sojss")


                ans=' '.join(z)
                Ciphertext=a + ' '+ ans +' '+ b
                print(Ciphertext)
        elif x==0:
            # decode
            x = input("Enter the Ciphertext ")
            step1 = x.replace("skdjfk", "")
            step2 = step1.replace("sdff", "")
            step3 = step2.split()
            # sojss uoy sojss ebol i
            count = 0
        
            for i in range(0, len(step3)-2):
                if i % 2 == 0:

                    z = count

                    
                    if count % 2 == 0:
                        step3.pop(count)

                    else:

                        step3.pop(count)

                    count = z+1


            step4 = ' '.join(step3)
            step5 = step4[::-1]
            print(step5)

        else:
            print("Good bye mate")
    
        
    
except:
    print("SPY ALERT!!!")
