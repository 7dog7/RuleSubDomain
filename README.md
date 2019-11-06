# RuleSubDomain
规则组合子域名生成
## 简介

资产收集系统抽出来,规则组合域名字典功能  
搭配lijiejie项目使用 https://github.com/lijiejie/subDomainsBrute/  
字典需要自己精简优化处理(随便弄了一个)  
这玩意自己用来爆破资产后台,有需求就精简出来了  

domain.txt 填入home.qq.com  

根据规则:  

 >'{domain}{sub}'  
 >'{sub}{rule}{domain}'  
 >'{domain}{rule}{sub}'  
 >'{domain}.{sub}'  
 >'{sub}.{domain}'  
 
生成出:  

>admhome.qq.com  
>homeadm.qq.com  
>adm.home.qq.com  
>home.adm.qq.com  
>adm-home.qq.com  
>home-adm.qq.com  
>adm_home.qq.com  
>home_adm.qq.com  

有问题和需求请Issues  

## 使用

    
使用说明

1. domain.txt文件(已存在的域名)
    >www.baidu.com  
    >www.222.baidu.com  
2. subname.txt (字典)  

3. ruleSub.txt (根据规则生成的字典)   

4. 扫描启动
   >python RuleSubDomain.py  

