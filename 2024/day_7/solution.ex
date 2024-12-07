defmodule Day7 do
  def parse(line) do
    [ans, nums] = String.split(line, ":")
    {String.to_integer(ans), nums |> String.trim() |> String.split() |> Enum.map(fn n -> String.to_integer(n) end)}
  end

  def dfs([], total, ans) do
    total == ans
  end

  def dfs([next | remaining], total, ans) do
    mul = fn n, t -> t * n end
    add = fn n, t -> t + n end
    concat = fn n, t -> String.to_integer(Integer.to_string(t) <> Integer.to_string(n)) end

    [mul, add, concat]
      |> Enum.map(fn op -> dfs(remaining, op.(next, total), ans) end)
      |> Enum.reduce(false, fn v, acc -> v or acc end)
  end

  def isPossible({ans, nums}) do
    [first | remaining] = nums
    dfs(remaining, first, ans)
  end

  def run(file) do
    File.stream!(file)
      |> Stream.map(fn line -> parse(line) end)
      |> Stream.filter(fn v -> isPossible(v) end)
      |> Stream.map(fn {ans, _} -> ans end)
      |> Enum.reduce(0, fn ans, acc -> ans + acc end)
  end
end
