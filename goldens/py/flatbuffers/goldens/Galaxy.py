# automatically generated by the FlatBuffers compiler, do not modify

# namespace: goldens

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class Galaxy(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Galaxy()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsGalaxy(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # Galaxy
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Galaxy
    def NumStars(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

def GalaxyStart(builder):
    builder.StartObject(1)

def Start(builder):
    GalaxyStart(builder)

def GalaxyAddNumStars(builder, numStars):
    builder.PrependInt64Slot(0, numStars, 0)

def AddNumStars(builder, numStars):
    GalaxyAddNumStars(builder, numStars)

def GalaxyEnd(builder):
    return builder.EndObject()

def End(builder):
    return GalaxyEnd(builder)