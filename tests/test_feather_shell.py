import pytest
import graphics.feather_shell as mod

CASES = [
    ("world_space_layer_gap", (1,)),
    ("transmit_phase_func", (1,)),
    ("wind_phase_persist", (1,)),
    ("position_tex_double_buffer", (1,)),
    ("shell_stable_sort", (1,)),
    ("lod_layer_match", (1,)),
    ("load_feather", (1,)),
    ("build_shells", (1,)),
    ("shade_feather", (1,)),
    ("present_feather", (1,)),
    ("validate_feather", (1,)),
    ("metrics_feather", (1,)),
    ("audit_feather", (1,)),
    ("fallback_feather", (1,)),
    ("determinism_feather", (1,)),
]

@pytest.mark.parametrize("fn_name,args", CASES)
def test_contract(fn_name, args):
    fn = getattr(mod, fn_name)
    assert fn(*args) is not None
