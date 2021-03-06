# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.camino.calib import SFLUTGen
def test_SFLUTGen_inputs():
    input_map = dict(ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    out_file=dict(position=-1,
    genfile=True,
    argstr='> %s',
    ),
    minvectsperbin=dict(units='NA',
    argstr='-minvectsperbin %d',
    ),
    args=dict(argstr='%s',
    ),
    terminal_output=dict(mandatory=True,
    nohash=True,
    ),
    binincsize=dict(units='NA',
    argstr='-binincsize %d',
    ),
    in_file=dict(mandatory=True,
    argstr='-inputfile %s',
    ),
    directmap=dict(argstr='-directmap',
    ),
    pdf=dict(usedefault=True,
    argstr='-pdf %s',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    outputstem=dict(argstr='-outputstem %s',
    usedefault=True,
    ),
    info_file=dict(mandatory=True,
    argstr='-infofile %s',
    ),
    order=dict(units='NA',
    argstr='-order %d',
    ),
    )
    inputs = SFLUTGen.input_spec()

    for key, metadata in input_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(inputs.traits()[key], metakey), value
def test_SFLUTGen_outputs():
    output_map = dict(lut_two_fibres=dict(),
    lut_one_fibre=dict(),
    )
    outputs = SFLUTGen.output_spec()

    for key, metadata in output_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(outputs.traits()[key], metakey), value
