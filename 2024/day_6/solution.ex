defmodule Day6 do

  def getStart(map) do
    map
      |> Enum.reduce({0, 0}, fn {{y, x}, v}, s ->
        case v == "^" do
          true -> {y, x}
          false -> s
        end
      end)
  end

  def bumpDirection(d) do
    case d do
      {-1, 0} -> {0, 1}
      {0, 1} -> {1, 0}
      {1, 0} -> {0, -1}
      {0, -1} -> {-1, 0}
    end
  end

  def nextDir(map, {y, x}, {dy, dx}) do
    case Map.get(map, {y + dy, x + dx}, "X") do
      "#" -> nextDir(map, {y, x}, bumpDirection({dy, dx}))
      _ -> {dy, dx}
    end
  end

  def takeStep(map, {y, x}, {dy, dx}) do
    case Map.get(map, {y + dy, x + dx}, "X") do
      "X" -> :done
      "#" -> takeStep(map, {y, x}, nextDir(map, {y, x}, {dy, dx}))
      _ -> {{y + dy, x + dx}, {dy, dx}}
    end
  end

  def getPath(map, path, p, d) do
    case takeStep(map, p, d) do
      :done -> path
      {p, d} -> getPath(map, Map.put(path, p, 0), p, d)
    end
  end

  def checkIfLoop(map, seen, p, d) do
    if Map.has_key?(seen, {p, d}) do
      true
    else
      case takeStep(map, p, d) do
        :done -> false
        {new_p, new_d} -> checkIfLoop(map, Map.put(seen, {p, d}, 0), new_p, new_d)
      end
    end
  end

  def asMap(strings) do
    String.split(strings, "\n")
      |> Enum.with_index()
      |> Enum.map(fn {line, y} ->
        line
          |> String.graphemes()
          |> Enum.with_index()
          |> Enum.reduce(%{}, fn {v, x}, acc -> Map.put(acc, {y, x}, v) end)
      end)
      |> Enum.reduce(%{}, fn line, acc -> Map.merge(line, acc) end)
  end

  def run(file) do
    map = case File.read(file) do
      {:ok, contents} -> asMap(contents)
    end

    start = getStart(map)
    path = getPath(map, %{start => 0}, start, {-1, 0})
    IO.puts Kernel.map_size(path)

    Map.keys(path)
      |> Task.async_stream(fn p -> checkIfLoop(Map.replace(map, p, "#"), %{}, start, {-1, 0}) end)
      |> Enum.filter(fn {:ok, v} -> v end)
      |> then(fn validCoords -> length(validCoords) end)
  end
end
