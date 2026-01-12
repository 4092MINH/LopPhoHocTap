
Mảng cộng dồn và mảng hiệu (Prefix sum array and difference array)
===
> Nguồn : [2School Guideline](https://hackmd.io/@2SchoolGuideline/H1HY_VKbp)
---

# Giới thiệu chung
Mảng cộng dồn và mảng hiệu là 2 kiến thức tuy cơ bản nhưng vô cùng quan trọng trong lập trình thi đấu. Tư tưởng của chúng là nền tảng cho nhiều kiến thức nâng cao hơn và chúng được ứng dụng rộng rãi trong các bài toán từ cơ bản đến nâng cao.

*Bài viết này sẽ đề cập đến các kiến thức liên quan đến độ phức tạp thời gian, bạn có thể xem lại bài viết "Độ phức tạp thời gian và bộ nhớ" của 2SG để dễ theo dõi hơn.*

# Mảng cộng dồn 1 chiều
## 1. Bài toán ví dụ
- Cho một mảng $A$ gồm $N$ số nguyên và $Q$ truy vấn tính $S$ là tổng các phần tử từ vị trí $l$ cho đến vị trí $r$ (hay $S = A_l + A_{l + 1} + A_{l + 2} + ... + A_{r - 1} + A_{r}$).
- Giới hạn: $1 \le N$, $Q \le 10^6$, $-10^9 \le A_i \le 10^9$ với $i = 1, 2, ..., N$.
- Hình ảnh minh hoạ cho truy vấn với $l = 2$ và $r = 5$ trong mảng 1 chiều $A$ có $7$ phần tử - ta cần tính tổng các phần tử được tô màu vàng:
![](https://hackmd.io/_uploads/H1GTdUtW6.png)
(*Nguồn ảnh: VNOI wiki*)
- Input mẫu:
```
6
0 2 0 9 1 9 4 5
3
1 4
2 5
6 6
```
- Output mẫu:
```
11
12
5
```

## 2. Cách tiếp cận 1: Duyệt trâu
- Ta sử dụng thuật toán duyệt trâu (hay còn gọi là vét cạn): duyệt từ vị trí $l$ đến vị trí $r$ để tính $S$ cho mỗi truy vấn và in ra kết quả.
- **Độ phức tạp của thuật toán:** Với mỗi truy vấn trong $Q$ truy vấn, ta duyệt qua mảng 1 chiều $A$ kích thước $N$, từ đó có độ phức tạp của thuật toán là $O(N \times Q)$.
- **Cài đặt:**
```cpp
long long Solve(int l, int r)
{
    long long sum = 0;
    for (int i = l; i <= r; ++i) sum += A[i];
    return sum;
}
```
- Ta có thể thấy với độ phức tạp trên thì sẽ không thể giải quyết bài toán trong giới hạn thời gian của đề bài, vì vậy cần tìm cách giải tối ưu hơn.
- **Gợi ý:** Bằng cách tính một số tổng của các phần tử trong $A$, ta có thể sử dụng mối liên hệ về mặt toán học của các tổng đó để nhanh chóng tính toán tổng $S$ trong mỗi truy vấn, các tổng này liên quan đến vị trí của các phần tử trong $A$ cũng như $l$ và $r$.

## 3. Cách tiếp cận 2: Mảng cộng dồn 1 chiều
- Ta viết ra tổng $S$ từ $l$ tới $r$ như sau: $A_l + A_{l + 1} + A_{l + 2} + ... + A_{r - 1} + A_{r}$.
- Giả sử ta có $A_1 + A_2 + A_3 + ... + A_{l - 1} + A_{l} + A_{l + 1} + ... + A_{r - 1} + A_{r}$ thì để tính được tổng $S$ ta cần loại bỏ $A_1 + A_2 + A_3 + ... + A_{l - 1}$, từ đó ta liên tưởng đến thuật toán tốt hơn.
- Gọi mảng 1 chiều $pref$ là mảng cộng dồn 1 chiều của mảng 1 chiều $A$, phần tử nằm ở vị trí $i$ của $pref$ chứa tổng các phần tử từ vị trí $1$ đến $i$ của $A$.
- **Xây dựng mảng cộng dồn 1 chiều:**
    + Theo định nghĩa của $pref$ đã nêu trên, ta đặt $pref_i = A_1 + A_2 + ... + A_i$ với $i = 1, 2, ..., N$.
    + Vì $A_1 + A_2 + ... + A_{i - 1} + A_i - (A_1 + A_2 + ... + A_{i - 1}) = A_{i}$ nên $pref_i - pref_{i - 1} = A_i$.
    + Chuyển vế đổi dấu, ta có công thức: $pref_{i} = pref_{i - 1} + A_i$.
- **Sử dụng mảng cộng dồn 1 chiều để tính truy vấn:**
    + Cũng giống như ở trên, vì $A_1 + A_2 + ... + A_r - (A_1 + A_2 + ... + A_{l - 1}) = A_l + A_{l + 1} + ... + A_r$ nên ta có công thức: $S = pref_r - pref_{l - 1}$
- **Độ phức tạp của thuật toán:** Đầu tiên ta tính giá trị của mảng 1 chiều $pref$ kích thước $N$ trong $O(N)$ và sau đó với $Q$ truy vấn ta tính mỗi truy vấn trong $O(1)$, từ đó có độ phức tạp của thuật toán là $O(N + Q)$.
- **Cài đặt:**
*(Lưu ý: do các giá trị trong mảng là số nguyên không nhỏ nên ta cần sử dụng kiểu dữ liệu `long long` thay cho `int` để tránh tràn số)*
```cpp
void Calc()
{
    for(int i = 1; i <= N; ++i) pref[i] = pref[i - 1] + A[i];
}

long long Solve(int l, int r)
{
    return pref[r] - pref[l - 1];
}
```

# Mảng hiệu
## 1. Khái niệm
- Từ mảng $A$, ta có thể xây dựng mảng hiệu (difference array) $D(A)$ theo quy tắc D[i] = A_{i+1} - A_i$ $(0 \le i < n)$
![](https://i.imgur.com/3IQ1YlB.gif)
(*Nguồn ảnh: VNOI wiki*)
- **Tính chất cần lưu ý:** Từ mảng hiệu $D$ và phần tử đầu tiên của mảng $A$, ta có thể khôi phục lại mảng $A$ thông qua phép tính $S(A_0, D(A)) = A$ với:
    + $A_0$: phần tử đầu tiên của mảng $A$
    + $D(A)$: mảng hiệu của mảng $A$
    + $S(A_0, D(A))$: mảng cộng dồn của mảng $D(A)$ với hằng số đầu tiên là $A_0$
- **Cài đặt:**
```cpp
vector <int> A(n), D(n);

void buildDifferenceArray()
{
    for (int i = 0; i < n - 1; ++i) D[i] = A[i + 1] - A[i];
}
```

## 2. Bài toán ví dụ
- Cho số $N$ và $Q$ truy vấn. Với mỗi truy vấn $i$ cho 2 số $L_i$ và $R_i$ biểu diễn cho đoạn $[L_i, R_i]$. Yêu cầu cho biết mỗi vị trí $x \in [1, N]$ được chứa bởi bao nhiêu đoạn $[L, R]$
- Giới hạn: $1 \le N, Q \le 10^7$ và $1 \le L_i \le R_i \le 10^7$
- Input mẫu:
```
5 4
1 3
4 5
3 4
1 5
```
- Output mẫu:
```
2 2 3 3 2
```

### 3.1. Cách tiếp cận 1: Duyệt trâu
- Ta có thể thấy rằng để tìm số lần mỗi vị trí được đi qua, ta duyệt qua $Q$ đoạn $[L_i, R_i]$ và cộng thêm $1$ đơn vị vào giá trị của tất cả các vị trí nằm trong đoạn đó.
- **Độ phức tạp của thuật toán:** Với mỗi truy vấn trong $Q$ truy vấn, ta duyệt qua mảng 1 chiều $A$ kích thước $N$, từ đó có độ phức tạp của thuật toán là $O(N \times Q)$.
- **Cài đặt:**
```cpp
void solve()
{
    int N, Q; cin >> N >> Q;
    
    vector <int> cnt(N + 1);
    
    for (int i = 1; i <= Q; ++i)
    {
        int l, r; cin >> L >> R;
        for (int j = L; j <= R; ++j) cnt[j]++;
    }
    for (int i = 1; i <= N; ++i) cout << cnt[i] << ' ';
}
```

### 3.2. Cách tiếp cận 2: Mảng hiệu kết hợp mảng cộng dồn
- Thay vì cộng từng phần tử trong đoạn $[L_i, R_i]$, ta có thể cộng giá trị cần cập nhật (cụ thể ở đây là $1$) ở vị trí $L_i$ và trừ đi giá trị cập nhật ở vị trí $R_i+1$ của mảng hiệu $D$. Mảng $D$ cần có $N + 2$ phần tử vì giá trị $R$ nằm trong khoảng $[1, N]$.
- Cuối cùng chạy 1 vòng lặp và thực hiện việc cộng dồn phần tử $dif_{i - 1}$ vào $dif_i$ và trả về kết quả của phần tử $i$.
- **Độ phức tạp của thuật toán:** Đầu tiên ta tính giá trị của mảng 1 chiều $dif$ kích thước $N$ trong $O(N)$ và sau đó với $Q$ truy vấn ta thực hiện mỗi truy vấn trong $O(1)$. Cuối cùng, ta duyệt qua mảng $dif$ để tính và in ra kết quả, từ đó có độ phức tạp của thuật toán là $O(N \times M + Q)$.
- **Cài đặt:**
```cpp
void solve()
{
    int n, q; cin >> n >> q;
    vector <int> dif(n+2);
    for (int i = 1; i <= q; ++i)
    {
        int l, r; cin >> l >> r;
        dif[l]++; dif[r+1]--;
    }
    for (int i = 1; i <= n; ++i)
    {
        dif[i] = dif[i-1] + dif[i];
        cout << dif[i] << ' ';
    }
}
```

# Mảng cộng dồn 2 chiều
## 1. Bài toán ví dụ
- Cho một mảng 2 chiều $A$ gồm $N \times M$ phần tử ($N$ hàng và $M$ cột) và $Q$ truy vấn. Mỗi truy vấn gồm có 4 số nguyên: $x_1$, $y_1$, $x_2$, $y_2$ ($x_1 \le x_2 \le N$, $y_1 \le y_2 \le M$), yêu cầu tính $S$ là tổng các phần tử trong hình chữ nhật có ô trên cùng bên trái nằm ở vị trí ${x_1 y_1}$ (hàng $x_1$, cột $y_1$) và ô dưới cùng bên phải nằm ở vị trí ${x_2 y_2}$ (hàng $x_2$, cột $y_2$) của mảng 2 chiều $A$ (hay $S = A_{x_1 y_1} + A_{x_1, y_1 + 1} + A_{x_1, y_1 + 2} + ... + B_{x_1 + 1, y_1} + A_{x_1 + 1, y_1 + 1} + A_{x_1 + 1, y_1 + 2} + ... + A_{x_2, y_2}$).
- Giới hạn: $1 \le N \le 10^3$, $1 \le M \le 10^3$, $-10^9 \le A_{i j} \le 10^9$ với $i = 1, 2, ..., N$ và $j = 1, 2, ..., M$.
- Hình ảnh minh hoạ cho truy vấn với $x_1 = 2$, $y_1 = 2$ và $x_2 = 4$, $y_2 = 3$ trong mảng 2 chiều $A$ có $4 \times 4$ phần tử ($4$ hàng, $4$ cột) - ta cần tính tổng các phần tử được tô màu vàng:
![](https://hackmd.io/_uploads/SJzUtLtWa.png)
(*Nguồn ảnh: VNOI wiki*)
- Input mẫu:
```
3 4
4 2 1 0
6 9 7 1
9 6 7 3
3
1 1 2 3
1 4 3 4
2 2 3 2
```
- Output mẫu:
```
29
4
15
```

## 2. Cách tiếp cận 1: Duyệt trâu
-  Ta duyệt từ vị trí $x_1$ $y_1$ đến vị trí $x_2$ $y_2$ để tính $S$ cho mỗi truy vấn và in ra kết quả.
-  **Độ phức tạp của thuật toán:** Với mỗi truy vấn trong $Q$ truy vấn, ta duyệt qua mảng 2 chiều $A$ kích thước $N \times M$, từ đó có độ phức tạp của thuật toán là $O(N \times M \times Q)$.
-  **Cài đặt:**
```cpp
long long Solve(int x1, int x2, int y1, int y2){
    long long sum = 0;
    for (int i = x1; i <= x2; ++i){
        for (int j = y1; j <= y2; ++j) sum += A[i][j];
    }
    return sum;
}
```
-  Ta có thể thấy với độ phức tạp trên thì sẽ không thể giải quyết bài toán trong giới hạn thời gian của đề bài, vì vậy cần tìm cách giải tối ưu hơn.

## 3. Cách tiếp cận 2: Mảng cộng dồn 2 chiều
- Áp dụng tư tưởng của mảng cộng dồn 1 chiều nhưng nâng cấp lên một tí, ta có được mảng cộng dồn 2 chiều.
- Gọi mảng 2 chiều $pref$ là mảng cộng dồn 2 chiều của mảng 2 chiều $A$, phần tử nằm ở hàng $i$, cột $j$ của $pref$ chứa tổng các phần tử từ hàng $1$, cột $1$ đến hàng $i$, cột $j$ của $A$.
- Chú ý: Ta quy ước $pref_{i, 0} = 0$ và $pref_{0, j} = 0$ với mọi $i = 1, 2, ..., N$ và $j = 1, 2, ..., M$.
- Hình ảnh minh hoạ cho $pref$ và $A$ tương ứng:
![](https://hackmd.io/_uploads/SyEuiOtbp.png)
(*Nguồn ảnh: VNOI wiki*)
- **Xây dựng mảng cộng dồn 2 chiều:**
    + Theo định nghĩa của $pref$ đã nêu trên, ta đặt $pref_{i j} = A_{1,1} + A_{1, 2} + ... + A_{2, 1} + A_{2, 2} + ... + A_{i j}$ với $i = 1, 2, ..., N$ và $j = 1, 2, ..., M$.
    + Ta có công thức: $pref_{i j} = pref_{i - 1, j} + pref_{i, j - 1} - pref_{i - 1, j - 1} + A_{i j}$.
    + Giải thích: Cách chứng minh toán học của công thức trên cũng tương tự như với mảng cộng dồn 1 chiều. Một cách khác để hiểu công thức trên sẽ được biểu diễn trong hình minh hoạ dưới đây:
![](https://hackmd.io/_uploads/SkDNAdYZ6.png)
(*Nguồn ảnh: VNOI wiki*)
    + Chú thích: Trong hình trên, ta có thể thấy trong quá trình tính giá trị của $pref_{i j}$, sau khi cộng $pref_{i - 1, j}$ và $pref_{i, j - 1}$ với nhau thì phần $pref_{i - 1, j - 1}$ sẽ bị tính 2 lần (lặp lại) nên ta phải trừ đi $pref_{i - 1, j - 1}$ để có được giá trị chính xác của $pref_{i j}$.
- **Sử dụng mảng cộng dồn 2 chiều để tính truy vấn:**
    + Ta có thể tính được tổng $S$ cho mỗi truy vấn theo công thức: $S = pref_{x_2 y_2} - pref_{x_1 - 1, y_2} - pref_{x_2, y_1 - 1} + pref_{x_1 - 1, y_1 - 1}$.
    + Giải thích: Cách chứng minh toán học của công thức trên cũng tương tự như với mảng cộng dồn 1 chiều. Một cách khác để hiểu công thức trên sẽ được biểu diễn trong hình minh hoạ dưới đây:
![](https://hackmd.io/_uploads/SyjF-YKZT.png)
(*Nguồn ảnh: VNOI wiki*)
- **Độ phức tạp của thuật toán:** Đầu tiên ta tính giá trị của mảng 2 chiều $pref$ kích thước $N \times M$ trong $O(N \times M)$ và sau đó với $Q$ truy vấn ta tính mỗi truy vấn trong $O(1)$, từ đó có độ phức tạp của thuật toán là $O(N \times M + Q)$.
- **Cài đặt:**
```cpp
void Calc(){
    for (int i = 1; i <= n; ++i){
        for (int j = 1; j <= m; ++j) {
            pref[i][j] = pref[i - 1][j] + pref[i][j - 1] - pref[i - 1][j - 1] + A[i][j];
        }
    }
}

long long Solve(int x1, int x2, int y1, int y2){
    return pref[x2][y2] - pref[x1 - 1][y2] - pref[x2][y1 - 1] + pref[x1 - 1][y1 - 1];
}
```

# Bài tập vận dụng
## Note: Một số kiến thức toán học
- $\sum$ : Kí hiệu **sigma** dùng để biểu diễn tổng của các giá trị thỏa một điều kiện nào đó. 
    + VD1: $\sum_{i = l}^{r} A_i$ nghĩa là $A_l + A_{l - 1} + ... + A_{r - 1} + A_r$.
    + VD2: $\sum_{i = x_1}^{x_2} \sum_{j = y_1}^{y_2} A_{i j}$ nghĩa là $A_{x_1, y_1} + A_{x_1, y_1 + 1} + ... + A_{x_1 + 1, y_1} + A_{x_1 + 1, y_1 + 1} + ... + A_{x_2 y_2}$.

## Bài 1
#### **Link:** [VNOJ - GIRLS](https://oj.vnoi.info/problem/bedao_m06_girls)
#### **Tóm tắt đề:** 
Cho mảng 1 chiều $A$ kích thước $M$, số nguyên dương $N$ và số nguyên không âm $K$. Chọn ra $N$ phần tử sao cho hiệu giữa phần tử lớn nhất và nhỏ nhất (trong số các phần tử được chọn) không vượt quá $K$ và tổng của $N$ phần tử được chọn phải lớn nhất. Nếu không tồn tại cách chọn thì in ra $-2$.
#### **Input**
- Dòng đầu gồm 3 số nguyên $N, M, K$ $(1 \le N \le M \le 10^6, 0 \le K \le 10^8)$. 
- Dòng thứ 2 gồm $M$ phần tử $A_i$ $(0 \le A_i \le 10^8)$.
#### **Output**
- Dòng duy nhất chứa số nguyên là đáp án, nếu không tồn tại đáp án in ra $-2$.
#### **Sample testcase**
- Input:
```
3 2 1
1 2 3
```
- Output:
```
5
```

## Bài 2
#### **Link:** [Codeforces - Greg and Array](https://codeforces.com/contest/296/problem/C)
#### **Tóm tắt đề:** 
Cho 1 mảng 1 chiều $a$ gồm $n$ phần tử, $m$ thao tác với mỗi thao tác gồm 3 giá trị $l_i, r_i, d_i (1 \le l_i \le r_i \le n)$ biểu diễn cho việc tăng 1 giá trị $d_i$ với cho mỗi phần tử trong mảng $a$ từ trong đoạn $[l_i, r_i]$. Sau đó gồm $k$ truy vấn, với mỗi truy vấn cho 2 số $x_i, y_i$. Nghĩa là mỗi truy vấn sẽ thực hiện các thao tác $x_i, x_{i+1}, x_{i+2},...,y_i$ lên mảng $a$
#### **Input**
- Dòng đầu gồm 3 số nguyên $n, m, k$ $(1 \le n, m, k \le 10^5)$. Dòng thứ 2 gồm $n$ phần tử $a_i$ $(0 \le a_i \le 10^5)$
- $m$ dòng tiếp theo chứa các thao tác, thao tác thứ $i$ chứa 3 số nguyên $l_i, r_i, d_i$ $(1 \le l_i,r_i \le n)$, $(0 \le d_i \le 10^5)$
- $k$ dòng tiếp theo chứa các truy vấn, truy vấn thứ $i$ gồm 2 số $x_i, y_i$ $(1 \le x_i, y_i \le m)$
#### **Output**
- Dòng duy nhất gồm $n$ số nguyên $a_1, a_2,...,a_n$: mảng $a$ sau khi thực hiện tất cả các truy vấn. Các số được in cách nhau 1 dấu cách.
#### **Sample testcase**
- Input:
```
3 3 3
1 2 3
1 2 1
1 3 2
2 3 4
1 2
1 3
2 3
```
- Output:
```
9 18 17
```

## Bài 3
#### **Link:** [VNOJ - CHIADAT](https://oj.vnoi.info/problem/olp304_18_chiadat//)
#### **Tóm tắt đề:** 
Cho một mảng 2 chiều $A$ kích thước $N * N$ chỉ chứa các giá trị $0$ và $1$. Tìm cách chia mảng $A$ thành 4 phần sao cho chênh lệch giữa phần có tổng giá trị (tổng giá trị các phần tử nằm trong phần đó) lớn nhất nhất và phần có tổng giá trị nhỏ nhất là nhỏ nhất.
#### **Input**
- Dòng đầu gồm 1 số nguyên $N$ $(N \le 500)$.
- $N$ dòng tiếp theo, mỗi dòng chứa $N$ phần tử $A_{ij}$ $(A_{ij} \in$ {$0, 1$}$)$.
#### **Output**
- Dòng duy nhất chứa số nguyên là đáp án.
#### **Sample testcase**
- Input:
```
6
1 0 1 0 0 1
0 1 0 0 0 1
1 0 0 0 0 0
0 1 1 0 0 1
0 1 0 0 1 0
1 0 1 0 0 0
```
- Output:
```
1
```

# Tài liệu tham khảo
:::info
[[1] vnoi.info/wiki/algo/data-structures/prefix-sum-and-difference-array.md](https://vnoi.info/wiki/algo/data-structures/prefix-sum-and-difference-array.md)
[[2] geeksforgeeks.org/difference-array-range-update-query-o1/](https://www.geeksforgeeks.org/difference-array-range-update-query-o1/)
[[3] codeforces.com/blog/entry/78762](https://codeforces.com/blog/entry/78762)
:::