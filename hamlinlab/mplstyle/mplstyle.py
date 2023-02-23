'''
Here are references to commonly used matplotlib styles.
'''

import pathlib

cwd = pathlib.Path.cwd() # The current working directory
project_root = cwd.parent

# Here we specify the folder where our custom styles live
mpl_config_dir = project_root / 'matplotlib_styles'

prb_regular = (
    mpl_config_dir / 'prb_defaults.mplstyle',
    mpl_config_dir / 'prb_regular.mplstyle'
    )
prb_wide = (
    mpl_config_dir / 'prb_defaults.mplstyle',
    mpl_config_dir / 'prb_wide.mplstyle'
    )
prb_verywide = (
    mpl_config_dir / 'prb_defaults.mplstyle',
    mpl_config_dir / 'prb_verywide.mplstyle'
    )
prb_tall = (
    mpl_config_dir / 'prb_defaults.mplstyle',
    mpl_config_dir / 'prb_tall.mplstyle'
    )
