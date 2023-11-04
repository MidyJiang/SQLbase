# #执行以下命令
# !apt-get update
# !apt install iputils-ping
# !apt install net-tools
# print('---------------------------iport done.-------------------------')
# print()
# !ping  172.16.27.188


import pymssql

 
    
server  ="192.168.157.16"#'172.16.27.188' 
user     ='sa' #用户名
password ='Qingyi0430' #密码
database  ='midy'#数据库名称
conn = pymssql.connect(server, user, password,  
                       database, port=1433,  as_dict=True)

if conn:
    cursor = conn.cursor() 
    print("连接成功!")
    
cursor.execute("SELECT * FROM send")
result=cursor.fetchall()
print(len(result))
print("all done,len dataframe result=[{}]".format(len(result))
