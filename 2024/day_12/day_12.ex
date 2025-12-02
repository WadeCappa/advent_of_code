defmodule Day12 do
  defp getRegion(map, {j, i}, c, seen, region) do
    case Map.has_key?(seen, {j, i}) do
      true -> {seen, region}
      false ->
        case Map.get(map, {j, i}) do
          ^c ->
            newSeen = Map.put(seen, {j, i}, :none)
            newRegion = Map.put(region, {j, i}, :none)
            [{1, 0}, {0, 1}, {-1, 0}, {0, -1}]
              |> Enum.map(fn {dy, dx} -> getRegion(map, {j + dy, i + dx}, c, newSeen, newRegion) end)
              |> Enum.reduce({%{}, %{}}, fn {lastSeen, lastRegion}, {accSeen, accRegion} ->
                {Map.merge(accSeen, lastSeen), Map.merge(accRegion, lastRegion)}
              end)
          _ -> {seen, region}
        end
    end
  end

  def getMap(file) do
    {:ok, content} = File.read(file)
    content
      |> String.trim()
      |> String.split("\n")
      |> Enum.with_index()
      |> Enum.map(fn {line, j} ->
        line
          |> String.graphemes()
          |> Enum.with_index()
          |> Enum.reduce(%{}, fn {c, i}, acc -> Map.put(acc, {j, i}, c) end)
      end)
      |> Enum.reduce(%{}, fn l, acc -> Map.merge(l, acc) end)
  end

  def getRegions(map) do
    map
      |> Map.keys()
      |> Enum.reduce({%{}, %{}}, fn p, {seen, regions} ->
        case Map.has_key?(seen, p) do
          true -> {seen, regions}
          false ->
            {newSeen, newRegion} = getRegion(map, p, Map.get(map, p), seen, %{})
            {Map.merge(newSeen, seen), Map.put(regions, p, newRegion)}
        end
      end)
  end

  defp getPerimeter(region) do
    region
      |> Map.keys()
      |> Enum.reduce(0, fn {j, i}, acc ->
        acc + [{1, 0}, {0, 1}, {-1, 0}, {0, -1}]
          |> Enum.map(fn {dy, dx} ->
            case Map.has_key?(region, {j + dy, i + dx}) do
              true -> 0
              false -> 1
            end
          end)
          |> Enum.reduce(0, fn c, acc -> c + acc end)
      end)
  end

  def getCost(region) do
    length(Map.keys(region)) * getPerimeter(region)
  end
end
