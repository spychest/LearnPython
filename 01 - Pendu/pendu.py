word_to_guess = input("Quel est le mot a faire deviner ? ").lower()
caracter_number = len(word_to_guess)
string_to_show = ""
for i in range(caracter_number):
    string_to_show += "_"

print(string_to_show)

error_count = 0
error_limit = 10

while error_count < error_limit:
    user_string = input('Entrez une lette ou un mot: ').lower()
    if len(user_string) > 1:
        if user_string == word_to_guess:
            print('Vous avez gagné');
            break
        else:
            print("Le mot n'est pas " + user_string + ".")
            error_count = error_count+1
            print("Vous avez actuellement " + str(error_count) + " erreur sur " + str(error_limit) + ".")
            continue

    if word_to_guess.find(user_string) == -1:
        print("La lettre " + user_string.upper() + " ne se trouve pas dans le mot.")
        error_count = error_count+1
        print("Vous avez actuellement " + str(error_count) + " erreur sur " + str(error_limit) + ".")
        continue
    else:
        print("La lettre " + user_string.upper() + " se trouve bien dans le mot.")
        string_to_show_as_array = list(string_to_show)
        for i, car in enumerate(word_to_guess):
            if car == user_string:
                string_to_show_as_array[i] = user_string
        string_to_show = "".join(string_to_show_as_array)
        print("Mot recherché: " + string_to_show)
        continue
        
if error_count >= error_limit:
    print("Vous avez perdu =(")
