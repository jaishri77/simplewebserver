from http.server import HTTPServer, BaseHTTPRequestHandler

content = '''
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <h1 align="center" >Web development</h1>
    <title>Document</title>
    <link rel="stylesheet" href="index.css">
</head>
<body bgcolor="lightblue">
    <h1 align="center" >TCP/IP</h1>
   
    <table border="1px" align="center" cellspacing="10px" cellpadding="10px">
        <tr>
            <th>List of protocols</th>
            <th>Name of the protocol</th>
            
            </tr>
            <tr>
                <td>Application layer</td>
                <td>HTTP,FTP</td>
              
                </tr>
            <tr>
                <td>Transport layer</td>
                <td>TCP,UDP</td>
                
            </tr>
            <tr>
                <td>Network layer</td>
                <td>IPv4,Ipv6</td>
                
            </tr>
            <tr>
                <td>Link layer</td>
                <td>Ethernet,FDDI,X.25,Frame Relay,Token Ring</td>
                
            </tr>
</body>
</html>'''

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200) 
        self.send_header("content-type", "text/html")       
        self.end_headers()
        self.wfile.write(content.encode())

print("This is my webserver") 
server_address =('',8000)
httpd = HTTPServer(server_address,MyServer)
httpd.serve_forever()