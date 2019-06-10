// Import module 
import java.io.*;
import java.net.*;
import java.util.Scanner; 

public class client {

    // Create socket 
    public static void main(String[] args) throws IOException {
    final int PORT_NUMBER = 12345;
    final String HOSTNAME = "192.168.59.75";

    // Connect to the server on local computer 
    try {
        Socket sock = new Socket(HOSTNAME, PORT_NUMBER);
        PrintWriter out = new PrintWriter(sock.getOutputStream(),true);
        DataInputStream in=new DataInputStream(sock.getInputStream());  
        System.out.println("Connection request sent");
        
    // Receive data from the server
    String str=(String)in.readUTF();  
    System.out.println(str);
    
    // Prompt input for command loop
    String prompt="";
    while(!prompt.equals("-quit")){
      System.out.println("\n##Input command: ");
      prompt = in.readLine();
      
      if (prompt.equals("-help")){
        System.out.println("\n##Command list: ---\n  -shut: Shut Down server \n  -quit: Disconnect from server \n  -spam: Spam clicks on server \n  coming soon: --");
      }
      else if (prompt.equals("-shut")){
        System.out.println("\n##Shutting down server");
        out.println(prompt);
        break;
      }
      else if (prompt.equals("-quit")){     
        System.out.println("\n##Quiting the connection to server");
        out.println(prompt);
      }
      //else if (prompt.equals("-")){
        
      //}
      else{   
        System.out.println("\n##Unrecognized input, input 'helpp' for manual");
      }
      out.flush();
    }

    sock.close(); // Close the connection
    out.close();
    in.close();
	    
    System.out.println("##Program Closed");
    } catch(Exception e) {
        e.printStackTrace();
    } }
}
