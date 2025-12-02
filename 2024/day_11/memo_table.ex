defmodule MemoTable do
  def initMemoTable do
    :ets.new(:memo_table, [:named_table, :set, :private])
  end

  def fetch(key, default) do
    case :ets.lookup(:memo_table, key) do
      [{^key, result}] -> result
      [] -> default
    end
  end

  def set(key, value) do
    :ets.insert(:memo_table, {key, value})
  end
end
