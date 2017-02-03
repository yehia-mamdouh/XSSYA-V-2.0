# XSSYA-V-2.0 (XSS Vulnerability Confirmation )


XSSYA is a Cross Site Scripting Scanner & Vulnerability Confirmation (Working in two Methods)
• Method number 1 for Confirmation Request and Response
• Method number 2 for Confirmation Execute encoded payload and search for the same payload in web HTML code but decoded
• Support HTTPS
• After Confirmation (execute payload to get cookies)
• Identify 3 Types of WAF (Mod_Security - WebKnight - F5 BIG IP)
• Can be run in (Windows - Linux)
XSSYA Continue Library of Encoded Payloads To Bypass WAF (Web Application Firewall) It Also Support Saving the Web Html Code Before Executing the Payload Viewing the Web HTML Code into the Screen or Terminal
$ Python xssya.py
Example
$ Python xssya.py
http://www.domain.com/
 http://www.domain.com= http://www.domain.com?


• What have been changed?
(XSSYA v 2.0 has more payloads; library contains 41 payloads to enhance detection level
XSS scanner is now removed from XSSYA to reduce false positive
URLs to be tested used to not allow any character at the end of the URL except (/ - = -?) but now this limitation has been removed


• What’s new in XSSYA V2.0 ? 
Custom Payload 
1 – You have the ability to Choose your Custom Payload Ex: and you can encode your custom payload with different types of encodings like (B64 – HEX – URL_Encode –- HEX with Semi Columns) 

(HTML Entities à Single & Double Quote only - brackets – And – or Encode all payload with HTML Entities) 
This feature will support also XSS vulnerability confirmation method which is you choose you custom payload 
and custom Encoding execute if response 200 check for same payload decoded in HTM code page. 

• What’s new in XSSYA V2.0? 
HTML5 Payloads 
XSYSA V2.0 contains a library of 44 HTLM5 payloads

• What’s New in XSSYA V 2.0? 

XSSYA have a Library for the most vulnerable application with XSS – Cross site scripting and this library counting 
(Apache – WordPress – PHPmy Admin) If you choose apache application it give the CVE Number version of Apache
which is affected and the link for CVE for more details so it will be easy to search for certain version 
that is affected with XSS 

• What’s New in XSSYA V 2.0? 
XSSYA has the feature to convert the IP address of the attacker to (Hex, Dword, Octal) to bypass any security mechanism 
or IPS that will be exist 
on the target Domain 


• What’s New in XSSYA V 2.0?

XSSYA check is the target is Vulnerable to XST (Cross Site Trace) which it sends custom Trace Request 
and check if the target domain is Vulnerable the request will be like this: 

TRACE / HTTP/1.0 
Host: demo.testfire.net 
Header1: < script >alert(document.cookie);


The Module need to be downloaded is
 colorama-0.2.7 https://pypi.python.org/pypi/colorama
gdshortener 0.0.2 https://pypi.python.org/pypi/gdshortener 

Note: if you face Https connection problem - just delete (class fake_ssl) and test again
