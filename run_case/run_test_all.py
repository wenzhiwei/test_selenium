import pytest

if __name__=="__main__":
     #单个
     #pytest.main(['../test_case/test_fore.py'])
     #多个
     #pytest.main(['../test_case/test_fore.py','../test_case/test_login.py'])
     #pytest.main(['../test_case','--html=../report/html/report.html'])
     #pytest.main(['../test_case', '--junitxml=../report/xml/report.xml'])
     #allure generate ./reportallure/ -o ./reporthtml/ --clean
     pytest.main(['../test_case', '--alluredir=../report/reportallure'])