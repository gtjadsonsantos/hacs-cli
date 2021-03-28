import argparse
from os import path, remove
import requests
import shutil
import os
import git

from const import (API_HACS,HEADERS,HACS_CLI_FOLDER)
from . import IBasic

class Integration(IBasic):
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

        localPath = os.path.join(args.config,HACS_CLI_FOLDER,repositorie.split("/")[1])

        git.Repo.clone_from(
          "git@github.com:{repositorie}.git".format(repositorie=repositorie),
          localPath
        )

        for item in os.listdir(os.path.join(args.config,HACS_CLI_FOLDER)):
            shutil.move(
                os.path.join(localPath,"custom_components",item),
                os.path.join(args.config,"custom_components")
        )

        shutil.rmtree(
            os.path.join(args.config,HACS_CLI_FOLDER)
        )
        pass

    def remove(self, args: argparse.Namespace) -> None:
        folder_name  = args.remove
        path_Integration = os.path.join(args.config,"custom_components",folder_name)
        
        if os.path.exists(path_Integration):
            shutil.rmtree(path_Integration)
        else:
            print("Integration not exists")

    def list(self, args: argparse.Namespace) -> None:
        response = requests.get(API_HACS + "/repositories",headers=HEADERS).json()

        for integration in response["integration"]:
            print(integration)

        pass

    def list_local(self, args: argparse.Namespace) -> None:

       for integration in os.listdir(os.path.join(args.config,"custom_components")):
           print(integration)
        

