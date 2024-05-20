from utils.apiutils_business import RequestsBase
from utils.YamlUtil import YamlReader
import pytest
import allure
from utils.generate_id import m_id, c_id

@allure.feature(next(m_id) + '电子商务管理系统__订单支付业务场景')
class TestProductBusiness:

	@pytest.mark.parametrize('api_info', YamlReader(r'./data/businessScenario/productBusiness.yml').read_yaml())
	@allure.story(next(c_id) + '商品下单支付流程')
	def test_product_business_sence(self, api_info):
		# print(api_info)
		allure.dynamic.title(api_info['baseinfo']['api_name'])
		RequestsBase().execute_test_cases(api_info)
