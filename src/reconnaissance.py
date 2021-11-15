from image import Image

def lecture_modeles(chemin_dossier):
	fichiers= ['_0.png','_1.png','_2.png','_3.png','_4.png','_5.png','_6.png', 
			'_7.png','_8.png','_9.png']
	liste_modeles = []
	for fichier in fichiers:
		model = Image()
		model.load(chemin_dossier + fichier)
		liste_modeles.append(model)
	return liste_modeles


def reconnaissance_chiffre(image, liste_modeles, S):
	best = {"simi": -1, "imgIndex": None}
	
	for i,img in enumerate(liste_modeles):
		simiTmp = image.binarisation(S).localisation().resize(img.H, img.W).similitude(img)
		if simiTmp > best["simi"]:
			best = {"simi": simiTmp, "imgIndex": i}
	
	return best["imgIndex"]
	
	
