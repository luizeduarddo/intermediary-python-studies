#Creating functions with *args and **kwargs
def show_verse(date, *args, **kwargs):
    text = "\n".join(args)
    metadata = "\n".join([f"{key.title()}:{value}" for key, value in kwargs.items()])
    message = f"{date} \n\n{text}\n\n{metadata}"

    print(message)

show_verse(
    "Friday, August, 19th, 2023" #First the program selects the date that will be the first argument
    "Sementes",                  #Then everything that comes between "" and followed by a , is understood as *args
    "Não jogue fora as sementes",
    "Guarde pra mim por favor",
    "Vou transformar as sementes",
    "Numa semente de amor",
    "Eu quero ver se eu consigo",
    "Fazer a transformação",
    "Eu quero ver se eu consigo",
    "Plantar amor pelo chão",
    "Amor pro meu corpo, amigo",
    "Amor pro seu coração",
    "Amor pro resto do mundo",
    "Se somos todos irmãos", #Last value of *args
    autor=" Marcelo D2", #Here as they are are informed like key and value, the program undestands that are **kwargs
    year=" 2021",
)