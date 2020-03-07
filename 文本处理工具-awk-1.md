### 文本过滤工具， awk

1. a.txt:

   ```kotlin
   # cat a.txt 
   
   welcome to linux
   
   Hello. How are you?
   ```

   

   -- 取出第一个字段：

   ```kotlin
   # awk '{print $1}' a.txt 
   welcome
   
   Hello.
   ```

   -- awk 显示文件系统的第一个字段

   ```kotlin
   \# df -hP | awk '{print $1}'
   
   文件系统
   
   /dev/mapper/rhel-root
   
   devtmpfs
   
   tmpfs
   
   tmpfs
   
   tmpfs
   
   /dev/sda1
   
   tmpfs
   
   /dev/sr0
   ```

    

   -- 以冒号作为分隔符，显示/etc/passwd 的第一个字段

   ```kotlin
   \# awk -F: '{print $1}' passwd 
   
   root
   
   bin
   
   daemon
   
   adm
   
   lp
   
   sync
   
   shutdown
   ```

   

   -- 指定输出符号（awk -v）：

   ```kotlin
   \# awk -v OFS=: '{print $1, $2}' a.txt 
   
   welcome:to
   
   Hello.:How
   ```

   

   Printf 显示格式(%s)：  -10s.  左对齐   \n 换行

   ```kotlin
   [root@localhost yujma]# awk '{printf "%-10s%s\n",  $1, $2}' a.txt 
   
   welcome    to
   
   Hello.         How
   ```

   

   /dev/stderr.   ====>.  标准错误输出

   ```kotlin
   # awk -F: '{printf "%-15s %i\n", $1, $3 > "/dev/stderr"}' /etc/passwd
   
   root      0
   
   bin       1
   
   daemon     2
   
   模式匹配：
   
   如果可以首行匹配，就显示该行的第3，4个字段的值
   ```

   

   -- 匹配非 root 开头 ，冒号分割， 打印第三列，第四列，最后一列。

   ```kotlin
   # awk -F: '$1 !~ /^root/{print $3, $4, $NF}' passwd 
   
   1 1 /sbin/nologin
   
   2 2 /sbin/nologin
   
   3 4 /sbin/nologin
   
   4 7 /sbin/nologin
   
   5 0 /bin/sync
   
   6 0 /sbin/shutdown
   ```

   

   -- 匹配 （如果某行包含 shell，则打印该行信息）：

   ```kotlin
   # awk -F: '/bash/{print $0}' passwd 
   
   root​ ​ x​ : x:0 :0:root:/root:/bin/bash
   ```

   

   --  匹配ID 号大于500

   ```kotlin
   # awk -F: '$3 >= 500 {print $1, $3}' /etc/passwd
   
   polkitd 999
   
   libstoragemgmt 998
   
   colord 997
   
   saslauth 996
   
   setroubleshoot 995
   
   nfsnobody 65534
   
   unbound 994
   
   chrony 993
   
   gluster 992
   ```

   

   -- 在匹配到的字符前面加标签BEGIN。

   ```kotlin
   # awk -F: 'BEGIN{print "Username   UID"}{printf "%-15s%s\n",$1,$3}' /etc/passwd | head -n5
   
   Username   UID
   
   root      0
   
   bin      1
   
   daemon     2
   
   adm      3
   ```

   

   -- 匹配结束之后添加提示符 Over

   ```kotlin
   [root@localhost yujma]# awk -F: 'BEGIN{print "Username   UID"}{printf "%-15s%s\n", $1, $3}END{print "Over"}' /etc/passwd 
   
   Username   UID
   
   root      0
   
   bin      1
   
   daemon     2
   
   test      1009
   
   Over
   ```

   

   -- awk. 显示三种提示符：

   ```kotlin
   # awk -v FS=: '{print $1, $3}' passwd     ---- -v FS=：
   
   root 0 
   
   bin 1
   
   daemon 2
   
   adm 3
   
   # awk -F: '{print $1, $3}' passwd         --- -F：
   
   root 0
   
   bin 1
   
   daemon 2
   
   adm 3
   
   # awk 'BEGIN{FS=":"}{print $1, $3}' passwd     ---begin 赋值
   
   root 0
   
   bin 1
   
   daemon 2
   
   adm 3
   
   
   ```

   ----------------------------------------------控制语句---------------------------------------------

   1. if - else

   ​     if (condition) {then-body} else ([ else-body  ])

   ```kotlin
   # awk -F: '{if ($3==0) print $1,"Admin" ; else print $1,"Common User"}' passwd 
   
   root Admin
   
   bin Common User
   
   daemon Common User
   
   adm Common User
   # awk -F: '{if ($3==0) printf "%-15s:%s\n",$1,"Admin"; else printf "%-15s:%s\n",$1,"Common User"}' passwd 
   root           :Admin
   bin            :Common User
   daemon         :Common User
   adm            :Common User
   lp             :Common User
   sync           :Common User
   shutdown       :Common User
   # awk -F: '{if ($3==0) printf "%-15s%s\n", $1,"Admin"; else printf "%-15s%s\n", $1,"Common User"}' passwd 
   root           Admin
   bin            Common User
   daemon         Common User
   adm            Common User
   lp             Common User
   sync           Common User
   shutdown       Common User
   
   -- 统计 UID >=500 的用户数量 
   # awk -F: -v sum=0 '{if ($3>=500) sum++} END{print sum}' /etc/passwd
   22
   
   ```

   

   2. while

      ```kotlin
      while (condition) {statement1, statement2, statement3... }
      
      \# awk -F: '$1!~/root/{i=1; while(i<=4) {print $i; i++}}' passwd 
      
      bin
      
      x
      
      1
      
      1
      ```

      

   3. do-while

      ```kotlin
      do  {statement1, statement2, statement3... } while (condition)
      
      # awk -F: '{i=1; do {print $i; i++} while(i<=3)}' passwd 
      
      root
      
      x
      
      0
      ```

      

   4. for

   ```kotlin
   # awk -F: '{for(i=1;i<NF;i+=2) print $i}' passwd 
   
   root
   
   0
   
   root
   
   bin
   
   1
   
   bin
   
   daemon
   
   2
   # awk -F: 'BEGIN{ for(i==1;i<99;i++)sum+=i; print sum}'
   4851
   
   ```

   

   -- awk 中使用数组：

   ```kotlin
   # awk 'BEGIN{A["m"]="Hello";A["n"]="world"; print A["m"]A["n"]}'
   
   Helloworld
   # awk 'BEGIN{A["m"]="Hello"; A["n"]="world"; for (B in A) print A[B]}'
   Hello
   world
   ```

   

   -- awk 统计 netstat 的状态数量：

   ```kotlin
   # netstat -ant | awk '{S[$NF]++} END{for (A in S) print A, S[A]}'
   
   LISTEN 13
   
   CLOSE_WAIT 11
   
   State 1
   
   ESTABLISHED 13
   
   established) 1
   
   # netstat -ant | awk '{S[$NF]++} END{for (A in S) printf "%-15s%s\n", A, S[A]}'
   
   LISTEN               13
   
   CLOSE_WAIT           11
   
   State                1
   
   ESTABLISHED          13
   
   established)         1
   
   ---  匹配 TCP 的 netstat 状态
   # netstat -ant | awk '$1~/tcp/{S[$NF]++} END{for (A in S) printf "%-15s%s\n", A, S[A]}'
   LISTEN         13
   CLOSE_WAIT     11
   ESTABLISHED    13
   ```

   

   -- awk 统计 /etc/passwd 中各 shell.(非空) 的个数：

   ```kotlin
   # awk -F: '$NF!~/^$/ {SHELL[$NF]++} END{for (A in SHELL) print A, SHELL[A]}' /etc/passwd
   
   /bin/sync 1
   
   /bin/bash 11
   
   /sbin/nologin 38
   
   /sbin/halt 1
   
   /bin/false 1
   
   /sbin/shutdown 1
   
   # awk -F: '$NF!~/^$/ {SHELL[$NF]++} END{for (A in SHELL) printf "%-15s%s\n", A, SHELL[A]}' /etc/passwd
   
   /bin/sync       1
   
   /bin/bash       11
   
   /sbin/nologin   38
   
   /sbin/halt      1
   
   /bin/false      1
   
   /sbin/shutdown  1
   
   -- 统计 http 的 acces_log 的访问IP的次数：
   # awk '{IP[$1]++} END{for (A in IP) print A, IP[A]}' access_log-20180624 
   格式化显示：
   # awk '{IP[$1]++} END{for (A in IP) printf "%-15s%s\n", A, IP[A]}' access_log-20180624 
   103.78.180.149 1
   110.232.248.2201
   36.75.224.75   2
   127.0.0.1      32
   197.149.90.94  1
   31.184.194.109 1
   123.139.66.171 222
   188.18.142.26  1
   103.31.45.132  1
   170.233.46.232 1
   182.32.70.201  1
   182.156.218.6  1
   ```

   split 函数在 awk 中的用法：

   

   ```kotlin
   -- 查询 80 端口的IP 和次数。且排序，取前50
   # netstat -ant | awk '/:80/{split($5, clients, ":"); IP[clients[1]]++} END{for (i in IP) print i, IP[i]}' | sort -rn | head -50
    1
   # netstat -ant | awk '/:80/{split($5, clients, ":"); IP[clients[1]]++} END{for (i in IP) printf "%-15s%s\n", i, IP[i]}'
   106.11.68.13   1
   47.111.163.223 1
   0.0.0.0        1
   47.104.93.40   1
   100.100.30.25  1
   39.107.88.3    1
   ```

   

   

   

   

   

   

   

   

   

