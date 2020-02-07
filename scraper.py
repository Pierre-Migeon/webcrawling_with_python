

try: 
    from googlesearch import search 
except ImportError:  
    print("No module named 'google' found") 

# to search 
query = "Bay Area Housing Prices"
  
for j in search(query, tld="com", lang='en', num=10): 
    print(j) 


