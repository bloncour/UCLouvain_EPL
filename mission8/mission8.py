class Duree :
    def __init__(self, h, m, s):
        """
        :param h: Nombre d'heures. Entier plus grand ou égal à 0
        :param m: Nombre de minutes. Entier compris dans [0;60[
        :param s: Nombre de secondes. Entier compris dans [0;60[
        """
        if 0 <= h:
            self.heure = int(h)
        else:
            print('"Heure" doit être un entier positif')
        if 0 <= m < 60:
            self.minute = int(m)
        else:
            print('"Minute" doit être un entier compris dans [0; 60[')
        if 0 <= s < 60:
            self.seconde = int(s)
        else:
            print('"Seconde" doit être un entier compris dans [0; 60[')

    def to_secondes(self):
        """
        Donne le nombre de secondes
        :return: le nombre de seconde
        """
        sec = 0
        sec += self.seconde + 60 * self.minute + 3600 * self.heure
        return sec

    def delta(self, d):
        """
        Donne la différence de secondes entre la durée self et la durée d
        :param d: Durée issue de la classe Durée
        :return: Entier, différence en secondes
        """
        return self.to_secondes() - d.to_secondes()

    def apres(self, d):
        """
        Retourne True si self est plus long que d
        :param d: Instance Durée
        :return: True si self > d, sinon false
        """
        if self.delta(d) > 0:
            return True
        return False

    def ajouter(self,d):
        """
        Additionne deux temps
        :param d: Instance de durée
        :return: Met à jour le self
        """
        sec = self.seconde + d.seconde
        minu = sec//60
        sec = sec%60
        minu += self.minute + d.minute
        heu = minu//60
        minu = minu%60
        heu += self.heure + d.heure
        self.seconde, self.minute, self.heure = sec, minu, heu
        return self

    def __str__(self):
        return "{:02}:{:02}:{:02}".format(self.heure, self.minute, self.seconde)


class Chanson :
    def __init__(self, t, a, d):
        """
        Initialise Chanson
        :param t: Le titre, str
        :param a: L'auteur, str
        :param d: La durée, int
        """
        self.titre = t
        self.auteur = a
        self.duree = d
        self.length = d.to_secondes()

    def __str__(self):
        return "{TITRE} - {AUTEUR} - {DUREE}".format(TITRE=self.titre,AUTEUR=self.auteur,DUREE=self.duree)

class Album :
    def __init__(self, numero):
        self.numero = numero
        self.duree = 0
        self.count = 0
        self.music = []
 
    def add(self,chanson):
        self.count += 1
        self.music.append("{:02}: ".format(self.count) + chanson.__str__())
        self.duree += chanson.length

    def __str__(self):
        text = ""
        for i in range(len(self.music)):
            text += "{:02}: ".format(i) + str(self.music[i]) + "\n"
        return text

    
with open("music-db.txt", "r") as file:
    all_music = file.read().split("\n")
    for i in range(len(all_music)):
        all_music[i] = all_music[i].split(" ")

count = 0
music_count = 0
while True:
    count += 1
    album = Album(count)
    while True:
        if music_count == len(all_music):
            break
        title = " ".join(all_music[music_count][0].split("_"))
        try:
            artist = " ".join(all_music[music_count][1].split("_"))
        except:
            pass
        try:
            length = Duree(0, int(all_music[music_count][-2]), int(all_music[music_count][-1]))
            chanson = Chanson(title, artist, length)
        except:
            continue
        if album.duree + length.to_secondes() < 4500:
            album.add(chanson)
            music_count += 1
        else:
            break
    print(album)
    if music_count == len(all_music):
        break
