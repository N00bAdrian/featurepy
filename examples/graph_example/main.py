import pytest
from basicGraph import *
from featurepy import select_equation, select
select_equation("config.equation")


pytest.main(["--pyargs", "basicGraph"])
