import argparse
import asyncio
from controllers.integrations import Integration
from controllers.themes import Themes
from controllers.appdaemon import AppDaemons

from const import VERSION


def get_arguments() -> argparse.Namespace :

    parser = argparse.ArgumentParser()
    
    parser = argparse.ArgumentParser(
        description="Hacs CLI",
        usage="hacs-cli"  
    )
    
    parser.add_argument("--version", action="version", version=VERSION)
    parser.add_argument("-c","--config", action="store", help="Path for your config homeassistant",required=True)
    
    subparser = parser.add_subparsers()

    integrations = subparser.add_parser("integrations")
    integrations.add_argument("-a","--add",action="store",help="Added new integration")    
    integrations.add_argument("-r","--remove",action="store",help="Remove integration installed")    
    integrations.add_argument("-l","--list",action="store_true",help="List all integrations")
    integrations.add_argument("-ll","--list-local",action="store_true",help="List all integrations local")
    integrations.set_defaults(func=Integration)
    
    themes = subparser.add_parser("themes")

    themes.add_argument("-a","--add",action="store",help="Added new theme")    
    themes.add_argument("-r","--remove",action="store",help="Remove theme installed")    
    themes.add_argument("-l","--list",action="store_true",help="List all themes")
    themes.add_argument("-ll","--list-local",action="store_true",help="List all local")
    themes.set_defaults(func=Themes)

    appdaemon = subparser.add_parser("appdaemon")   
    
    appdaemon.add_argument("-a","--add",action="store",help="Added new appdaemon")    
    appdaemon.add_argument("-r","--remove",action="store",help="Remove appdaemon installed")    
    appdaemon.add_argument("-l","--list",action="store_true",help="List all appdaemons")
    appdaemon.add_argument("-ll","--list-local",action="store_true",help="List all local")
    appdaemon.set_defaults(func=AppDaemons)

    plugins = subparser.add_parser("plugins")
    pythonscripts = subparser.add_parser("pythonscripts")
    netdaemon = subparser.add_parser("netdaemon")

    arguments = parser.parse_args()
    return arguments


async def main():
    args = get_arguments()
    args.func(args)

asyncio.run(main())
