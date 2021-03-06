# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.afni.preprocess import Merge
def test_Merge_inputs():
    input_map = dict(ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    out_file=dict(name_source='in_file',
    name_template='%s_merge',
    argstr='-prefix %s',
    ),
    blurfwhm=dict(units='mm',
    argstr='-1blur_fwhm %d',
    ),
    args=dict(argstr='%s',
    ),
    outputtype=dict(),
    in_files=dict(copyfile=False,
    mandatory=True,
    position=-1,
    argstr='%s',
    ),
    terminal_output=dict(mandatory=True,
    nohash=True,
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    doall=dict(argstr='-doall',
    ),
    )
    inputs = Merge.input_spec()

    for key, metadata in input_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(inputs.traits()[key], metakey), value
def test_Merge_outputs():
    output_map = dict(out_file=dict(),
    )
    outputs = Merge.output_spec()

    for key, metadata in output_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(outputs.traits()[key], metakey), value
