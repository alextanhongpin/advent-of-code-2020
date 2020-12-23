package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"sort"
	"strings"
)

func main() {
	input := `mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)`
	b, err := ioutil.ReadFile("input_21.txt")
	if err != nil {
		log.Fatal(err)
	}
	_ = input
	input2 := string(b)
	ingredients, allergensMap := parseInput(input2)
	allergenSet := make(map[string]bool)

	allergens := make(map[string]string)

	for _, ingredients := range allergensMap {
		for ingredient := range ingredients {
			allergenSet[ingredient] = true
		}
	}

	var count int
	for _, ing := range ingredients {
		for k, v := range ing {
			if _, ok := allergenSet[k]; !ok {
				count += v
			}
		}
	}

	fmt.Printf("Part one: %d\n", count)

	for len(allergensMap) != len(allergens) {
		for allergen, ingredients := range allergensMap {
			if len(ingredients) == 1 {
				var ingredient string
				for i := range ingredients {
					ingredient = i
				}
				allergens[allergen] = ingredient
				for all, ing := range allergensMap {
					if all == allergen {
						continue
					}
					if _, exists := ing[ingredient]; exists {
						delete(ing, ingredient)
					}
				}
			}
		}
	}

	var a []string
	for allergen := range allergens {
		a = append(a, allergen)
	}
	sort.Strings(a)

	result := make([]string, len(a))
	for i, name := range a {
		result[i] = allergens[name]
	}
	fmt.Printf("Part two: %v\n", strings.Join(result, ","))
}

func intersectMap(a, b map[string]int) map[string]int {
	if len(b) > len(a) {
		return intersectMap(b, a)
	}
	m := make(map[string]int)
	for k := range a {
		if _, ok := b[k]; ok {
			m[k] = 1
		}
	}
	return m
}

func hasExact(str, tgt string) bool {
	for _, s := range strings.Fields(str) {
		if s == tgt {
			return true
		}
	}
	return false
}

func parseInput(input string) (map[string]map[string]int, map[string]map[string]int) {
	ingredients := make(map[string]map[string]int)
	allergensMap := make(map[string]map[string]int)

	for _, line := range strings.Split(input, "\n") {
		line = strings.TrimSpace(line)
		if line == "" {
			continue
		}
		line = strings.ReplaceAll(line, "(", "")
		line = strings.ReplaceAll(line, ")", "")
		line = strings.ReplaceAll(line, ",", "")

		parts := strings.Split(line, " contains ")

		allergens := strings.Fields(parts[1])
		sort.Strings(allergens)
		allKey := strings.Join(allergens, " ")

		ings := strings.Fields(parts[0])
		if m, exists := ingredients[allKey]; exists {
			for _, i := range ings {
				m[i]++
			}
		} else {
			m := make(map[string]int)
			for _, i := range ings {
				m[i]++
			}
			ingredients[allKey] = m
		}

		for _, allergen := range allergens {
			if _, exists := allergensMap[allergen]; !exists {
				allergensMap[allergen] = ingredients[allKey]
			} else {
				allergensMap[allergen] = intersectMap(allergensMap[allergen], ingredients[allKey])
			}
		}
	}
	return ingredients, allergensMap
}
