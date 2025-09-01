
# Add Two Numbers

### 🔗 Problem Link: [Add Two Numbers – LeetCode](https://leetcode.com/problems/add-two-numbers/)

---

## 🧠 Problem Description

You are given two non-empty linked lists representing two non-negative integers.  

- The digits are stored in **reverse order**, and each of their nodes contains a single digit.  
- Add the two numbers and return the sum as a linked list.  

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

---

## 🧪 Examples

### Example 1
**Input:**  
l1 = [2,4,3], l2 = [5,6,4]  
**Output:**  
[7,0,8]  
**Explanation:** 342 + 465 = 807  

---

### Example 2
**Input:**  
l1 = [0], l2 = [0]  
**Output:**  
[0]  

---

### Example 3
**Input:**  
l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]  
**Output:**  
[8,9,9,9,0,0,0,1]  

---

## ✅ Constraints

- The number of nodes in each linked list is in the range **[1, 100]**  
- `0 <= Node.val <= 9`  
- It is guaranteed that the list represents a number that does not have leading zeros.  

---

## 💡 Approach

1. Use a dummy head node to simplify list construction.  
2. Traverse both linked lists simultaneously.  
3. At each step, add:
   - The value from `l1` (if available).  
   - The value from `l2` (if available).  
   - The carry (if exists).  
4. Compute:
   - New digit = `(sum % 10)`  
   - New carry = `Math.floor(sum / 10)`  
5. Move pointers to the next nodes.  
6. After the loop, if carry remains, add it as a new node.  

---

## ⏱ Complexity

- **Time Complexity:** `O(max(m, n))` where `m` and `n` are the lengths of the two lists.  
- **Space Complexity:** `O(max(m, n))` for the output linked list.  

---