from basicGraph import *
import heapq
import pytest
from featurepy import select_equation, select
select_equation("config.equation")


pytest.main(["--pyargs", "basicGraph"])
