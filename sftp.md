# SFTP

### SFTP 概述：

sftp（Secure File Transfer Protocol）是安全文件传输协议的缩写，是一种安全的文件传送协议，可以为传输文件提供一种安全的加密方法。是ssh内含协议，也就是说只要sshd服务器启动了，sftp就可使用，不需要额外安装，它的默认端口和SSH一样为22。

SFTP本身没有单独的守护进程，它必须使用SSHD守护进程（端口号默认是22）来完成相应的连接操作，所以从某种意义上来说，SFTP并不像一个服务器程序，而更像是一个客户端程序。

sftp通过使用加密/解密技术来保障传输文件的安全性，因此sftp的传输效率比普通的FTP要低，但sftp的安全性要比ftp高，因此sftp通常用于报表、对账单等对安全性要求较高的场景。

### 与SSH相关：

ssh协议本身提供了两个服务器功能：
一个就是远程连接使用shell的服务器，即俗称的ssh。
一个就是类似FTP服务器的sftp-server，提供更安全的FTP服务。
SFTP可以从远程服务器上下载/上传文件，使用的是SSH的通道（port 22）。

### sftp 与 ftp 区别：

FTP是一种文件传输协议，一般是为了方便数据共享的。包括一个FTP服务器和多个FTP客户端.FTP客户端通过FTP协议在服务器上下载资源。
而SFTP协议是在FTP的基础上对数据进行加密，使得传输的数据相对来说更安全。
但是这种安全是以牺牲效率为代价的，也就是说SFTP的传输效率比FTP要低（不过现实使用当中，没有发现多大差别）
FTP要安装，SFTP不要安装；SFTP更安全，但更安全带来副作用就是的效率比FTP要低些

### Linux 下搭建 SFTP：

1. 创建用户，组 和密码

   1.1 创建 sftp用户组：

​            [root@localhost ~]# groupadd sftp

​      1.2 创建 sftp 系统用户test，禁止登陆：

​             [root@localhost ~]# useradd -g sftp -s /bin/false test  

​             /bin/false是最严格的禁止login选项，一切服务都不能用， 

​            /sbin/nologin只是不允许系统login，可以使用其他ftp等服务 

​       1.3 设置 test 用户密码：

​            [root@localhost ~]# echo "test" | passwd test --stdin

2 .指定sftp用户（test）的家目录，然后通过用户名来区分：

​       2.1 创建（test用户）目录

​           [root@localhost ~]# mkdir -p /data/sftp/test  

​       2.2 指定上文目录为 test 用户的家目录

​           [root@localhost ~]# usermod -d /data/sftp/test test

3. 更改配置文件 

   3.1 修改配置文件/etc/ssh/sshd_config

   ​    [root@localhost ~]# cp /etc/ssh/sshd_config /etc/ssh/sshd_config.bak

   ​    “#Subsystem sftp /usr/libexec/openssh/sftp-server”	##注释这行，文件尾部位置 

   ​     ##然后在后面添加下面这些：

   ​     #Subsystem   sftp  /usr/libexec/openssh/sftp-server

   ​     Subsystem    sftp internal-sftp

   ​     Match Group sftp

   ​     ChrootDirectory /data/sftp/test

   ​     X11Forwarding no

   ​     AllowTcpForwarding yes

   ​     PermitTTY yes

   ​     ForceCommand internal-sftp

   

   3.2 修改理由

   ​      如果这行文字存在且没有被注释掉，那么SFTP已经开启，所有可使用ssh的用户都可使用SFTP。 但是这种方式有一个缺陷，就是用户在SFTP软件里面可以cd / 从而看到系统所有文件。 所以说，我们要对其进行一些限定

   

   3 .3 配置详解

   ​     Match Group sftp

    \    #  匹配用户组，如果要匹配多个组，多个组之间用逗号分割 

   ​     ChrootDirectory  %h/%u

   \     # 指定登陆用户到自己的用户目录  %h为相应的家目录 %u为相应的用户名

   ​      Subsystem    sftp internal-sftp

   \     # 指定sftp 命令

   ​      X11Forwarding no

   ​      AllowTcpForwarding yes

   ​      Match user sftpadmin         

   \    #匹配用户，多个用户名之间也是用逗号分割

   

   3.4 needinfo

   ​     1.chrootDirectory目录的父目录及其子目录的拥有者都只能是 root，用户组可以不是 root。

   ​     2.chrootDirectory目录的父目录及其子目录都不可以具有群组写入权限

   ​     3.chrootDirectory目录的父目录及其子目录属主只能是root，并且不能由任何其他用户写入，否则你
   将在日志中看到错误报错"chroot目录的错误所有权或模式"。

   ​     4.sftp使用chrootDirectory指定根目录后，根应是无法写入的，所以要在chrootDirectory目录下新建一
   个目录如upload，供test用户上传文件，这个目录所有者为test，所有组为sftp，所有者有写入
   权限，而所有组无写入权限，权限为700、750或者755。

   ​     5.如果 chrootDirectory/upload 权限为700、750或者755,那么只能是 test用户上传文件，
   如果其他用户属于sftp组，要使其也有上传权限，目录权限需设置为770。

      6. 配置 参数文件的时候可指定日志：

         Subsystem sftp internal-sftp -l VERBOSE -f AUTH,local5        

         #设置日志级别为VERBOSE，并指定日志记录的收集设施 

         ForceCommand internal-sftp -l VERBOSE        

         #设置日志级别为VERBOSE 

         ForceCommand internal-sftp -l VERBOSE       

          #设置日志级别为VERBOSE 

4. 设置chrootDirectory属主和目录权限

   4.1 设置目录属主为root用户

   ​     [root@localhost data]# ls -l /data/sftp/

   ​     总用量 0

   ​     drwxr-xr-x. 2 root root 6 3月  4 21:35 test

   ​     [root@localhost data]# chown root:sftp /data/sftp/test/

   4.2 设置目录权限为755，不允许群组及其他用户有写入权限

   ​     [root@localhost data]# chmod -R 755 /data/sftp/test/

   ​     [root@localhost data]# ls -l /data/sftp/

   ​     总用量 0

   ​     drwxr-xr-x. 2 root sftp 6 3月  4 21:35 test

5. 创建test用户登录以后可以上传文件的目录

​       5.1 创建upload目录供test用户上传文件

​           [root@localhost data]# mkdir /data/sftp/test/upload

​       5.2 修改upload目录的属主为test用户，属组为sftp

​           [root@localhost data]# chown test:sftp /data/sftp/test/upload/ 

​       5.3 修改upload目录的权限为755，所有者有写入权限，所属组无写入权限

​           [root@localhost data]# chmod 755 /data/sftp/test/upload/

6. 关闭selinux 

   6.1 修改配置文件/etc/selinux/config

   ​     [root@catyuan ~]# vim /etc/selinux/config 

   ​     将文件中的SELINUX=enforcing 修改为 SELINUX=disabled

   6.2 查看enforce 值

   ​     [root@localhost data]# setenforce 0

   ​     [root@localhost data]# getenforce 

   ​     Permissive

7. 重启sshd 服务

   ​     [root@localhost data]# systemctl restart sshd

   ​     [root@localhost data]# systemctl status sshd | grep active

   ​     3:  Active: **active** (running) since 三 2020-03-04 22:04:48 CST; 13s ago

8. 登录验证

   ​     [root@localhost data]# sftp test@localhost

   ​     [root@localhost data]# sftp test@172.40.23.240

   ​     sftp>

9. 设定密钥：

   [root@localhost sftp]# ssh-keygen 

   https://blog.csdn.net/yeiweilan/article/details/89489253?ops_request_misc=%7B%22request%5Fid%22%3A%22158332444419724847041623%22%2C%22scm%22%3A%2220140713.130056874..%22%7D&request_id=158332444419724847041623&biz_id=0&utm_source=distribute.pc_search_result.none-task

   

   

   

   ### sftp 的登录与退出

1. 登录

   1.1 sftp [remotehost IP ]

   ​     通过sftp连接[host]，端口为默认的22，在弹出来的窗口输入要登录的用户名以及密码

   ​     [root@localhost data]# sftp 172.40.23.240.        #  密码为操作系统密码

   1.2  sftp [user]@[remotehost IP]

   ​     [root@localhost data]# sftp test@localhost

   ​     [root@localhost data]# sftp test@172.40.23.240

   ​     sftp>  

   1.3  sftp-oPort=[port] [remotehost IP]

   ​     通过sftp连接远程服务器，指定端口[port]，用户为Linux当前登录用户。

   1.4 sftp -oPort= [port ] [user]@ [ remotehost IP]

   ​     通过sftp连接[remotehost IP]，端口为[port]，用户为[user]。

2. 退出(exit | bye | quit)

   sftp> exit

   sftp> bye 

   sftp> quit

   

   ### sftp 命令

1. 操作远程服务器（server）的命令

   cd: 切换目录
   mkdir: 创建目录
   ls/dir: 查看目录下的文件信息
   rmdir: 删除目录
   pwd：显示当前工作目录
   chgrp：更改文件或目录的属组
   chown：更改文件或目录的属主
   chmod：更改文件或目录的权限
   ln：建立文件链接
   rm：删除文件或目录
   rename：更改文件名或目录名

2.  操作本地（client）的命令，命令前加l

   lcd：切换目录

   lls：列出当前主机所在目录的文件 

   lmkdir：创建目录 

   lpwd：显示当前目录 

   put：上传本机文件，格式为put [本机文件] 

   get：下载远程文件，get [远程文件]

14. sftp如何连接特定端口

    sftp -oPort=6003 user@host

    sftp如何批量下载文件

    mget dir/*

    

    ### sftp 配置密钥认证：

    1. 概述

       密钥登录无需用户设置密码，通过rsa密钥对加解密验证，在客户端和服务器端建立安全的连接，简单地说，public key放在服务器端，即下面配置的authorized_keys，private key放在客户端，客户端发起请求连接，服务器根据请求用户名识别对应客户端公钥，sshd服务产生一个随机数，用public key进行加密后，发回到客户端，客户端用private key解密得到该随机数，客户端将解密后的随机数发回服务器端，服务端进行匹配，匹配成功认证通过，允许登录。这种方式避免了密码暴力破解尝试的危险，当然密钥认证因为有加解密和随机数传输验证的过程，连接耗时自然比密码方式长些。

    2. 配置详解

       2.1 创建密钥对

       [root@localhost ~]# ssh-keygen -t rsa.    # 创建密钥对

       

       2.2 查看目录下生成的密钥

       [root@localhost ~]# ls /root/.ssh/

       id_rsa id_rsa.pub known_hosts

       

       2.3 把公钥拷贝到远程服务器的~/.ssh/authorized_keys文件中

       [root@localhost ~]# mkdir /data/sftp/test/.ssh

       [root@localhost ~]# ssh-copy-id test@172.40.23.240

       This service allows sftp connections only.

       [root@localhost ~]# cp .ssh/id_rsa.pub /data/sftp/test/.ssh/

       [root@localhost ~]# cat ~/.ssh/id_rsa.pub | ssh -p 22 test@172.40.23.240 ‘cat >>~/.ssh/authorized_keys

       

       

       

       [root@localhost .ssh]# sftp root@172.40.23.240

       root@172.40.23.240's password: 

       Connected to 172.40.23.240.

       

       

       注：几种拷贝的方法

       1、将公钥通过scp拷贝到服务器上，然后追加到~/.ssh/authorized_keys文件中，这种方式比较麻烦。scp -P 22~/.ssh/id_rsa.pub user@host:~/。
       2、通过ssh-copy-id程序，就是我演示的方法，ssh-copy-id user@ip即可
       3、可以通过cat ~/.ssh/id_rsa.pub | ssh -p 22 user@host ‘cat >>~/.ssh/authorized_keys’，这个也是比较常用的方法，因为可以更改端口号。

       

       2.4  修改权限

       .ssh目录的权限为700，其下文件authorized_keys和私钥的权限为600。否则会因为权限问题导致无法免密码登录。我们可以看到登陆后会有known_hosts文件生成

       [root@catyuan ~]# chown -R test:sftp /data/sftp/test/.ssh/
       [root@catyuan ~]# chmod 600 /data/sftp/test/.ssh/authorized_keys 
       [root@catyuan ~]# chmod 700 /data/sftp/test/.ssh/

       

       2.5 修改配置文件

       如果只允许用户使用密钥认证登录，可以射置/etc/ssh/sshd_config
       PasswordAuthentication no
       如果不改，密钥认证和密钥认证两种登录方式都允许。

       [root@catyuan ~]# vim /etc/ssh/sshd_config
       PermitRootLogin yes	#允许root用户登录
       RSAAuthentication yes	#允许 RSA 安全验证
       PubkeyAuthentication yes	#允许密钥登录
       AuthorizedKeysFile      /data/sftp/test/.ssh/authorized_keys   #指出公钥的位置，这一项配置文件中是有的，把它注释掉。

       

       2.6 重启服务

       [root@localhost ~]# systemctl restart sshd

       

       2.7  测试用密钥登录：

       [root@localhost ~]# sftp 172.40.23.240 

       Connected to 172.40.23.240.

       sftp> 

       #此时登录就无需密码了，使用秘钥登录 sftp> 

       

       

    





















