import tkinter as tk

windows = tk.Tk()
windows.geometry("600x600")
windows.title("Multilingualism Dictionary")

windows.columnconfigure((0,1,2,), weight=2)
windows.rowconfigure((0,1,2,3,4,5), weight=2)

yoruba_btn = tk.Button(windows, text='Yoruba Dictionary')
yoruba_btn.grid(row=1, column=1)

igbo_btn = tk.Button(windows, text='Igbo Dictionary')
igbo_btn.grid(row=2, column=1)

hausa_btn = tk.Button(windows, text='Hausa Dictionary')
hausa_btn.grid(row=3, column=1)

espanol_btn = tk.Button(windows, text= 'Espanol Dictionary')
espanol_btn.grid(row=4, column=1)

french_btn = tk.Button(windows, text= 'French Dictionary')
french_btn.grid(row=5, column=1)

espanol_dictionary = {
    "hello":"hola",
    "bien":"fine",
    "goodbye":"adiós", 
    "thank you":"gracias",
    "please":"por favor", 
    "yes":"sí" ,
    "no": "no",
    "good":"bueno",
    "bad":"mal",
    "love":"amot",
    "all":"todo",
    "very":"muy",
    "same":"mismo", 
    "equal":"igual",
    "before":"antes",
    "now":"ahora",
    "later":"después",
    "familia": "Family",
    "amigo": "Friend",
    "love":"Amor",
    "house": "Casa",
    "dog": "Perro",
    "cat": "Gato",
    "tree": "Árbol",
    "water": "Agua",
    "food": "Comida",
    "book": "Libro",
    "window": "Ventana",
    "door": "Puerta",
    "sky": "Cielo",
    "sun": "Sol",
    "moon": "Luna",
    "star": "Estrella",
    "table": "Mesa",
    "chair": "Silla",
    "shoe": "Zapato",
    "clothes": "Ropa",
    "street": "Calle",
    "city": "Ciudad",
    "country": "País",
}



igbo_dictionary = {
    "hello": "Ndewo",
    "goodbye": "Ka chi fo",
    "thank you": "Imela",
    "how are you": "Kedu?",
    "i'm fine": "A di mma",
    "water": "Mmiri",
    "food": "Nri",
    "house": "Ụlọ",
    "car": "Oche",
    "tree": "Osu",
    "love": "Ịhụnanya",
    "family": "Ụmụnne",
    "friend": "Enyi",
    "mother": "Nne",
    "father": "Nna",
    "brother": "Nwanne",
    "sister": "Nwanyị",
    "yes": "Ee",
    "no": "Mba",
    "maybe": "Inwere",
    "excuse me": "Kedu kedu",
    "sorry": "Mgbaghara",
    "good morning": "Ụtụtụ ọma",
    "good afternoon": "Ehihie ọma",
    "good evening": "Ụchi ọma",
    "good night": "Ụlọ ọma"
}






windows.mainloop()