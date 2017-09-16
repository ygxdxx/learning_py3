#! python3

# TODO RabbitMQ
# 官方教程
# http://www.rabbitmq.com/tutorials/tutorial-one-python.html
# TODO 安装过程
# homebrew无法正确安装，从官网下载下来的文件为.tar.xz结尾
# .xz是一种压缩率非常高的格式，在Linux下使用xz -d xxx.xz，先将.xz文件解压为.tar文件；然后再使用tar xvf xxx.tar进行tar包的解压
# 1.完成上述步骤之后，会出现一个sbin目录，执行sbin/rabbitmq-server命令后会在前台运行rabbitmq服务器
# 2.默认安装以后是不会启动插件管理的，需要进入sbin目录，执行sudo ./rabbitmq-plugins enable rabbitmq_management命令启动插件
# 3.登录http://localhost:15672登录到rabbitmq中，默认用户名和密码都为guest
# TODO 教程
# RabbitMQ是一个消息队列中间件，它可以在发送端和接收端中间进行消息接收、缓存和发送的过程
# （所谓中间件只是的独立于操作系统和程序语言的第三方软件，屏蔽了底层的通讯、连接和通信等复杂又通用的方式，起到一个支撑的作用，用户在使用的过程当中并不能直接感知到它的存在。）
# 在RabbitMQ的两端，一侧发送方作为一个生产者Producer-P，另一侧是接收方作为一个消费者Consumer-C
# 生产者发送数据和消息到RabbitMQ中，其中有一个queue可以对接收到的数据进行存储。这个队列需要本地的磁盘空间和内存空间作为一个消息的缓存区域
# 可以有多个生产者向其中发送消息，同时也可以有多个消费者从中读取消息
# 在创建程序之前，需要先通过pip3安装rabbitmq的python库，称为pika



