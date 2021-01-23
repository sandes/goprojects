package main

import "C"
import (
	"sync"
)

var count string
var mtx sync.Mutex

//export findLower
func findLower(a []int) (response int) {

	var low int = a[0]

	for _, v := range a {
		if v < low {
			low = v
		}
	}

	return low

}

func main() {

	//fmt.Println(Add())

}
