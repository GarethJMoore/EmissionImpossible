"""Parameter configuration definitions extracted from the notebook."""

import copy

# Parameter Configs
"""
We set universal parameter configurations for each volatile
"""
param_config_DMNT = {
    # 'R_peak': {'min': 5, 'max':  60 },
    # 't_peak': {'min': 1.5, 'max':  3.5 },
    "t_onset": {"min": 0, "max": 10},
    "t_mean": {"min": 0, "max": 20},
}

param_config_indole = {
    # 'R_peak': {'min': 30, 'max':  90 },
    # 't_peak': {'min': 2, 'max':  4 },
    "t_onset": {"min": 0, "max": 10},
    "t_mean": {"min": 1, "max": 20},
}

param_config_TMTT = {
    # 'R_peak': {'min': 2, 'max':  10 },
    # 't_peak': {'min': 6, 'max':  10 },
    "t_onset": {"min": 0, "max": 10},
    "t_mean": {"min": 1, "max": 20},
}

param_config_sesq = {
    # 'R_peak': {'min': 10, 'max':  50 },
    # 't_peak': {'min': 6, 'max':  9 },
    "t_onset": {"min": 0, "max": 10},
    "t_mean": {"min": 1, "max": 20},
}

param_config_mono = {
    # 'R_peak': {'min': 25, 'max':  150 },
    # 't_peak': {'min': 3.1, 'max':  8 },
    "t_onset": {"min": 0, "max": 10},
    "t_mean": {"min": 1, "max": 20},
}


def get_default_param_configs():
    """Return deep-copied default per-compound parameter configs."""
    return {
        "DMNT": copy.deepcopy(param_config_DMNT),
        "indole": copy.deepcopy(param_config_indole),
        "TMTT": copy.deepcopy(param_config_TMTT),
        "sesq": copy.deepcopy(param_config_sesq),
        "mono": copy.deepcopy(param_config_mono),
    }
