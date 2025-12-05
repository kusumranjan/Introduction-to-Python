

# LIST – Exercises (5)


# Exercise 1
# Rearrange integers so negatives come first, then positives (no sort()).
def rearrange_neg_pos(lst):
    negs = []
    poss = []
    for x in lst:
        if isinstance(x, int) and x < 0:
            negs.append(x)
        else:
            poss.append(x)
    return negs + poss

# Alternative in-place two-pointer partition (not stable):

def rearrange_neg_pos_inplace(lst):
    i, j = 0, len(lst) - 1
    while i <= j:
        if lst[i] < 0:
            i += 1
        elif lst[j] >= 0:
            j -= 1
        else:
            lst[i], lst[j] = lst[j], lst[i]
            i += 1
            j -= 1
    return lst

# Exercise 2
# Create a new list of elements which appear more than once (do NOT use set())

def more_than_once(lst):
    # Use a dict for counting (allowed)
    counts = {}
    for x in lst:
        counts[x] = counts.get(x, 0) + 1
    result = []
    for x in lst:
        if counts[x] > 1 and x not in result:
            result.append(x)
    return result

# Exercise 3
# Rotate a list to the left by N positions using only loops.

def rotate_left(lst, n):
    if not lst:
        return lst
    n = n % len(lst)
    for _ in range(n):
        first = lst[0]
        # shift left using loops
        for i in range(len(lst) - 1):
            lst[i] = lst[i + 1]
        lst[-1] = first
    return lst

# Exercise 4
# Remove all strings with length < 3.
def remove_short_strings(strings):
    result = []
    for s in strings:
        if isinstance(s, str) and len(s) >= 3:
            result.append(s)
    return result

# Exercise 5
# Flatten a nested list using loops only.
def flatten_list(nested):
    flat = []
    stack = nested[::-1]  # use a stack; push nested lists in reverse to preserve order
    while stack:
        item = stack.pop()
        if isinstance(item, list):
            # extend with reversed to maintain left-to-right order when popping
            stack.extend(item[::-1])
        else:
            flat.append(item)
    return flat



# TUPLE – Exercises (5)


# Exercise 1
# Separate numbers and strings into two tuples.
def separate_tuple(tp):
    nums = []
    strs = []
    for x in tp:
        if isinstance(x, (int, float)):
            nums.append(x)
        elif isinstance(x, str):
            strs.append(x)
    return tuple(nums), tuple(strs)

# Exercise 2
# Determine whether a tuple of numbers is strictly increasing.
def is_strictly_increasing(tp):
    if len(tp) < 2:
        return True
    for i in range(1, len(tp)):
        if tp[i] <= tp[i - 1]:
            return False
    return True

# Exercise 3
# Reverse each word in a tuple of strings.
def reverse_words_tuple(tp):
    out = []
    for w in tp:
        out.append(w[::-1])
    return tuple(out)

# Exercise 4
# Find index positions of a given value inside a tuple without using index().
def find_indices(tp, value):
    indices = []
    for i in range(len(tp)):
        if tp[i] == value:
            indices.append(i)
    return tuple(indices)

# Exercise 5
# Given a nested tuple, print all integers using recursion.
def print_integers_recursive(tp):
    def rec(x):
        if isinstance(x, tuple):
            for y in x:
                rec(y)
        elif isinstance(x, int):
            print(x)
        # ignore non-int, non-tuple values
    rec(tp)



# SET – Exercises (5)


# Exercise 1
# Elements present in union but not in intersection (symmetric difference) WITHOUT using ^.
def union_minus_intersection(a, b):
    # Build union
    union = set()
    for x in a:
        union.add(x)
    for x in b:
        union.add(x)
    # Build intersection
    inter = set()
    for x in a:
        if x in b:
            inter.add(x)
    # union - intersection
    result = set()
    for x in union:
        if x not in inter:
            result.add(x)
    return result

# Exercise 2
# Convert list with duplicates to a set and back to a list, preserving order of first occurrences.
def dedup_preserve_order(lst):
    seen = set()
    out = []
    for x in lst:
        if x not in seen:
            seen.add(x)
            out.append(x)
    return out

# Exercise 3
# Find all pairs in a set that sum to target. Include (x, x) if 2*x == target. No duplicate pairs.
def pairs_sum_to_target(s, target):
    res = []
    seen_pairs = set()  # to avoid duplicates, store tuple pairs
    for x in s:
        y = target - x
        if y in s:
            # canonical ordering for pair
            pair = (x, y) if x <= y else (y, x)
            if pair not in seen_pairs:
                seen_pairs.add(pair)
                res.append(pair)
    return res

# Exercise 4
# Check whether two sets are disjoint WITHOUT using the built-in method.
def are_disjoint(a, b):
    for x in a:
        if x in b:
            return False
    return True

# Exercise 5
# Find all unique characters across a list of words using sets.
def unique_chars(words):
    chars = set()
    for w in words:
        for ch in w:
            chars.add(ch)
    return chars



# DICTIONARY – Exercises (5)


# Exercise 1
# Print keys that have the maximum value WITHOUT using max().
def keys_with_max(d):
    max_val = None
    for v in d.values():
        if max_val is None or v > max_val:
            max_val = v
    keys = []
    for k, v in d.items():
        if v == max_val:
            keys.append(k)
    return keys

# Exercise 2
# Invert a dictionary: values become keys; group keys into a list for duplicates.
def invert_dict(d):
    inv = {}
    for k, v in d.items():
        if v not in inv:
            inv[v] = [k]
        else:
            inv[v].append(k)
    return inv

# Exercise 3
# Merge two dictionaries; if a key appears in both, store the values in a list.
def merge_dicts(d1, d2):
    out = {}
    for k, v in d1.items():
        out[k] = v
    for k, v in d2.items():
        if k in out:
            if isinstance(out[k], list):
                out[k].append(v)
            else:
                out[k] = [out[k], v]
        else:
            out[k] = v
    return out

# Exercise 4
# Remove all items with price below 100.
def remove_below_100(items):
    # Return new dict; avoids mutating input.
    cleaned = {}
    for k, v in items.items():
        if v >= 100:
            cleaned[k] = v
    return cleaned

# Exercise 5
# Count how many employees belong to each department in a nested dictionary.
def count_by_department(employees):
    counts = {}
    for _, info in employees.items():
        dept = info.get("dept")
        if dept is None:
            continue
        counts[dept] = counts.get(dept, 0) + 1
    return counts


