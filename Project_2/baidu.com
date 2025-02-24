HTTP/1.1 302 Found
Date: Mon, 24 Feb 2025 06:28:33 GMT
Server: Apache
Location: http://www.baidu.com/search/error.html
Cache-Control: max-age=86400
Expires: Tue, 25 Feb 2025 06:28:33 GMT
Content-Length: 222
Connection: Keep-Alive
Content-Type: text/html; charset=iso-8859-1

<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html><head>
<title>302 Found</title>
</head><body>
<h1>Found</h1>
<p>The document has moved <a href="http://www.baidu.com/search/error.html">here</a>.</p>
</body></html>
