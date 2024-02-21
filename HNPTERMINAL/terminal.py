import os
from rich.console import Console
from rich.progress import track
from rich.style import Style
from rich.tree import Tree as Tr
import datetime
import shutil
import psutil
import requests
import webbrowser
import sys
import subprocess
import time

boldorange_style = Style.parse("#ffaa2a")
greenita_style = Style.parse("italic green")
console = Console()


def help():
    treehelp = Tr("[bold yellow]Help")
    treehelp.add("[italic blue]mkdir | créer un dossier")
    treehelp.add("[italic blue]cf | créer un fichier")
    treehelp.add("[italic blue]whoami | Si l'user est administrateur ou non")
    treehelp.add("[italic blue]cd | acceder a un dossier")
    treehelp.add("[italic blue]ls | Affiche les fichiers du dossier.")
    treehelp.add("[italic blue]rm | Supprime un dossier/fichier.")
    treehelp.add("[italic blue]cp | copie/colle un dossier/fichier.")
    treehelp.add("[italic blue]mv | deplace un dossier/fichier.")
    treehelp.add("[italic blue]ps | copie/colle un dossier/fichier.")
    treehelp.add("[italic blue]time | donne la date exacte.")
    treehelp.add("[italic blue]clear | clear le terminale.")
    treehelp.add("[italic blue]pip | installe un package.")
    treehelp.add("[italic blue]lbdr | ...")
    treehelp.add("[bold green] Coming Soon..")

    console.print(treehelp)
    

def mkdir():
    mkdir1 = console.input(r"[italic yellow][?] Chemin & Nom du dossier > ")
    try:
        os.mkdir(mkdir1)
    except TypeError as e:
        print(e)
    except PermissionError as e:
        print(e)
        
def cf():
    console.print('[italic yellow][?][/] [italic red]Attention:[/][italic yellow] si le fichier existe déjà il va écraser celui-ci. Il est donc conseillé de verifier au préalable si le fichier existe déjà dans votre répertoire courant.')
    cf = console.input(r"[italic yellow][?] Chemin & Nom du fichier (avec extension) > ")
    f = open(cf)


def whoami():
    console.print(r"[red]", os.environ.get("USERNAME"))
    
def cd():
    go_to_directory = console.input(r"[italic yellow][?] Chemin > ")
    try:
        os.chdir(go_to_directory)
        
    except PermissionError as e:
        print(e)



def ls():
    Directory = os.listdir()
    console.print(Directory, style=boldorange_style)
    

def rm():
    console.print("""
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
""", style=greenita_style)
    rm1 = console.input(r"[italic yellow][?] Chemin & Nom du Fichier/Dossier a supprimer >")
    console.print("""
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■""", style=greenita_style)
    try:
        os.remove(rm1)
        
    except PermissionError as e:
        print(e)

def cp(): 
    console.print("""
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
""", style=greenita_style)
    copy_folder = console.input(r"[italic yellow][?] Chemin du Fichier/Dossier a copier > ")
    folder_dest = console.input(r"[italic yellow][?] Chemin du Fichier/Dossier a deplacer > ")
    shutil.copyfile(copy_folder, folder_dest)

def mv():
    console.print("""
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
""", style=greenita_style)
    move_folder = input(r"[italic yellow][?] Chemin du Fichier/Dossier a deplacer >")
    desitination_folder = console.input(r"[italic yellow][?] Chemin de destination du Fichier/Dossier a deplacer >")
    console.print("""
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■""", style=greenita_style)
    
    try:
        shutil.move(move_folder, desitination_folder)
    except PermissionError as e:
        print(e)
    except FileNotFoundError as e:
        print(e)


def ps():
    processlist=list()
    for process in psutil.process_iter():
        processlist.append(process.name())
    print(processlist)

def lbdr():
    for i in range(5):
        webbrowser.open("https://youtu.be/hht4RtpMcBI?si=7ESnvnHU1B0XynWg")    

def pip():
    pipinput = console.input("[italic yellow][?] Quel package veux-tu installer > ")
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', pipinput])

 
def Terminale():
    
    
    greenita_style = Style.parse("italic green")
    
    for i in track(range(100), description="Téléchargement.. | Made by Psycho."):
        time.sleep(0.02)

    time.sleep(1)
    print("\033c", end='')

    
    while True:
        #input
        
        current_directory = os.getcwd()
        
        console.print("""
[+] Chemin:""", current_directory, style=greenita_style)
        commande = console.input("""[italic green][?] Terminal > """)

        #execution des commandes
        if commande in ["help", "--h", "HELP", "--h"]:
            help()
        #mkdir
        elif commande in ["mkdir", "makedir", "MKDIR"]:
            mkdir()
        #cf
        elif commande in ["cf", "createf", "createfile", "CF", "CREATEF", "CREATEFILE"]:
            cf()
        #whoami
        elif commande in ["whoami", "WHOAMI"]:
            whoami()
        #cd
        elif commande in ["cd", "CD"]:
            cd()
        #ls
        elif commande in ["ls", "LS"]:
            ls()
        #remove
        elif commande in ["rm", "remove", "RM", "REMOVE"]:
            rm()
        #copy
        elif commande in ["cp", "CP", "copy", "COPY"]:
            cp()
        #move
        elif commande in ["mv", "move", "MV", "MOVE"]:
            mv()
        #ps
        elif commande in ["ps", "PS"]:
            ps()
        #time
        elif commande in ["time", "TIME"]:
            print(datetime.datetime.now())
        #clear
        elif commande in ["clear", "clr", "CLEAR", "CLR"]:
            print("\033c", end='')
        elif commande in ["lbdr"]:
            lbdr()
        elif commande in ["pip"]:
            pip()
        #exit
        elif commande == ["exit", "leave", "quit", "quitte", "quitter" "EXIT", "leave", "quit", "quitte", "quitter"]:
            break
        
        else:
            console.print("""[bold red][-] Le terme écris dans la console n'est pas reconnu comme nom d'applet de commande, fonction, fichier de script ou programme exécutable.
[+] Vérifiez l'orthographe du nom, ou si un chemin d'accès existe, vérifiez que le chemin d'accès est correct et réessayez.""")
