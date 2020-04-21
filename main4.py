import json
x = '{"bomonque":[{"iu": [{"iu-1": []},{"iu10":[{"cozers": ["Zversky", "GoldGem", "Cnya176"]}]}]},{"fn":[{"fn-12":[{"obercozers": [],"cozers": ["Ivanov", "Petrov"]}]}]}]}'
y = json.loads(x)
print(y["bomonque"][0]["iu"][1]["iu10"][0]["cozers"])
print(y["bomonque"][1]["fn"][0]["fn-12"][0]["cozers"])


