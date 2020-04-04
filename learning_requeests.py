import requests
p={'username':'raman','password':'raman2'}
#r = requests.get('https://imgs.xkcd.com/comics/python.png')
r = requests.post('https://httpbin.org/post',data=p)

#with open('comic.png','wb') as f:
 #   f.write(r.content)
#print(r.status_code)
#print(r.ok)
#print(r.headers)

r_dict=r.json()
print(r_dict['form'])




