defmodule Aoc2 do
    def asTrend([], _) do
        [:stop]
    end

    def asTrend([n | rest], :start) do
        [:start | asTrend(rest, n)]
    end

    def asTrend([n | rest], last) do
        trend = cond do
            last - n >= 1 and last - n <= 3 ->
                :dec
            n - last >= 1 and n - last <= 3 ->
                :asc
            true ->
                :invalid
        end
        [trend | asTrend(rest, n)]
    end

    def isSafeWithSkip(level) do
        withIndex = Enum.with_index(level)
        withIndex
            |> Enum.map(fn {_, i} ->
                withIndex
                    |> Enum.filter(fn {_, j} -> i != j end)
                    |> Enum.map(fn {v, _} -> v end)
                    |> isSafe()
            end)
            |> Enum.reduce(false, fn isSafe, acc -> acc or isSafe end)
    end

    def isSafe(level) do
        trend = level
            |> asTrend(:start)
            |> Enum.reduce(:start, fn trend, lastTrend ->
                cond do
                    lastTrend == :start and trend == :start ->
                        :start
                    lastTrend == :start ->
                        trend
                    trend == lastTrend ->
                        trend
                    trend == :stop ->
                        lastTrend
                    true ->
                        :invalid
                end
            end)
        cond do
            trend == :dec or trend == :asc -> true
            true -> false
        end
    end

    def part2(path) do
        File.stream!(path)
            |> Stream.map(fn line ->
                line
                    |> String.trim()
                    |> String.split(" ")
                    |> Enum.map(fn l -> String.to_integer(l) end)
                    |> then(fn level -> isSafeWithSkip(level) end)
            end)
            |> Enum.reduce(0, fn level, t ->
                t + if level, do: 1, else: 0
            end)
    end

    def part1(path) do
        File.stream!(path)
            |> Stream.map(fn line ->
                line
                    |> String.trim()
                    |> String.split(" ")
                    |> Enum.map(fn l -> String.to_integer(l) end)
                    |> then(fn level -> isSafe(level) end)
            end)
            |> Enum.reduce(0, fn level, t ->
                t + if level, do: 1, else: 0
            end)
    end
end
