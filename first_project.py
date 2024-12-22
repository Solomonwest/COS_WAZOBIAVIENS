import tkinter as tk

windows = tk.Tk()
windows.geometry("600x600")
windows.title("Multilingualism Dictionary")

windows.columnconfigure((0,1,2,), weight=2)
windows.rowconfigure((0,1,2,3,4,5), weight=2)

intro = tk.Label(windows,text="WELCOME TO MULTILINGUAL DICTIONARY", font=('Arial', 15))
intro.grid(row=0, column=1)

daniel_matric = tk.Label(windows,text="BHU/24/04/10/0001", font=('Arial', 13))
daniel_matric.grid(row=1, column=0)

samuel_matric = tk.Label(windows,text="BHU/24/04/10/0029", font=('Arial', 13))
samuel_matric.grid(row=2, column=0)

aaron_matric = tk.Label(windows,text="BHU/24/04/05/0105", font=('Arial', 13))
aaron_matric.grid(row=3, column=0)

solomon_matric = tk.Label(windows,text="BHU/24/04/05/0052", font=('Arial', 13))
solomon_matric.grid(row=4, column=0)

tayo_matric = tk.Label(windows,text="BHU/24/04/10/0001", font=('Arial', 13))
tayo_matric.grid(row=5, column=0)

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

hausa={
    'House': 'Gida',
    'Water': 'Ruwa',
    'Food': 'Abinci',
    'Person': 'Mutum',
    'Boy': 'Yaro',
    'Girl': 'Yarinya',
    'Money': 'Kudi',
    ' Book': 'Littafi',
    'School': 'Makaranta',
    'Clothes': 'Kaya',
    'World': 'Duniya',
    'Sun': 'Rana',
    'Night': 'Dare',
    'Heart': 'Zuciya',
    'River': 'Rafi',
    'Father': 'Uba',
    'Many': 'mYawa',
    'Health': 'Lafiya',
    'Write': 'Rubutu',
    'Road': 'Hanya',
    'hunger': 'yunwa'
}








windows.mainloop()