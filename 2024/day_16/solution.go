package main

import (
	"bufio"
	"fmt"
	"iter"
	"math"
	"os"
)

type direction rune

const (
	START = 'S'
	END   = 'E'
	WALL  = '#'

	UP    direction = '^'
	LEFT  direction = '<'
	RIGHT direction = '>'
	DOWN  direction = 'v'
)

type point struct {
	y int
	x int
}

func main() {
	file := os.Args[1]
	f, err := os.Open(file)
	if err != nil {
		panic(err)
	}
	defer f.Close()

	scanner := bufio.NewScanner(f)
	var maze []string
	for scanner.Scan() {
		line := scanner.Text()
		maze = append(maze, line)
	}
	for _, line := range maze {
		fmt.Println(line)
	}
	start := findStart(maze)
	res := doDfs(maze, start, RIGHT)
	fmt.Println(res)
}

func findStart(maze []string) point {
	for y, line := range maze {
		for x, c := range line {
			if c == START {
				return point{y, x}
			}
		}
	}
	panic("failed to find start")
}

func getDirections(d direction) iter.Seq[direction] {
	switch d {
	case UP, DOWN:
		return func(yield func(direction) bool) {
			if !yield(LEFT) || !yield(RIGHT) {
				return
			}
		}
	case LEFT, RIGHT:
		return func(yield func(direction) bool) {
			if !yield(UP) || !yield(DOWN) {
				return
			}
		}
	}
	panic("unexpected direction")
}

func getDyDx(d direction) (dy int, dx int) {
	switch d {
	case UP:
		return -1, 0
	case DOWN:
		return 1, 0
	case LEFT:
		return 0, -1
	case RIGHT:
		return 0, 1
	}
	panic("unexpected direction")
}

func dfs(seen map[string]uint64, maze []string, start point, d direction, score uint64) uint64 {
	if maze[start.y][start.x] == WALL {
		return math.MaxUint64
	}
	if maze[start.y][start.x] == END {
		return score
	}
	index := fmt.Sprintf("%d.%d.%c", start.y, start.x, d)
	previousScore, exists := seen[index]
	if exists && previousScore <= score {
		return math.MaxUint64
	}
	seen[index] = score
	bestScore := uint64(math.MaxUint64)
	for next := range getDirections(d) {
		bestScore = min(bestScore, dfs(seen, maze, start, next, score+1000))
	}

	dy, dx := getDyDx(d)
	bestScore = min(bestScore, dfs(seen, maze, point{start.y + dy, start.x + dx}, d, score+1))
	return bestScore
}

func doDfs(maze []string, start point, d direction) (minimumScore uint64) {
	seen := map[string]uint64{}
	return dfs(seen, maze, start, d, 0)
}
