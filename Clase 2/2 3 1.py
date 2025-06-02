contra = input("Escriba una contraseña segura ")
num=False
mayu=False

for i in contra:
    if i.isdigit():
        num=True
        
    if i.isupper():
        mayu=True
        
if len(contra)>8 and num==True and mayu==True:
    print("Contraseña segura")
else:
    print("Contraseña no segura")