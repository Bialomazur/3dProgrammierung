def order_by_domain(addresses):

    result = []
    com_list, gov_list, org_list,other  = [], [], [], []

    other_domains = []

    standard_list = {"com":com_list, "gov":gov_list, "org":org_list}
    other_list = {}

    for url in addresses:
        domain = None
        if url.count("/") > 2:
            domain = url.split(".")[url.count(".")].split("/")[0]
        else:
            domain = url.split(".")[url.count(".")]
        
        if domain in standard_list.keys():
            standard_list[domain].append(url)
        elif domain in other_list.keys():
            other_list[domain].append(url)
            other_domains.append(domain)
        else:
            other_list[domain] = [url]
            other_domains.append(domain)
            
    other_domains.sort()
    for index in standard_list:
        standard_list[index].sort()
        result.extend(standard_list[index])
    
    for domain in other_domains:
       # print(other_list[domain])
        result.extend(other_list[domain]) 
    return result

    
        
    










input_list = [
    "http://www.google.en/?x=jsdfkj",
    "http://www.google.de/?x=jsdfkj",
    "http://www.google.com/?x=jsdfkj",
    "http://www.google.org/?x=jsdfkj",
    "http://www.google.gov/?x=jsdfkj"
]

print(order_by_domain(input_list))

"""
expected = [
    "http://www.google.com/?x=jsdfkj",
    "http://www.google.gov/?x=jsdfkj",
    "http://www.google.org/?x=jsdfkj",
    "http://www.google.de/?x=jsdfkj",
    "http://www.google.en/?x=jsdfkj",
]


"""

"""
Write a code that orders collection of Uris based on it's domain next way that it will returns fisrt Uris with domain "com", "gov", "org" (in alphabetical order of their domains) and then all other Uris ordered in alphabetical order of their domains In addition to that

content of Uri should not be changed,
other part of Uri doesn't affect sorting. (uris "c.com","b.com","a.com" can be placed in any order inside their group, so both "c.com","b.com","a.com" and "a.com","c.com","b.com" are correct, till they are stand before *.org

"""