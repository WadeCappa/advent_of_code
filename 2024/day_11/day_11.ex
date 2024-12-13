defmodule Day11 do
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

  def dfs(stone, its, getMemo, setMemo) do
    key = {stone, its}
    case getMemo.(key) do
      :miss ->
        result = if its == 0 do
          1
        else
          blink(stone)
            |> Enum.map(fn s -> dfs(s, its - 1, getMemo, setMemo) end)
            |> Enum.reduce(fn stones, acc -> stones + acc end)
        end

        setMemo.(key, result)
        result
      result -> result
    end
  end

  def countStonesAfterBlinks(stones, its, getMemo, setMemo) do
    stones
      |> Enum.map(fn s -> dfs(s, its, getMemo, setMemo) end)
      |> Enum.reduce(fn stones, acc -> stones + acc end)
  end
end
