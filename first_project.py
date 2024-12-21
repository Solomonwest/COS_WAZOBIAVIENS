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


igbo_words = {
    "Aka": "hand",
    "Anya": "eye",
    "Chineke": "God",
    "Eze": "king",
    "Egwu": "dance",
    "Enyi": "friend",
    "Ego": "money",
    "Ike": "strength",
    "Ife": "thing",
    "Igbo": "Igbo people",
    "Isi": "head",
    "Kedu": "how are you?",
    "Maka": "because",
    "Mmadụ": "person",
    "Nwa": "child",
    "Nri": "food",
    "Nkịta": "dog",
    "Ọchị": "laughter",
    "Ọma": "good",
    "Ọhụrụ": "new",
    "Ụzọ": "road",
    "Udo": "peace",
    "Ụkwụ": "leg",
    "Ụlọnọ": "house",
    "Ụlọ akwụkwọ": "school",
    "Ọgwụ": "medicine",
    "Ọjị": "kola nut",
    "Ọlụ": "work",
    "Yiri": "wear",
    "Mụọ": "to learn",
    "Jikere": "prepare",
    "Chukwu": "God",
    "Di": "husband",
    "Dibia": "medicine man",
    "Biri": "live",
    "Ndị": "people",
    "Nke": "that",
    "Nwụ": "die",
    "Nkọ": "name",
    "Ubi": "farm",
    "Ọzụzụ": "training",
    "Aba": "wealth",
    "Kpọrọ": "call",
    "Jụọ": "ask",
    "Mụta": "learn",
    "Mụọ": "study",
    "Gburugburu": "everywhere",
    "Ọhịa": "forest",
    "Nkwekọrịta": "agreement",
    "Akara": "mark",
    "Ọzọ": "again",
    "Okpuru": "bottom",
    "Uche": "thought",
    "Chọta": "find"
}

yoruba_dictionary = {
    "Stand":'Duro',
    "Joy":'Ayo',
    "Healthy":'Alafia',
    "Light":'Imole',
    "Sit":'Jokoo',
    "Black":'Dudu',
    "Lies":'Iro',
    "Sickness":'Aisan',
    "Fire":'Ina',
    "world":'Aye',
    "Earth":'Ile',
    "Air":'Afefe',
    "Water":'Omi',
    "Good morning":'Ekaro',
    "Love":'Ife',
    "Wealth":'Ola',
    "God":'Oluwa',
    "Rest":'Simi',
    "Enjoyment":'igbadun',
    "woman":'Obirin',
    "Come":'Wa',
    "Child":'Omo',
    "Man":'Okurin',
    "Cap":'Fila',
    "House":'Ile',
    "Beans":'Ewa',
    "Friend":'Ore',
    "Festival":'Odun',
    "Crown":'Ade',
    "Clock":'Ago',
}






windows.mainloop()