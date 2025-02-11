import java.io.*;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.Properties;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class SimpleWebServer {
    private int port;
    private ServerSocket serverSocket;
    private ExecutorService threadPool;
    private static final Logger logger = LoggerFactory.getLogger(SimpleWebServer.class);

    public SimpleWebServer() {
        loadConfiguration("config.properties");
        threadPool = Executors.newFixedThreadPool(10); // Thread pool for handling clients
        addShutdownHook();
    }

    private void loadConfiguration(String configFilePath) {
        Properties properties = new Properties();
        try (FileInputStream inputStream = new FileInputStream(configFilePath)) {
            properties.load(inputStream);
            port = Integer.parseInt(properties.getProperty("server.port", "8080"));
        } catch (IOException e) {
            logger.error("Error reading the configuration file: {}", e.getMessage());
            System.exit(1);
        } catch (NumberFormatException e) {
            logger.error("Invalid port number in configuration: {}", e.getMessage());
            System.exit(1);
        }
    }

    public void startServer() {
        try {
            serverSocket = new ServerSocket(port);
            logger.info("Server started on port: {}", port);
            while (true) {
                Socket clientSocket = serverSocket.accept();
                handleClient(clientSocket);
            }
        } catch (IOException e) {
            logger.error("Error starting the server: {}", e.getMessage());
        }
    }

    private void handleClient(Socket clientSocket) {
        threadPool.execute(() -> {
            try (InputStream in = clientSocket.getInputStream();
                 OutputStream out = clientSocket.getOutputStream()) {
                     
                Request request = readRequest(in);
                Response response = processRequest(request);
                sendResponse(out, response);

            } catch (IOException e) {
                logger.error("Error handling client: {}", e.getMessage());
            } finally {
                try {
                    clientSocket.close();
                } catch (IOException e) {
                    logger.error("Error closing client socket: {}", e.getMessage());
                }
            }
        });
    }

    private void addShutdownHook() {
        Runtime.getRuntime().addShutdownHook(new Thread(() -> {
            try {
                if (serverSocket != null && !serverSocket.isClosed()) {
                    serverSocket.close();
                    logger.info("Server closed gracefully.");
                }
                threadPool.shutdown();
            } catch (IOException e) {
                logger.error("Error closing server socket: {}", e.getMessage());
            }
        }));
    }

    private Request readRequest(InputStream in) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(in));
        String line = reader.readLine();
        if (line == null || line.isEmpty()) {
            throw new IOException("Empty request");
        }
        String[] requestLine = line.split(" ");
        validateRequest(requestLine);
        return new Request(requestLine[0], requestLine[1]);
    }

    private void validateRequest(String[] requestLine) throws IOException {
        if (requestLine.length < 2) {
            throw new IOException("Invalid request format");
        }
        String method = requestLine[0];
        String path = requestLine[1];
        if (!method.equals("GET")) { // Extend this check as needed
            throw new IOException("Method Not Allowed: " + method);
        }
        if (!isValidPath(path)) {
            throw new IOException("Invalid path requested");
        }
    }

    private boolean isValidPath(String path) {
        // Add more validation rules as needed
        return path.matches("[^<>]*");
    }

    private Response processRequest(Request request) {
        // Here we can return a simple response for demonstration purposes
        String responseBody = "Hello World! You requested: " + request.getPath();
        return new Response("HTTP/1.1 200 OK", responseBody);
    }

    private void sendResponse(OutputStream out, Response response) throws IOException {
        PrintWriter writer = new PrintWriter(out, true);
        writer.println(response.getStatus());
        writer.println("Content-Length: " + response.getBody().length());
        writer.println("Content-Type: " + getContentType(response.getBody()));
        writer.println(); // Blank line separating headers and body
        writer.println(response.getBody());
    }

    private String getContentType(String body) {
        // Basic example, expand to handle different content types
        return "text/plain"; // Add more content types based on file types as needed
    }

    public static void main(String[] args) {
        SimpleWebServer server = new SimpleWebServer();
        server.startServer();
    }

    // Inner class for client requests
    static class Request {
        private String method;
        private String path;

        public Request(String method, String path) {
            this.method = method;
            this.path = path;
        }

        public String getMethod() {
            return method;
        }

        public String getPath() {
            return path;
        }
    }

    // Inner class for server responses
    static class Response {
        private String status;
        private String body;

        public Response(String status, String body) {
            this.status = status;
            this.body = body;
        }

        public String getStatus() {
            return status;
        }

        public String getBody() {
            return body;
        }
    }
}