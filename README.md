# ♟️ Bài toán 8 Quân Hậu & PEAS

## 📌 Giới thiệu
Dự án này bao gồm:
- 🧩 **Giải thuật 8 quân hậu** bằng Python (Jupyter Notebook).
- 💻 **Mô phỏng giao diện** với Tkinter.
- 📊 **Phân tích PEAS** (Performance, Environment, Actuators, Sensors) cho:
  - Bài toán 8 quân hậu.
  - Trò chơi Caro.

---

## 📂 Cấu trúc thư mục
```
📦 8quanhau
 ┣ 📂 output
 ┃ ┗ 📜 8queens_duongdi.txt          # File chứa đường đi lời giải
 ┣ 📜 8QuanHau.py                    # File chính giải bài toán 8 quân hậu
 ┣ 📜 PEAS - 8QueenAndCaro.docx      # Tài liệu mô tả PEAS
 ┗ 📜 README.md                      # Tài liệu mô tả repo
```

---
## 👑 Trực Quan Hóa Giải Thuật — Bài Toán 8 Quân Hậu

Dự án là một ứng dụng desktop được xây dựng bằng Python và Tkinter, giúp trực quan hóa quá trình giải bài toán 8 Quân Hậu thông qua nhiều thuật toán Trí tuệ Nhân tạo (AI) khác nhau.
Mục tiêu là mang đến một công cụ học tập sinh động, giúp người dùng dễ dàng quan sát, so sánh và hiểu sâu cách hoạt động của từng thuật toán.


### ✨ Tính Năng Nổi Bật

🎨 Giao diện trực quan: Thiết kế bằng Tkinter, thân thiện và dễ sử dụng.

🧩 Minh họa từng bước: Hiển thị rõ ràng quá trình tìm kiếm, từ trạng thái ban đầu đến khi tìm được lời giải.

🧠 Đa dạng thuật toán: Hơn 15 thuật toán AI kinh điển, thuộc nhiều nhóm khác nhau — từ tìm kiếm mù, có thông tin đến tối ưu hóa cục bộ và CSP.


### 🎮 Điều khiển linh hoạt:

Xem cách thuật toán duyệt (Step-by-step)

Bỏ qua đến kết quả (Skip)

Xuất đường đi (Export Traversal)


⚙️ Tùy chỉnh tốc độ: Người dùng có thể thay đổi tốc độ mô phỏng trong file cấu hình.


### 🚀 Các Thuật Toán Được Cài Đặt

🔹 Tìm kiếm mù - không có thông tin (Uninformed Search)

BFS (Breadth-First Search) – Tìm lời giải ở độ sâu nhỏ nhất.

DFS (Depth-First Search) – Đi sâu theo từng nhánh.

UCS (Uniform Cost Search) – Mở rộng nút có chi phí thấp nhất.

DLS (Depth-Limited Search) – DFS có giới hạn độ sâu.

IDS (Iterative Deepening Search) – Kết hợp ưu điểm của BFS và DFS.


🔹 Tìm kiếm có thông tin (Informed Search)

Greedy Search – Tìm kiếm tham lam dựa trên heuristic.

A* – Kết hợp chi phí thực tế (g) và ước lượng (h) để tối ưu hóa đường đi.


🔹 Tìm kiếm cục bộ & Metaheuristic

Hill Climbing – Leo đồi, tìm trạng thái tốt hơn trong vùng lân cận.

Simulated Annealing – Cho phép chọn trạng thái xấu hơn để tránh kẹt tối ưu cục bộ.

Beam Search – Giữ lại một số trạng thái tốt nhất trong mỗi bước.

Genetic Algorithm – Mô phỏng tiến hóa tự nhiên (lai ghép, đột biến) để tìm lời giải.


🔹 Thuật toán nâng cao trong môi trường phức tạp

And-Or Search – Giải các bài toán có thể tách thành nhiều bài toán con.

Belief Space Search – Dựa trên mô hình xác suất, tương tự EDA.

Partial Search – Tiếp cận linh hoạt, giải theo nhóm quân hậu thay vì từng quân một.


🔹 Giải bài toán ràng buộc (CSP)

Backtracking – Thử và sai có hệ thống.

Forward Checking – Kiểm tra và loại bỏ giá trị không hợp lệ sau mỗi bước gán.

AC-3 (Arc Consistency Algorithm #3) – Tiền xử lý đảm bảo tính nhất quán giữa các biến.


### 🎯 Mục Tiêu Dự Án

Cung cấp một nền tảng trực quan hóa học thuật giúp sinh viên và người yêu thích AI có thể:

 - Quan sát chi tiết quá trình tìm kiếm lời giải.

 - So sánh hiệu suất giữa các thuật toán.

 - Hiểu sâu hơn về bản chất của từng hướng tiếp cận trong AI.
 
---
## 🚀 Cách chạy
### 1️⃣ Clone repo
```bash
git clone https://github.com/teehihi/8quanhau.git
cd 8quanhau
```

### 2️⃣ Mở
Mở `8QuanHau.py` bằng **Visual Studio Code** hoặc **PyCharm**.

### 3️⃣ Chạy chương trình
Chạy file `8QuanHau.py` , chọn thuật toán sau đó bấm **Start**

---

## 🧠 PEAS Phân tích

| Thành phần | 8 Quân Hậu | Trò chơi Caro |
|-------------|-------------|----------------|
| **Performance** | Tìm tất cả các nghiệm hợp lệ | Tìm nước đi tối ưu |
| **Environment** | Bàn cờ 8x8 | Bàn cờ NxN |
| **Actuators** | Đặt quân hậu | Đặt X hoặc O |
| **Sensors** | Kiểm tra hàng, cột, chéo | Kiểm tra thắng/thua |

---

## ♟️ Demo 8 Quân Hậu
Ví dụ nghiệm hợp lệ:
```
[0, 4, 7, 5, 2, 6, 1, 3]
```

---
## ⚙️ Demo các nhóm thuật toán

### 🟦 Nhóm 1: Tìm kiếm không thông tin
<table align="center">
  <tr>
    <td align="center">
      <img src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExY2NpcW10emVtdDRtcmV6NTk0OHJza2NsaWZrcmE5ajR6dGRyZTdkMiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/6NUMgZzaqOHjCrDcFP/giphy.gif" width="220"><br><strong>BFS</strong>
    </td>
    <td align="center">
      <img src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExOXV0aDdiYWdnenB1eGpjdnAweWt5YTFrb3duejljMTIxYWF5ZHhyayZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/RGHqRWT06h93Vhog4x/giphy.gif" width="220"><br><strong>DFS</strong>
    </td>
    <td align="center">
      <img src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExMHE5ZjMzdTVnZmJ1NnBlZGhvdzN2ZmF3aG9reXB1Mnh2OTNnZG5waSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/EJVxIjwKV22pfY6Qxe/giphy.gif" width="220"><br><strong>DLS</strong>
    </td>
  </tr>
</table>



### 🟩 Nhóm 2: Tìm kiếm có thông tin
<table align="center">
  <tr>
    <td align="center">
      <img src="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExYjJndDQ4ZGx6eGQ5MjB4bWI2Mm4yamFseHRjZm1pZGpwdm1nNWtkZSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Thcf7r7jQ5RwqZexs3/giphy.gif" width="220"><br><strong>UCS</strong>
    </td>
    <td align="center">
      <img src="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExZmN3dThreTZjN2tlZjA5MzQyYXpxcmMwZDhhb2xwZ29obW52MTczMyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Vg0iULhr7tPGlgT5GZ/giphy.gif" width="220"><br><strong>Greedy</strong>
    </td>
    <td align="center">
      <img src="https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExZDl0bTVmMXFiNjYxNjJwYnljbmRzcjU3c2FzYWdlN2M2NGFldndraiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Da8bfgwyXTaapY0sF0/giphy.gif" width="220"><br><strong>A*</strong>
    </td>
  </tr>
</table>



### 🟨 Nhóm 3: Tìm kiếm cục bộ
<table align="center">
  <tr>
    <td align="center">
      <img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExdzY5azZyNzVkdGVkcG0ybWVmN2hmNGEyaHB0M2d1ZHIyN2ZpOGMzcyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/fwURZKClaObu7DYd6u/giphy.gif" width="220"><br><strong>Hill Climbing</strong>
    </td>
    <td align="center">
      <img src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExMWZkcWZmb3Z1MTI4Y3hjOWd0aXVjd3NheDJnNjlvb3cxeWVncmFmaSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/X2pnqwaTWHOmf0y1cS/giphy.gif" width="220"><br><strong>Genetic</strong>
    </td>
    <td align="center">
      <img src="https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExd2M2dmcxOG5kOTlmY2JpOHVtZmk3czdyNzU0dm9pMjN0YzB5YTNreCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/StEqsKxViwN5W2DUvV/giphy.gif" width="220"><br><strong>Simulated Annealing</strong>
    </td>
    <td align="center">
      <img src="https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExandscXg2MjdwbXh5aTRwN3JxZW1ocGJ1dXppMGt2ZDJ5bDF2a3RjMyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/C96AsTTHZWemfb8kgL/giphy.gif" width="220"><br><strong>Beam Search</strong>
    </td>
  </tr>
</table>
🚩 Nhiều thuật toán, kéo qua phải để xem tiếp 🤓


### 🟪 Nhóm 4: Tìm kiếm môi trường phức tạp
<table align="center">
  <tr>
    <td align="center">
      <img src="https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExdHZ5bWJ6d2F0YnVjMDBpemZva3dpZWthbHlnMzBzNXdyeGh0MnkxcyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/1pVM8Y321RySuqIqeN/giphy.gif" width="220"><br><strong>And-Or Graph</strong>
    </td>
    <td align="center">
      <img src="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExYjhtMWZlbGk5eWUzeG9yN2YxaHdwbmJqOXMzOHF1ZWIwbjV5YnMzdiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/LENbm2RcNxgPuqMwSM/giphy.gif" width="220"><br><strong>Partial Order</strong>
    </td>
    <td align="center">
      <img src="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExNm53dDF0eDl5Nm5iZWNtNjZmemJhZDBzNjdhOTNnNTc2a2Y5ejJzcCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/yfun04WXspBazmvFro/giphy.gif" width="220"><br><strong>Belief Network</strong>
    </td>
  </tr>
</table>



### 🟧 Nhóm 5: Tìm kiếm môi trường ràng buộc
<table align="center">
  <tr>
    <td align="center">
      <img src="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExZHlocGV4bTBtemoweHhqaXk5cG50cTRqeDl6M3oxYjJuZTVzajA4OCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/klyFRk1QT7tO22Zrca/giphy.gif" width="220"><br><strong>Backtracking</strong>
    </td>
    <td align="center">
      <img src="https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExYXg5MDIzYmozaWwydWhiYWk0OG1lNHBxcHAxcWdobnlyYnVvdnRwbiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/soMbZgWXBMv3NsTqhT/giphy.gif" width="220"><br><strong>Forward Checking</strong>
    </td>
    <td align="center">
      <img src="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExb2Qxc2t0NHBodWc1cHhmOHJra3dmOWFqNTd5eno0dDFxamk3d3YzcCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/hpf2L1yxYjQmhD67Ti/giphy.gif" width="220"><br><strong>AC-3</strong>
    </td>
  </tr>
</table>

---

## ✨ Tác giả
👤 **teehihi**  
🔗 [linktr.ee/nkqt.tee](https://linktr.ee/nkqt.tee)
