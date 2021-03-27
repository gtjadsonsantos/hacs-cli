import argparse
import requests
import git

from const import (API_HACS,HEADERS)
from . import IBasic

class Integration(IBasic):
    def __init__(self,args:argparse.Namespace):

        
        if args.add: 
            self.add(args)
        if args.remove: 
            self.remove(args)
        if args.list: 
            self.list(args)

    def add(self, args: argparse.Namespace) -> None:
        
        [repositorie,localPath] = args.add

        git.Repo.clone_from(
          "git@github.com:{repositorie}.git".format(repositorie=repositorie),
          localPath
        )
        pass

    def remove(self, args: argparse.Namespace) -> None:
        pass

    def list(self, args: argparse.Namespace) -> None:
        response = requests.get(API_HACS + "/repositories",headers=HEADERS).json()

        for integration in response["integration"]:
            print(integration)

        pass

