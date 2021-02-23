**micro-client-server README**
===

Joseph Polaski and Megan Morrison\
CS361: Sprint 4\
Winter 2021

### **Overview**:

micro-client-server is a lightweight communication system developed for desktop microservices in python. We designed it for our Software Engineering course, when we needed a way to have our desktop microservices to communicate. However, it can be reused and altered to work between any two python apps running on the same machine. 

### **Dependencies**:
Our goal was for this to be as lightweight as possible, and so, there are no external dependencies! Just the Python standard library!

### **Pre-condition**:
Just put the modules in the same directory you are working in and import them:
```
import micro_client
import micro_server
```
---
### **Example of starting a server**:
A server requires a callback function to be passed and creation. This function should be something in your app that will return the data you wish to send to a requesting client. The second argument 'LIFE_GEN' specifies which port will be selected to listen on. These are associated with dictionary keys that have preselected ports and can be interchanged with anything you like. The ports are completely arbitrary and may be changed as well.
```
    import micro_server

    # create a new server
    server = micro_server(call_back_function, 'LIFE_GEN') 
    server.start_listening()
```

### **Example of starting a client**:
A client needs to have a port selection keyword passed as an argument at creation. This should correspond to which ever server you are trying to reach. In this case it matches the server created above. Then you just send a request message containing whatever you like to the server. This can be a string that is tokenized however you wish in order to pass data to the server. You can create your own protocol if you like! The server will then process that message and return data back.
```
    import micro_client

    # create a new client
    client = micro_client('LIFE_GEN')
    response_data = client.send_message("Give me some data back!!")
```