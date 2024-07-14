# import pytest
#
# class TestClass:
#     @pytest.fixture()   # decorator
#     def setup(self):
#         print("Launching browser...")
#         print("Open application..")
#
#     def test_Login(self,setup):
#         print("This is login test")
#
#     def test_Search(self,setup):
#         print("this is search test")
#
#     def test_Advancedsearch(self):
#         print("this is advanced search test")






import pytest

class Testpytestframework:
    @pytest.fixture()

    def setup(self):
        print("first launching the browser")
        print("then open the application")
    def  test_login(self,setup):
        print("this method is for login purpose")
    def test_search(self,setup):
        print("this is used for the searching purpose")
    def test_Advancedsearch(self):
        print("this is used for the advanced search purpose")