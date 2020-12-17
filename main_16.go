package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

type Range struct {
	lo int
	hi int
}

func NewRange(lo, hi int) Range {
	return Range{
		lo: lo,
		hi: hi,
	}
}

type Rule struct {
	name   string
	ranges []Range
}

func NewRule(name string, ranges []Range) Rule {
	return Rule{
		name:   name,
		ranges: ranges,
	}
}

func (r Rule) Or(n int) bool {
	for _, rng := range r.ranges {
		if n >= rng.lo && n <= rng.hi {
			return true
		}
	}
	return false
}

func main() {
	var sections int
	var rules []Rule
	var yourTicket []int
	var tickets [][]int
	validTickets := make(map[int]int)
	var columns []int

	parseRange := func(s string) Range {
		ranges := strings.Split(s, "-")
		lo, hi := ranges[0], ranges[1]
		l, err := strconv.Atoi(lo)
		if err != nil {
			log.Fatal(err)
		}
		h, err := strconv.Atoi(hi)
		if err != nil {
			log.Fatal(err)
		}
		return NewRange(l, h)
	}

	parseTickets := func(s []string) []int {
		tickets := make([]int, len(s))
		for i, ticket := range s {
			t, err := strconv.Atoi(ticket)
			if err != nil {
				log.Fatal(err)
			}
			tickets[i] = t
		}
		return tickets
	}

	f, err := os.Open("./input_16.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer f.Close()

	scanner := bufio.NewScanner(f)
	for scanner.Scan() {
		txt := scanner.Text()
		if txt == "" {
			continue
		}
		if strings.HasPrefix(txt, "your ticket:") || strings.HasPrefix(txt, "nearby tickets:") {
			sections++
			continue
		}

		switch sections {
		case 0:
			params := strings.Split(txt, ": ")
			name, rawRules := params[0], params[1]
			ranges := make([]Range, 2)
			for i, r := range strings.Split(rawRules, " or ") {
				ranges[i] = parseRange(r)
			}
			rules = append(rules, NewRule(name, ranges))
		case 1:
			yourTicket = parseTickets(strings.Split(txt, ","))
			tickets = append(tickets, yourTicket)
		case 2:
			tickets = append(tickets, parseTickets(strings.Split(txt, ",")))
		default:
		}
	}

	for i, rule := range rules {
		for _, rng := range rule.ranges {
			for j := rng.lo; j <= rng.hi; j++ {
				validTickets[j] |= (1 << i)
			}
		}
	}

	var errorRate int
	for _, ticket := range tickets {
		for _, no := range ticket {
			if _, ok := validTickets[no]; !ok {
				errorRate += no
			}
		}
	}
	fmt.Println("part 1: error rate is", errorRate)

	columns = make([]int, len(rules))

	// For each column set all rules to be valid.
	var allRules int
	for j := range rules {
		allRules |= (1 << j)
	}
	for i := range columns {
		columns[i] = allRules
	}

	for _, ticket := range tickets {
		var valid bool
		for _, no := range ticket {
			_, valid = validTickets[no]
			if valid {
				break
			}
		}
		if !valid {
			continue
		}

		// For each column, check which rules are not valid.
		for i, no := range ticket {
			bit, ok := validTickets[no]
			if !ok {
				continue
			}
			for j := range rules {
				b := 1 << j
				if bit&b != b {
					columns[i] &^= b
				}
			}
		}
	}

	columnMapping := make(map[int]string)
	for len(columnMapping) != len(rules) {
		for i, col := range columns {
			if _, ok := columnMapping[i]; ok {
				continue
			}
			var potentialColumns []Rule
			var k int
			for j := range rules {
				b := 1 << j
				if col&b == b {
					k = j
					potentialColumns = append(potentialColumns, rules[j])
					if len(potentialColumns) > 1 {
						break
					}
				}
			}
			if len(potentialColumns) == 1 {
				columnMapping[i] = potentialColumns[0].name
				for c := range columns {
					columns[c] &^= (1 << k)
				}
			}
		}
	}
	var result int
	for k, v := range columnMapping {
		if strings.HasPrefix(v, "departure") {
			if result == 0 {
				result = yourTicket[k]
			} else {
				result *= yourTicket[k]
			}
		}
	}
	fmt.Println("part 2:", result)
}
