import argparse
import requests
import shutil
import os
import git

from const import (API_HACS,HEADERS,HACS_CLI_FOLDER)
from . import IBasic

class AppDaemons(IBasic):
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
            if self.__findAppdaemon(repositorie):

                if os.path.exists(os.path.join(args.config,HACS_CLI_FOLDER)):
                    shutil.rmtree(os.path.join(args.config,HACS_CLI_FOLDER))


                localPath = os.path.join(args.config,HACS_CLI_FOLDER,repositorie.split("/")[1])

                git.Repo.clone_from(
                "git@github.com:{repositorie}.git".format(repositorie=repositorie),
                localPath
                )

                if not os.path.exists(os.path.join(args.config,"apps")):
                        os.mkdir(os.path.join(args.config,"apps"))  
              
                for item in os.listdir(os.path.join(localPath,"apps")):

                    if os.path.exists(os.path.join(args.config,"apps",item)):
                        shutil.rmtree(os.path.join(args.config,"apps",item))

                    shutil.move(
                        os.path.join(localPath,"apps",item),
                        os.path.join(args.config,"apps",item)
                   )

                shutil.rmtree(
                    os.path.join(args.config,HACS_CLI_FOLDER)
                )
            else:
                print("AppDaemon not found")
                print("Hacs Development: https://hacs.xyz/docs/publish/appdaemon")
                
        except shutil.Error as e :
            print(e)
        pass

    def remove(self, args: argparse.Namespace) -> None:
        folder_name  = args.remove
        path_Appdaemon = os.path.join(args.config,"apps",folder_name)
        
        if os.path.exists(path_Appdaemon):
            shutil.rmtree(path_Appdaemon)
        else:
            print("App Daemon not exists")

    def list(self, args: argparse.Namespace) -> None:
        response:dict = requests.get(API_HACS + "/repositories",headers=HEADERS).json()

        for appdaemon in response["appdaemon"]:
            print(appdaemon)
        pass

    def list_local(self, args: argparse.Namespace) -> None:

       try:
          for appdaemon in os.listdir(os.path.join(args.config,"apps")):
            print(appdaemon)
       except FileNotFoundError as e:
            print(e)

    def __findAppdaemon(self,repo_appdaemon:str) -> bool:
        response:dict = requests.get(API_HACS + "/repositories",headers=HEADERS).json()

        isExists = False

        for appdaemon in response["appdaemon"]:
            if appdaemon == repo_appdaemon: isExists = True
        
        return isExists
        pass


