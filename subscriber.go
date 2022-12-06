package main

import (
   "context"
   "github.com/kubemq-io/kubemq-go"
   "net/http"
   "log"
   "fmt"
)

var msgChan chan string
var count int

func getTime(w http.ResponseWriter, r *http.Request) {

	w.Header().Set("Access-Control-Allow-Origin", "*")

    fmt.Println("Checking for messages...")
    ctx, cancel := context.WithCancel(context.Background())
    defer cancel()
    client, err := kubemq.NewClient(ctx,
      kubemq.WithAddress("localhost", 50000),
      kubemq.WithClientId("test-queue-client-id"),
      kubemq.WithTransportType(kubemq.TransportTypeGRPC))
    if err != nil {
        log.Fatal(err)
    }
    defer client.Close()
    channel := "lambda-test"

    for true {
       receiveResult, err := client.NewReceiveQueueMessagesRequest().
       SetChannel(channel).
       SetMaxNumberOfMessages(1).
       SetWaitTimeSeconds(5).
       Send(ctx)
       if err != nil {
           log.Fatal(err)
       }
        for _, msg := range receiveResult.Messages {
            if msgChan != nil {
		        msgChan <- string(msg.Body)
		    }
        }
    }
}

func sseHandler(w http.ResponseWriter, r *http.Request) {
	fmt.Println("Client connected")
	w.Header().Set("Access-Control-Allow-Origin", "*")
	w.Header().Set("Content-Type", "text/event-stream")
	w.Header().Set("Cache-Control", "no-cache")
	w.Header().Set("Connection", "keep-alive")

	msgChan = make(chan string)

	defer func() {
		close(msgChan)
		msgChan = nil
		fmt.Println("Client closed connection")
	}()

	flusher, ok := w.(http.Flusher)
	if !ok {
		fmt.Println("Could not init http.Flusher")
	}

	for {
		select {
		case message := <- msgChan:
			fmt.Print("sending message \t")
			fmt.Println(message)
			count++
			fmt.Fprintf(w, "data: %s\n\n", message)
			flusher.Flush()
		case <- r.Context().Done():
            fmt.Println("Client closed connection")
            fmt.Println(count)
            return
		}
	}
}

func main() {
	 router := http.NewServeMux()

	 router.HandleFunc("/event", sseHandler)
	 router.HandleFunc("/time", getTime)

	 log.Fatal(http.ListenAndServe(":3500", router))
}
































// func main() {
//    fmt.Println("Checking for messages...")
//    ctx, cancel := context.WithCancel(context.Background())
//    defer cancel()
//    client, err := kubemq.NewClient(ctx,
//       kubemq.WithAddress("localhost", 50000),
//       kubemq.WithClientId("test-queue-client-id2"),
//       kubemq.WithTransportType(kubemq.TransportTypeGRPC))
//    if err != nil {
//       log.Fatal(err)
//    }
//    defer client.Close()
//    channel := "hello-world-queue"
//
//    for true {
//        receiveResult, err := client.NewReceiveQueueMessagesRequest().
//        SetChannel(channel).
//        SetMaxNumberOfMessages(1).
//        SetWaitTimeSeconds(5).
//        Send(ctx)
//        if err != nil {
//            log.Fatal(err)
//        }
//        for _, msg := range receiveResult.Messages {
//            fmt.Println(string(msg.Body))
//        }
//        time.Sleep(250*time.Millisecond)
//    }
// }

