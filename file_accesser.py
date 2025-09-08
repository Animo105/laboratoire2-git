import secret

print("Entrez le code secret: ")
code = input()

if code != secret.mon_code_super_secret:
    print("Mauvais code entré.")

elif code == secret.mon_code_super_secret:
    print("contenu du fichier secret:")
    f = open("fichier_secret.txt")
    print(f.read())