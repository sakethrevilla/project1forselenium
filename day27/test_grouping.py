import pytest

class Testgroup:
    @pytest.mark.sanity
    def test_LoginByNakuari(self):
        print("Please Enter The Login Details")
        assert 1==1
    @pytest.mark.sanity
    def test_LoginBytesla(self):
        print("Please Enter The Login Details")
        assert 1 == 1
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_LoginByking(self):
        print("Please Enter The Login Details")
        assert 1 == 1

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_LoginByNakuari(self):
        print("Please Enter The Login Details")
        assert 1 == 1

    @pytest.mark.regression
    def test_LoginByTesla(self):
        print("Please Enter The Login Details")
        assert 1 == 1

    @pytest.mark.unit
    def test_LoginByKing(self):
        print("Please Enter The Login Details")
        assert 1 == 1



