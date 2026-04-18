# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class Bild(KaitaiStruct):
    def __init__(self, _io, _parent=None, _root=None):
        super(Bild, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._read()

    def _read(self):
        self.magic = self._io.read_bytes(4)
        if not self.magic == b"\x42\x49\x4C\x44":
            raise kaitaistruct.ValidationNotEqualError(b"\x42\x49\x4C\x44", self.magic, self._io, u"/seq/0")
        self.version = self._io.read_u4le()
        self.num_symbols = self._io.read_u4le()
        self.num_frames = self._io.read_u4le()
        self.len_build_name = self._io.read_u4le()
        self.build_name = (self._io.read_bytes(self.len_build_name)).decode(u"UTF-8")
        self.num_materials = self._io.read_u4le()
        self.materials = []
        for i in range(self.num_materials):
            self.materials.append(Bild.Material(self._io, self, self._root))

        self.symbols = []
        for i in range(self.num_symbols):
            self.symbols.append(Bild.Symbol(self._io, self, self._root))

        self.num_vertices = self._io.read_u4le()
        self.vertices = []
        for i in range(self.num_vertices):
            self.vertices.append(Bild.Vertex(self._io, self, self._root))

        self.num_hashed_strings = self._io.read_u4le()
        self.hashed_strings = []
        for i in range(self.num_hashed_strings):
            self.hashed_strings.append(Bild.HashedString(self._io, self, self._root))

        self.tail = self._io.read_bytes_full()


    def _fetch_instances(self):
        pass
        for i in range(len(self.materials)):
            pass
            self.materials[i]._fetch_instances()

        for i in range(len(self.symbols)):
            pass
            self.symbols[i]._fetch_instances()

        for i in range(len(self.vertices)):
            pass
            self.vertices[i]._fetch_instances()

        for i in range(len(self.hashed_strings)):
            pass
            self.hashed_strings[i]._fetch_instances()


    class Frame(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(Bild.Frame, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.frame_num = self._io.read_u4le()
            self.duration = self._io.read_u4le()
            self.x = self._io.read_f4le()
            self.y = self._io.read_f4le()
            self.w = self._io.read_f4le()
            self.h = self._io.read_f4le()
            self.vb_start_index = self._io.read_u4le()
            self.num_verts = self._io.read_u4le()


        def _fetch_instances(self):
            pass


    class HashedString(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(Bild.HashedString, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.hash = self._io.read_u4le()
            self.len_original_string = self._io.read_u4le()
            self.original_string = (self._io.read_bytes(self.len_original_string)).decode(u"UTF-8")


        def _fetch_instances(self):
            pass


    class Material(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(Bild.Material, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.len_material_texture_name = self._io.read_u4le()
            self.material_texture_name = (self._io.read_bytes(self.len_material_texture_name)).decode(u"UTF-8")


        def _fetch_instances(self):
            pass


    class Symbol(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(Bild.Symbol, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.symbol_hash = self._io.read_u4le()
            self.num_frames = self._io.read_u4le()
            self.frames = []
            for i in range(self.num_frames):
                self.frames.append(Bild.Frame(self._io, self, self._root))



        def _fetch_instances(self):
            pass
            for i in range(len(self.frames)):
                pass
                self.frames[i]._fetch_instances()



    class Vertex(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(Bild.Vertex, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.x = self._io.read_f4le()
            self.y = self._io.read_f4le()
            self.z = self._io.read_f4le()
            self.u = self._io.read_f4le()
            self.v = self._io.read_f4le()
            self.w = self._io.read_f4le()


        def _fetch_instances(self):
            pass



