from run import incrementWildcard


class TestIncrementWildcard():
    def test_simple(self):
        wildcards = [0]
        assert incrementWildcard(wildcards, 0) == [1]

    def test_complicated(self):
        wildcards = [25, 25]
        assert incrementWildcard(wildcards, 0) == False

    def test_carryTheOne(self):
        wildcards = [25, 2]
        assert incrementWildcard(wildcards, 0) == [0, 3]
