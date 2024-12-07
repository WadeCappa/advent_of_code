defmodule Day1 do

    def asInts(line) do
        [l, r] = String.split(String.trim(line), "   ")
        {String.to_integer(l), String.to_integer(r)}
    end

    def input() do
        part1("input.txt")
        part2("input.txt")
    end

    def toy() do
        part1("toy.txt")
        part2("toy.txt")
    end

    def part1(path) do
        File.stream!(path)
            |> Stream.map(fn line -> asInts(line) end)
            |> Enum.unzip()
            |> then(fn {l, r} ->
                Enum.zip(Enum.sort(l), Enum.sort(r))
            end)
            |> Enum.reduce(0, fn {l, r}, total ->
                total + abs(l - r)
            end)
    end

    def part2(path) do
        File.stream!(path)
            |> Stream.map(fn line -> asInts(line) end)
            |> Enum.unzip()
            |> then(fn {l, r} ->
                f = Enum.frequencies(r)
                Enum.reduce(l, 0, fn v, total ->
                    total + (v * Map.get(f, v, 0))
                end)
            end)
    end
end
