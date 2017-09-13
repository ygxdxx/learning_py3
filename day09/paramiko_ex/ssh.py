#! python3

import paramiko

# 创建SSH对象
ssh = paramiko.SSHClient()
# 允许连接不在know_hosts文件中的主机
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 连接服务器
ssh.connect(hostname='localhost', port=9999, username='xiaoming', password='123')
# 执行命令
stdin, stdout, stderr = ssh.exec_command('cmd')
# 获取命令结果
result = stdout.read()
# 关闭连接
ssh.close()
