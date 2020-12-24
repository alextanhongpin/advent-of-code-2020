package main

import (
	"fmt"
	"log"
	"strconv"
	"strings"
)

func main() {
	input1 := `Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10`
	input2 := `Player 1:
28
50
9
11
4
45
19
26
42
43
31
46
21
40
33
20
7
6
17
44
5
39
35
27
10

Player 2:
18
16
29
41
14
12
30
37
36
24
48
38
47
34
15
8
49
23
1
3
32
25
22
13
2`

	a, b := parseInput(input2)
	for len(a) > 0 && len(b) > 0 {
		if a[0] > b[0] {
			a = append(a, a[0], b[0])
		} else {
			b = append(b, b[0], a[0])
		}
		a = a[1:]
		b = b[1:]
	}

	computeScore := func(in []int) int {
		var total int
		for i, n := range in {
			total += (len(in) - i) * n
		}
		return total
	}

	if len(a) > 0 {
		fmt.Println("Part 1:", computeScore(a))
	} else {
		fmt.Println("Part 1:", computeScore(b))
	}
	_ = input1
	c, d := parseInput(input2)

	var recursiveCombat func(a, b []int) (result []int, p1 bool)
	recursiveCombat = func(a, b []int) ([]int, bool) {
		cache := NewCache()
		for len(a) > 0 && len(b) > 0 {
			key := fmt.Sprintf("%v-%v", a, b)
			if cache.Has(key) {
				return a, true
			}
			cache.Set(key, nil)

			var isA bool
			if len(a)-1 >= a[0] && len(b)-1 >= b[0] {
				anew := clone(a[1 : a[0]+1])
				bnew := clone(b[1 : b[0]+1])
				_, isA = recursiveCombat(anew, bnew)
			} else {
				isA = a[0] > b[0]
			}

			if isA {
				a = append(a, a[0], b[0])
			} else {
				b = append(b, b[0], a[0])
			}
			a = a[1:]
			b = b[1:]
		}

		if len(a) == 0 {
			return b, false
		}
		return a, true
	}
	winner, _ := recursiveCombat(c, d)
	fmt.Println("Part two:", computeScore(winner))
}

func clone(in []int) []int {
	result := make([]int, len(in))
	for i, n := range in {
		result[i] = n
	}
	return result
}

type Cache struct {
	data map[string]interface{}
}

func NewCache() *Cache {
	return &Cache{
		data: make(map[string]interface{}),
	}
}

func (c *Cache) Set(key string, value interface{}) bool {
	if _, exists := c.data[key]; exists {
		return false
	}
	c.data[key] = value
	return true
}

func (c *Cache) Has(key string) bool {
	_, exists := c.data[key]
	return exists
}

func parseInput(in string) ([]int, []int) {
	var a, b []int
	var next int
	lines := strings.Split(in, "\n")
	for _, line := range lines {
		line = strings.TrimSpace(line)
		if line == "" {
			continue
		}

		if strings.HasPrefix(line, "Player") {
			next++
			continue
		}
		n, err := strconv.Atoi(line)
		if err != nil {
			log.Fatal(err)
		}
		if next == 1 {
			a = append(a, n)
		}
		if next == 2 {
			b = append(b, n)
		}
	}
	return a, b
}
