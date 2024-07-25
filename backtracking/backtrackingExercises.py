def stringPermutations(current_permutation, remaining_chars, result):
    if not remaining_chars:
        # Se non ci sono caratteri rimanenti, aggiungi la permutazione al risultato
        result.append(''.join(current_permutation))
        return

    for i in range(len(remaining_chars)):
        # Aggiungi il carattere corrente alla permutazione
        current_permutation.append(remaining_chars[i])
        # Chiama ricorsivamente per generare permutazioni con il carattere corrente rimosso
        stringPermutations(current_permutation, remaining_chars[:i] + remaining_chars[i+1:], result)
        # Backtracking: rimuovi l'ultimo carattere aggiunto
        current_permutation.pop()

    return result

def generate_permutations(chars):
    result = []
    stringPermutations([], chars, result)
    return result

# Esempio di utilizz


def substrings(string, start, result):
    if start >= len(string):
        return

    for end in range(start + 1, len(string) + 1):
        result.append(string[start:end])
        substrings(string, end, result)

def permute(current_permutation, remaining_nums, result):
    if not remaining_nums:
        result.append(current_permutation[:])
        return

    for i in range(len(remaining_nums)):
        num = remaining_nums[i]
        current_permutation.append(num)
        permute(current_permutation, remaining_nums[:i] + remaining_nums[i+1:], result)
        current_permutation.pop()

def generate_permutations(nums):
    result = []
    permute([], nums, result)
    return result


def backtrackingSum(numbers, target, currentSum, result):
    if sum(currentSum) == target:
        result.append(currentSum.copy())
        return
    if sum(currentSum) > target:
        return

    for i in range(len(numbers)):
        currentSum.append(numbers[i])
        backtrackingSum(numbers, target, currentSum, result)
        currentSum.pop()

    return result

numbers = [2,3,5,8,4,3,2,1]
target = 8
result = []
backtrackingSum(numbers, target, [], result)
print(result)