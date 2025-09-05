# Palindrome Number

### 🔗 Problem Link: [Palindrome Number – LeetCode](https://leetcode.com/problems/palindrome-number/)

---

## 🧠 Problem Description

Given an integer `x`, return **true** if `x` is a palindrome, and **false** otherwise.  

A palindrome is a number that reads the same backward as forward.

---

## 🧪 Examples

### Example 1
**Input:**  
`x = 121`  
**Output:**  
`true`  
**Explanation:** 121 reads the same forward and backward.  

---

### Example 2
**Input:**  
`x = -121`  
**Output:**  
`false`  
**Explanation:** Reads as `-121` from left to right, but `121-` from right to left. Not the same.  

---

### Example 3
**Input:**  
`x = 10`  
**Output:**  
`false`  
**Explanation:** Reads as `01` backward, which is not equal to `10`.  

---

## ✅ Constraints

- `-2³¹ <= x <= 2³¹ - 1`  

---

## 💡 Approach

### Method 1: String Conversion (Simple)
1. Negative numbers are not palindromes.  
2. Convert number to string.  
3. Use two pointers (`i` from start, `j` from end).  
4. Compare characters until `i >= j`.  

---

### Method 2: Mathematical Reversal (Optimized)
1. Negative numbers or numbers ending with 0 (except 0 itself) are not palindromes.  
2. Reverse half of the number using modulo and division.  
3. Compare the original half with the reversed half.  
4. Works without converting to string.  

---

## ⏱ Complexity

- **Time Complexity:** `O(log₁₀(n))` → number of digits in `x`  
- **Space Complexity:** `O(1)` (for the math method), `O(n)` for string conversion  

---


