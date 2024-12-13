defmodule Day11 do
  def initMemoTable do
    :ets.new(:blink_table, [:named_table, :set, :public])
  end

  def readStones(file) do
    case File.read(file) do
      {:ok, stones} -> stones
        |> String.trim()
        |> String.split(" ")
        |> Enum.map(fn x -> String.to_integer(x) end)
    end
  end

  def blink(stone) do
    s = Integer.to_string(stone)
    l = String.length(s)
    if stone == 0 do
      [1]
    else
      if rem(l, 2) == 0 do
        m = div(String.length(s), 2)
        [String.slice(s, 0..m-1), String.slice(s, m..l)]
          |> Enum.map(fn x -> String.to_integer(x) end)
      else
        [stone * 2024]
      end
    end
  end

  def dfs(stone, its) do
    key = {stone, its}
    case :ets.lookup(:blink_table, key) do
      [{^key, result}] -> result
      [] ->
        result = if its == 0 do
          1
        else
          blink(stone)
            |> Enum.map(fn s -> dfs(s, its - 1) end)
            |> Enum.reduce(fn stones, acc -> stones + acc end)
        end

        :ets.insert(:blink_table, {key, result})
        result
    end
  end

  def countStonesAfterBlinks(stones, its) do
    stones
      |> Enum.map(fn s -> dfs(s, its) end)
      |> Enum.reduce(fn stones, acc -> stones + acc end)
  end
end

[file, its | _] = System.argv
its = String.to_integer(its)
IO.puts file
IO.puts its

stones = Day11.readStones(file)

Day11.initMemoTable()
Day11.countStonesAfterBlinks(stones, its) |> IO.inspect()
