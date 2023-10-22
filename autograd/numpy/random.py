from __future__ import absolute_import
import os
if os.environ.get("DP_NUMPY", "1") == "0":
    import numpy.random as npr
else:
    import dp_numpy.random as npr
from .numpy_wrapper import wrap_namespace

wrap_namespace(npr.__dict__, globals())
