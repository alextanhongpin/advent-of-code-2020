package main

import (
	"fmt"
	"log"
	"strconv"
	"strings"
)

func main() {
	{
		cups := parseInput("389125467")
		n := 10
		node := solver(cups, n)
		fmt.Println(partOne(node, len(cups)-1)) // 92658374
	}
	{
		// Part one.
		cups := parseInput("418976235")
		n := 100
		node := solver(cups, n)
		fmt.Println(partOne(node, len(cups)-1)) // 96342875
	}

	// Part two.
	{
		initials := parseInput("389125467")
		n := 1_000_000 // 1 million.
		cups := make([]int, n)
		for i := 0; i < n; i++ {
			if i < len(initials) {
				cups[i] = initials[i]
			} else {
				cups[i] = i + 1
			}
		}
		node := solver(cups, n*10)
		fmt.Println(partTwo(node))
	}

	{
		initials := parseInput("418976235")
		n := 1_000_000 // 1 million.
		cups := make([]int, n)
		for i := 0; i < n; i++ {
			if i < len(initials) {
				cups[i] = initials[i]
			} else {
				cups[i] = i + 1
			}
		}
		node := solver(cups, n*10)
		fmt.Println(partTwo(node))
	}
}

func solver(cups []int, n int) *Node {
	cache := make(map[int]*Node)
	var head, tail *Node
	var max int
	for i := 0; i < len(cups); i++ {
		n := cups[i]
		if n > max {
			max = n
		}
		if tail == nil {
			head = NewNode(n)
			tail = head
		} else {
			tail.Next = NewNode(n)
			tail.Next.Prev = tail
			tail = tail.Next
		}
		cache[tail.Data] = tail
	}

	tail.Next = head
	head.Prev = tail

	for i := 0; i < n; i++ {
		curr := head
		dst := curr.Data - 1

		set := make(map[int]bool)
		pickUpTailNode := curr
		for i := 0; i < 3; i++ {
			pickUpTailNode = pickUpTailNode.Next
			set[pickUpTailNode.Data] = true
		}
		if dst == 0 {
			dst = max
		}
		if set[dst] {
			for set[dst] {
				dst--
				if dst == 0 {
					dst = max
				}
			}
		}

		pickUpHeadNode := curr.Next
		curr.Next = pickUpTailNode.Next
		pickUpTailNode.Next.Prev = curr

		curr = cache[dst]

		tailNode := curr.Next
		curr.Next = pickUpHeadNode
		pickUpHeadNode.Prev = curr

		pickUpTailNode.Next = tailNode
		tailNode.Prev = pickUpTailNode
		head = head.Next
	}

	return cache[1]
}

func partOne(head *Node, n int) []int {
	result := make([]int, n)
	for i := 0; i < n; i++ {
		head = head.Next
		result[i] = head.Data
	}
	return result
}

func partTwo(node *Node) int {
	for node.Data != 1 {
		node = node.Next
	}
	return node.Next.Data * node.Next.Next.Data

}

type Node struct {
	Next *Node
	Prev *Node
	Data int
}

func NewNode(n int) *Node {
	return &Node{
		Data: n,
	}
}

func parseInput(in string) []int {
	numbers := strings.Split(in, "")
	result := make([]int, len(numbers))
	for i, n := range numbers {
		var err error
		result[i], err = strconv.Atoi(n)
		if err != nil {
			log.Fatal(err)
		}
	}
	return result
}
