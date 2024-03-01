
# class - 1

# what is dectionary
# dectionary is a set of key value pair refernce by a single line

#dictionary
cameras = {"sony":600,"nikon":500,"cannon":650}
print(cameras)
cameras["nikon"]=650 # To changing the key's value
print(cameras)

# last classs
print(cameras.keys()) # To get keys only
print(cameras.values())  # To get values only

copy_cameras = cameras.copy() # We can copy the dictionary
print(copy_cameras)

del cameras["sony"] # To deleting the key - if we delete key the value also will delete
print(cameras)

cameras.clear() # it will clear all the data but " stracture will be there "
print(cameras)
