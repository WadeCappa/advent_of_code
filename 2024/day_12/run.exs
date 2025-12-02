
[file | _] = System.argv

map = Day12.getMap(file)
regions = Day12.getRegions(map)
  |> IO.inspect()

regions
  |> Enum.map(fn r -> Day12.getCost(r) end)
  |> IO.inspect()
  |> Map.reduce(0, fn c, acc -> c + acc end)
  |> IO.inspect()

# {timeInMicros, res} = :timer.tc fn ->  end
# IO.inspect(timeInMicros / 1_000_000)
# IO.inspect(res)
