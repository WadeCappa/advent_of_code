
defmodule Day3 do
     def getMul({s, l}, line) do
        v = String.slice(line, s+4..s+l-2)
            |> String.split(",")
            |> Enum.reduce(1, fn x, t -> t * String.to_integer(x) end)
        {s, v}
    end

    def getMul([{s, l}], line) do
        getMul({s, l}, line)
    end

    def getMuls(muls, line) do
        muls
            |> Enum.map(fn m ->
                getMul(m, line)
            end)
    end

    def input() do
        file = "input.txt"
        IO.puts part1(file)
        IO.puts part2(file)
    end

    def toy() do
        file = "toy.txt"
        IO.puts part1(file)
        IO.puts part2(file)
    end

    def part1(path) do
        mul_ops = ~r/mul\(\d{1,3},\d{1,3}\)/
        input = File.stream!(path)
            |> Enum.reduce(fn l, lines -> lines <> l end)
        mul_idx = Regex.scan(mul_ops, input, return: :index, capture: :first)
        getMuls(mul_idx, input)
            |> Enum.reduce(0, fn {_, v}, t -> v + t end)
    end

    def resumeAtIndex(line, i) do
        String.slice(line, i + 1..-1//1)
    end

    def getSum("", _addNext) do
        0
    end

    def getSum(input, addNext) do
        if addNext do
            dont_i = case Regex.run(~r/don't\(\)/, input, return: :index, capture: :first) do
                [{dont_i, _}] -> dont_i
                nil -> String.length(input)
            end
            {mul_i, mul_l} = case Regex.run(~r/mul\(\d{1,3},\d{1,3}\)/, input, return: :index, capture: :first) do
                [{mul_i, mul_l}] -> {mul_i, mul_l}
                nil -> {String.length(input), 0}
            end
            if dont_i <= mul_i do
                getSum(resumeAtIndex(input, dont_i), false)
            else
                {i, v} = getMul({mul_i, mul_l}, input)
                v + getSum(resumeAtIndex(input, i), true)
            end
        else
            i = case Regex.run(~r/do\(\)/, input, return: :index, capture: :first) do
                [{i, _}] -> i
                nil -> String.length(input)
            end
            getSum(resumeAtIndex(input, i), true)
        end
    end

    def part2(path) do
        input = File.stream!(path)
            |> Enum.reduce(fn l, lines -> lines <> l end)
        getSum(input, true)
    end
end
