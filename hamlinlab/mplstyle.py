'''
Here are references to commonly used matplotlib styles.
'''

import pathlib

# Path to the directory that holds this file
here = pathlib.Path(__file__).parent

# Styles should be kept inside a folder called matplotlib_styles.
# that is in the same direcotry as this module.
mpl_config_dir = here / 'matplotlib_styles'

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
