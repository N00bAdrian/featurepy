from featurepy import select_equation, select
select_equation("config.equation")

from basicGraph import *
import pytest


pytest.main(["--pyargs", "basicGraph"])
