import sys
from pathlib import Path

import numpy as np
import pandas as pd
import pytest
from pandas.testing import assert_frame_equal

# Ensures that the code in src can be run and accessed from the console:
# see importing sibling packages in Python
sys.path.append(str(Path(__file__).parents[1].resolve()))

from utils import validate_expectations


def test_validate_expectations_non_df():
    with pytest.raises(ValueError):

        @validate_expectations(suite_name="")
        def non_df():
            x = pd.DataFrame(
                columns=[
                    "person_id",
                    "person_name",
                    "person_created",
                    "person_status",
                    "status_timestamp",
                ]
            ).to_numpy()

        non_df()
