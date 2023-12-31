Title: Network Administration Hw1: Setup DHCP, NAT, Firewall  
Date: 2013-04-09 15:29  
Author: fkz  
Category: Note  
Tags: Linux, Arch Linux, iptables, Firewall, DHCP, NAT, sysadmin  
Slug: network-administration-hw1-setup-dhcp-nat-firewall  
Modified: 2015-10-27 21:31  
Summary: NCTUCS 2013 Spring Network Administration Homework1  
  
  
## Setup DHCP, NAT, Firewall  
  
> I done this homework in Arch Linux  
  
---  
  
## SPEC  
  
```  
Server - dhcp server, NAT, Firewall, ftp-proxy, transparent http proxy (TP)  
(home-q) dhcp server => dhcpd;  
         NAT, Firewall, ftp-proxy => iptables;  
         transparent http proxy => squid;  
         外網網卡 enp0s18 140.113.27.37  
         內網網卡 enp0s19 172.16.1.254  
```  
  
```  
HostA -  dhcp client with private ip (172.16.1.101~172.16.1.200)  
(www-q)  http client browse through Server's TP  
         dhcp client => dhcpcd;  
         內網網卡 enp0s18  
```  
  
```  
HostB -  dhcp client with static private ip (172.16.1.30)  
(mail-q) provide ssh service (bind on Server's 222 port)  
         provide ftp service (bind on Server's 21 port)  
         ftp service => vsftpd;  
         內網網卡 enp0s18; MAC 5a:49:97:32:c3:13 (拿來給 dhcpd 發 static private ip)  
```  
  
---  
  
## DHCP server (on home-q)  
  
+ <https://wiki.archlinux.org/index.php/Dhcpd>  
+ <http://linux.vbird.org/linux_server/0340dhcp.php>  
  
基本上就照著 Arch wiki 作  
`# ip addr add 172.16.1.254/24 dev enp0s19`  
然後在 `/etc/dhcpd.conf` 中寫下規則  
  
```  
option domain-name "nctucs.net";                                                  
option domain-name-servers 8.8.8.8, 140.113.1.1;                                  
option subnet-mask 255.255.255.0;                                                  
option routers 172.16.1.254;                                                      
option broadcast-address 172.16.1.255;                                            
                                                                                   
default-lease-time 3600;                                                          
max-lease-time 7200;                                                              
ddns-update-style none;                                                            
log-facility local7;                                                              
                                                                                   
#pool                                                                              
subnet 172.16.1.0 netmask 255.255.255.0 {                                          
    range 172.16.1.101 172.16.1.200;                                              
}                                                                                  
                                                                                   
#static private ip                                                                
host mail-q {                                                                      
    hardware ethernet 5a:49:97:32:c3:13;                                          
    fixed-address 172.16.1.30;                                                    
}  
```  
   
為了讓 dhcpd 只 listen 特定的 interface  
在 `/etc/conf.d/dhcp` 中 把 `DHCP4_ARGS="-q"` 改成 `DHCP4_ARGS="-q enp0s19"`  
然後 `# systemctl start dhcpd4` 應該就能成功當起 dhcp server 了  
  
---  
  
## DHCP client (on www-q and mail-q)  
  
+ <https://wiki.archlinux.org/index.php/Network_Configuration#Dynamic_IP_address>  
  
一樣照著 arch wiki 作 預設應該就有裝 dhcpcd 了  
`# dhcpcd enp0s18`  
這裡的 enp0s18 是內網網卡  
然後 `# systemctl start dhcpcd@enp0s18`  
用 `$ lspci -k` 察看跟網卡相關的 modules  
結果如下  
  
```  
00:13.0 Ethernet controller: Realtek Semiconductor Co., Ltd. RTL-8139/8139C/8139C+ (rev 20)  
        Subsystem: Red Hat, Inc Device 1100  
        Kernel driver in use: 8139cp  
```  
  
所以可以知道在 `/etc/modules-load/realtek.conf`  
  
### Note  
  
這邊卡關了一下是因為 dv 也在 140.113.27 網段底下架了一台 dhcp Server  
結果我的 client 一直拿到他的 server 發出來的 ip 而不是我自己架的  
看了鳥哥的網頁  
<http://linux.vbird.org/linux_server/0340dhcp.php#client_linux>  
裏面有提到在 client 端上的 /var/lib/dhclient/ 裏面有跟租約相關的檔案  
可以用 vim 開啟直接改寫  
`option dhcp-server-identifier 172.16.1.254` 指定 dhcp Server  
可是在 archlinux 底下無法直接這樣改寫，用vim開起來會是亂碼  
後來是在 client 端的 `/etc/dhcpcd.conf` 中加上 `static routers=172.16.1.254` 解決  
  
---  
  
## NAT & Firewall  
  
> In Linux we use iptables, while in FreeBSD we use PF  
  
+ <http://linux.vbird.org/linux_server/0250simple_firewall.php>  
+ <https://wiki.archlinux.org/index.php/Internet_Share>  
+ <https://wiki.archlinux.org/index.php/Simple_Stateful_Firewall>  
+ <https://wiki.archlinux.org/index.php/Iptables>  
+ <https://wiki.archlinux.org/index.php/Router>  
+ <http://www.revsys.com/writings/quicktips/nat.html>  
   
參考了以上的連結之後，目前 iptables 的設定如下  
  
```  
# Generated by iptables-save v1.4.18 on Tue Apr  9 04:40:40 2013                
*mangle                                                                        
:PREROUTING ACCEPT [369:34165]                                                  
:INPUT ACCEPT [278:20862]                                                      
:FORWARD ACCEPT [91:13303]                                                      
:OUTPUT ACCEPT [153:20248]                                                      
:POSTROUTING ACCEPT [244:33551]                                                
COMMIT                                                                          
# Completed on Tue Apr  9 04:40:40 2013                                        
# Generated by iptables-save v1.4.18 on Tue Apr  9 04:40:40 2013                
*filter                                                                        
:INPUT ACCEPT [3:418]                                                          
:FORWARD ACCEPT [91:13303]                                                      
:OUTPUT ACCEPT [153:20248]                                                      
:BADHOST - [0:0]                                                                
-A INPUT -j BADHOST                                                            
-A BADHOST -s 140.113.101.10 -j DROP                                            
-A INPUT -i enp0s18 -p icmp -m icmp --icmp-type 8 -j DROP                      
-A INPUT -m state --state INVALID -j DROP                                      
-A INPUT -m state --state RELATED,ESTABLISHED -j ACCEPT                        
-A INPUT -i lo -j ACCEPT                                                        
-A INPUT -i enp0s18 -s 140.113.230.88 -j ACCEPT                                
-A FORWARD -m state --state INVALID -j DROP                                    
-A FORWARD -s 140.113.17.0/24 -d 172.16.1.30 -p tcp --dport 21 -j REJECT --reject-with tcp-reset  
-A FORWARD -m state --state RELATED,ESTABLISHED -j ACCEPT  
-A FORWARD -s 140.113.230.88 -d 172.16.1.30 -p tcp --dport 21:22 -j ACCEPT      
-A FORWARD -s 140.113.27.47 -d 172.16.1.30 -p tcp --dport 22 -j ACCEPT        
-A FORWARD -s 140.113.235.0/24 -d 172.16.1.30 -p tcp --dport 21 -j ACCEPT      
-A FORWARD -s 140.113.17.0/24 -d 172.16.1.30 -p tcp --dport 22 -j ACCEPT        
-A FORWARD -d 172.16.1.30 -p tcp --dport 21 -j DROP                            
-A FORWARD -d 172.16.1.30 -p tcp --dport 22 -j DROP                            
COMMIT                                                                          
# Completed on Tue Apr  9 04:40:40 2013                                        
# Generated by iptables-save v1.4.18 on Tue Apr  9 04:40:40 2013                
*nat                                                                            
:PREROUTING ACCEPT [2:426]                                                      
:INPUT ACCEPT [1:354]                                                          
:OUTPUT ACCEPT [0:0]                                                            
:POSTROUTING ACCEPT [1:60]                                                      
-A PREROUTING -i enp0s18 -p tcp --dport 21 -j DNAT --to-destination 172.16.1.30:21  
-A PREROUTING -i enp0s18 -p tcp --dport 222 -j DNAT --to-destination 172.16.1.30:22  
-A PREROUTING -s 172.16.1.0/24 -i enp0s19 -p tcp -m tcp --dport 80 -j REDIRECT --to-ports 3128  
-A POSTROUTING -s 172.16.1.0/24 -o enp0s18 -j MASQUERADE                        
COMMIT                                                                          
# Completed on Tue Apr  9 04:40:40 2013  
```  
  
> 140.113.230.88 是寢室的 ip  
> 140.113.27.47 是社窩無網的ip  
> 為了方便操作用  
  
---  
  
## Proxy  
  
### ftp-proxy  
  
好像在 iptables 就設定完了 根本不用像 FreeBSD 還要用 ftp-proxy  
猜測是因為 `-A FORWARD -m state --state RELATED,ESTABLISHED -j ACCEPT` 的緣故  
  
+ <https://wiki.archlinux.org/index.php/Squid>  
+ <http://linux.vbird.org/linux_server/0420squid.php>  
  
  
### transparent http proxy  
  
在 `/etc/squid/squid.conf` 中 `http_port` 後面加上 `intercept`  
  
`http_port 3128 intercept`  
  
> 鳥哥裏面是寫 `http_port 3128 transparent`  
> 在 <http://www.squid-cache.org/Doc/config/http_port/> 有寫到在 3.1 的版本以後  
> intercept - Rename of old 'transparent' option to indicate proper functionality.  
  
把 `cache_dir ufs /var/cache/squid 256 16 256` 的註解取消  
再加上 `cache_mem 8 MB` (預設是 8 MB 可以自己改)  
  
`# squid -z` (在 `/var/cache/squid/` 建立資料夾)  
`# squid -k check` (檢查 `/etc/squid/squid.conf` 有沒有問題)  
`# systemctl start squid`  
  
之後在 iptables 的 nat table 中加上新的 rule,  
把內網往外傳的 http request 轉到 squid 上  
`-A PREROUTING -i enp0s19 -s 172.16.1.0/24 -p tcp --dport 80 -j REDIRECT --to-ports 3128`  
然後 reload iptables  
  
---  
  
## vsftpd  
  
遇到兩個錯誤  
  
1. `500 OOPS: priv_sock_get_cmd`  
    + 解決方法  
        + <https://bbs.archlinux.org/viewtopic.php?id=147074>  
        + 在 `/etc/vsftpd.conf` 加上 `seccomp_sandbox=0`  
2. `500 OOPS: vsftpd: refusing to run with writable root inside chroot()`  
    + 解決方法  
        + <http://www.ubuntu-tw.org/modules/newbb/viewtopic.php?post_id=236642>  
        + `chmod a-w $dir`  
        + 該 root dir 不可有寫入的權限  
  
---  
  
## 感想  
  
用 Arch Linux 蠻方便的  
基本上就照著鳥哥和 Arch Wiki 的教學邊做邊學應該就差不多了  
不過跟上課教的好像差蠻多的XD  
教的是 FreeBSD, PF  
結果我用 Linux, iptables  
這樣期中考真的沒問題嗎w?  
