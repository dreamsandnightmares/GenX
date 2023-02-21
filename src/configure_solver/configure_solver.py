import string
import src.configure_solver.configure_scipy

import os
def configure_solver(solver:str,solver_settings_path:str):
    solver =solver.lower()

    if solver =='scipy':
        scipy_settings_path = os.path.join(solver_settings_path,"highs_settings.yml")
        OPTIMIZER = src.configure_solver.configure_scipy.configure_scipy((scipy_settings_path))
        return OPTIMIZER

