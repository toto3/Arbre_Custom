#!/usr/bin/python
# -*- coding: utf-8 -*-
from tkinter import * #pour les images doit être la
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import pandas as pd # pour installer C:\Users\audetpa\AppData\Local\Programs\Python\Python39\Scripts>pip install pandas   et  pip install numpy==1.19.3
import xlrd # pour installer C:\Users\audetpa\AppData\Local\Programs\Python\Python39\Scripts>pip install xlrd
import subprocess
import sys
import os
import datetime
import warnings



#WARNING: The scripts pip.exe, pip3.10.exe and pip3.exe are installed 
#in 'C:\Users\audetpa\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\Scripts'
# which is not on PATH.  Consider adding this directory to PATH or, if you prefer to suppress this warning,
# use --no-warn-script-location.

# Installation sur une nouvelle machine
#pip install --upgrade pip
#pip install pandas
#pip install numpy==1.19.3
#pip install xlrd
#pip install openpyxl



# == ATTENTION !!!!! AVANT DE ROULER CE SCRIPT on doit faire l'épape suivante:
# == prépare un fichier de données .xlsx 
# == prépare un fichier newick de base 


#=======================================================================


#Pour Geany dans le menu construire les config doivent etre:
#Compile = C:\Users\audetpa\AppData\Local\Programs\Python\Python39\python -m py_compile "%f"
#Execute = C:\Users\audetpa\AppData\Local\Programs\Python\Python39\python "%f"
#Execute =python3 "%f"



#Script programmé par Pascal Audet pour le LEMP
#Débuté le 16 avril 2025 
 



#=======================================================================

     
        
class faireArbreCustom:
	def __init__(self,nomfichierInput,nomfichierOutput):				
		self.nomfichier=nomfichierInput		
		self.nomfichierOutput=nomfichierOutput
		self.arbreBase="rien"

	def AjouterChampsDansNewick(self):
		ftree=open(arbreBase)#fichier newick d'origine'
		fListe_TEMP=open("Liste_TEMP.csv")#fichier key	temporaire
		x = datetime.datetime.now()
		dateheure =x.strftime("%Y") +"-"+x.strftime("%m")+"-"+x.strftime("%d")+"_"+x.strftime("%H")+"h"+ x.strftime("%M")+"s"+ x.strftime("%S")
		fout=open(arbreBase+"_CUSTOM_"+dateheure+".tree","w+")#nouveau ficher newick
		arbre=ftree.readline()#mettre l'arbre dans une string'
		#print(arbre)
		line=fListe_TEMP.readline()
		line=line.replace("\n","")
		while line !='':
			line=line.replace("\n","")
			aline=line.replace("\r","")
			#lines=line.split("\t")
			lines=line.split(";")
			#print('a',lines[0],lines[1])
			arbre=arbre.replace(lines[0],lines[0]+lines[1])#ajout des info au bout de la key
			line=fListe_TEMP.readline()
		#print(arbre)
		fout.write(arbre)
		fout.close()
		ftree.close()
		fListe_TEMP.close()
		# ouverture de l arbre avec archéopthéryx
		a = subprocess.Popen('forester.jar '+arbreBase+'_CUSTOM_'+dateheure+'.tree', shell=True, stdin = subprocess.PIPE, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
       
		
		 

	def boucleFichier(self): # pour faire un .csv à fartire d'un .xslx
		f=open(self.nomfichier)
		f_out=open(self.nomfichierOutput,"w+")
		line=f.readline()
		line=f.readline()
		f_out.write("Key;Info\n")
		while line !='':
			line=line.replace("\n","")
			line=line.replace("\r","")
			line=line.replace("\"","_")
			line=line.split("	")
			LigneREQ=''\
			+''+Type_Format(line[0],"VARCHAR")\
			+';_'+Type_Format(line[1],"VARCHAR")\
			+'_'+Type_Format(line[2],"VARCHAR")\
			+'_'+Type_Format(line[3],"VARCHAR")\
			+'_'+Type_Format(line[4],"VARCHAR")\
			+'_'+Type_Format(line[5],"VARCHAR")\
			+'_'+Type_Format(line[6],"VARCHAR")\
			+'_'+Type_Format(line[7],"VARCHAR")\
			+'_'+Type_Format(line[8],"VARCHAR")\
			+'_'+Type_Format(line[9],"VARCHAR")\
			+'_'+Type_Format(line[10],"VARCHAR")\
			+''
			LigneREQ=LigneREQ.replace("\t","")
			LigneREQ=LigneREQ.replace("_____","_")
			LigneREQ=LigneREQ.replace("____","_")
			LigneREQ=LigneREQ.replace("___","_")
			LigneREQ=LigneREQ.replace("__","_")
			#print(self.nomfichier," 1 ",self.nomfichierOutput," 2 ",LigneREQ);
			f_out.write(LigneREQ+"\n")
			line=f.readline()
		f.close()
		f_out.close()




def Type_Format(champ,choix):
	if (choix=="INT"):return ''+champ+''
	if (choix=="VARCHAR"):return ''+champ+'' 
	return ''+champ+''
	
	
#===========================================
#         PROGRAMME PRINCIPAL
#===========================================
#interface gui permettant de sélectionner avec les boutons

root= tk.Tk()
root.geometry('850x500')
root.resizable(width=False, height=False)
root.title('LEMP - Faire un arbre custom (version du 2025_05_05) ') 





w = 850
h= 500
canvas1 = tk.Canvas(root, width = w, height = h, bg = 'lightsteelblue2', relief = 'flat')
canvas1.pack()



label1 = tk.Label(root, text='Ce Programme utilise un arbre Newick \npour y ajouter des informations externes:\n\n1)Sélectionnez un arbre newick de base\n\n  2)Sélectionnez un fichier Excel contenant \nles données que vous désirer voir dans l\'arbre\n\n Le Newick sera généré et Archaeoptreyx\n l\'ouvrira automatiquement ', bg = 'lightsteelblue2')
label1.config(font=('Courier', 10))
canvas1.create_window(w/1.5, 120, window=label1)


# affichier le chemin du programme
label2 = tk.Label(root, text="(LEMP) Laboratoire d'épidémiologie et de médecine porcine", bg = 'lightsteelblue2')
label2.config(font=('helvetica', 8))
canvas1.create_window(w/2, h-15, window=label2)


img = PhotoImage(file="LogoLemp3.png")
canvas1.create_image(120, 23, anchor=NW, image=img)



def getNewick ():  # sélectionner dans les rep un arbre newick de base
    global arbreBase     
    arbreBase = filedialog.askopenfilename(initialdir = G_chemin ,filetypes=[("Newick tree", ".tree .tre")])
    print(" arbre ",arbreBase) #D:/SRRP_dallaire/RUN_CLASSIFICATION/ArbreCustom/R144/ArbreFinal_Run144.tree


    
def getExcel ():    # sélectionner dans les rep un fichier .xlsx contenant les donner voulus dans l'arbre
    global read_file_Feuil1
    label3 = tk.Label(root, text="Travail en cours", bg = 'red')
    label3.config(font=('Courier', 15))
    canvas1.create_window(w/2, h-50, window=label3) 
    import_file_path = filedialog.askopenfilename(initialdir = G_chemin ,filetypes=[("Excel files", ".xlsx .xls")])
    print(" Excel ",import_file_path)    #D:/SRRP_dallaire/RUN_CLASSIFICATION/ArbreCustom/R144/cluster_final_Run144.xlsx
    print("   GÉNÉRATION DU NEWICK    ")
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        read_file_Feuil1 = pd.read_excel (import_file_path, 'Feuil1',engine="openpyxl")
    nomFichierCDPQ=import_file_path
    read_file_Feuil1.to_csv ( G_chemin + '.csv', index = None, header=True,sep='\t')
    if (arbreBase=="rien"):
        label3 = tk.Label(root, text="Sélectionnez un arbre de base avant ", bg = 'red')
        label3.config(font=('Courier', 15))
        canvas1.create_window(w/2, h-50, window=label3)   
    if (arbreBase!="rien"):
        # productin du fichier temp en csv  
        uneImport = faireArbreCustom(G_chemin +'.csv',G_chemin +"\Liste_TEMP.csv")
        uneImport.boucleFichier()
        # production et ouverture du fichier newick
        uneImport.AjouterChampsDansNewick()
        print("Fichier : arbre  OK")
        label4 = tk.Label(root, text="                                                ", bg = 'lightsteelblue2')
        label4.config(font=('Courier', 17))
        canvas1.create_window(w/2, h-50, window=label4)

def lanceArchao ():  # sélectionner dans les rep un arbre newick existant
    global arbreBase     
    arbreBase = filedialog.askopenfilename(initialdir = G_chemin ,filetypes=[("Newick tree", ".tree .tre")])
    print(arbreBase)
    a = subprocess.Popen('forester.jar '+arbreBase, shell=True, stdin = subprocess.PIPE, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
        
def lanceExcel ():  # sélectionner dans les rep un arbre newick existant
    global fichierExcel     
    fichierExcel = filedialog.askopenfilename(initialdir = G_chemin ,filetypes=[("Excel files", ".xlsx .xls")])
    print(fichierExcel)
    a = subprocess.Popen('start excel.exe '+fichierExcel, shell=True, stdin = subprocess.PIPE, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
      
def ouvrir_Rep (): 
	path = G_chemin
	path = os.path.realpath(path)
	os.startfile(path)



# chemin de travail	
G_chemin = os.path.dirname(os.path.realpath(__file__))  #"D:\\SRRP_dallaire\\RUN_CLASSIFICATION\\utilitaires\\ArbreCustom\\"


	
browseButton_Newick = tk.Button(text="   1-Choisir le fichier arbre de base   ", command=getNewick, bg='#eb7a34', fg='black', font=('helvetica', 11, 'bold'))
canvas1.create_window(w/2-130, 280, window=browseButton_Newick)  
    
browseButton_Excel = tk.Button(text="   2-Choisir le fichier Excel   ", command=getExcel, bg='#eb7a34', fg='black', font=('helvetica', 11, 'bold'))
canvas1.create_window(w/2+130, 280, window=browseButton_Excel)

separator = ttk.Separator(root, orient='horizontal')
separator.place(relx=0, rely=0.64, relwidth=1, relheight=0.001)


browseButton_Archao = tk.Button(text="  Ouvrir un arbre existant  ", command=lanceArchao, bg='#34eb95', fg='black', font=('helvetica', 10, 'bold'))
canvas1.create_window(w/2-130, 355, window=browseButton_Archao)
browseButton_Excel = tk.Button(text="  Ouvrir et éditer un fichier Excel  ", command=lanceExcel, bg='#34eb95', fg='black', font=('helvetica', 10, 'bold'))
canvas1.create_window(w/2+130, 355, window=browseButton_Excel)

browseButton_Rep = tk.Button(text="     "+os.path.dirname(os.path.realpath(__file__))+"     ", command=ouvrir_Rep, bg='#f5e020', fg='black', font=('Courier', 9, 'bold')) #Courier
canvas1.create_window(w/2, 415, window=browseButton_Rep)


root.mainloop()












