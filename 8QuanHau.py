import os
import tkinter as tk
from tkinter import messagebox
from queue import Queue, PriorityQueue

# --- Hàm kiểm tra an toàn có thể chèn hậu ---
def isSafe(vitri, row, col):
    for r, c in enumerate(vitri):
        if c == col or abs(c - col) == abs(r - row):
            return False
    return True

# --- Thuật toán tìm kiếm ---
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
    # số cặp tấn công khi thêm hậu ở (row, col)
    attacks = 0
    for r, c in enumerate(state):
        if c == col or abs(c - col) == abs(r - row):
            attacks += 1
    # chi phí cơ bản = 1, cộng thêm phạt nặng nếu có xung đột
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
            new_cost = cost + cost_function(vitri, row, col, n)
            pq.put((new_cost, vitri + [col]))
            yield vitri + [col]

# --- Depth Limited Search (DLS)---
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

# --- Iterative Deepening Search ---
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

# --- Hàm heuristic: số cặp hậu tấn công nhau ---
def heuristic(state):
    attacks = 0
    n = len(state)
    for i in range(n):
        for j in range(i + 1, n):
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                attacks += 1
    return attacks

# --- Thuật toán Greedy ---
def greedy_8queens_steps():
    n = 8
    # Khởi tạo random 1 state (mỗi hàng 1 hậu)
    import random
    state = [random.randint(0, n-1) for _ in range(n)]
    yield state

    while True:
        h_now = heuristic(state)
        if h_now == 0:  # nghiệm
            return

        best_state = None

        best_h = h_now

        # Thử di chuyển từng hậu sang cột khác để giảm h
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
            # Không giảm được nữa => local minima
            return
        else:
            state = best_state
            yield state

# --- A* Search ---
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
            # heuristic = số hậu chưa đặt + số cặp xung đột * hệ số
            h_new = (n - len(new_state)) + heuristic(new_state) * 10
            f_new = g_new + h_new
            pq.put((f_new, g_new, new_state))
            yield new_state


# --- GUI ---
root = tk.Tk()
root.title("8 Queens - BFS/DFS/UCS/DLS/IDS")
root.geometry("1200x700+100+30")
root.configure(bg="#BDE7E7")

title_label = tk.Label(root, text="8 QUEENS SEARCH (BFS / DFS / UCS / DLS / IDS)",
                       font=("SegoeUI", 20, "bold"),
                       fg="#0E2846", bg="#BDE7E7")
title_label.pack(pady=10)

main_frame = tk.Frame(root, bg="#BDE7E7")
main_frame.pack(fill="both", expand=True, padx=10, pady=10)

board = tk.Frame(main_frame, width=480, height=480)
board.pack(side="left", padx=20)
board.pack_propagate(False)

for row in range(8):
    for col in range(8):
        color = "#47C0C0" if (row + col) % 2 == 0 else "#17375C"
        cell = tk.Frame(board, width=60, height=60, bg=color)
        cell.grid(row=row, column=col)

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
            cell = tk.Frame(placedFrame, width=60, height=60, bg=color)
            cell.grid(row=row, column=col)
            cell.pack_propagate(False)
            row_cells.append(cell)
        cells.append(row_cells)
    return cells

def draw_solution(cells, solution):
    for row in range(8):
        for col in range(8):
            for widget in cells[row][col].winfo_children():
                widget.destroy()
    for row, col in enumerate(solution):
        lbl = tk.Label(cells[row][col], text="\u2655", fg="red",
                       bg=cells[row][col]["bg"], font=("Arial", 24, "bold"))
        lbl.pack(expand=True, fill="both")

# --- Biến toàn cục ---
cells_global = draw_empty_board()
search_generator = None
delay = 100
algo_choice = tk.StringVar(value="BFS")
skip_delay = False
running = False
traversal_history = []  # Lưu toàn bộ quá trình duyệt

def run_step():
    global search_generator, cells_global, skip_delay, running, last_dls_result, traversal_history
    if not running:
        return
    try:
        if skip_delay:
            last_state = None
            for state in search_generator:
                last_state = state
                traversal_history.append(state)  # lưu lại bước
            if last_state is not None:
                cells_global = draw_empty_board()
                draw_solution(cells_global, last_state)
            skip_delay = False
            return
        else:
            state = next(search_generator)
            traversal_history.append(state)  # lưu lại bước
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
    global search_generator, cells_global, running, last_dls_result, traversal_history
    cells_global = draw_empty_board()
    choice = algo_choice.get()
    last_dls_result = None
    traversal_history = []  # reset lịch sử
    if choice == "BFS":
        search_generator = bfs_8queens_steps()
    elif choice == "DFS":
        search_generator = dfs_8queens_steps()
    elif choice == "UCS":
        search_generator = ucs_8queens_steps()
    elif choice == "IDS":
        try:
            limit = int(dls_limit_var.get())
            if limit < 0: limit = 8
        except Exception: limit = 8
        search_generator = ids_8queens_steps(limit_max=limit)

    elif choice == "Greedy":
        search_generator = greedy_8queens_steps()
    elif choice == "A*":
        search_generator = astar_8queens_steps()

    else:
        try:
            limit = int(dls_limit_var.get())
            if limit < 0: limit = 8
        except Exception: limit = 8
        search_generator = dls_8queens_steps(limit=limit)
    
    running = True
    run_step()

def skip_search():
    global skip_delay, running
    if not running: return
    skip_delay = True
    run_step()

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

# --- Xuất quá trình duyệt ---
def export_traversal():
    if not traversal_history:
        messagebox.showwarning("Chưa có dữ liệu", "Chưa có bước duyệt nào để xuất.")
        return
    
    output_dir = os.path.join(os.path.dirname(__file__), "output")
    os.makedirs(output_dir, exist_ok=True)  # tạo nếu chưa có
    file_path = os.path.join(output_dir, "8queens_duongdi.txt")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(f"====Thuật toán: {algo_choice.get()}====\n")
        for idx, state in enumerate(traversal_history, 1):
            f.write(f"=== Bước {idx} ===\n")
            board = [["." for _ in range(8)] for _ in range(8)]
            for r, c in enumerate(state):
                board[r][c] = "♕"
            for row in board:
                f.write(" ".join(row) + "\n")
            f.write("\n")
    messagebox.showinfo("Xuất xong", "Đã lưu vào 8queens_duongdi.txt")

# --- Control panel ---
control_label = tk.Frame(root, bg="#BDE7E7")
control_label.pack(pady=5)

tk.Radiobutton(control_label, text="BFS", variable=algo_choice,
               value="BFS", bg="#BDE7E7").pack(side="left", padx=5)
tk.Radiobutton(control_label, text="DFS", variable=algo_choice,
               value="DFS", bg="#BDE7E7").pack(side="left", padx=5)
tk.Radiobutton(control_label, text="UCS", variable=algo_choice,
               value="UCS", bg="#BDE7E7").pack(side="left", padx=5)
tk.Radiobutton(control_label, text="DLS", variable=algo_choice,
               value="DLS", bg="#BDE7E7").pack(side="left", padx=5)
tk.Radiobutton(control_label, text="IDS", variable=algo_choice,
               value="IDS", bg="#BDE7E7").pack(side="left", padx=5)
tk.Radiobutton(control_label, text="Greedy", variable=algo_choice,
               value="Greedy", bg="#BDE7E7").pack(side="left", padx=5)
tk.Radiobutton(control_label, text="A*", variable=algo_choice,
               value="A*", bg="#BDE7E7").pack(side="left", padx=5)

dls_limit_var = tk.StringVar(value="8")
dls_limit_frame = tk.Frame(root, bg="#BDE7E7")
dls_limit_frame.pack(pady=3)
tk.Label(dls_limit_frame, text="DLS/IDS max depth:", bg="#BDE7E7").pack(side="left")
tk.Entry(dls_limit_frame, textvariable=dls_limit_var, width=4).pack(side="left", padx=5)

control_panel = tk.Frame(root, bg="#BDE7E7")
control_panel.pack(pady=10)
btn_start = tk.Button(control_panel, text="Start", font=("SegoeUI", 14, "bold"),
                      width=10, command=start_search, bg ="#BDE7E7")
btn_start.pack(side="left", padx=10)

btn_skip = tk.Button(control_panel, text="Skip", font=("SegoeUI", 14, "bold"),
                     width=10, command=skip_search, bg ="#BDE7E7")
btn_skip.pack(side="left", padx=10)

btn_reset = tk.Button(control_panel, text="Reset", font=("SegoeUI", 14, "bold"),
                      width=10, command=reset_board, bg ="#BDE7E7")
btn_reset.pack(side="left", padx=10)

btn_export = tk.Button(control_panel, text="Export Traversal", font=("SegoeUI", 14, "bold"),
                       width=15, command=export_traversal, bg ="#BDE7E7")
btn_export.pack(side="left", padx=10)

btn_quit = tk.Button(control_panel, text="Quit", font=("SegoeUI", 14, "bold"),
                     width=10, command=quit_app, bg ="#BDE7E7")
btn_quit.pack(side="left", padx=10)

root.mainloop()
