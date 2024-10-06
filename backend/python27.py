#file

# ls=[]

# while True:
#                       a=input("ismnikirit: ")
#                       if a=="0":
#                                             break
#                       else:
#                                             ls.append(a)
# print(ls)


# fl=open('text.txt')#open bu boshqa faylni ochadi
# print(fl.read()) #endi bu faylni ichini o'qimoqchi bo'lsak read qilishiiz kerak
# fl.close()#har bir faylni ochgandan keyin yopish kerak


# with open('text.txt') as fl:#bu depadagini boshqachasi with yaxshi tarafi o'zi ochib yopadi epadagiga o'ziz yopasiz
#                       a=fl.read()
# print(a)


# with open('text.txt',"w") as fl:#write depadagini yozib beradi
#                       w=fl.write('SALOM')
# print(w)

# with open('text.txt',"a") as fl:#a depadagini yozib yonidan qo'shadi beradi faqat o'zi 3ta harfi bor "a","r","w"qo'shadi o'qiydi yozadi
#                       a=fl.write('SALOM')
# print(a)


# while  True:
#                       ism=input("sinfdagi bolalarni kirit: ")
#                       if ism =="0":
#                                             break
#                       else:
#                                             with open('text.txt',"a") as f:
#                                                                   f.write(ism)


#amaliy mashgulot

                      

# with open('text.txt') as f:
#     d  = f.read()
    
# def search(age):
#                       a=input("yoshingni kirit>>> ")

#                       if a in d:
#                                             print('Yoshing bor')
#                       else:
#                                             print("Yoshing yuq")
        
# search('')
                                            
                                            