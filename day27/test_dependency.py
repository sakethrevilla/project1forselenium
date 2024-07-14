# import pytest
#
# class Testdependency:
#
#     @pytest.mark.dependency()
#     def test_openapp(self):
#         print("please first open the app")
#         assert False
#     @pytest.mark.dependency(depends=['Testdependency::test_openapp'])
#     def test_login(self):
#         print("login has been successful")
#         assert True
#
#     @pytest.mark.dependency(depends=['Testdependency::test_login'])
#     def test_search(self):
#         print("please enter the search text")
#         assert True
#
#     def test_advancedsearch(self):
#         assert  True
#
#     @pytest.mark.dependency(depends=['Testdependency::test_login'])
#     def test_logout(self):
#         print("after complication of your work please logout")
#         assert True



import pytest
class TestClass:

    @pytest.mark.dependency()
    def test_openApp(self):
        assert False

    @pytest.mark.dependency(depends=['TestClass::test_openApp'])
    def test_login(self):
        assert False

    @pytest.mark.dependency(depends=['TestClass::test_login'])
    def test_search(self):
        assert False

    @pytest.mark.dependency(depends=['TestClass::test_login','TestClass::test_search'])
    def test_advsearch(self):
        assert True

    @pytest.mark.dependency(depends=['TestClass::test_login'])
    def test_logout(self):
        assert True