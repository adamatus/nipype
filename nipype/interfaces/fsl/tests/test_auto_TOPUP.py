# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.fsl.epi import TOPUP
def test_TOPUP_inputs():
    input_map = dict(minmet=dict(argstr='--minmet=%d',
    ),
    splineorder=dict(argstr='--splineorder=%d',
    ),
    out_base=dict(argstr='--out=%s',
    ),
    subsamp=dict(argstr='--subsamp=%d',
    ),
    fwhm=dict(argstr='--fwhm=%f',
    ),
    out_logfile=dict(argstr='--logout=%s',
    ),
    scale=dict(argstr='--scale=%d',
    ),
    encoding_direction=dict(),
    out_field=dict(argstr='--fout=%s',
    ),
    regrid=dict(argstr='--regrid=%d',
    ),
    in_file=dict(mandatory=True,
    argstr='--imain=%s',
    ),
    config=dict(argstr='--config=%s',
    usedefault=True,
    ),
    encoding_file=dict(argstr='--datain=%s',
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    out_corrected=dict(argstr='--iout=%s',
    ),
    max_iter=dict(argstr='--miter=%d',
    ),
    interp=dict(argstr='--interp=%s',
    ),
    readout_times=dict(),
    args=dict(argstr='%s',
    ),
    terminal_output=dict(mandatory=True,
    nohash=True,
    ),
    warp_res=dict(argstr='--warpres=%f',
    ),
    estmov=dict(argstr='--estmov=%d',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    output_type=dict(),
    numprec=dict(argstr='--numprec=%s',
    ),
    )
    inputs = TOPUP.input_spec()

    for key, metadata in input_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(inputs.traits()[key], metakey), value
def test_TOPUP_outputs():
    output_map = dict(out_corrected=dict(),
    out_logfile=dict(),
    out_topup=dict(),
    out_fieldcoef=dict(),
    out_movpar=dict(),
    out_enc_file=dict(),
    out_field=dict(),
    )
    outputs = TOPUP.output_spec()

    for key, metadata in output_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(outputs.traits()[key], metakey), value
