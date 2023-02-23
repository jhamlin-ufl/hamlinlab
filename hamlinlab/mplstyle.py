'''
Here are references to commonly used matplotlib styles.
'''

import pathlib

__all__ = [
    'prb_regular',
    'prb_wide',
    'prb_verywide',
    'prb_tall'
    ]

cwd = pathlib.Path.cwd() # The current working directory

# Here we specify the folder where our custom styles live
mpl_config_dir = cwd / 'matplotlib_styles'

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
