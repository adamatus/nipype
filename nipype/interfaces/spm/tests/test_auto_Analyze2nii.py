# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.spm.utils import Analyze2nii
def test_Analyze2nii_inputs():
    input_map = dict(ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    analyze_file=dict(mandatory=True,
    ),
    paths=dict(),
    use_v8struct=dict(min_ver='8',
    usedefault=True,
    ),
    use_mcr=dict(),
    matlab_cmd=dict(),
    mfile=dict(usedefault=True,
    ),
    )
    inputs = Analyze2nii.input_spec()

    for key, metadata in input_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(inputs.traits()[key], metakey), value
def test_Analyze2nii_outputs():
    output_map = dict(ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    paths=dict(),
    use_v8struct=dict(min_ver='8',
    usedefault=True,
    ),
    use_mcr=dict(),
    matlab_cmd=dict(),
    mfile=dict(usedefault=True,
    ),
    nifti_file=dict(),
    )
    outputs = Analyze2nii.output_spec()

    for key, metadata in output_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(outputs.traits()[key], metakey), value
