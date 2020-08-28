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
<p> The top of right-hand of diagram above is first several stages of socket_server.py. As you can see the beginning of server_connection function is creating a socket object. 
    <br>
    <pre>
    Like this:  
          <b>socket.socket(socket.AF_INET, socket.SOCK_STREAM)</b>
    </pre>
    We get this socket() function so the first step for the server side. 
    The next step is bind() function. Type of 2-Tuple host name and ports number is passed as parameters we defined at the top of socket_server.py.
    <pre>
        We use in the code file for instance: 
            <b>soc.bind((host_address, port_number))</b>
    </pre>

   Now, there is need to listen ports thus we use listen() function like this <b> soc.listen(). </b>
   <br>
   Before beginning the other with statement in the code, we define accept() function. This function provide connection and starts data loop. Also in this loop there ara
   two more function recv() and send().

</p>



<br>
