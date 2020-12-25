package main

import (
	"fmt"
)

func main() {
	cardKey := 18499292
	doorKey := 8790390

	cardLoopSize := computeLoopSize(cardKey)
	doorLoopSize := computeLoopSize(doorKey)

	fmt.Println(transformSubjectNumber(cardLoopSize, doorKey))
	fmt.Println(transformSubjectNumber(doorLoopSize, cardKey))
}

func computeLoopSize(key int) int {
	subjectNumber := 7
	val := 1
	var loopSize int
	for val != key {
		loopSize++
		val *= subjectNumber
		val %= 20201227
	}
	return loopSize
}

func transformSubjectNumber(loopSize, subjectNumber int) int {
	val := 1
	for i := 0; i < loopSize; i++ {
		val *= subjectNumber
		val %= 20201227
	}
	return val
}
