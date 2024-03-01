# rest AIP
# representational state transfer
# soap api u should search
# URI
# every website will have URI uniform resorese identifier
# it consist of Uri = base url + resourse + parameter

# this is amazone uri :-https://www.amazon.in/?tag=msndeskstdin-21&ref=pd_sl_5l00737rji_e&adgrpid=1328211703591630&hvadid=83013495293827&hvnetw=o&hvqmt=e&hvbmt=be&hvdev=c&hvlocint=&hvlocphy=155828&hvtargid=kwd-83014163472827:loc-90&hydadcr=5621_2377279

# install post man api craetor

# HTTP METHOS
# GET = Its a link address of a website like :-  amazone.com
# POST = here we will send some payload along with post like :- login format()
# PUT = it is a child of 'post' and it would change the existing data like :- Editing after submition of our login page if you want to
# change your address or like any data that will be using put
# DELETE :- delete is nothing but delete only

# rest assured java api request package.


# import requests
# # GET requests
# response =  requests.get("http://216.10.245.166 {id:62154}")
# print(response.text)


def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str


print(reverse("vis"))