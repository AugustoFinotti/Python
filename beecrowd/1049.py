carac_1 = input()
carac_2 = input()
carac_3 = input()

if(carac_1 == "vertebrado"):
    if(carac_2 == "ave"):
        if(carac_3 == "carnivoro"):
            animal = "aguia"
        else:
            animal = "pomba"
    else:
        if(carac_3 == "onivoro"):
            animal = "homem"
        else:
            animal = "vaca"
            
else:
    if(carac_2 == "inseto"):
        if(carac_3 == "hematofago"):
            animal = "pulga"
        else:
            animal = "lagarta"
    else:
        if(carac_3 == "hematofago"):
            animal = "sanguessuga"
        else:
            animal = "minhoca"

print(animal)