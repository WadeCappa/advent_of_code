
[file, its | _] = System.argv
its = String.to_integer(its)
IO.puts file
IO.puts its

stones = Day11.readStones(file)

{:ok, pid} = GenServer.start_link(MemoServer, %{})
getter = fn key -> GenServer.call(pid, {:get, key}) end
setter = fn key, value -> GenServer.call(pid, {:put, key, value}) end

Day11.countStonesAfterBlinks(stones, its, getter, setter)
  |> IO.inspect()
