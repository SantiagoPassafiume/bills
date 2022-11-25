package main

import "fmt"

func main() {
	myBill := newBill("Mario's bill")

	myBill.addItem("onion soup", 4.50)
	myBill.updateTip(10)

	fmt.Println(myBill.format())

}
