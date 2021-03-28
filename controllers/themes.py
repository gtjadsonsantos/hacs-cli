import argparse
from os import path, remove
import requests
import shutil
import os
import git

from const import (API_HACS,HEADERS,HACS_CLI_FOLDER)
from . import IBasic

class Themes(IBasic):
    def __init__(self,args:argparse.Namespace):
        
        if args.add: 
            self.add(args)
        if args.remove: 
            self.remove(args)
        if args.list: 
            self.list(args)
        if args.list_local: 
            self.list_local(args)


    def add(self, args: argparse.Namespace) -> None:
        repositorie = str(args.add)        

        try:
            if self.__findTheme(repositorie):
                
                if os.path.exists(os.path.join(args.config,HACS_CLI_FOLDER)):
                    shutil.rmtree(os.path.join(args.config,HACS_CLI_FOLDER))

                localPath = os.path.join(args.config,HACS_CLI_FOLDER,repositorie.split("/")[1])

                git.Repo.clone_from(
                "git@github.com:{repositorie}.git".format(repositorie=repositorie),
                localPath
                )

                for item in os.listdir(os.path.join(args.config,HACS_CLI_FOLDER)):
                    shutil.move(
                        os.path.join(localPath,"themes",item),
                        os.path.join(args.config,"themes"
                        )
                )
                shutil.rmtree(
                    os.path.join(args.config,HACS_CLI_FOLDER)
                )
            else:
                print("Theme not found")
                print("Hacs Development: https://hacs.xyz/docs/publish/theme")
                
        except shutil.Error as e :
            print(e)
        pass

    def remove(self, args: argparse.Namespace) -> None:
        filename  = args.remove
        pathTheme = os.path.join(args.config,"themes",filename)
        
        if os.path.exists(pathTheme):
            shutil.rmtree(pathTheme)
        else:
            print("Theme not exists")

    def list(self, args: argparse.Namespace) -> None:
        response:dict = requests.get(API_HACS + "/repositories",headers=HEADERS).json()

        for theme in response["theme"]:
            print(theme)
        pass

    def list_local(self, args: argparse.Namespace) -> None:

       for theme in os.listdir(os.path.join(args.config,"themes")):
           print(theme)
        

    def __findTheme(self,repo_theme:str) -> bool:
        response:dict = requests.get(API_HACS + "/repositories",headers=HEADERS).json()

        isExists = False

        for theme in response["themes"]:
            if theme == repo_theme: isExists = True
        
        return isExists
        pass


