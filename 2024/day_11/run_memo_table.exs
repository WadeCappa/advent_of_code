
[file, its | _] = System.argv
its = String.to_integer(its)
IO.puts file
IO.puts its

stones = Day11.readStones(file)

MemoTable.initMemoTable()
getter = fn key -> MemoTable.fetch(key) end
setter = fn key, value -> MemoTable.set(key, value) end

Day11.countStonesAfterBlinks(stones, its, getter, setter)
  |> IO.inspect()
