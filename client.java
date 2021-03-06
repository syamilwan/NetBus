// Import module 
import java.io.*;
import java.net.*;
import java.util.*; 

public class client {

    // Create socket 
    public static void main(String[] args) throws IOException {
    final int PORT_NUMBER = 12345;
    final String HOSTNAME = "192.168.59.75";
    String data;
    String prompt;
    // Connect to the server on local computer 
    try {
        Socket socket = new Socket(HOSTNAME, PORT_NUMBER);
    	PrintWriter outt =
        	new PrintWriter(socket.getOutputStream(), true);
    	BufferedReader inn =
        	new BufferedReader(
            	new InputStreamReader(socket.getInputStream()));
    	BufferedReader stdIn =
        	new BufferedReader(
            	new InputStreamReader(System.in));
        System.out.println("Connection request sent");
        
    // Output received data from the server
    //data=inn.readLine();
    //System.out.println(data);
    
    // Prompt input for command loop
    prompt="aaaaa";
    while(!prompt.equals("-quit")){
      System.out.println("\n##Input command: ");
      prompt = stdIn.readLine();
      
      if (prompt.equals("-help")){
        System.out.println("\n##Command list: ---\n  -shut: Shut Down server \n  -quit: Disconnect from server \n  -spam: Spam clicks on server \n  coming soon: --");
      }
      else if (prompt.equals("-shut")){
        System.out.println("\n##Shutting down server");
        outt.println(prompt);
        break;
      }
      else if (prompt.equals("-quit")){     
        System.out.println("\n##Quiting the connection to server");
        outt.println(prompt);
      }
      else if (prompt.equals("-spam")){     
        System.out.println("\n##Spamming the server with clicks");
        outt.println(prompt);
      }
      else{   
        System.out.println("\n\n#\n#\n##Unrecognized input, input '-help' for manual");
      }
      outt.flush();
    }
    outt.close();
    inn.close();
    socket.close(); // Close the connection

    System.out.println("##Program Closed");
    } catch(Exception e) {
        e.printStackTrace();
    } }
}
