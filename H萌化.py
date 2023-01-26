original=open('原文.txt','r',encoding='UTF-8')
after=open('处理后.txt','w', encoding='UTF-8')
after.truncate()
length=len(original.readlines())
original.seek(0)
for p in range(length):
    o=original.readline()
    i=0
    while i < len(o):
        if o[i:i+2]=='[[' \
           and not (o[i+2:i+7]=='File:' or o[i+2:i+7]=='file:'or o[i+2:i+5]=='文件:'):
            after.write('{{萌百|')
            i+=2
            while o[i:i+2]!=']]':
                after.write(o[i])
                i+=1
            else:
                after.write('}}')
                i+=2
        else:
            after.write(o[i])
            i+=1
original.close()
after.close()
