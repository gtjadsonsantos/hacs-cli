import argparse
import requests
import shutil
import os
import git

from const import (API_HACS,HEADERS,HACS_CLI_FOLDER)
from . import IBasic

class NetDaemons(IBasic):
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
            if self.__findNetDaemon(repositorie):

                if os.path.exists(os.path.join(args.config,HACS_CLI_FOLDER)):
                    shutil.rmtree(os.path.join(args.config,HACS_CLI_FOLDER))

                localPath = os.path.join(args.config,HACS_CLI_FOLDER,repositorie.split("/")[1])

                git.Repo.clone_from(
                "git@github.com:{repositorie}.git".format(repositorie=repositorie),
                localPath
                )

                for item in os.listdir(os.path.join(args.config,HACS_CLI_FOLDER)):
                    shutil.move(
                        os.path.join(localPath,"netdaemon","apps",item),
                        os.path.join(args.config,"netdaemon","apps"
                        )
                )
                shutil.rmtree(
                    os.path.join(args.config,HACS_CLI_FOLDER)
                )
            else:
                print("NetDaemon not found")
                print("Hacs Development: https://hacs.xyz/docs/publish/netdaemon")
                
        except shutil.Error as e :
            print(e)
        pass

    def remove(self, args: argparse.Namespace) -> None:
        folder_name  = args.remove
        path_Netdaemon = os.path.join(args.config,"netdaemon","apps",folder_name)
        
        if os.path.exists(path_Netdaemon):
            shutil.rmtree(path_Netdaemon)
        else:
            print("Net Daemon not exists")

    def list(self, args: argparse.Namespace) -> None:
        response:dict = requests.get(API_HACS + "/repositories",headers=HEADERS).json()

        for netdaemon in response["netdaemon"]:
            print(netdaemon)
        pass

    def list_local(self, args: argparse.Namespace) -> None:

       try:
          for netdaemon in os.listdir(os.path.join(args.config,"netdaemon","apps")):
            print(netdaemon)
       except FileNotFoundError as e:
            print(e)

    def __findNetDaemon(self,repo_netdaemon:str) -> bool:
        response:dict = requests.get(API_HACS + "/repositories",headers=HEADERS).json()

        isExists = False

        for netdaemon in response["netdaemon"]:
            if netdaemon == repo_netdaemon: isExists = True
        
        return isExists
        pass


