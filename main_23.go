package main

import (
	"fmt"
	"log"
	"strconv"
	"strings"
)

func main() {
	// The problem can be solved by using reverse linked list.
	// The property of the solution (each number can represent an index in an array, starting from 1, not zero)
	// allows efficient usage of array.
	// In the input below, "38...", to map 3 to 8, we set the array[3] = 8
	{
		input := "389125467"
		cups := strToIntSlice(input)
		visualize(solver(cups, 10), len(cups)-1)
	}

	{
		input := "418976235"
		cups := strToIntSlice(input)
		visualize(solver(cups, 100), len(cups)-1)
	}

	{
		input := "389125467"
		initials := strToIntSlice(input)
		n := 1_000_000
		cups := make([]int, n)
		for i := 0; i < n; i++ {
			if i < len(initials) {
				cups[i] = initials[i]
			} else {
				cups[i] = i + 1
			}
		}
		linkedList := solver(cups, n*10)
		a := linkedList[1]
		b := linkedList[a]
		fmt.Println(a, b, a*b)
	}

	{
		input := "418976235"
		initials := strToIntSlice(input)
		n := 1_000_000
		cups := make([]int, n)
		for i := 0; i < n; i++ {
			if i < len(initials) {
				cups[i] = initials[i]
			} else {
				cups[i] = i + 1
			}
		}
		linkedList := solver(cups, n*10)
		a := linkedList[1]
		b := linkedList[a]
		fmt.Println(a, b, a*b)
	}
}

func solver(cups []int, n int) []int {
	linkedList := make([]int, len(cups)+1)

	var max int
	for i := 1; i < len(cups)+1; i++ {
		if cups[i-1] > max {
			max = cups[i-1]
		}
		linkedList[cups[i-1]] = cups[i%len(cups)]
	}

	curr := cups[0]
	for i := 0; i < n; i++ {
		a := linkedList[curr]
		b := linkedList[a]
		c := linkedList[b]
		dst := curr - 1
		if dst == 0 {
			dst = max
		}
		for dst == a || dst == b || dst == c {
			dst--
			if dst == 0 {
				dst = max
			}
		}

		linkedList[curr] = linkedList[c]
		d := linkedList[dst]
		linkedList[dst] = a
		linkedList[c] = d
		curr = linkedList[curr]
	}
	return linkedList
}

func visualize(ll []int, n int) {
	var result []int
	var curr = 1
	for i := 0; i < n; i++ {
		result = append(result, ll[curr])
		curr = ll[curr]
	}
	fmt.Println(result)
}

func strToIntSlice(in string) []int {
	result := make([]int, len(in))
	for i, s := range strings.Split(in, "") {
		n, err := strconv.Atoi(s)
		if err != nil {
			log.Fatal(err)
		}
		result[i] = n
	}
	return result
}
