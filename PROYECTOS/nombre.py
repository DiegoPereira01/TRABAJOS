def ejercicio3(name,lastname,country):
    if name:
        return f"Hello, {name} {lastname} from {country}!"
    else:
        return "Hello, world!"

if __name__ == "__main__":
    user_name = input("Nombre: ")
    if user_name!="":
        user_lastname = input("Apellido: ")
        user_country = input("Pais: ")       
        greeting = ejercicio3(user_name,user_lastname,user_country)
    else:
        greeting = ejercicio3(user_name,"","")
    print(greeting)