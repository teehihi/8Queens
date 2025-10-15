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

---

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

---

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
---

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

---

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
