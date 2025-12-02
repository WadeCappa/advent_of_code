package main

import (
	"bufio"
	"fmt"
	"iter"
	"os"
)

const (
	ROBOT     = '@'
	WALL      = '#'
	BOX_LEFT  = '['
	BOX_RIGHT = ']'
)

type Warehouse [][]rune

type point struct {
	y int
	x int
}

func (w Warehouse) swap(p1, p2 point) {
	v := w[p1.y][p1.x]
	w[p1.y][p1.x] = w[p2.y][p2.x]
	w[p2.y][p2.x] = v
}

func (w Warehouse) moveTo(p point, dy, dx int) (moved bool) {
	if dy == 0 {
		return w.moveHorizontal(p, dy, dx)
	}
	return w.maybeMoveVertical(p, dy, dx)
}

func (w Warehouse) moveHorizontal(p point, dy, dx int) (moved bool) {
	next := w[p.y+dy][p.x+dx]
	nextPoint := point{p.y + dy, p.x + dx}
	if next == WALL {
		return false
	}
	if next == BOX_LEFT || next == BOX_RIGHT {
		if w.moveHorizontal(nextPoint, dy, dx) {
			w.swap(p, nextPoint)
			return true
		}
		return false
	}
	w.swap(p, nextPoint)
	return true
}

func (w Warehouse) maybeMoveVertical(p point, dy, dx int) (moved bool) {
	if w.touchesWall(p, dy, dx) {
		return false
	}

	return w.moveVertical(p, dy, dx)
}

func (w Warehouse) moveVertical(p point, dy, dx int) (moved bool) {
	next := w[p.y+dy][p.x+dx]
	nextPoint := point{p.y + dy, p.x + dx}
	if next == WALL {
		return false
	}
	if next == BOX_LEFT {
		if w.moveVertical(nextPoint, dy, dx) && w.moveVertical(point{nextPoint.y, nextPoint.x + 1}, dy, dx) {
			w.swap(p, nextPoint)
			return true
		}
		return false
	}
	if next == BOX_RIGHT {
		if w.moveVertical(nextPoint, dy, dx) && w.moveVertical(point{nextPoint.y, nextPoint.x - 1}, dy, dx) {
			w.swap(p, nextPoint)
			return true
		}
		return false
	}
	w.swap(p, nextPoint)
	return true
}

func (w Warehouse) touchesWall(p point, dy, dx int) bool {
	next := w[p.y+dy][p.x+dx]
	nextPoint := point{p.y + dy, p.x + dx}
	if next == WALL {
		return true
	}
	if next == BOX_LEFT {
		return w.touchesWall(nextPoint, dy, dx) || w.touchesWall(point{nextPoint.y, nextPoint.x + 1}, dy, dx)
	}
	if next == BOX_RIGHT {
		return w.touchesWall(nextPoint, dy, dx) || w.touchesWall(point{nextPoint.y, nextPoint.x - 1}, dy, dx)
	}
	return false
}

func main() {
	file := os.Args[1]
	reader, err := os.Open(file)
	if err != nil {
		panic(err)
	}
	defer reader.Close()

	scanner := bufio.NewScanner(reader)

	warehouse, robot := buildWarehouse(scanner)
	for _, line := range warehouse {
		fmt.Println(string(line))
	}
	fmt.Println(sumBoxes(warehouse))

	moves := getMoves(scanner)
	for dy, dx := range moves {
		if warehouse.moveTo(robot, dy, dx) {
			robot = point{robot.y + dy, robot.x + dx}
		}
		for _, line := range warehouse {
			fmt.Println(string(line))
		}
		fmt.Printf("robot at %d %d\n", robot.y, robot.x)
	}

	if err := scanner.Err(); err != nil {
		panic(err)
	}
	for _, line := range warehouse {
		fmt.Println(string(line))
	}

	fmt.Println(sumBoxes(warehouse))
}

func buildWarehouse(scanner *bufio.Scanner) (warehouse Warehouse, robot point) {
	robot = point{0, 0}
	var result [][]rune
	for scanner.Scan() {
		line := scanner.Text()
		if line == "" {
			break
		}
		row := make([]rune, len(line)*2)
		for i, c := range line {
			if c == 'O' {
				row[i*2] = BOX_LEFT
				row[i*2+1] = BOX_RIGHT
				continue
			}
			if c == ROBOT {
				robot = point{len(result), i * 2}
				row[i*2] = ROBOT
				row[i*2+1] = '.'
				continue
			}
			row[i*2] = c
			row[i*2+1] = c
		}
		result = append(result, row)
	}
	return result, robot
}

func getMoves(scanner *bufio.Scanner) iter.Seq2[int, int] {
	return func(yield func(int, int) bool) {
		for scanner.Scan() {
			line := scanner.Text()
			for _, c := range line {
				if !yield(getMovesFromRune(c)) {
					return
				}
			}
		}
	}
}

func getMovesFromRune(move rune) (dy int, dx int) {
	switch move {
	case '<':
		return 0, -1
	case '^':
		return -1, 0
	case '>':
		return 0, 1
	case 'v':
		return 1, 0
	}
	panic("unexpected rune")
}

func sumBoxes(w Warehouse) uint64 {
	result := uint64(0)
	for y, line := range w {
		for x, r := range line {
			if r != BOX_LEFT {
				continue
			}
			result += uint64(100*y + x)
		}
	}
	return result
}
