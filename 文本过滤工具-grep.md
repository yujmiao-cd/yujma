### 文本过滤工具 --- grep

文本过滤工具（grep）

regexp ： 元字符

-- 匹配 /etc/password 下包含 root 字符串的行

```kotlin
# grep --color 'root' passwd 

1:**root**:x:0:0:**root**:/**root**:/bin/bash
```

basic regexp : 基本正则表达式，元字符

​       .  :匹配任意单个字符

​       *  :匹配其前面的字符任意次

extend regex: 扩展正表达式

[:upper:]   [:lower:]    [:digit:]  [:alpha:]   [:alnum:]   [:pace:]   [:punct]

x\ {m, n \ }

x\ {m, \ }

x\{0, n \ }

x\ { m \ }

?:  匹配其前面的字符0 次或1次

ab?c : abc   abbc   ac



 锚定符：

  ^    锚定行首

  $    锚定行尾

​        ^$  空白行

  \ <  : \b 锚定词首

​         \ <r..t.   ====   \br..t

 \ >   : \b 锚定词尾

​        r..t \ >     ====    r..t\b



\ ( \ ) : 分组

后向引用：\1  ,   \2



grep 选项：

-v 对结果取反





-- grep 匹配 r ..t 中间至少两个字符（/etc/passwd）

```kotlin
# grep --color 'root' passwd 

1:**root**:x:0:0:**root**:/**root**:/bin/bash

-- 匹配 r 和 t 之间至少两个字符
# grep 'r[a-z]\{2,\}t' /etc/passwd
1:**root**:x:0:0:**root**:/**root**:/bin/bash
10:operator:x:11:0:operator:/**root**:/sbin/nologin

-- 匹配空白行至少一条
# grep "[[:space:]]\{1,\}" /etc/passwd
12:ftp:x:14:50:FTP User:/var/ftp:/sbin/nologin
14:systemd-network:x:192:192:systemd Network Management:/:/sbin/nologin
15:dbus:x:81:81:System message bus:/:/sbin/nologin
16:polkitd:x:999:998:User for polkitd:/:/sbin/nologin

-- 匹配非空白行至少一条
# grep "[^[:space:]]\{1,\}" /etc/passwd
1:root:x:0:0:root:/root:/bin/bash
2:bin:x:1:1:bin:/bin:/sbin/nologin
3:daemon:x:2:2:daemon:/sbin:/sbin/nologin
4:adm:x:3:4:adm:/var/adm:/sbin/nologin

-- 锚定行首
# grep "^root" /etc/passwd
1:root:x:0:0:root:/root:/bin/bash
# grep "root" /etc/passwd
1:root:x:0:0:root:/root:/bin/bash
10:operator:x:11:0:operator:/root:/sbin/nologin

-- 分组演示
# cat a.txt 
He love his lover.
She like her liker.
He love HIs liker.
She like Her lover.
# grep "\(l..e\).*\1r" a.txt 
1:He love his lover.
2:She like her liker.

-- 匹配 user1 用户的信息  /etc/password.  user1 - user11 - myuser1 - user1's uncle
# useradd user1
# useradd user11
# useradd myuser1
# grep "\<user1\>" /etc/passwd   # 单词锚定(Fail)
56:user1:x:1012:1012::/home/user1:/bin/bash

# useradd -c "user1's uncle" hello
# grep "\<user1\>" /etc/passwd
56:user1:x:1012:1012::/home/user1:/bin/bash
57:hello:x:1013:1016:user1's uncle:/home/hello:/bin/bash

# grep "^user1\>" /etc/passwd   # 行首锚定词尾锚定
56:user1:x:1012:1012::/home/user1:/bin/bash
# grep "^\<user1\>" /etc/passwd    # 行首词首锚定词尾锚定
56:user1:x:1012:1012::/home/user1:/bin/bash

-- 匹配当前系统名字为user 后面跟了数字的用户的相关信息
# grep "^user[0-9]\{1,\}\>" /etc/passwd
54:user11:x:1010:1014::/home/user11:/bin/bash
56:user1:x:1012:1012::/home/user1:/bin/bash
58:user2:x:1014:1017::/home/user2:/bin/bash

-- 查找当前系统上以其为附加组的用户有两个或两个以上的组的相关信息。  /etc/group,
# grep "," /etc/group
71:vbirdgroup:x:1001:vbirduser1,vbirduser2,vbirduser3,vbirduser4,vbirduser5
79:project:x:1008:alex,arod
# grep "," /etc/group | cut -d: -f2    # 显示组名
vbirdgroup
project
# grep "," /etc/group |awk -F: '{print $2}'  # 显示组名
vbirdgroup
project

-- 查找当前系统上其用户账号密码最长使用期限为9999天的用户账号的相关信息。99999
# grep "99999" /etc/shadow | cut -d: -f2
root
bin
daemon

-- 分析 /etc/inittab 文件中如下两行的文本特征，请写出可以精确找到类似两行的模式，而且要求每行出现的数字相同
# cat b.txt 
# inittab is no longer used when using systemd.
#
# ADDING CONFIGURATION HERE WILL HAVE NO EFFECT ON YOUR SYSTEM.
#
l1:1:wait:/etc/rc.d/rc  1 
l3:3:wait:/etc/rc.d/rc  3
l4:5:wait:/etc/rc.d/rc  3

# grep --color "l\([13]\):\1:.* \1" b.txt   # 匹配1，3
5:l1:1:wait:/etc/rc.d/rc  1 
6:l3:3:wait:/etc/rc.d/rc  3

# grep "l\([0-9]\):\1:.* \1" b.txt    匹配 0-9 一次
5:l1:1:wait:/etc/rc.d/rc  1 
6:l3:3:wait:/etc/rc.d/rc  3

# grep "l\([0-9]\{1,\}\):\1.* \1" b.txt   # 0-9 出现任意多次 
5:l1:1:wait:/etc/rc.d/rc  1 
6:l3:3:wait:/etc/rc.d/rc  3

```



练习：

- 显示 /proc/meminfo 文件中以不区分大小的 s 开头的行；

  ```kotlin
  # grep "^[Ss]" /proc/meminfo 
  
  # grep --color "^[Ss].*" /proc/meminfo 
  ```

  

- 显示 /etc/passwd 中以 nologin结尾的行；

  ```kotlin
  # grep --color "nologin$" /etc/passwd 
  ```

  

- 显示 /etc/inittab  中包含了: 一个数字: （即两个冒号中间一个数字）的行；

  ```kotlin
  # grep --color ":[0-9]:" c.txt 
  
  18:l1**:1:**wait:/etc/rc.d/rc 1 
  
  19:l3**:3:**wait:/etc/rc.d/rc 3
  
  20:l4**:5:**wait:/etc/rc.d/rc 3
  ```

  

- 显示 /etc/inittab  中以 # 开头，且后面跟了一个或多个空白字符，而后又跟了任意非空白字符的行；

  ```kotlin
  # grep --color "^#[[:space:]]\{1,\}[^[:space:]]" c.txt 
  
  1:**# i**nittab is no longer used when using systemd.
  
  3:**# A**DDING CONFIGURATION HERE WILL HAVE NO EFFECT ON YOUR SYSTEM.
  ```

  

- 显示 /boot/grub/grub.conf 文件以一个或多个空白字符开头的行；

  ```kotlin
  # grep --color "^[[:space:]]\{1,\}" d.txt 
  
  12: load_env
  
  15:  set default="${next_entry}"
  
  16:  set next_entry=
  
  17:  save_env next_entry
  ```

  

- 显示  /etc/inittab 文件中以一个数字开头并以一个与开头数字相同的数字结尾的行；

  ```kotlin
  # grep --color "^\([0-9]\).*\1$" c.txt 
  
  21:**4:2345:respawn:/sbin/mingetty tty4**
  
  22:**5:2345:respawn:/sbin/mingetty tty5**
  
  23:**6:2345:respawn:/sbin/mingetty tty6**
  
  24:**7:2345:respawn:/sbin/mingetty tty7**
  ```

-  显示  /etc/inittab 文件中 非空白行

  ```kotlin
  # grep "^$" c.txt 
  
  25:
  
  26:
  
  
  # grep -v "^$" c.txt    # -v 取反
  
  1:# inittab is no longer used when using systemd.
  
  2:#
  
  3:# ADDING CONFIGURATION HERE WILL HAVE NO EFFECT ON YOUR SYSTEM.
  
  4:#
  
  5:# Ctrl-Alt-Delete is handled by /usr/lib/systemd/system/ctrl-alt-del.target
  ```

- Grep  选项：
  -v     取反

  -i      忽略大小写

  -o    仅显示匹配到的字符串

  -E    支持扩展正则表达式

  -A    显示匹配包含下面一行

  -B   显示匹配包含上面一行

  -C   显示匹配包含上下面各一行

  

- 取出当前网络上所有网卡的IP地址的信息

  ```kotlin
  # ifconfig | grep "inet\>" | cut -d ' ' -f10
  172.16.66.20
  127.0.0.1
  172.40.23.240
  192.168.122.1
  
  # ifconfig | grep "inet\>" | awk -F ' '  '{print $3}'
  172.16.66.20
  127.0.0.1
  172.40.23.240
  192.168.122.1
  ```

- 取出当前系统上没有IP地址的网络设备的名称

  

- 取出当前系统上 ens32 网卡的IP 地址

  ```kotlin
  # ifconfig | grep -A 1 "ens32" | grep -o "inet [0-9.]\{1,\}"
  2:**inet 172.16.66.20**
  # ifconfig | grep -A1 "ens32" | grep -o "inet [0-9.]\{1,\}" | cut -d ' ' -f2
  172.16.66.20
  ```

  

扩展正则表达式：

   \ ( \ )   ------->  ()

  \ { \ }  ------ >  {}

  ➕  次数匹配，匹配其前的字符至少一次

  ｜  或者

举例：

```kotlin
# egrep --color "(l..e).*\1r" a.txt 

He **love his lover**.

She **like her liker**.

-- 找出 ifconfig 中 1-255 中的值
# ifconfig | grep --color  -E "\<([1-9]|[1-9][0-9]|[1][0-9]{2}|[2][0-5]{2})\>"
2:        inet 172.16.66.20  netmask 255.255.255.255  broadcast 172.16.66.20
```









