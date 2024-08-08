meme_dict = {
            "CRINGE": "Garip Utandırıcı bir şey",
            "LOL": "Laugh out Loud demektir, Sesli gülmek",
            "FAKE": "Sahte olan",
            "TROLL": "İronik ve komik olan şey",
            "BRUH":"Kanka, anlamına gelen sözcük"
}

word = input("Anlamadığınız Bir Kelime Giriniz..:")

if word in meme_dict.keys():
    print("girdiğiniz kelimenin analmı:",meme_dict[word])
else:
    print("maalesef anlamını bulamadım..")
