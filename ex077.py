palavras = ('aprender', 'programa', 'linguagem' , 'python' ,
            'curso' , 'gratis' , 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programa' , 'futuro')
for p in palavras:
    print(f'Na palavra {p} temos ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')











