
package main

import (
   "context"
   "github.com/kubemq-io/kubemq-go"
   "log"
   "time"
   "strings"
   "math/rand"
   "fmt"
   "strconv"
   "bytes"
   "encoding/gob"
)


func get_job_task_id() string {
    // Set the seed for the random number generator.
    rand.Seed(time.Now().UnixNano())

    // Create a string of alphabets to choose from.
    alphabets := "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers := "0123456789"

    // Create a slice of strings to hold the selected alphabets.
    selected := make([]string, 0)

    // Choose 10 random alphabets and append them to the selected slice.
    elements := []int{4, 2, 2, 6}
    for _, element := range elements {
        temp := make([]string, 0)
        for j := 0; j < element; j++ {
            // Generate a random integer in the range [0, 26) (i.e., 0 to 25 inclusive)
            // using the rand.Intn function.
            a_index := rand.Intn(26)
            n_index := rand.Intn(9)
            // Use the random integer as an index into the string of alphabets to
            // select a random alphabet.
            alphabet := alphabets[a_index]
            number := numbers[n_index]

            // Append the selected alphabet to the selected slice.
            temp = append(temp, string(alphabet))
            temp = append(temp, string(number))
        }
        temp_result := strings.Join(temp, "")
        selected = append(selected, strings.ToLower(temp_result))
    }
    // Use the string.Join function to join the selected alphabets together
    // into a single string, with a hyphen (-) as the separator.
    result := strings.Join(selected, "-")
    return result
}

func main() {
    for i := 0; i < 10; i++ {
//         go func() {
            type Payload struct {
                Job_id string
                Chunk string
                Task_id string
                Status string
            }
            p := new(Payload)
            p.Job_id = get_job_task_id()

            for i:=0; i<7; i++{

                p.Task_id = get_job_task_id()
                p.Chunk = strings.Join([]string{"chunk",strconv.Itoa(rand.Intn(6)),".log"},"")


                ctx, cancel := context.WithCancel(context.Background())
                defer cancel()
                client, err := kubemq.NewClient(ctx,
                   kubemq.WithAddress("localhost", 50000),
                   kubemq.WithClientId("test-command-client-id"),
                   kubemq.WithTransportType(kubemq.TransportTypeGRPC))
                if err != nil {
                  log.Fatal(err)
                }
                defer client.Close()
                channel := "hello-world-queue"
                var buf bytes.Buffer
                enc := gob.NewEncoder(&buf)
                err_ := enc.Encode(p)
                if err_ != nil{
                    sendResult, err := client.NewQueueMessage().
                    SetChannel(channel).
                    SetBody(buf.Bytes()).
                    Send(ctx)
                    if err != nil {
                        log.Fatal(err)
                    }
                    fmt.Printf("Send to Queue Result: MessageID:%s,Sent At: %s, Message: %s\n", sendResult.MessageID, time.Unix(0, sendResult.SentAt).String(), sendResult)
                }
//                 fmt.Println(buf.Bytes())


            }


//         }()
    }
}
