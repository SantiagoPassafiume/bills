package main

import "fmt"

func main() {
	myBill := newBill("Mario's bill")

	myBill.format()

	fmt.Println(myBill.format())
}
