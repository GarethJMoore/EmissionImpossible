"""Emission model package."""

from .cleaning import clean_and_reconstruct, reconstruct_with_svd, subtract_background
from .configs import (
    param_config_DMNT,
    param_config_indole,
    param_config_mono,
    param_config_sesq,
    param_config_TMTT,
)
from .fitting import process_single_group, process_single_group_three, r_squared, run_de_then_slsqp
from .io import save_results_to_csv
from .model import duration, model_gamma, shape, total_integral_model_gamma

__all__ = [
    "clean_and_reconstruct",
    "reconstruct_with_svd",
    "subtract_background",
    "param_config_DMNT",
    "param_config_indole",
    "param_config_mono",
    "param_config_sesq",
    "param_config_TMTT",
    "process_single_group",
    "process_single_group_three",
    "r_squared",
    "run_de_then_slsqp",
    "save_results_to_csv",
    "duration",
    "model_gamma",
    "shape",
    "total_integral_model_gamma",
]
