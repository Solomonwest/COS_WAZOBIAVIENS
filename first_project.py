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
        word = entry.get().title()
        if word in hausa:
            result_label.config(text=f"{word} in Hausa is: {hausa[word]}")
        else:
            result_label.config(text="Word not found in the dictionary.")

    search_btn = tk.Button(hausa_window, text="Search", command=search_word, font=('Arial', 12))
    search_btn.pack(pady=10)

    result_label = tk.Label(hausa_window, text="", font=('Arial', 12))
    result_label.pack(pady=10)


def espanol_search():

    def search(value):
        if value in espanol_dictionary:
            espanol.set(espanol_dictionary[value])
            print(espanol_dictionary[value])

        else:
            espanol.set("Search Not Found")
            print("Search Not Found")

    espanol_window = tk.Toplevel()
    espanol_window.geometry('500x500')
    espanol_window.title("Espanol/Spanish Dictionary")

    espanol_window.config(background='#2a6356')

    espanol_intro_label = tk.Label(espanol_window,
                                   text='Type your desired entry in english')
    espanol_intro_label.config(font=('Georgia',15),bg='#2a6356',fg='white')
    espanol_intro_label.pack(pady=15)

    espanol_entry =tk.Entry(espanol_window,
                            text='enter',
                            width=30,
                            font=('Arial',20))
    espanol_entry.pack(pady=15)

    translate = tk.PhotoImage(file='translate.png')
    espanol_search_btn =tk.Button(espanol_window,image=translate,
                                  bg='#2a6356',bd=0,activebackground='#228ed1')
    espanol_search_btn.config(command=lambda: search(espanol_entry.get().lower()))
    espanol_search_btn.pack()

    espanol = tk.StringVar()
    espanol_label = tk.Label(espanol_window,textvariable=espanol,
                             font=('Ink Free',30),
                             width=25)
    espanol_label.config()
    espanol_label.pack(pady=20)

    espanol_window.mainloop()

def igbo_search():
    igbo_window = tk.Toplevel()
    igbo_window.geometry('500x500')
    igbo_window.title("Igbo Dictionary")
    igbo_window.config(background='black')

    def igbo_search_word(igbo_word):
        if igbo_word in igbo_dictionary:
            igbo_translation_label.config(text=igbo_dictionary[igbo_word])
            print(igbo_dictionary[igbo_word])
        else:
            igbo_translation_label.config(text=" word not found in dictionary.")


    igbo_instruction_label = tk.Label(igbo_window, text="Enter an English word:", font=('Garamond', 15), bg='black', fg='white')
    igbo_instruction_label.pack(pady=10)

    igbo_word_entry = tk.Entry(igbo_window, font=('Garamond', 16), width=25)
    igbo_word_entry.pack(pady=10)

    igbo_translation_label = tk.Label(igbo_window, text="", font=('Baskerville', 16), bg='black', fg='white')
    igbo_translation_label.pack(pady=10)

    igbo_translate_button = tk.Button(igbo_window, text="Translate", font=('Garamond', 16), command=lambda: igbo_search_word(igbo_word_entry.get().lower()))
    igbo_translate_button.pack(pady=10)

    igbo_window.mainloop()


def yoruba_search():
    def search(word):
        if word in yoruba_dictionary:
            yoruba.set(yoruba_dictionary[word])
            print(yoruba_dictionary)
        else:
            yoruba.set("Not Found")
            print("Not Found")

    yoruba_windows = tk.Toplevel()
    yoruba_windows.title("yoruba_dictionary")
    yoruba_windows.config(background='orange')
    yoruba_windows.geometry("500x500")

    yoruba_input_label = tk.Label(yoruba_windows, text="Enter an English word",
                                  font=('Arial', 13), background='white')
    yoruba_input_label.pack(pady=10)

    yoruba_entry = tk.Entry(yoruba_windows,
                            width=25, bd=8,
                            font=('Arial', 13))
    yoruba_entry.pack(pady=10)

    yoruba_search_btn = tk.Button(yoruba_windows,
                                  text="Search/ṣàwárí",
                                  font=('Arial', 13), width=15, background='white', bd=4)
    yoruba_search_btn.config(command=lambda: search(yoruba_entry.get().lower()))
    yoruba_search_btn.pack(pady=10)

    yoruba = tk.StringVar()
    yoruba_label = tk.Label(yoruba_windows, textvariable=yoruba,
                            font=('Arial', 15), width=25, background='white', bd=8)
    yoruba_label.pack(padx=10, pady=10)
    yoruba_windows.mainloop()


def french_search():
    def translate(word):
        if word in french_dictionary:
            french.set(french_dictionary[word])
            print(french_dictionary[word])

        else:
            french.set('word not found')
            print('word not found')

    french_window = tk.Toplevel()
    french_window.geometry('500x500')
    french_window.title("french_dictionary")
    french_window.config(background='blue')

    instruction_label = tk.Label(french_window, text="Enter an English word:",font=('Arial', 14), bg='blue', fg='grey')
    instruction_label.pack(pady=20, padx=20)

    french_entry = tk.Entry(french_window, font=('Arial', 14), width=25)
    french_entry.pack(pady=20, padx=20)

    translation_label = tk.Label(french_window, text="Translation", font=('Arial', 14), bg='blue', fg='grey')
    translation_label.pack(pady=20, padx=20)

    french = tk.StringVar()
    french_label = tk.Label(french_window, textvariable=french, font=('Arial', 14), bg='blue', fg='grey')
    french_label.pack(pady=20, padx=20)

    translate_button = tk.Button(french_window, text="Translate", font=('Arial', 14), bg='blue', fg='grey',
                                 command=lambda: translate(french_entry.get().lower()))
    translate_button.pack(pady=20, padx=20)

    french_window.mainloop()

windows = tk.Tk()
windows.geometry("600x600")
windows.title("Multilingualism Dictionary")
windows.config()
windows.resizable(False,False)

bg = tk.PhotoImage(file='COS101.png')
window_display =tk.Label(windows, image=bg)
window_display.place(x=0,y=0,relheight=1,relwidth=1)

windows.columnconfigure((0,1,2,), weight=2)
windows.rowconfigure((0,1,2,3,4,5), weight=2)

intro = tk.Label(windows,text="WELCOME TO THE MULTILINGUAL DICTIONARY", font=('Arial', 15))
intro.grid(row=0, column=0, columnspan=2)

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

yoruba_btn = tk.Button(windows, text='Yoruba Dictionary', font=('Arial', 13))
yoruba_btn.config(command=yoruba_search)
yoruba_btn.grid(row=1, column=1)

igbo_btn = tk.Button(windows, text='Igbo Dictionary', font=('Arial', 13))
igbo_btn.config(command=igbo_search)
igbo_btn.grid(row=2, column=1)


hausa_btn = tk.Button(windows, text='Hausa Dictionary', font=('Arial', 13))
hausa_btn.config(command=hausa_search)
hausa_btn.grid(row=3, column=1)

espanol_btn = tk.Button(windows, text= 'Espanol Dictionary', font=('Arial', 13))
espanol_btn.config(command=espanol_search)
espanol_btn.grid(row=4, column=1)

french_btn = tk.Button(windows, text= 'French Dictionary', font=('Arial', 13))
french_btn.config(command=french_search)
french_btn.grid(row=5, column=1)

espanol_dictionary = {
    "hello":"hola",
    "fine":"bien",
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
    "hope": "Olileanya",
    "truth": "Eziokwu",
    "lie": "Ịgha",
    "beautiful": "Mma",
    "strong": "Ike",
    "big": "Ọtụtụ",
    "small": "Ntẹ",
    "clean": "Ịcha",
    "dirty": "Nkọrọ",
    "hot": "Okpomọkụ",
    "cold": "Oyi",
    "happy": "Anwụ",
    "sad": "Ụjọ",
    "tall": "Elu",
    "short": "Ntanye",
    "wide": "Gbagọrọ",
    "narrow": "Ọkpụkpụ",
    "light": "Ìhè",
    "dark": "Ụtụtụ",
    "sharp": "Ọkpụkpụ",
    "dull": "Ọkpụkpọ",
    "young": "Ntoro",
    "old": "Okenye",
    "quick": "Ọsọ",
    "slow": "Nkọda",
    "clear": "Ihie",
    "cloudy": "Iwu"
}


yoruba_dictionary = {
    "stand": 'Duro',
    "joy": 'ayọ̀',
    "healthy": 'Ìlera',
    "light": 'ìmọ́lẹ̀',
    "sit": 'Jókòó',
    "black": 'Dudu',
    "lies": 'irọ́',
    "sickness": 'àìsàn',
    "fire": 'iná',
    "world": 'Aye',
    "earth": 'ilẹ',
    "air": 'afẹ́fẹ́',
    "water": 'Omi',
    "good morning": 'Kàárọ̀',
    "love": 'ìfẹ́',
    "wealth": 'ọrọ̀',
    "god": 'Ọlọ́run',
    "rest": 'Sinmi',
    "enjoyment": 'igbadun',
    "woman": 'obìnrin',
    "come": 'wá',
    "child": 'ọmọ',
    "man": 'ọkùnrin',
    "cap": 'fila',
    "house": 'Ilé',
    "beans": 'ẹ̀wà',
    "friend": 'ọ̀rẹ́',
    "festival": 'Àjọ̀dún',
    "crown": 'Ade',
    "clock": 'Aago',
    "go": 'Lọ',
    "eat": 'jẹ',
    "drink": 'ohun mímu',
    "heaven": 'ọrun'
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
                   'library':'Bibliotheque',
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