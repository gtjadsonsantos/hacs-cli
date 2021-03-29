import argparse
from os import path, remove
import requests
import shutil
import os
import git

from const import (API_HACS,HEADERS,HACS_CLI_FOLDER)
from . import IBasic

class PythonScripts(IBasic):
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
            if self.__findPythonScript(repositorie):
                
                if os.path.exists(os.path.join(args.config,HACS_CLI_FOLDER)):
                    shutil.rmtree(os.path.join(args.config,HACS_CLI_FOLDER))

                localPath = os.path.join(args.config,HACS_CLI_FOLDER,repositorie.split("/")[1])

                git.Repo.clone_from(
                "git@github.com:{repositorie}.git".format(repositorie=repositorie),
                localPath
                )

                if not os.path.exists(os.path.join(args.config,"python_scripts")):
                        os.mkdir(os.path.join(args.config,"python_scripts"))

                for item in os.listdir(os.path.join(localPath,"python_scripts")):

    
                    if os.path.exists(os.path.join(args.config,"python_scripts",item)):
                        os.remove(os.path.join(args.config,"python_scripts",item))
                    
                    
                    shutil.move(
                        os.path.join(localPath,"python_scripts",item),
                        os.path.join(args.config,"python_scripts",item)
                    )

                shutil.rmtree(
                    os.path.join(args.config,HACS_CLI_FOLDER)
                )
            else:
                print("Python Script not found")
                print("Hacs Development: https://hacs.xyz/docs/publish/python_script")
                
        except shutil.Error as e :
            print(e)
        except FileNotFoundError as e:
            print(e)
        pass

    def remove(self, args: argparse.Namespace) -> None:
        filename  = args.remove
        pathPythonScript = os.path.join(args.config,"python_scripts",filename)
        
        if os.path.exists(pathPythonScript):
            if os.path.isdir(pathPythonScript):
                shutil.rmtree(pathPythonScript)
            else:
                os.remove(pathPythonScript)
        else:
            print("Python script not exists")

    def list(self, args: argparse.Namespace) -> None:
        response:dict = requests.get(API_HACS + "/repositories",headers=HEADERS).json()

        for python_script in response["python_script"]:
            print(python_script)
        pass

    def list_local(self, args: argparse.Namespace) -> None:
        
        try:
          for python_scrip in os.listdir(os.path.join(args.config,"python_scripts")):
            print(python_scrip)
        except FileNotFoundError as e:
            print(e)

    def __findPythonScript(self,repo_python_script:str) -> bool:
        response:dict = requests.get(API_HACS + "/repositories",headers=HEADERS).json()

        isExists = False

        for python_script in response["python_script"]:
            if python_script == repo_python_script: isExists = True
        
        return isExists
        pass


