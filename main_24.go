package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"regexp"
	"strings"
)

type Position struct {
	X int
	Y int
}

func main() {
	input := `sesenwnenenewseeswwswswwnenewsewsw
neeenesenwnwwswnenewnwwsewnenwseswesw
seswneswswsenwwnwse
nwnwneseeswswnenewneswwnewseswneseene
swweswneswnenwsewnwneneseenw
eesenwseswswnenwswnwnwsewwnwsene
sewnenenenesenwsewnenwwwse
wenwwweseeeweswwwnwwe
wsweesenenewnwwnwsenewsenwwsesesenwne
neeswseenwwswnwswswnw
nenwswwsewswnenenewsenwsenwnesesenew
enewnwewneswsewnwswenweswnenwsenwsw
sweneswneswneneenwnewenewwneswswnese
swwesenesewenwneswnwwneseswwne
enesenwswwswneneswsenwnewswseenwsese
wnwnesenesenenwwnenwsewesewsesesew
nenewswnwewswnenesenwnesewesw
eneswnwswnwsenenwnwnwwseeswneewsenese
neswnwewnwnwseenwseesewsenwsweewe
wseweeenwnesenwwwswnew`

	b, err := ioutil.ReadFile("input_24.txt")
	if err != nil {
		log.Fatal(err)
	}
	input = string(b)
	r, err := regexp.Compile("e|se|sw|w|nw|ne")
	if err != nil {
		log.Fatal(err)
	}
	lines := strings.Split(input, "\n")

	floor := make(map[Position]bool)
	positions := map[string]Position{
		"e":  Position{X: 2},
		"w":  Position{X: -2},
		"ne": Position{X: 1, Y: -1},
		"se": Position{X: 1, Y: 1},
		"nw": Position{X: -1, Y: -1},
		"sw": Position{X: -1, Y: 1},
	}

	for _, line := range lines {
		line = strings.TrimSpace(line)
		if len(line) == 0 {
			continue
		}
		var pos Position
		for _, dir := range r.FindAllStringSubmatch(line, -1) {
			p := positions[dir[0]]
			pos.X += p.X
			pos.Y += p.Y
		}
		if _, exists := floor[pos]; !exists {
			floor[pos] = true // White to black
		} else {
			floor[pos] = !floor[pos]
		}
	}
	var count int
	for _, black := range floor {
		if black {
			count++
		}
	}
	fmt.Println(count)

	adjacentBlackTiles := func(pos Position) int {
		var n int
		for _, p := range positions {
			pp := pos
			pp.X += p.X
			pp.Y += p.Y
			if floor[pp] {
				n++
			}
		}
		return n
	}
	for i := 0; i < 100; i++ {
		changes := make(map[Position]bool)
		recordChanges := func(pos Position, black bool) {
			n := adjacentBlackTiles(pos)
			if black && (n == 0 || n > 2) {
				changes[pos] = false
			} else if !black && n == 2 {
				changes[pos] = true
			}
		}

		for pos, black := range floor {
			recordChanges(pos, black)
			for _, p := range positions {
				pp := pos
				pp.X += p.X
				pp.Y += p.Y
				recordChanges(pp, floor[pp])
			}
		}
		for pos, black := range changes {
			floor[pos] = black
		}
		count = 0
		for _, black := range floor {
			if black {
				count++
			}
		}
		fmt.Println("Day", i+1, count)
	}
}
