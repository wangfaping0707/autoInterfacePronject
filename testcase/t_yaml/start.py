import yaml
from utils.YamlUtil import YamlReader

res = YamlReader('data1.yml').read_yaml()

print(res)