defmodule MemoServer do
  use GenServer
  @impl true
  def init(init) do
    {:ok, init}
  end

  @impl true
  def handle_call({:get, k}, _from, state) do
    if Map.has_key?(state, k) do
      {:reply, Map.get(state, k), state}
    else
      {:reply, :miss, state}
    end
  end

  @impl true
  def handle_cast({:put, k, v}, state) do
    {:noreply, Map.put(state, k, v)}
  end
end
