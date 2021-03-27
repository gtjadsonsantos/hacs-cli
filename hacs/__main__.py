import argparse
import asyncio
from constrollers.integrations import Integration

from const import VERSION


def get_arguments() -> argparse.Namespace :

    parser = argparse.ArgumentParser()
    
    parser = argparse.ArgumentParser(
        description="Hacs CLI"
    )
    
    parser.add_argument("--version", action="version", version=VERSION)
    
    subparser = parser.add_subparsers()

    integrations = subparser.add_parser("integrations")
    integrations.add_argument("-a","--add",action="store",nargs="*",help="Added new integration")    
    integrations.add_argument("-r","--remove",action="store_true",help="Added new integration")    
    integrations.add_argument("-l","--list",action="store_true",help="List all integrations")
    integrations.set_defaults(func=Integration)
    

    themes = subparser.add_parser("themes")
    plugins = subparser.add_parser("plugins")
    pythonscripts = subparser.add_parser("pythonscripts")
    netdaemon = subparser.add_parser("netdaemon")
    appdaemon = subparser.add_parser("appdaemon")   

    arguments = parser.parse_args()
    return arguments


async def main():
    args = get_arguments()
    args.func(args)

asyncio.run(main())













