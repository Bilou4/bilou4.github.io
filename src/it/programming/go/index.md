# Go

Why Go?
- clean package management system
- cross compilation
- rich standard library
- concurrency

Why not Go?
- binary size
- verbosity

## Build flags

- buildvcs=false omits version control information
- ldflags=
  - "-w -s" strips binaries
  - "-X path/to/a/variable" change variable value at compile time
- CGO_ENABLED
  - =0 ideal for scratch docker image (no host OS to be bundled). It uses a basic Go implementation
  - =1 uses the native OS libraries. It implies a smaller binary size but relies on delivering a host OS too. It must be set to 1 if your application imports a package with C code.



```go
for idx, value := range &a{} // a is copied

for idx, value := range a{} // a is not copied
```



```go
uintptr // type containing an integer of a memory address and not a reference to a pointer
```

Go type-safe pointer → keeps its reference to the runtime without Garbage Collector problem

unsafe.Pointer → can be garbage collected

## Variables are passed by value

In Go, arrays are passed by value.

```Go
var t1 [5]int32
var t2 [5]int32{0,0,0,0,0}
var t3 [...]int32{0,0,0} // number of elements in the array are computed at compile time
```

Slices are passed by reference.
```Go
s1 := t1[:]
s2 := []int{0,1,2,3}
```

### Except for slices and maps

TODO: examples
For slices: values can be changed but you cannot add elements.
For maps: any changes are reflected in the variable passed into the function.

### Pretty print - table print

```Go
package main

import (
	"fmt"
	"os"
	"strings"
	"text/tabwriter"
)

func main() {
	writer := tabwriter.NewWriter(os.Stdout, 0, 4, 0, '\t', 0)
	table := [][]string{{"A", "B"}, {"A", "B"}, {"A", "B"}}
	for _, line := range table {
		fmt.Fprintln(writer, strings.Join(line, "\t")+"\t")
	}
	writer.Flush()
}
```

```bash
# Output
A	B
A	B
A	B
```

### Download indication

```Go
package main

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func lenItoa(i int) int {
	return len(strconv.Itoa(i))
}

func main() {
	var s string = "Downloading:  0%"

	fmt.Print(s)
	for i := 0; i <= 100; i++ {

		time.Sleep(100 * time.Millisecond)
		fmt.Print(strings.Repeat("\b", lenItoa(i)+1))
		fmt.Printf("%d%%", i)
	}
	fmt.Println()
}

```


## Memoization in Go

Closures in Go can help you perform memoization on a specific function prototype.

Closures are functions declared inside of functions. The inner function is able to access and modify variables declared in the outer function.

```Go
package main
import (
  "fmt"
  "time"
)
func add(a, b int) int {
  time.Sleep(5 * time.Second)
  return a+b
}

func memoization(f func(int,int)int) func(int,int)int{
  cache := make(map[string]int)
  return func(a,b int) int{
    i := fmt.Sprintf("%d+%d",a,b)
    if v,ok := cache[i]; ok {
      return v
    }
    res := f(a,b)
    cache[i] = res
    return res
  }
}

func main() {
  println("add(1,1) without memoization")
  start := time.Now()
  // the execution will last at least 5 seconds
  println("res = ", add(1,1), time.Since(start).String())

  addMemoized := memoization(add)
  println("add(1,1) with memoization 1/n")
  start = time.Now()
  // the execution will last at least 5 seconds
  println("res = ", addMemoized(1,1), time.Since(start).String())

  println("add(1,1) with memoization 2/n")
  start = time.Now()
  // the execution will be instant
  println("res = ", addMemoized(1,1), time.Since(start).String())
}
```

## Gracefully shutdown your server

```Go
ctx := context.Background()
done := make(chan os.Signal, 1)

signal.Notify(done, os.Interrupt, syscall.SIGTERM)

serv := &http.Server{
  Addr: addr,
  Handler: routes,
}

go srv.ListenAndServe()
<- done
srv.Shutdown()
log.Println("server stopped")
```

## Hot reload

`SIGHUP` is a signal sent to a process when its controlling terminal is closed. It is commn practice for daemonized process to use `SIGHUP` for configuration reload .This allows us to not terminatethe process while making changes.

```bash
kill -SIGHUP PID
```

```go
package main

import (
	"fmt"
	"net/http"
	"os"
	"os/signal"
	"syscall"
)

type config struct {
	Msg string
}

var conf = &config{Msg: "Hello World"}

func main() {
	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		w.Write(([]byte(conf.Msg)))
	})

	sigs := make(chan os.Signal, 1)

	signal.Notify(sigs, syscall.SIGHUP)
	go http.ListenAndServe(":8000", nil)
	fmt.Println("Program PID:", os.Getpid())
	for {
		// blocking if no default
		select {
		case <-sigs:
			conf.Msg = "Go Go Go"
		}
	}
}
```

```bash
$ ./server &
Program PID: 17247
$ curl localhost:8000
Hello World
$ kill -SIGHUP 17247 
$ curl localhost:8000
Go Go Go
```

## Using a map as a Set

There are 2 possibilities.
The first one is using bool as value: it uses one byte in memory. But it is easier to read/understand.

```Go
intSet := map[int]bool{}

if intSet[100] {
  print("100 is in the Set")
}
```

The second one is using empty struct as value: it uses 0 byte in memory but is a bit trickier.

```Go
intSet := map[int]struct{}{}

if _, ok := intSet[100]; ok {
  print("100 is in the Set")
}
```


## Benchmark in Go

Functions start with 'Benchmark'.

```bash
# default, runs using all CPUs available. Otherwise, -cpu=X
go test -bench=.
# -count X -> runs X times each benchmark function
# -benchmem -> include memory allocation statistics
```

Output format


```bash
BenchmarkFunctionName-<number-of-CPU> <number-of-execution> <speed-of-each-operation>
# number-of-execution = b.N
```