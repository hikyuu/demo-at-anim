# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class Anim(KaitaiStruct):
    def __init__(self, _io, _parent=None, _root=None):
        super(Anim, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._read()

    def _read(self):
        self.magic = self._io.read_bytes(4)
        if not self.magic == b"\x41\x4E\x49\x4D":
            raise kaitaistruct.ValidationNotEqualError(b"\x41\x4E\x49\x4D", self.magic, self._io, u"/seq/0")
        self.version = self._io.read_u4le()
        self.num_elements = self._io.read_u4le()
        self.num_frames = self._io.read_u4le()
        self.num_events = self._io.read_u4le()
        self.num_anims = self._io.read_u4le()
        self.anims = []
        for i in range(self.num_anims):
            self.anims.append(Anim.Anim(self._io, self, self._root))

        self.num_hashed_strings = self._io.read_u4le()
        self.hashed_strings = []
        for i in range(self.num_hashed_strings):
            self.hashed_strings.append(Anim.HashedString(self._io, self, self._root))

        self.tail = self._io.read_bytes_full()


    def _fetch_instances(self):
        pass
        for i in range(len(self.anims)):
            pass
            self.anims[i]._fetch_instances()

        for i in range(len(self.hashed_strings)):
            pass
            self.hashed_strings[i]._fetch_instances()


    class Anim(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(Anim.Anim, self).__init__(_io)
            self._parent = _parent
            self._root = _root or self
            self._read()

        def _read(self):
            self.len_name = self._io.read_u4le()
            self.name = (self._io.read_bytes(self.len_name)).decode(u"UTF-8")
            self.validfacings = self._io.read_u1()
            self.root_symbol_hash = self._io.read_u4le()
            self.frame_rate = self._io.read_f4le()
            self.num_frames = self._io.read_u4le()
            self.frames = []
            for i in range(self.num_frames):
                self.frames.append(Anim.Frame(self._io, self, self._root))



        def _fetch_instances(self):
            pass
            for i in range(len(self.frames)):
                pass
                self.frames[i]._fetch_instances()



    class Element(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(Anim.Element, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.symbol_hash = self._io.read_u4le()
            self.symbol_frame = self._io.read_u4le()
            self.folder_hash = self._io.read_u4le()
            if self._root.version == 5:
                pass
                self.unknown_value = self._io.read_f4le()

            if self._root.version == 6:
                pass
                self.unknown_hash = self._io.read_u4le()

            self.mat = Anim.Mat(self._io, self, self._root)


        def _fetch_instances(self):
            pass
            if self._root.version == 5:
                pass

            if self._root.version == 6:
                pass

            self.mat._fetch_instances()


    class Event(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(Anim.Event, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.event_hash = self._io.read_u4le()


        def _fetch_instances(self):
            pass


    class Frame(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(Anim.Frame, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.x = self._io.read_f4le()
            self.y = self._io.read_f4le()
            self.w = self._io.read_f4le()
            self.h = self._io.read_f4le()
            self.num_events = self._io.read_u4le()
            self.events = []
            for i in range(self.num_events):
                self.events.append(Anim.Event(self._io, self, self._root))

            self.num_elements = self._io.read_u4le()
            self.elements = []
            for i in range(self.num_elements):
                self.elements.append(Anim.Element(self._io, self, self._root))



        def _fetch_instances(self):
            pass
            for i in range(len(self.events)):
                pass
                self.events[i]._fetch_instances()

            for i in range(len(self.elements)):
                pass
                self.elements[i]._fetch_instances()



    class HashedString(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(Anim.HashedString, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.hash = self._io.read_u4le()
            self.len_original_string = self._io.read_u4le()
            self.original_string = (self._io.read_bytes(self.len_original_string)).decode(u"UTF-8")


        def _fetch_instances(self):
            pass


    class Mat(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(Anim.Mat, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.a = self._io.read_f4le()
            self.b = self._io.read_f4le()
            self.c = self._io.read_f4le()
            self.d = self._io.read_f4le()
            self.tx = self._io.read_f4le()
            self.ty = self._io.read_f4le()
            self.z = self._io.read_f4le()
            if self._root.version == 6:
                pass
                self.unknown_value = self._io.read_f4le()

            self.sa = self._io.read_f4le()
            self.sb = self._io.read_f4le()
            self.sc = self._io.read_f4le()
            self.sd = self._io.read_f4le()
            self.stx = self._io.read_f4le()
            self.sty = self._io.read_f4le()
            self.sz = self._io.read_f4le()


        def _fetch_instances(self):
            pass
            if self._root.version == 6:
                pass




