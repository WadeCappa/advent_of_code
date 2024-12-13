defmodule MemoTable do
  def initMemoTable do
    :ets.new(:memo_table, [:named_table, :set, :private])
  end

  def fetch(key) do
    case :ets.lookup(:memo_table, key) do
      [{^key, result}] -> result
      [] -> :miss
    end
  end

  def set(key, value) do
    :ets.insert(:memo_table, {key, value})
  end
end
