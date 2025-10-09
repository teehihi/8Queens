import os
import tkinter as tk
from tkinter import messagebox
from queue import Queue, PriorityQueue
from collections import deque
import random, math

# ------------------ Utility ------------------
def isSafe(vitri, row, col):
    for r, c in enumerate(vitri):
        if c == col or abs(c - col) == abs(r - row):
            return False
    return True

def heuristic(state):
    attacks = 0
    n = len(state)
    for i in range(n):
        for j in range(i + 1, n):
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                attacks += 1
    return attacks

# ------------------ Generators for algorithms ------------------
def bfs_8queens_steps():
    n = 8
    q = Queue()
    q.put([])
    while not q.empty():
        vitri = q.get()
        row = len(vitri)
        if row == n:
            yield vitri
            return
        for col in range(n):
            if isSafe(vitri, row, col):
                q.put(vitri + [col])
                yield vitri + [col]

def dfs_8queens_steps():
    n = 8
    stack = [[]]
    while stack:
        vitri = stack.pop()
        row = len(vitri)
        if row == n:
            yield vitri
            return
        for col in range(n-1, -1, -1):
            if isSafe(vitri, row, col):
                stack.append(vitri + [col])
                yield vitri + [col]

def cost_function(state, row, col, n=8):
    attacks = 0
    for r, c in enumerate(state):
        if c == col or abs(c - col) == abs(r - row):
            attacks += 1
    return 1 + attacks * 5

def ucs_8queens_steps():
    n = 8
    pq = PriorityQueue()
    pq.put((0, []))
    while not pq.empty():
        cost, vitri = pq.get()
        row = len(vitri)
        if row == n:
            yield vitri
            return
        for col in range(n):
            if isSafe(vitri, row, col):
                new_cost = cost + cost_function(vitri, row, col, n)
                pq.put((new_cost, vitri + [col]))
                yield vitri + [col]

# DLS / IDS (with last_dls_result)
last_dls_result = None
def dls_8queens_steps(limit=8):
    global last_dls_result
    n = 8
    def recurse(state, depth):
        row = len(state)
        if row == n:
            yield state
            return "solution"
        if depth == limit:
            return "cutoff"
        cutoff_occurred = False
        for col in range(n):
            if isSafe(state, row, col):
                yield state + [col]
                res = yield from recurse(state + [col], depth + 1)
                if res == "cutoff":
                    cutoff_occurred = True
                elif res == "solution":
                    return "solution"
        if cutoff_occurred:
            return "cutoff"
        else:
            return "failure"
    try:
        res = yield from recurse([], 0)
    except GeneratorExit:
        last_dls_result = None
        raise
    last_dls_result = res
    return

def ids_8queens_steps(limit_max=8):
    global last_dls_result
    for depth in range(0, limit_max + 1):
        last_dls_result = None
        gen = dls_8queens_steps(limit=depth)
        try:
            for st in gen:
                yield st
        except GeneratorExit:
            gen.close()
            raise
        if last_dls_result == "solution":
            return
    last_dls_result = "failure"
    return

def greedy_8queens_steps():
    n = 8
    state = [random.randint(0, n-1) for _ in range(n)]
    yield state
    while True:
        h_now = heuristic(state)
        if h_now == 0:
            return
        best_state = None
        best_h = h_now
        for row in range(n):
            original_col = state[row]
            for col in range(n):
                if col == original_col:
                    continue
                new_state = state.copy()
                new_state[row] = col
                h_new = heuristic(new_state)
                if h_new < best_h:
                    best_h = h_new
                    best_state = new_state
        if best_state is None:
            return
        else:
            state = best_state
            yield state

def astar_8queens_steps():
    n = 8
    pq = PriorityQueue()
    pq.put((0, 0, []))  # (f, g, state)
    while not pq.empty():
        f, g, state = pq.get()
        row = len(state)
        if row == n:
            yield state
            return
        for col in range(n):
            new_state = state + [col]
            g_new = g + 1
            h_new = (n - len(new_state)) + heuristic(new_state) * 10
            f_new = g_new + h_new
            pq.put((f_new, g_new, new_state))
            yield new_state

# --- NEW ALGORITHMS: Hill, Genetic, Beam, SA ---
def hill_climbing_steps(max_iters=1000):
    n = 8
    state = [random.randint(0, n-1) for _ in range(n)]
    yield state
    it = 0
    while it < max_iters:
        it += 1
        h_now = heuristic(state)
        if h_now == 0:
            return
        best_state = None
        best_h = h_now
        for row in range(n):
            orig = state[row]
            for col in range(n):
                if col == orig: continue
                ns = state.copy(); ns[row] = col
                h_ns = heuristic(ns)
                if h_ns < best_h:
                    best_h = h_ns; best_state = ns
        if best_state is None:
            return
        state = best_state
        yield state

def beam_steps(beam_width=4):
    n = 8
    beam = [[]]
    yield []
    for depth in range(n):
        candidates = []
        for st in beam:
            row = len(st)
            for col in range(n):
                new_state = st + [col]
                candidates.append((heuristic(new_state), new_state))
        if not candidates:
            return
        candidates.sort(key=lambda x: x[0])
        beam = [s for _, s in candidates[:beam_width]]
        for b in beam:
            yield b
        for b in beam:
            if len(b) == n and heuristic(b) == 0:
                yield b
                return
    return

def genetic_steps(pop_size=60, max_gens=200, crossover_rate=0.8, mutation_rate=0.15):
    n = 8
    max_pairs = n*(n-1)//2
    def fitness(state): return max_pairs - heuristic(state)
    population = [[random.randint(0, n-1) for _ in range(n)] for _ in range(pop_size)]
    for gen in range(1, max_gens+1):
        pop_with_fit = [(fitness(ind), ind) for ind in population]
        pop_with_fit.sort(key=lambda x: -x[0])
        best_fit, best_ind = pop_with_fit[0]
        yield best_ind
        if heuristic(best_ind) == 0:
            return
        # tournament selection + crossover + mutation
        new_pop = []
        while len(new_pop) < pop_size:
            # tournament 3
            parents = [random.choice(population) for _ in range(3)]
            parents.sort(key=lambda p: fitness(p), reverse=True)
            parent1 = parents[0]
            parents = [random.choice(population) for _ in range(3)]
            parents.sort(key=lambda p: fitness(p), reverse=True)
            parent2 = parents[0]
            child1, child2 = parent1.copy(), parent2.copy()
            if random.random() < crossover_rate:
                cp = random.randint(1, n-2)
                child1 = parent1[:cp] + parent2[cp:]
                child2 = parent2[:cp] + parent1[cp:]
            def mutate(ind):
                if random.random() < mutation_rate:
                    if random.random() < 0.5:
                        i, j = random.sample(range(n), 2)
                        ind[i], ind[j] = ind[j], ind[i]
                    else:
                        i = random.randrange(n)
                        ind[i] = random.randrange(n)
                return ind
            child1 = mutate(child1); child2 = mutate(child2)
            new_pop.append(child1)
            if len(new_pop) < pop_size:
                new_pop.append(child2)
        population = new_pop
    # final
    pop_with_fit = [(fitness(ind), ind) for ind in population]
    pop_with_fit.sort(key=lambda x: -x[0])
    yield pop_with_fit[0][1]
    return

def sa_steps(T0=10.0, alpha=0.95, max_iters=5000):
    n = 8
    state = [random.randint(0, n-1) for _ in range(n)]
    yield state
    T = T0
    it = 0
    while it < max_iters and T > 1e-6:
        it += 1
        row = random.randrange(n)
        col = random.randrange(n)
        while col == state[row]:
            col = random.randrange(n)
        new_state = state.copy(); new_state[row] = col
        deltaE = heuristic(new_state) - heuristic(state)
        accept = False
        if deltaE <= 0:
            accept = True
        else:
            if random.random() < math.exp(-deltaE / T):
                accept = True
        if accept:
            state = new_state
            yield state
            if heuristic(state) == 0:
                return
        T *= alpha
    return

# ------------------ And-Or Search (generator) ------------------
def and_or_8queens_steps():
    """
    A simple And-Or recursive generator for n-queens where:
    - OR node: choose a column for current row
    - AND node: ensure that choice allows future rows to have solutions (we attempt them)
    This will behave similar to backtracking but yields at OR expansions and when a solution found.
    """
    n = 8
    def recurse(state):
        row = len(state)
        # yield the current partial assignment as an OR-node expansion
        yield state
        if row == n:
            yield state  # full solution
            return True
        # OR: try each possible action (column)
        for col in range(n):
            if isSafe(state, row, col):
                # yield the choice (OR child)
                yield state + [col]
                # AND: we must prove that all "outcomes" (here deterministic) lead to success
                # For deterministic CSP, we simply recurse; if recursion finds a solution, return True
                res = yield from recurse(state + [col])
                if res:
                    return True
        return False
    try:
        yield from recurse([])
    except GeneratorExit:
        return

# ------------------ Belief Search (domains + AC-3 like propagation) ------------------
def belief_8queens_steps():
    """
    Belief search: duy trì miền giá trị (domain) cho mỗi hàng.
    Dùng propagation kiểu AC-3, sau đó rẽ nhánh với hàng có domain nhỏ nhất > 1.
    Đảm bảo đặt đủ 8 hậu.
    """
    n = 8
    domains = [set(range(n)) for _ in range(n)]
    yield [ds.copy() for ds in domains]

    def ac3(domains):
        q = deque((i, j) for i in range(n) for j in range(n) if i != j)
        changed = False
        while q:
            xi, xj = q.popleft()
            if revise(domains, xi, xj):
                changed = True
                if len(domains[xi]) == 0:
                    return False
                for xk in range(n):
                    if xk != xi and xk != xj:
                        q.append((xk, xi))
        return True

    def search(domains):
        # yield trạng thái hiện tại
        yield [ds.copy() for ds in domains]

        # propagation
        ok = ac3(domains)
        yield [ds.copy() for ds in domains]
        if not ok:
            return False

        # check full assignment
        all_single = all(len(ds) == 1 for ds in domains)
        if all_single:
            sol = [next(iter(ds)) for ds in domains]
            if all(isSafe(sol[:r], r, sol[r]) for r in range(n)):
                yield sol
                return True
            else:
                return False

        # chọn hàng có domain nhỏ nhất > 1 để branch
        row = min((i for i in range(n) if len(domains[i]) > 1),
                  key=lambda i: len(domains[i]))
        for val in sorted(domains[row]):
            new_domains = [ds.copy() for ds in domains]
            new_domains[row] = {val}
            yield [ds.copy() for ds in new_domains]
            res = yield from search(new_domains)
            if res:
                return True
        return False

    yield from search(domains)

def revise(domains, xi, xj):
    """
    Revise domain xi wrt xj. Remove values in domains[xi] that are incompatible with every value in domains[xj].
    For n-queens: value a in xi is incompatible with b in xj if a==b or abs(a-b)==abs(i-j)
    If we remove any value from domains[xi], return True.
    """
    removed = False
    to_remove = set()
    n = len(domains)
    for a in set(domains[xi]):
        # check existence of some b in domains[xj] that is compatible
        ok_exist = False
        for b in domains[xj]:
            if a != b and abs(a - b) != abs(xi - xj):
                ok_exist = True
                break
        if not ok_exist:
            to_remove.add(a)
    if to_remove:
        domains[xi] -= to_remove
        removed = True
    return removed

# ------------------ NEW: Partial / Backtracking / Forward Checking / AC3+Backtrack ------------------

def partial_8queens_steps(pre_filled=None):
    """
    Tìm kiếm khi biết trước một phần kết quả (partial assignment).
    pre_filled: list các vị trí đã biết, -1 nếu chưa xác định.
    Nếu pre_filled is None => treat as all unknown.
    """
    n = 8
    if pre_filled is None:
        pre_filled = [-1] * n
    # Validate length
    if len(pre_filled) != n:
        pre_filled = (pre_filled + [-1]*n)[:n]

    def recurse(state, row):
        yield state
        if row == n:
            yield state
            return True
        if pre_filled[row] != -1:
            col = pre_filled[row]
            # if pre-filled conflicts with earlier assignment -> fail this branch
            if isSafe(state, row, col):
                res = yield from recurse(state + [col], row + 1)
                if res: return True
            return False
        for col in range(n):
            if isSafe(state, row, col):
                res = yield from recurse(state + [col], row + 1)
                if res: return True
        return False

    yield from recurse([], 0)


def backtracking_8queens_steps():
    """
    Backtracking full search as generator.
    """
    n = 8

    def recurse(state, row):
        yield state
        if row == n:
            yield state
            return True
        for col in range(n):
            if isSafe(state, row, col):
                res = yield from recurse(state + [col], row + 1)
                if res: return True
        return False

    yield from recurse([], 0)


def forward_checking_8queens_steps():
    """
    Forward checking: domains + assign left-to-right, prune forward domains.
    Yields domain snapshots and final solution when found.
    """
    n = 8
    domains = [set(range(n)) for _ in range(n)]

    def recurse(state, row, domains):
        yield [d.copy() for d in domains]
        if row == n:
            sol = [next(iter(d)) for d in domains]
            yield sol
            return True
        for col in list(domains[row]):
            if isSafe(state, row, col):
                new_domains = [d.copy() for d in domains]
                new_domains[row] = {col}
                # forward checking: prune later rows
                failure = False
                for r in range(row + 1, n):
                    if col in new_domains[r]:
                        new_domains[r].remove(col)
                    diff = r - row
                    if (col - diff) in new_domains[r]:
                        new_domains[r].remove(col - diff)
                    if (col + diff) in new_domains[r]:
                        new_domains[r].remove(col + diff)
                    if len(new_domains[r]) == 0:
                        failure = True
                        break
                if failure:
                    continue
                res = yield from recurse(state + [col], row + 1, new_domains)
                if res: return True
        return False

    yield from recurse([], 0, domains)


def ac3_8queens_steps():
    """
    AC-3 propagation then (if needed) backtracking over remaining domains.
    Yields domain snapshots during propagation and yields final solution when found.
    """
    n = 8
    domains = [set(range(n)) for _ in range(n)]
    yield [ds.copy() for ds in domains]

    # AC-3 propagation
    queue = deque((i, j) for i in range(n) for j in range(n) if i != j)
    while queue:
        xi, xj = queue.popleft()
        if revise(domains, xi, xj):
            yield [ds.copy() for ds in domains]
            if len(domains[xi]) == 0:
                return
            for xk in range(n):
                if xk != xi and xk != xj:
                    queue.append((xk, xi))

    # If everything singleton and consistent -> solution
    if all(len(d) == 1 for d in domains):
        sol = [next(iter(ds)) for ds in domains]
        if all(isSafe(sol[:r], r, sol[r]) for r in range(n)):
            yield sol
            return

    # Otherwise do backtracking using current domains (MRV ordering could be added)
    # We'll choose next unassigned row (left-to-right) but only try values in domain
    def backtrack_from_domains(partial, domains_local):
        row = len(partial)
        # If partial is shorter than number of rows, we still must pick by row index
        if row == n:
            yield partial
            return True
        # If row already assigned in domains_local as singleton earlier than len(partial), handle
        for val in list(domains_local[row]):
            if isSafe(partial, row, val):
                # create new domains copy and assign
                new_domains = [d.copy() for d in domains_local]
                new_domains[row] = {val}
                # forward prune
                fail = False
                for r in range(row + 1, n):
                    if val in new_domains[r]:
                        new_domains[r].remove(val)
                    diff = r - row
                    if (val - diff) in new_domains[r]:
                        new_domains[r].remove(val - diff)
                    if (val + diff) in new_domains[r]:
                        new_domains[r].remove(val + diff)
                    if len(new_domains[r]) == 0:
                        fail = True
                        break
                if fail:
                    continue
                # yield domains snapshot after assignment
                yield [d.copy() for d in new_domains]
                res = yield from backtrack_from_domains(partial + [val], new_domains)
                if res:
                    return True
        return False

    # Kick off backtracking starting with empty partial but using domains as pruned by AC3
    yield from backtrack_from_domains([], domains)
    return


# ------------------ GUI ------------------
root = tk.Tk()
root.title("8 Queens - Search Algorithms")
root.geometry("1200x760+80+20")
root.configure(bg="#BDE7E7")

title_label = tk.Label(root, text="8 QUEENS SEARCH (BFS / DFS / UCS / DLS / IDS / Greedy / A* / Hill / Genetic / Beam / SA / And-Or / Belief / Partial / Backtracking / Forward Checking / AC3)",
                       font=("SegoeUI", 14, "bold"), fg="#0E2846", bg="#BDE7E7")
title_label.pack(pady=8)

main_frame = tk.Frame(root, bg="#BDE7E7")
main_frame.pack(fill="both", expand=True, padx=10, pady=6)

# left empty visual board (for current state if desired)
board = tk.Frame(main_frame, width=480, height=480)
board.pack(side="left", padx=20)
board.pack_propagate(False)
for row in range(8):
    for col in range(8):
        color = "#47C0C0" if (row + col) % 2 == 0 else "#17375C"
        cell = tk.Frame(board, width=60, height=60, bg=color)
        cell.grid(row=row, column=col)

# right placed frame that we draw into
placedFrame = tk.Frame(main_frame, width=480, height=480)
placedFrame.pack(side="right", padx=20)
placedFrame.pack_propagate(False)

def draw_empty_board():
    for widget in placedFrame.winfo_children():
        widget.destroy()
    cells = []
    for row in range(8):
        row_cells = []
        for col in range(8):
            color = "#47C0C0" if (row + col) % 2 == 0 else "#17375C"
            cell = tk.Frame(placedFrame, width=60, height=60, bg=color, relief="raised", bd=1)
            cell.grid(row=row, column=col)
            cell.pack_propagate(False)
            row_cells.append(cell)
        cells.append(row_cells)
    return cells

def draw_solution(cells, solution):
    # clear
    for row in range(8):
        for col in range(8):
            for widget in cells[row][col].winfo_children():
                widget.destroy()
    # If solution is a list of ints -> draw queens
    if isinstance(solution, list) and solution and all(isinstance(x, int) for x in solution):
        for row, col in enumerate(solution):
            if 0 <= row < 8 and 0 <= col < 8:
                lbl = tk.Label(cells[row][col], text="\u2655", fg="red",
                               bg=cells[row][col]["bg"], font=("Arial", 24, "bold"))
                lbl.pack(expand=True, fill="both")
    # If solution is list of sets (belief domains) -> draw queens for singletons, else show number of possibilities
    elif isinstance(solution, list) and solution and all(isinstance(x, set) for x in solution):
        for row, ds in enumerate(solution):
            if len(ds) == 1:
                col = next(iter(ds))
                lbl = tk.Label(cells[row][col], text="\u2655", fg="red",
                               bg=cells[row][col]["bg"], font=("Arial", 22, "bold"))
                lbl.pack(expand=True, fill="both")
            else:
                # show small label in each column indicating possible or empty
                for col in range(8):
                    if col in ds:
                        sub = tk.Label(cells[row][col], text="·", fg="yellow", bg=cells[row][col]["bg"], font=("Arial", 14))
                        sub.pack(expand=True, fill="both")
                # also show count in leftmost cell
                count_lbl = tk.Label(cells[row][0], text=str(len(ds)), fg="black", bg=cells[row][0]["bg"], font=("Arial", 10))
                count_lbl.place(relx=0.02, rely=0.02)
    else:
        # unknown format -> no draw
        pass

cells_global = draw_empty_board()

# control vars
algo_choice = tk.StringVar(value="BFS")
dls_limit_var = tk.StringVar(value="8")
sa_T_var = tk.StringVar(value="10.0")
sa_alpha_var = tk.StringVar(value="0.95")
beam_width_var = tk.StringVar(value="4")

# control frame (radios)
control_label = tk.Frame(root, bg="#BDE7E7")
control_label.pack(pady=6)

algorithms = ["BFS", "DFS", "UCS", "DLS", "IDS",
              "Greedy", "A*", "Hill", "Genetic", "Beam", "SA",
              "And-Or", "Belief",
              "Partial", "Backtracking", "Forward Checking", "AC3"]

# 2 hàng nút
half = len(algorithms) // 2
row1 = tk.Frame(control_label, bg="#BDE7E7")
row1.pack()
for name in algorithms[:half]:
    tk.Radiobutton(row1, text=name, variable=algo_choice,
                   value=name, bg="#BDE7E7", command=lambda: update_params()).pack(side="left", padx=4)

row2 = tk.Frame(control_label, bg="#BDE7E7")
row2.pack()
for name in algorithms[half:]:
    tk.Radiobutton(row2, text=name, variable=algo_choice,
                   value=name, bg="#BDE7E7", command=lambda: update_params()).pack(side="left", padx=4)

# parameter area (DLS/IDS depth, SA params, Beam width)
param_frame = tk.Frame(root, bg="#BDE7E7")
param_frame.pack(pady=3)

frame_dls = tk.Frame(param_frame, bg="#BDE7E7")
tk.Label(frame_dls, text="DLS/IDS max depth:", bg="#BDE7E7").pack(side="left")
tk.Entry(frame_dls, textvariable=dls_limit_var, width=4).pack(side="left", padx=5)

frame_sa = tk.Frame(param_frame, bg="#BDE7E7")
tk.Label(frame_sa, text="T0:", bg="#BDE7E7").pack(side="left")
tk.Entry(frame_sa, textvariable=sa_T_var, width=6).pack(side="left", padx=5)
tk.Label(frame_sa, text="Alpha:", bg="#BDE7E7").pack(side="left")
tk.Entry(frame_sa, textvariable=sa_alpha_var, width=6).pack(side="left", padx=5)

frame_beam = tk.Frame(param_frame, bg="#BDE7E7")
tk.Label(frame_beam, text="Beam Width:", bg="#BDE7E7").pack(side="left")
tk.Entry(frame_beam, textvariable=beam_width_var, width=4).pack(side="left", padx=5)

def update_params():
    # hide all frames, then show the one needed
    frame_dls.pack_forget()
    frame_sa.pack_forget()
    frame_beam.pack_forget()
    choice = algo_choice.get()
    if choice in ("DLS", "IDS"):
        frame_dls.pack()
    elif choice == "SA":
        frame_sa.pack()
    elif choice == "Beam":
        frame_beam.pack()

update_params()  # initial hide/show

# traversal history & runtime control
search_generator = None
running = False
skip_delay = False
delay = 120
traversal_history = []

def run_step():
    global search_generator, cells_global, skip_delay, running, last_dls_result, traversal_history
    if not running:
        return
    try:
        if skip_delay:
            last_state = None
            for state in search_generator:
                last_state = state
                traversal_history.append(state)
            if last_state is not None:
                cells_global = draw_empty_board()
                draw_solution(cells_global, last_state)
            skip_delay = False
            running = False
            messagebox.showinfo("Kết thúc", "Đã skip tới cuối traversal.")
            return
        else:
            state = next(search_generator)
            traversal_history.append(state)
            cells_global = draw_empty_board()
            draw_solution(cells_global, state)
            root.after(delay, run_step)
    except StopIteration:
        choice = algo_choice.get()
        if choice == "DLS":
            if last_dls_result == "solution":
                messagebox.showinfo("Thông báo", "Đã tìm được nghiệm!")
            elif last_dls_result == "cutoff":
                messagebox.showinfo("Kết quả DLS", f"Cutoff occurred (limit = {dls_limit_var.get()})")
            else:
                messagebox.showinfo("Kết quả DLS", "Không tìm được nghiệm.")
        elif choice == "IDS":
            if last_dls_result == "solution":
                messagebox.showinfo("Thông báo", "IDS: Đã tìm được nghiệm!")
            else:
                messagebox.showinfo("Kết quả IDS", f"IDS: Không tìm được nghiệm (max depth = {dls_limit_var.get()}).")
        else:
            messagebox.showinfo("Thông báo", "Đã kết thúc tìm kiếm.")
        running = False

def start_search():
    global search_generator, cells_global, running, last_dls_result, traversal_history, skip_delay
    cells_global = draw_empty_board()
    choice = algo_choice.get()
    last_dls_result = None
    traversal_history = []
    skip_delay = False

    try:
        if choice == "BFS":
            search_generator = bfs_8queens_steps()
        elif choice == "DFS":
            search_generator = dfs_8queens_steps()
        elif choice == "UCS":
            search_generator = ucs_8queens_steps()
        elif choice == "DLS":
            limit = int(dls_limit_var.get())
            if limit < 0: limit = 8
            search_generator = dls_8queens_steps(limit=limit)
        elif choice == "IDS":
            limit = int(dls_limit_var.get())
            if limit < 0: limit = 8
            search_generator = ids_8queens_steps(limit_max=limit)
        elif choice == "Hill":
            search_generator = hill_climbing_steps()
        elif choice == "Genetic":
            search_generator = genetic_steps()
        elif choice == "Beam":
            try:
                beam_width = int(beam_width_var.get())
            except ValueError:
                beam_width = 4
            if beam_width <= 0:
                beam_width = 4
            search_generator = beam_steps(beam_width=beam_width)
        elif choice == "SA":
            try:
                T0 = float(sa_T_var.get())
                a = float(sa_alpha_var.get())
            except:
                T0, a = 10.0, 0.95
            search_generator = sa_steps(T0=T0, alpha=a)
        elif choice == "Greedy":
            search_generator = greedy_8queens_steps()
        elif choice == "A*":
            search_generator = astar_8queens_steps()
        elif choice == "And-Or":
            search_generator = and_or_8queens_steps()
        elif choice == "Belief":
            search_generator = belief_8queens_steps()
        elif choice == "Partial":
            # mặc định không ép xung đột (tất cả -1)
            pre = [-1] * 8
            search_generator = partial_8queens_steps(pre_filled=pre)
        elif choice == "Backtracking":
            search_generator = backtracking_8queens_steps()
        elif choice == "Forward Checking":
            search_generator = forward_checking_8queens_steps()
        elif choice == "AC3":
            search_generator = ac3_8queens_steps()
        else:
            search_generator = dls_8queens_steps(limit=8)
    except Exception as ex:
        messagebox.showerror("Lỗi", f"Không thể khởi tạo thuật toán: {ex}")
        return

    running = True
    run_step()

def skip_search():
    global skip_delay, running
    if not running: return
    skip_delay = True

def reset_board():
    global search_generator, running, skip_delay, last_dls_result, traversal_history
    running = False
    skip_delay = False
    search_generator = None
    last_dls_result = None
    traversal_history = []
    draw_empty_board()

def quit_app():
    root.quit()

def export_traversal():
    if not traversal_history:
        messagebox.showwarning("Chưa có dữ liệu", "Chưa có bước duyệt nào để xuất.")
        return
    output_dir = os.path.join(os.path.dirname(__file__), "output")
    os.makedirs(output_dir, exist_ok=True)
    file_path = os.path.join(output_dir, "8queens_duongdi.txt")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(f"====Thuật toán: {algo_choice.get()}====\n")
        for idx, state in enumerate(traversal_history, 1):
            f.write(f"=== Bước {idx} ===\n")
            # If state is list of ints
            if isinstance(state, list) and state and all(isinstance(x, int) for x in state):
                board = [["." for _ in range(8)] for _ in range(8)]
                for r, c in enumerate(state):
                    if 0 <= r < 8 and 0 <= c < 8:
                        board[r][c] = "♕"
                for row in board:
                    f.write(" ".join(row) + "\n")
            # If state is list of sets (belief)
            elif isinstance(state, list) and state and all(isinstance(x, set) for x in state):
                for r, ds in enumerate(state):
                    line = f"Row {r}: " + ("{" + ",".join(str(x) for x in sorted(ds)) + "}" if ds else "{}")
                    f.write(line + "\n")
            else:
                f.write(str(state) + "\n")
            f.write("\n")
    messagebox.showinfo("Xuất xong", f"Đã lưu vào {file_path}")

# --- Control panel (buttons) ---
control_panel = tk.Frame(root, bg="#BDE7E7")
control_panel.pack(pady=10)

btn_start = tk.Button(control_panel, text="Start", font=("SegoeUI", 12, "bold"),
                      width=12, command=start_search, bg ="#ffffff")
btn_start.pack(side="left", padx=8)

btn_skip = tk.Button(control_panel, text="Skip", font=("SegoeUI", 12, "bold"),
                     width=12, command=skip_search, bg ="#ffffff")
btn_skip.pack(side="left", padx=8)

btn_reset = tk.Button(control_panel, text="Reset", font=("SegoeUI", 12, "bold"),
                      width=12, command=reset_board, bg ="#ffffff")
btn_reset.pack(side="left", padx=8)

btn_export = tk.Button(control_panel, text="Export Traversal", font=("SegoeUI", 12, "bold"),
                       width=15, command=export_traversal, bg ="#ffffff")
btn_export.pack(side="left", padx=8)

btn_quit = tk.Button(control_panel, text="Quit", font=("SegoeUI", 12, "bold"),
                     width=10, command=quit_app, bg ="#ffffff")
btn_quit.pack(side="left", padx=8)

root.minsize(1000,740)
root.mainloop()
