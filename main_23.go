package main

import (
	"fmt"
	"log"
	"strconv"
	"strings"
)

func main() {
	input := "389125467"
	input = "418976235"
	cups := parseInput(input)
	var move int
	for i := 0; i < 100; i++ {
		curr := cups[move]
		pickUp := pickN(cups, move, 3)
		available := exclude(cups, append(pickUp, curr))
		destination := curr - 1

		var hasDestination bool
		for !hasDestination {
			for _, n := range available {
				if n == destination {
					hasDestination = true
					break
				}
			}
			if !hasDestination {
				destination--
			}
			if destination < 0 {
				hasDestination = true
				destination = max(available)
			}
		}
		sepCups := exclude(cups, pickUp)
		dstIdx := findIndex(sepCups, destination)
		newCups := append([]int(nil), sepCups[:dstIdx+1]...)
		newCups = append(newCups, pickUp...)
		newCups = append(newCups, sepCups[dstIdx+1:]...)
		cups = newCups
		move = (findIndex(newCups, curr) + 1) % len(newCups)
	}
	idx := findIndex(cups, 1) + 1

	var n int
	for i := 0; i < len(cups)-1; i++ {
		n = (n * 10) + cups[(i+idx)%len(cups)]
	}
	fmt.Println(n)
}

func pickN(in []int, offset, n int) []int {
	result := make([]int, n)
	for i := 0; i < n; i++ {
		result[i] = in[(offset+1+i)%len(in)]
	}
	return result
}

func findIndex(in []int, t int) int {
	for i, n := range in {
		if n == t {
			return i
		}
	}
	return -1
}
func exclude(in []int, exclusion []int) []int {
	m := make(map[int]bool)
	for _, n := range exclusion {
		m[n] = true
	}
	var result []int
	for _, n := range in {
		if !m[n] {
			result = append(result, n)
		}
	}
	return result
}

func max(in []int) int {
	var result int
	for _, n := range in {
		if n > result {
			result = n
		}
	}
	return result
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
