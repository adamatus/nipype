# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.spm.model import ThresholdStatistics
def test_ThresholdStatistics_inputs():
    input_map = dict(ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    paths=dict(),
    spm_mat_file=dict(copyfile=True,
    mandatory=True,
    ),
    use_v8struct=dict(min_ver='8',
    usedefault=True,
    ),
    use_mcr=dict(),
    extent_threshold=dict(usedefault=True,
    ),
    contrast_index=dict(mandatory=True,
    ),
    matlab_cmd=dict(),
    height_threshold=dict(mandatory=True,
    ),
    mfile=dict(usedefault=True,
    ),
    stat_image=dict(copyfile=False,
    mandatory=True,
    ),
    )
    inputs = ThresholdStatistics.input_spec()

    for key, metadata in input_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(inputs.traits()[key], metakey), value
def test_ThresholdStatistics_outputs():
    output_map = dict(voxelwise_P_RF=dict(),
    voxelwise_P_FDR=dict(),
    voxelwise_P_Bonf=dict(),
    clusterwise_P_FDR=dict(),
    clusterwise_P_RF=dict(),
    voxelwise_P_uncor=dict(),
    )
    outputs = ThresholdStatistics.output_spec()

    for key, metadata in output_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(outputs.traits()[key], metakey), value
