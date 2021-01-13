import requests, json

f = open("./README.md", "w")

the_cat_response = requests.get("https://api.thecatapi.com/v1/images/search?mime_types=gif")

the_cat_object = the_cat_response.json()[0]

f.write(f'''
## Hi, I am Lilian :wave:

Thanks for visiting my GitHub page.

Here, a cat gif for you. Have a nice day!

<img src="{the_cat_object['url']}" width="{the_cat_object['width']}" height="{the_cat_object['height']}">

''')

f.close()