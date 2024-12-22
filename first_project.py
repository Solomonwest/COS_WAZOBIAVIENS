import tkinter as tk



def hausa_search():
    hausa_window = tk.Toplevel()
    hausa_window.geometry("500x500")
    hausa_window.title("Hausa Dictionary")
    hausa_window.config(bg="blue")


    label = tk.Label(hausa_window, text="Enter word in English:", font=('Arial', 12))
    label.pack(pady=10)


    entry = tk.Entry(hausa_window, font=('Arial', 12))
    entry.pack(pady=10)


    def search_word():
        word = entry.get().lower()
        if word in hausa:
            result_label.config(text=f"{word} in Hausa is: {hausa[word]}")
        else:
            result_label.config(text="Word not found in the dictionary.")

    search_btn = tk.Button(hausa_window, text="Search", command=search_word, font=('Arial', 12))
    search_btn.pack(pady=10)

    result_label = tk.Label(hausa_window, text="", font=('Arial', 12))
    result_label.pack(pady=10)


def espanol_search():
    espanol_window = tk.Toplevel()
    espanol_window.geometry('500x500')
    espanol_window.title("Espanol/Spanish Dictionary")
    espanol_window.config(background='cyan')
    espanol_window.mainloop()

def igbo_search():
    igbo_window = tk.Toplevel()
    igbo_window.geometry('500x500')
    igbo_window.title("Igbo Dictionary")
    igbo_window.config(background='black')


    instruction_label = tk.Label(igbo_window, text="Enter an English word:", font=('Arial', 12), bg='black', fg='white')
    instruction_label.pack(pady=10)


    word_entry = tk.Entry(igbo_window, font=('Arial', 12), width=25)
    word_entry.pack(pady=10)


    translation_label = tk.Label(igbo_window, text="", font=('Arial', 12), bg='black', fg='white')
    translation_label.pack(pady=10)


    translate_button = tk.Button(igbo_window, text="Translate", font=('Arial', 12))
    translate_button.pack(pady=10)


    igbo_window.mainloop()


def yoruba_search():
    yoruba_windows = tk.Toplevel()
    yoruba_windows.title("yoruba_dictionary")
    yoruba_windows.config(background='grey')
    yoruba_windows.geometry("500x500")
    yoruba_windows.mainloop()

def french_search():
    french_window = tk.Toplevel()
    french_window.geometry('500x500')
    french_window.title("french_dictionary")
    french_window.config(background='blue')
    french_window.mainloop()

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


lay2lo_matric = tk.Label(windows,text="BHU/24/04/09/0022", font=('Arial', 13))
lay2lo_matric.grid(row=5, column=0)

yoruba_btn = tk.Button(windows, text='Yoruba Dictionary')
yoruba_btn.config(command=yoruba_search)
yoruba_btn.grid(row=1, column=1)

igbo_btn = tk.Button(windows, text='Igbo Dictionary')
igbo_btn.config(command=igbo_search)
igbo_btn.grid(row=2, column=1)


hausa_btn = tk.Button(windows, text='Hausa Dictionary')
hausa_btn.config(command=hausa_search)
hausa_btn.grid(row=3, column=1)

espanol_btn = tk.Button(windows, text= 'Espanol Dictionary')
espanol_btn.config(command=espanol_search)
espanol_btn.grid(row=4, column=1)

french_btn = tk.Button(windows, text= 'French Dictionary')
french_btn.config(command=french_search)
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
    "hand": "Aka",
    "eye": "Anya",
    "God": "Chineke",
    "king": "Eze",
    "dance": "Egwu",
    "friend": "Enyi",
    "money": "Ego",
    "strength": "Ike",
    "thing": "Ife",
    "Igbo people": "Igbo",
    "head": "Isi",
    "how are you?": "Kedu",
    "because": "Maka",
    "person": "Mmadụ",
    "child": "Nwa",
    "food": "Nri",
    "dog": "Nkịta",
    "laughter": "Ọchị",
    "good": "Ọma",
    "new": "Ọhụrụ",
    "road": "Ụzọ",
    "peace": "Udo",
    "leg": "Ụkwụ",
    "house": "Ụlọnọ",
    "school": "Ụlọ akwụkwọ",
    "medicine": "Ọgwụ",
    "kola nut": "Ọjị",
    "work": "Ọlụ",
    "wear": "Yiri",
    "to learn": "Mụọ",
    "prepare": "Jikere",
    "husband": "Di",
    "medicine man": "Dibia",
    "live": "Biri",
    "people": "Ndị",
    "that": "Nke",
    "die": "Nwụ",
    "name": "Nkọ",
    "farm": "Ubi",
    "training": "Ọzụzụ",
    "wealth": "Aba",
    "call": "Kpọrọ",
    "ask": "Jụọ",
    "learn": "Mụta",
    "study": "Mụọ",
    "everywhere": "Gburugburu",
    "forest": "Ọhịa",
    "agreement": "Nkwekọrịta",
    "mark": "Akara",
    "again": "Ọzọ",
    "bottom": "Okpuru",
    "thought": "Uche",
    "find": "Chọta",
    "sun": "Anyanwụ",
    "moon": "Osimiri",
    "star": "Kpakpando",
    "night": "Abalị",
    "day": "Ụtụtụ",
    "rain": "Mmegharị",
    "wind": "Ifufe",
    "fire": "Ọkụ",
    "water": "Mmiri",
    "earth": "Álụ",
    "sky": "Eluigwe",
    "tree": "Osisi",
    "flower": "Okooko",
    "bird": "Ndị n’ụwa",
    "fish": "Azụ",
    "cow": "Efu",
    "horse": "Ịnyịnya",
    "love": "Ihụnanya",
    "hate": "Ịghọtara",
    "joy": "Anwụ",
    "sorrow": "Ichefu",
    "family": "Ụgbọ",
    "friendship": "Enyi",
    "hope": "Olileanya"
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
french_dictionary={'hello':'Bonjour',
                   'thank you':'Merci',
                   'goodbye':'Au revoir',
                   'excuse me':'Excusez-moi',
                   'house':'Maison',
                   "school":"L'ecole",
                   'hospital':'Hopital',
                   'park':'Parc',
                   'libary':'Bibliotheque',
                   'mother':'mere',
                   'father':'Pere',
                   'brother':'Frere',
                   'sister':'Soeur',
                   'friend':'Ami',
                   'cold':'Froid',
                   'hot':'Chaud',
                   'sad':'Triste',
                   'tired':'Fatigue',
                   'good morning':'Bonjour',
                   'hat':'Chapeau'
}








windows.mainloop()