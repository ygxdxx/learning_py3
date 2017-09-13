#! python3

import paramiko

# 传输文件
transport = paramiko.Transport(('hostname', 22))
transport.connect(username='xiaoming', password='123')
# 当作参数传入
ftp = paramiko.SFTPClient.from_transport(transport)
# 将本地文件上传到服务器
ftp.put('local.py', 'remote.py')
# 将远端文件下载到本地
ftp.get('remote.py', 'local.py')

# 关闭连接
transport.close()
