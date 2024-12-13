
[file, its | _] = System.argv
its = String.to_integer(its)
IO.puts file
IO.puts its

stones = Day11.readStones(file)

getter = fn _key -> :miss end
setter = fn _key, _value -> :ok end

{timeInMicros, res} = :timer.tc fn -> Day11.countStonesAfterBlinks(stones, its, getter, setter) end
IO.inspect(timeInMicros / 1_000_000)
IO.inspect(res)
