import random
import string
import time

mdp = "Wax Générateur mdp 1.0"

print("""
    #  wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww
#  wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww
#  wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwWWWWWWWWwwwwwwwwwwwwwwwwwwwwwwwwwwwWWWWWWWWwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww
#  wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwW::::::WwwwwwwwwwwwwwwwwwwwwwwwwwwwW::::::Wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww
#  wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwW::::::WwwwwwwwwwwwwwwwwwwwwwwwwwwwW::::::Wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww
#  wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwW::::::WwwwwwwwwwwwwwwwwwwwwwwwwwwwW::::::Wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww
#  wwwgggggggggwwwgggggwwwweeeeeeeeeeeewwwwnnnnwwnnnnnnnnwwwwwwwwwwW:::::WwwwwwwwwwwwWWWWWwwwwwwwwwwwW:::::Waaaaaaaaaaaaawwwxxxxxxxwwwwwwxxxxxxx
#  wwg:::::::::ggg::::gwwee::::::::::::eewwn:::nn::::::::nnwwwwwwwwwW:::::WwwwwwwwwwW:::::WwwwwwwwwwW:::::Wwa::::::::::::awwwx:::::xwwwwx:::::xw
#  wg:::::::::::::::::gwe::::::eeeee:::::een::::::::::::::nnwwwwwwwwwW:::::WwwwwwwwW:::::::WwwwwwwwW:::::Wwwaaaaaaaaa:::::awwwx:::::xwwx:::::xww
#  g::::::ggggg::::::gge::::::ewwwwwe:::::enn:::::::::::::::nwwwwwwwwwW:::::WwwwwwW:::::::::WwwwwwW:::::Wwwwwwwwwwwwwa::::awwwwx:::::xx:::::xwww
#  g:::::gwwwwwg:::::gwe:::::::eeeee::::::ewwn:::::nnnn:::::nwwwwwwwwwwW:::::WwwwW:::::W:::::WwwwW:::::Wwwwwwwaaaaaaa:::::awwwwwx::::::::::xwwww
#  g:::::gwwwwwg:::::gwe:::::::::::::::::ewwwn::::nwwwwn::::nwwwwwwwwwwwW:::::WwW:::::WwW:::::WwW:::::Wwwwwwaa::::::::::::awwwwwwx::::::::xwwwww
#  g:::::gwwwwwg:::::gwe::::::eeeeeeeeeeewwwwn::::nwwwwn::::nwwwwwwwwwwwwW:::::W:::::WwwwW:::::W:::::Wwwwwwa::::aaaa::::::awwwwwwx::::::::xwwwww
#  g::::::gwwwwg:::::gwe:::::::ewwwwwwwwwwwwwn::::nwwwwn::::nwwwwwwwwwwwwwW:::::::::WwwwwwW:::::::::Wwwwwwa::::awwwwa:::::awwwwwx::::::::::xwwww
#  g:::::::ggggg:::::gwe::::::::ewwwwwwwwwwwwn::::nwwwwn::::nwwwwwwwwwwwwwwW:::::::WwwwwwwwW:::::::Wwwwwwwa::::awwwwa:::::awwwwx:::::xx:::::xwww
#  wg::::::::::::::::gwwe::::::::eeeeeeeewwwwn::::nwwwwn::::nwwwwwwwwwwwwwwwW:::::WwwwwwwwwwW:::::Wwwwwwwwa:::::aaaa::::::awwwx:::::xwwx:::::xww
#  wwgg::::::::::::::gwwwee:::::::::::::ewwwwn::::nwwwwn::::nwwwwwwwwwwwwwwwwW:::WwwwwwwwwwwwW:::Wwwwwwwwwwa::::::::::aa:::awx:::::xwwwwx:::::xw
#  wwwwgggggggg::::::gwwwwweeeeeeeeeeeeeewwwwnnnnnnwwwwnnnnnnwwwwwwwwwwwwwwwwwWWWwwwwwwwwwwwwwWWWwwwwwwwwwwwaaaaaaaaaawwaaaaxxxxxxxwwwwwwxxxxxxx
#  wwwwwwwwwwwwg:::::gwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww
#  ggggggwwwwwwg:::::gwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww
#  g:::::ggwwwgg:::::gwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww
#  wg::::::ggg:::::::gwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww
#  wwgg:::::::::::::gwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww
#  wwwwggg::::::gggwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww
#  wwwwwwwggggggwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww
""", mdp)

def generer_mot_de_passe(longueur):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    mot_de_passe = ''.join(random.choice(caracteres) for _ in range(longueur))
    return mot_de_passe

def generer_mots_de_passe(nombre_mdp):
    mots_de_passe = []
    for i in range(nombre_mdp):
        longueur_mot_de_passe = int(input(f"Entrez la longueur du mot de passe {i + 1} : "))
        mot_de_passe = generer_mot_de_passe(longueur_mot_de_passe)
        mots_de_passe.append(mot_de_passe)
    return mots_de_passe

nombre_mdp_a_generer = int(input("Entrez le nombre de mots de passe à générer : "))

mots_de_passe_genere = generer_mots_de_passe(nombre_mdp_a_generer)
print("Mots de passe générés : ")
for i, mot_de_passe in enumerate(mots_de_passe_genere, 1):
    print(f"{i}. {mot_de_passe}")

time.sleep(5)

print("génération fini(e)", mdp)
time.sleep(10)
print("""
    #  wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww
#  wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww
#  wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwWWWWWWWWwwwwwwwwwwwwwwwwwwwwwwwwwwwWWWWWWWWwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww
#  wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwW::::::WwwwwwwwwwwwwwwwwwwwwwwwwwwwW::::::Wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww
#  wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwW::::::WwwwwwwwwwwwwwwwwwwwwwwwwwwwW::::::Wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww
#  wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwW::::::WwwwwwwwwwwwwwwwwwwwwwwwwwwwW::::::Wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww
#  wwwgggggggggwwwgggggwwwweeeeeeeeeeeewwwwnnnnwwnnnnnnnnwwwwwwwwwwW:::::WwwwwwwwwwwwWWWWWwwwwwwwwwwwW:::::Waaaaaaaaaaaaawwwxxxxxxxwwwwwwxxxxxxx
#  wwg:::::::::ggg::::gwwee::::::::::::eewwn:::nn::::::::nnwwwwwwwwwW:::::WwwwwwwwwwW:::::WwwwwwwwwwW:::::Wwa::::::::::::awwwx:::::xwwwwx:::::xw
#  wg:::::::::::::::::gwe::::::eeeee:::::een::::::::::::::nnwwwwwwwwwW:::::WwwwwwwwW:::::::WwwwwwwwW:::::Wwwaaaaaaaaa:::::awwwx:::::xwwx:::::xww
#  g::::::ggggg::::::gge::::::ewwwwwe:::::enn:::::::::::::::nwwwwwwwwwW:::::WwwwwwW:::::::::WwwwwwW:::::Wwwwwwwwwwwwwa::::awwwwx:::::xx:::::xwww
#  g:::::gwwwwwg:::::gwe:::::::eeeee::::::ewwn:::::nnnn:::::nwwwwwwwwwwW:::::WwwwW:::::W:::::WwwwW:::::Wwwwwwwaaaaaaa:::::awwwwwx::::::::::xwwww
#  g:::::gwwwwwg:::::gwe:::::::::::::::::ewwwn::::nwwwwn::::nwwwwwwwwwwwW:::::WwW:::::WwW:::::WwW:::::Wwwwwwaa::::::::::::awwwwwwx::::::::xwwwww
#  g:::::gwwwwwg:::::gwe::::::eeeeeeeeeeewwwwn::::nwwwwn::::nwwwwwwwwwwwwW:::::W:::::WwwwW:::::W:::::Wwwwwwa::::aaaa::::::awwwwwwx::::::::xwwwww
#  g::::::gwwwwg:::::gwe:::::::ewwwwwwwwwwwwwn::::nwwwwn::::nwwwwwwwwwwwwwW:::::::::WwwwwwW:::::::::Wwwwwwa::::awwwwa:::::awwwwwx::::::::::xwwww
#  g:::::::ggggg:::::gwe::::::::ewwwwwwwwwwwwn::::nwwwwn::::nwwwwwwwwwwwwwwW:::::::WwwwwwwwW:::::::Wwwwwwwa::::awwwwa:::::awwwwx:::::xx:::::xwww
#  wg::::::::::::::::gwwe::::::::eeeeeeeewwwwn::::nwwwwn::::nwwwwwwwwwwwwwwwW:::::WwwwwwwwwwW:::::Wwwwwwwwa:::::aaaa::::::awwwx:::::xwwx:::::xww
#  wwgg::::::::::::::gwwwee:::::::::::::ewwwwn::::nwwwwn::::nwwwwwwwwwwwwwwwwW:::WwwwwwwwwwwwW:::Wwwwwwwwwwa::::::::::aa:::awx:::::xwwwwx:::::xw
#  wwwwgggggggg::::::gwwwwweeeeeeeeeeeeeewwwwnnnnnnwwwwnnnnnnwwwwwwwwwwwwwwwwwWWWwwwwwwwwwwwwwWWWwwwwwwwwwwwaaaaaaaaaawwaaaaxxxxxxxwwwwwwxxxxxxx
#  wwwwwwwwwwwwg:::::gwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww
#  ggggggwwwwwwg:::::gwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww
#  g:::::ggwwwgg:::::gwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww
#  wg::::::ggg:::::::gwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww
#  wwgg:::::::::::::gwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww
#  wwwwggg::::::gggwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww
#  wwwwwwwggggggwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww
""")
