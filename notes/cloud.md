<!-- 这个是云计算概念的笔记 -->

1.出租计算容量和处理能力。
2.云计算是分布式计算的一种特殊形式，引入了效用模型来远程供给可扩展和可测量的资源。云就是一个独特的IT资源（硬件/软件资源），设计目的就是为了远程供给可扩展和可测量的IT资源，也可以说是对一组分散的IT资源进行远程访问。
3.云的可扩展性：
	水平扩展和垂直扩展：
		1.水平扩展：分配和释放资源
		2.垂直扩展：当前资源被高级资源取代，如CPU 2 --> 4
4.云的特性：
	1.按需使用		on-demand usage
	2.随处访问		ubiquitous access
	3.多租户			multitenacy
	4.弹性			elasticity
	5.可测量的使用	measured usage
	6.可恢复性		resilient computing
5.云交付模型
	1.基础设施为服务	IaaS
	2.平台为服务		PaaS
	3.软件为服务		SaaS
6.云部署模型
	1.公有云
	2.私有云
	3.社区云
	4.混合云
	5.互联网云--多个云互联
7.云使能技术
	1.虚拟化技术：将物理IT资源转换为虚拟IT资源
		1.硬件无关性
		2.服务器整合
		3.资源复制		复制磁盘
		4.有基于操作系统/基于硬件的虚拟化
8.多租户和虚拟化的区别：
	1.虚拟化：一个物理机上可以容纳多个虚拟副本，每个副本都可以独立配置，提供给不同的用户，安装不同的OS/软件
	2.多租户：一个物理/虚拟服务器运行着一个应用程序，允许被多个用户共享，而每个用户都感觉只有自己在使用该应用程序。
9.云安全
	1.保密性：被授权了才能访问
	2.完整性：未被未授权方篡改的特性
	3.真实性：事物是由经过授权的源提供的这一特性
	4.可用性：在特定的时间段内可以访问和可以使用的特性
10.云安全威胁
	1.流量窃听
	2.恶意媒介
	3.拒绝服务		负载过重引起的
	4.授权不足
11.云设施
	1.逻辑网络边界
	2.虚拟服务器
	3.云存储设备			1.文件 2.块 3.数据集 4.对象
	4.云使用监控
	5.资源复制
	6.已就绪环境			PaaS的交付模型
