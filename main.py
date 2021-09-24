import argparse, time
from reconhece_frente import reconhece_frente
from reconhece_verso import reconhece_verso
from reconhece_texto import reconhece_texto
from apply_filter import apply_filter


def main():
    name = str(time.time()).split('.')[0]
    
    parser = argparse.ArgumentParser()

    parser.add_argument('-s', '--support')
    parser.add_argument('-f', '--frente')
    parser.add_argument('-v', '--verso')

    args = parser.parse_args()

    for currentArgument in args.__dict__:
        if args.__dict__[currentArgument] != None:
            if currentArgument == 'frente':
                doc_frente = args.__dict__[currentArgument]

            elif currentArgument == 'verso':
                doc_verso = args.__dict__[currentArgument]

            elif currentArgument == 'support':
                print('Help')

            else:
                print(f'{currentArgument} não é um argumento válido')

    if doc_frente and doc_verso:
        reconhece_frente(doc_frente, name)
        reconhece_verso(doc_verso, name)
        apply_filter(name)
        reconhece_texto(name)


if __name__ == "__main__":
    main()
