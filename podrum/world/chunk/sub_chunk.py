################################################################################
#                                                                              #
#  ____           _                                                            #
# |  _ \ ___   __| |_ __ _   _ _ __ ___                                        #
# | |_) / _ \ / _` | '__| | | | '_ ` _ \                                       #
# |  __/ (_) | (_| | |  | |_| | | | | | |                                      #
# |_|   \___/ \__,_|_|   \__,_|_| |_| |_|                                      #
#                                                                              #
# Copyright 2021 Podrum Studios                                                #
#                                                                              #
# Permission is hereby granted, free of charge, to any person                  #
# obtaining a copy of this software and associated documentation               #
# files (the "Software"), to deal in the Software without restriction,         #
# including without limitation the rights to use, copy, modify, merge,         #
# publish, distribute, sublicense, and/or sell copies of the Software,         #
# and to permit persons to whom the Software is furnished to do so,            #
# subject to the following conditions:                                         #
#                                                                              #
# The above copyright notice and this permission notice shall be included      #
# in all copies or substantial portions of the Software.                       #
#                                                                              #
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR   #
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,     #
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE  #
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER       #
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING      #
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS #
# IN THE SOFTWARE.                                                             #
#                                                                              #
################################################################################

from world.chunk.block_storage import block_storage

class sub_chunk:
    def __init__(self, block_storages: list = []) -> None:
        self.block_storages: list = block_storages

    def get_block_storage(self, layer: int) -> object:
        temp: int = (len(self.block_storages) - 1) - layer
        needs: int = 0 if temp > 0 else abs(temp)
        for i in range(0, needs):
            self.block_storages.append(block_storage())
        return self.block_storages[layer]
    
    def is_empty(self) -> bool:
        return bool(len(self.block_storages))
    
    def get_block(self, x: int, y: int, z: int, layer: int) -> tuple:
        return self.get_block_storage(layer).get_block(x, y & 0x0f, z)
    
    def set_block(self, x: int, y: int, z: int, block_id: int, meta: int, layer: int) -> None:
        self.get_block_storage(layer).set_block(x, y & 0x0f, z, block_id, meta)

    def network_serialize(self, stream: object) -> None:
        stream.write_unsigned_byte(8)
        stream.write_unsigned_byte(len(self.block_storages))
        for block_storage in self.block_storages:
            block_storage.network_serialize(stream)
