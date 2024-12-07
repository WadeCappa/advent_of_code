package main

import (
	"bufio"
	"errors"
	"fmt"
	"os"
	"strings"
)

type Node struct {
	left  string
	right string
}

func getAdjacency(line string) (string, string, string) {
	split := strings.Split(line, " = ")
	adjacencies := strings.Split(split[1], ", ")
	return split[0], adjacencies[0][1:], adjacencies[1][:len(adjacencies[1])-1]
}

func getNextNode(node Node, move string) (string, error) {
	switch move {
	case "L":
		return node.left, nil
	case "R":
		return node.right, nil
	}

	return "", errors.New("unrecognized direction")
}

func getMovesToEnd(adjacencyList map[string]Node, moves string, start string, res chan int) {
	distance := 0
	p := 0
	node := start
	for !strings.Contains(node, "Z") {
		nextNode, error := getNextNode(adjacencyList[node], moves[p:p+1])
		if error != nil {
			fmt.Printf("encountered an error %s", error)
			return
		}

		node = nextNode
		distance += 1
		p = (p + 1) % len(moves)
	}

	res <- distance
}

func GCD(a, b int) int {
	for b != 0 {
		t := b
		b = a % b
		a = t
	}
	return a
}

func LCMForTwo(a, b int) int {
	return a * b / GCD(a, b)
}

func LCM(integers []int) int {
	a := integers[0]
	b := integers[1]
	result := LCMForTwo(a, b)

	for i := 2; i < len(integers); i++ {
		result = LCMForTwo(result, integers[i])
	}

	return result
}

func main() {
	file, _ := os.Open(os.Args[1])
	defer file.Close()

	var adjacencyList map[string]Node = make(map[string]Node)

	var count int = 0
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		var text string = scanner.Text()
		if count == 0 {
			count += 1
			continue
		}
		name, left, right := getAdjacency(text)
		adjacencyList[name] = Node{left, right}
	}

	moves := os.Args[2]
	var results []chan int
	for node := range adjacencyList {
		if strings.Contains(node, "A") {
			newChan := make(chan int)
			go getMovesToEnd(adjacencyList, moves, node, newChan)
			results = append(results, newChan)
		}
	}

	var nums []int
	for r := range results {
		num := <-results[r]
		nums = append(nums, num)
	}

	fmt.Printf("res of %d", LCM(nums))
}
