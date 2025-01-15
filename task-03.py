import timeit

# Boyer-Moore Algorithm
def boyer_moore(text, pattern):
    m, n = len(pattern), len(text)
    if m == 0: return -1

    # Build the bad character table
    bad_char = {char: m for char in set(text)}
    for i in range(m - 1):
        bad_char[pattern[i]] = m - i - 1

    i = 0
    while i <= n - m:
        j = m - 1
        while j >= 0 and text[i + j] == pattern[j]:
            j -= 1
        if j < 0:
            return i  # Match found
            i += (m if i + m < n else 1)
        else:
            i += max(1, j - bad_char.get(text[i + j], m))

    return -1  # No match

# Knuth-Morris-Pratt Algorithm
def kmp(text, pattern):
    m, n = len(pattern), len(text)
    if m == 0: return -1

    # Build the prefix table (also known as "partial match" table)
    lps = [0] * m
    j = 0
    for i in range(1, m):
        while j > 0 and pattern[i] != pattern[j]:
            j = lps[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
        lps[i] = j

    # Search for the pattern in the text
    i = j = 0
    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1
            if j == m:
                return i - m  # Match found
        else:
            if j > 0:
                j = lps[j - 1]
            else:
                i += 1

    return -1  # No match

# Rabin-Karp Algorithm
def rabin_karp(text, pattern):
    m, n = len(pattern), len(text)
    if m == 0: return -1

    # Compute the hash of the pattern and the initial hash of the text window
    base = 256
    prime = 101
    pattern_hash = sum(ord(pattern[i]) * (base ** (m - i - 1)) for i in range(m)) % prime
    window_hash = sum(ord(text[i]) * (base ** (m - i - 1)) for i in range(m)) % prime

    for i in range(n - m + 1):
        if window_hash == pattern_hash and text[i:i+m] == pattern:
            return i  # Match found

        if i < n - m:
            window_hash = (base * (window_hash - ord(text[i]) * (base ** (m - 1)))) + ord(text[i + m])
            window_hash %= prime

    return -1  # No match

# Function to benchmark each algorithm
def benchmark_boyer_moore(text, pattern):
    return timeit.timeit(lambda: boyer_moore(text, pattern), number=1)

def benchmark_kmp(text, pattern):
    return timeit.timeit(lambda: kmp(text, pattern), number=1)

def benchmark_rabin_karp(text, pattern):
    return timeit.timeit(lambda: rabin_karp(text, pattern), number=1)

# Main function to run the benchmarking for both articles
def main():
    # Sample Texts (Replace with your actual texts)
    text1 = "some long text from article 1..."
    text2 = "some long text from article 2..."
    
    # Example substrings
    existing_substring = "substring that exists"  # Replace with an actual substring
    non_existing_substring = "random substring that doesn't exist"  # Replace with a non-existing substring

    # Measure the execution time for each algorithm on both types of substrings
    results = {
        "Boyle Moore (Article 1, Existing)": benchmark_boyer_moore(text1, existing_substring),
        "Knuth-Morris-Pratt (Article 1, Existing)": benchmark_kmp(text1, existing_substring),
        "Rabin-Karp (Article 1, Existing)": benchmark_rabin_karp(text1, existing_substring),
        "Boyle Moore (Article 1, Non-existing)": benchmark_boyer_moore(text1, non_existing_substring),
        "Knuth-Morris-Pratt (Article 1, Non-existing)": benchmark_kmp(text1, non_existing_substring),
        "Rabin-Karp (Article 1, Non-existing)": benchmark_rabin_karp(text1, non_existing_substring),
        "Boyle Moore (Article 2, Existing)": benchmark_boyer_moore(text2, existing_substring),
        "Knuth-Morris-Pratt (Article 2, Existing)": benchmark_kmp(text2, existing_substring),
        "Rabin-Karp (Article 2, Existing)": benchmark_rabin_karp(text2, existing_substring),
        "Boyle Moore (Article 2, Non-existing)": benchmark_boyer_moore(text2, non_existing_substring),
        "Knuth-Morris-Pratt (Article 2, Non-existing)": benchmark_kmp(text2, non_existing_substring),
        "Rabin-Karp (Article 2, Non-existing)": benchmark_rabin_karp(text2, non_existing_substring),
    }

    # Display results
    for name, time_taken in results.items():
        print(f"{name}: {time_taken:.6f} seconds")

# Run the program
if __name__ == "__main__":
    main()