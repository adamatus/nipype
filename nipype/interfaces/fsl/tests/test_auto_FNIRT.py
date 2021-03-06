# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.fsl.preprocess import FNIRT
def test_FNIRT_inputs():
    input_map = dict(derive_from_ref=dict(argstr='--refderiv',
    ),
    in_intensitymap_file=dict(argstr='--intin=%s',
    ),
    modulatedref_file=dict(hash_files=False,
    argstr='--refout=%s',
    ),
    refmask_val=dict(argstr='--imprefval=%f',
    ),
    hessian_precision=dict(argstr='--numprec=%s',
    ),
    skip_implicit_in_masking=dict(argstr='--impinm=0',
    ),
    inmask_file=dict(argstr='--inmask=%s',
    ),
    refmask_file=dict(argstr='--refmask=%s',
    ),
    apply_refmask=dict(argstr='--applyrefmask=%s',
    xor=['skip_refmask'],
    sep=',',
    ),
    skip_lambda_ssq=dict(argstr='--ssqlambda=0',
    ),
    intensity_mapping_model=dict(argstr='--intmod=%s',
    ),
    affine_file=dict(argstr='--aff=%s',
    ),
    apply_inmask=dict(argstr='--applyinmask=%s',
    xor=['skip_inmask'],
    sep=',',
    ),
    spline_order=dict(argstr='--splineorder=%d',
    ),
    inwarp_file=dict(argstr='--inwarp=%s',
    ),
    subsampling_scheme=dict(sep=',',
    argstr='--subsamp=%s',
    ),
    in_file=dict(mandatory=True,
    argstr='--in=%s',
    ),
    warped_file=dict(argstr='--iout=%s',
    hash_files=False,
    genfile=True,
    ),
    skip_refmask=dict(xor=['apply_refmask'],
    argstr='--applyrefmask=0',
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    ref_fwhm=dict(sep=',',
    argstr='--reffwhm=%s',
    ),
    args=dict(argstr='%s',
    ),
    config_file=dict(argstr='--config=%s',
    ),
    skip_inmask=dict(xor=['apply_inmask'],
    argstr='--applyinmask=0',
    ),
    field_file=dict(hash_files=False,
    argstr='--fout=%s',
    ),
    inmask_val=dict(argstr='--impinval=%f',
    ),
    apply_intensity_mapping=dict(argstr='--estint=%s',
    xor=['skip_intensity_mapping'],
    sep=',',
    ),
    regularization_lambda=dict(sep=',',
    argstr='--lambda=%s',
    ),
    terminal_output=dict(mandatory=True,
    nohash=True,
    ),
    regularization_model=dict(argstr='--regmod=%s',
    ),
    jacobian_range=dict(argstr='--jacrange=%f,%f',
    ),
    out_intensitymap_file=dict(hash_files=False,
    argstr='--intout=%s',
    ),
    skip_implicit_ref_masking=dict(argstr='--imprefm=0',
    ),
    log_file=dict(argstr='--logout=%s',
    hash_files=False,
    genfile=True,
    ),
    ref_file=dict(mandatory=True,
    argstr='--ref=%s',
    ),
    biasfield_resolution=dict(argstr='--biasres=%d,%d,%d',
    ),
    fieldcoeff_file=dict(argstr='--cout=%s',
    ),
    warp_resolution=dict(argstr='--warpres=%d,%d,%d',
    ),
    jacobian_file=dict(hash_files=False,
    argstr='--jout=%s',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    output_type=dict(),
    skip_intensity_mapping=dict(xor=['apply_intensity_mapping'],
    argstr='--estint=0',
    ),
    in_fwhm=dict(sep=',',
    argstr='--infwhm=%s',
    ),
    bias_regularization_lambda=dict(argstr='--biaslambda=%f',
    ),
    intensity_mapping_order=dict(argstr='--intorder=%d',
    ),
    max_nonlin_iter=dict(sep=',',
    argstr='--miter=%s',
    ),
    )
    inputs = FNIRT.input_spec()

    for key, metadata in input_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(inputs.traits()[key], metakey), value
def test_FNIRT_outputs():
    output_map = dict(modulatedref_file=dict(),
    fieldcoeff_file=dict(),
    jacobian_file=dict(),
    field_file=dict(),
    warped_file=dict(),
    log_file=dict(),
    out_intensitymap_file=dict(),
    )
    outputs = FNIRT.output_spec()

    for key, metadata in output_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(outputs.traits()[key], metakey), value
