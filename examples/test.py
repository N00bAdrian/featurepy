from featurepy import Aspect, Proceed, Return, weave
from featurepy.feature_class import feature


@Aspect
def add_one(x, y):
    z = yield Proceed(x, y)
    yield Return(z + 1)


def add(x, y):
    return x + y


with weave(add, add_one):
    with weave(add, add_one):
        print(add(1, 1))

# with weave(add, [add_one, add_one]):
#     print(add(1, 1))
