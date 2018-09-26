#!/usr/bin/python
# -*- coding: UTF-8-*-

filename = "fat{}.png"
wfilename = "/home/wcl/Documents/node/hexo/source/_posts/fat32结构介绍/fat{}.png"

for i in range(1,8):
    fo = open(filename.format(i), 'rb')
    fw = open(wfilename.format(i), 'wb')
    
    data = fo.read()
    fw.write(data)

    fo.close()
    fw.close()

