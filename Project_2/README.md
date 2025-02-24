# **Project 2 Report**
### Matthew Papesh - Feb 22nd, 2025
### CS 3516

## Overview:    
A proxy server for caching website data. The program is designed to create a server on a TCP socket to run on local host with port `5665`. When visiting websites through this host and port, if the website is not cached, the server will request that site's contents to then write to a create cache file to then forward the contents to the proxy host:port address. Should a website already be cached by the server, the server will be capable of pulling contents locally for viewin in the browser without requesting contents from the World Wide Web. 

## How To Use:
The python program expects an arugment for specifying the proxy server IP address to use as its host. The server can be run by calling the following on the command line: 
```bash
python3 proxy_server.py 127.0.0.1
```
This bash command will run the program to setup the proxy server under the specified argument and IP of the *localhost*: `127.0.0.1`. Once the server is running, it is ready to handle requesting online contents of website for caching and retrieving local caches for the user browser. 

With the program running, websites can be visited by HTTP on your browser through the server. This can be done by typing the following into your url: **http://localhost:5665/<website url>**. In the case of visiting the website: *www.baidu.com*, the url for using the proxy server to visit this site would be: **http://localhost:5665/baidu.com**. The server will retrieve the cached contents for the browser to load. If baidu.com is not cached, the server will pull its contents from the online internet, cache them, and then write the to view in your browser. 