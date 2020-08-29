# socket-server-client-connection
simple communication between server and client using python
# socket-server-client-connection
## simple communication between server and client using python

<b>Requirements</b>
<li>socket</li>
<br>
<b>Functions in the socket modul</b>
<br>
<br>
<li>socket()</li>
<li>bind()</li>
<li>listen()</li>
<li>accept()</li>
<li>connect()</li>
<li>send()</li>
<li>recv()</li>
<li>close()</li>
<br>
<p> In the below, the diagram has sequence of socket API and how to TCP data flow. We follow up the right-hand when we write server side. The left-hand shows client's steps.</p>
<br>

![NW_Diagrams](https://user-images.githubusercontent.com/29188196/91567223-77ce8c00-e94d-11ea-876f-2d8111166b8e.png)

<a>https://www.keil.com/pack/doc/mw6/Network/html/using_network_sockets_bsd.html</a>

<br>
<p> The top of right-hand of diagram above is first several stages of socket_server.py. As you can see the beginning of server_connection function is creating a socket object. Also passed two parameters to this function, one of them is AF_INET and second is SOCK_STREAM. AF_INET is the Internet address family for IPv4. SOCK_STREAM is the socket type for TCP, the protocol that will be used to transport our messages in the network. Anyways, we now have a new socket object.
    <br>
    <pre>
    Like this:  
          <b>socket.socket(socket.AF_INET, socket.SOCK_STREAM)</b>
    </pre>
    We get this <b>socket()</b> function so the first step for the server side.
    The next step is <b>bind()</b> function. Type of 2-Tuple host name and ports number is passed as parameters we defined at the top of <b>socket_server.py.</b>
    <pre>
        We use in the code file for instance: 
            <b>soc.bind((host_address, port_number))</b>
    </pre>

   Now, there is need to listen ports thus we use <b>listen()</b> function like this <b> soc.listen().</b>
   <br>
   Before beginning the other with statement in the code, we define <b>accept()</b> function. This function provide connection and starts data loop. Also in this loop there are
   two more functions <b>recv()</b> and <b>send().</b> Also <b>send()</b> is used to as <b>sendall()</b> in while loop.
   
   Getting the client socket object from <b>accept()</b> with connection that infinite loop is used to over <b>connection.recv()</b> function. 
   <pre>
   
            while True: 
                data = connection.recv(1024)
                if not data:
                    break
                connection.sendall(data)
   
   </pre>

   Lastly start the server socket program with <b>server_connection().</b>
   <br>
   If you compare the client with the server you will see similar things probably and so simple according to server side. Now, the beginning of the client is same with server      side. These four steps start with creating a socket object so: 
   <pre>
        <b>socket.socket(socket.AF_INET, socket.SOCK_STREAM)</b>
   </pre>
   The order of other steps is <b>connect(), send() and recv().</b> Lastly, it calls <b>soc.recv()</b> to read the server’s reply and then prints it.  
   <pre>
       So, we use that
           
           <b>data = soc.recv(1024)</b> 
   </pre>     
   and start client_connection().
</p>



<br>
