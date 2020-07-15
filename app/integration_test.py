import requests
from main import port
url = 'http://127.0.0.1:'+port

first_response = requests.get(url+"/stats")
response = requests.post(url+"/mutant", json={"dna":["ACGT","CATG","CATG","CATG"]})
second_response = requests.get(url+"/stats")

f_human = first_response.json()["count_human_dna"]
s_human = second_response.json()["count_human_dna"]
assert f_human + 1 == s_human