"""
*  ____           _
* |  _ \ ___   __| |_ __ _   _ _ __ ___
* | |_) / _ \ / _` | '__| | | | '_ ` _ \
* |  __/ (_) | (_| | |  | |_| | | | | | |
* |_|   \___/ \__,_|_|   \__,_|_| |_| |_|
*
* Licensed under the Mozilla Public License, Version 2.
* Permissions of this weak copyleft license are conditioned on making
* available source code of licensed files and modifications of those files 
* under the same license (or in certain cases, one of the GNU licenses).
* Copyright and license notices must be preserved. Contributors
* provide an express grant of patent rights. However, a larger work
* using the licensed work may be distributed under different terms and without 
* source code for files added in the larger work.
"""

from podrum.command.Command import Command
from podrum.plugin.Plugin import Plugin
from podrum.utils.Utils import Utils

class StopCommand(Command):
    def __init__(self, name = "", description = ""):
        super().__init__("stop", "Stop Command")

    def execute(self, sender, args):
        sender.sendMessage("Stopping server...")
        Plugin.unloadAll()
        sender.sendMessage("Server stopped.")
        Utils.killServer()
