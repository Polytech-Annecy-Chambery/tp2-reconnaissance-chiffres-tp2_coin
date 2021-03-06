from skimage import io
from skimage.transform import resize
import matplotlib.pyplot as plt
import numpy as np

import pdb

class Image:
	def __init__(self):
		"""Initialisation d'une image composee d'un tableau numpy 2D vide
		(pixels) et de 2 dimensions (H = height et W = width) mises a 0
		"""
		self.pixels = None
		self.H = 0
		self.W = 0
	

	def set_pixels(self, tab_pixels):
		""" Remplissage du tableau pixels de l'image self avec un tableau 2D (tab_pixels)
		et affectation des dimensions de l'image self avec les dimensions 
		du tableau 2D (tab_pixels) 
		"""
		self.pixels = tab_pixels
		self.H, self.W = self.pixels.shape


	def load(self, file_name):
		""" Lecture d'un image a partir d'un fichier de nom "file_name"""
		self.pixels = io.imread(file_name)
		self.H,self.W = self.pixels.shape 
		print("lecture image : " + file_name + " (" + str(self.H) + "x" + str(self.W) + ")")


	def display(self, window_name):
		"""Affichage a l'ecran d'une image"""
		fig = plt.figure(window_name)
		if (not (self.pixels is None)):
			io.imshow(self.pixels)
			io.show()
		else:
			print("L'image est vide. Rien à afficher")


	#==============================================================================
	# Methode de binarisation
	# 2 parametres :
	#   self : l'image a binariser
	#   S : le seuil de binarisation
	#   on retourne une nouvelle image binarisee
	#==============================================================================
	def binarisation(self, S):
		im_bin = Image()
		
		im_bin.set_pixels(np.zeros((self.H, self.W), dtype=np.uint8))
		for i,row in enumerate(self.pixels):
			for n, pix in enumerate(row):
				if pix >= S : im_bin.pixels[i][n] = 255
				if pix < S : im_bin.pixels[i][n] = 0
		
		#pdb.set_trace()
		return im_bin


	#==============================================================================
	# Dans une image binaire contenant une forme noire sur un fond blanc
	# la methode 'localisation' permet de limiter l'image au rectangle englobant
	# la forme noire
	# 1 parametre :
	#   self : l'image binaire que l'on veut recadrer
	#   on retourne une nouvelle image recadree
	#==============================================================================
	def localisation(self):
		
		pixY = [self.H, 0] ; pixX = [self.W, 0]
		for i,row in enumerate(self.pixels):
			for n,pix in enumerate(row):
				if pix == 0:
					if i < pixY[0] : pixY[0] = i
					if i > pixY[1] : pixY[1] = i
				if pix == 0:
					if n < pixX[0] : pixX[0] = n
					if n > pixX[1] : pixX[1] = n
				
		newImage = Image()
		newImage.set_pixels(self.pixels[pixY[0]:pixY[1], pixX[0]:pixX[1]])
		return newImage
	#==============================================================================
	# Methode de redimensionnement d'image
	#==============================================================================
	def resize(self, new_H, new_W):
		resizedimg = Image()
		resizedimg.set_pixels( np.uint8( resize(self.pixels, (new_H,new_W), 0)*255 ) ) 
		return resizedimg

	#==============================================================================
	# Methode de mesure de similitude entre l'image self et un modele im
	#==============================================================================

	def similitude(self, im):
		samePix = 0
		tot = 0
		
		for i,row in enumerate(self.pixels):
			for n,pix in enumerate(row):
				if pix == im.pixels[i][n] : samePix += 1
				tot += 1
		return samePix / tot

