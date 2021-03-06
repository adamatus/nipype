# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.afni.preprocess import Resample
def test_Resample_inputs():
    input_map = dict(ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    out_file=dict(name_source='in_file',
    name_template='%s_resample',
    argstr='-prefix %s',
    ),
    args=dict(argstr='%s',
    ),
    outputtype=dict(),
    resample_mode=dict(argstr='-rmode %s',
    ),
    voxel_size=dict(argstr='-dxyz %f %f %f',
    ),
    terminal_output=dict(mandatory=True,
    nohash=True,
    ),
    master=dict(argstr='-master %s',
    ),
    in_file=dict(copyfile=False,
    mandatory=True,
    position=-1,
    argstr='-inset %s',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    orientation=dict(argstr='-orient %s',
    ),
    )
    inputs = Resample.input_spec()

    for key, metadata in input_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(inputs.traits()[key], metakey), value
def test_Resample_outputs():
    output_map = dict(out_file=dict(),
    )
    outputs = Resample.output_spec()

    for key, metadata in output_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(outputs.traits()[key], metakey), value
