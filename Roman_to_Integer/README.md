# Roman to Integer

### 🔗 Problem Link: [Roman to Integer – LeetCode](https://leetcode.com/problems/roman-to-integer/)

---

## 🧠 Problem Description

Roman numerals are represented by seven symbols:  

- `I = 1`  
- `V = 5`  
- `X = 10`  
- `L = 50`  
- `C = 100`  
- `D = 500`  
- `M = 1000`  

Numbers are usually written largest to smallest from left to right.  
However, in **six cases**, subtraction is used instead of addition:  

- `IV = 4`, `IX = 9`  
- `XL = 40`, `XC = 90`  
- `CD = 400`, `CM = 900`  

Given a Roman numeral string `s`, return its integer value.  

---

## 🧪 Examples

### Example 1  
**Input:**  
`s = "III"`  
**Output:**  
`3`  
**Explanation:** III = 3.  

---

### Example 2  
**Input:**  
`s = "LVIII"`  
**Output:**  
`58`  
**Explanation:** L = 50, V = 5, III = 3 → 58.  

---

### Example 3  
**Input:**  
`s = "MCMXCIV"`  
**Output:**  
`1994`  
**Explanation:** M = 1000, CM = 900, XC = 90, IV = 4 → 1994.  

---

## ✅ Constraints

- `1 <= s.length <= 15`  
- `s` contains only: `'I', 'V', 'X', 'L', 'C', 'D', 'M'`  
- Guaranteed valid Roman numeral in the range `[1, 3999]`  

---

## 💡 Approach

1. Create a mapping of Roman symbols to their values.  
2. Traverse the string from left to right.  
3. If the current value is **less than the next**, subtract it.  
4. Otherwise, add it to the total.  
5. Return the final result.  

---



