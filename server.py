#import socket module
from socket import *
serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket
#Fill in start
serverPort=7178
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
#Fill in end
while True:
  #Establish the connection
  print 'Ready to serve...'
  connectionSocket, addr = serverSocket.accept()#Fill in start #Fill in end
  filename=None
  try:
     message = connectionSocket.recv(1024)#Fill in start #Fill in end
     filename = message.split()[1]
     f = open(filename[1:])
     outputdata = f.read()#Fill in start #Fill in end
     #Send one HTTP header line into socket
     #Fill in start
     header="HTTP/1.1 200 OK\r\n" + "\r\n"
     connectionSocket.send(header)
     #Fill in end
     #Send the content of the requested file to the client
     for i in range(0, len(outputdata)):
       connectionSocket.send(outputdata[i])
     connectionSocket.close()
  except IOError:
    #Send response message for file not found
    #Fill in start
    header="HTTP/1.1 404 Not Found\r\n\r\n"\
        "<!DOCTYPE html>\n"\
        "<html><head>\n"\
        "<meta charset=\"UTF-8\">\n"\
        "<title>Not Found!</title>\n"\
        "</head><body>\n"\
        "<h1><b>404<b><br>Not Found!</h1>\n"\
        "<p>The requested URL %s was not found on this server.</p>\n"\
        "</body></html>\n" % (filename)
    connectionSocket.send(header)
    #Fill in end
    #Close client socket
    #Fill in start
    connectionSocket.close()
    #Fill in end
  except IndexError:
    header="HTTP/1.1 400 Bad Request\r\n\r\n"\
    "<!DOCTYPE html>\n"\
    "<html><head>\n"\
    "<meta charset=\"UTF-8\">\n"\
    "<title>Bad Request!</title>\n"\
    "</head><body>\n"\
    "<h1><b>400<b><br>Bad Request!</h1>\n"\
    "</body></html>\n"
    connectionSocket.send(header)
    connectionSocket.close()
serverSocket.close()
