 h = pow(d, m - 1, q)
    p_hash = t_hash = 0
    matches, comparisons = [], 0
    for i in range(m):
        p_hash = (d * p_hash + ord(pattern[i])) % q
        t_hash = (d * t_hash + ord(text[i])) % q
    for s in range(n - m + 1):
        if p_hash == t_hash:
            for k in range(m):
                comparisons += 1
                if text[s + k] != pattern[k]:
                    break
            else:
                matches.append(s)
        if s < n - m:
            t_hash = (d * (t_hash - ord(text[s]) * h) + ord(text[s + m])) % q
            if t_hash < 0:
                t_hash += q
    return matches, comparisons
 
# --- Main Execution ---
text = 'AABAACAADAABAABA'
pattern = 'AABA'
print(f'Text:    {text}')
print(f'Pattern: {pattern}')
 
m1, c1 = naive_search(text, pattern)
m2, c2 = kmp_search(text, pattern)
m3, c3 = rabin_karp(text, pattern)
 
print(f'\nNaive  -> Matches at: {m1}, Comparisons: {c1}')
print(f'KMP    -> Matches at: {m2}, Comparisons: {c2}')
print(f'RK     -> Matches at: {m3}, Comparisons: {c3}')
 
# Performance comparison
text_large = ''.join(random.choices('ABCD', k=10000))
patterns = ['AB', 'ABCD', 'ABCDAB', 'ABCDABCD']
print(f'\n{"Pattern":>12} {"Naive":>10} {"KMP":>10} {"RK":>10}')
print('-' * 50)
for p in patterns:
    _, c1 = naive_search(text_large, p)
    _, c2 = kmp_search(text_large, p)
    _, c3 = rabin_karp(text_large, p)
    print(f'{p:>12} {c1:>10} {c2:>10} {c3:>10}')
 
