class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        # T: O(n * 2 ** n), S: O(n * 2 ** n)
        def isValid(string: str) -> bool:
            balance = 0
            for char in string:
                if char == "(":
                    balance += 1
                elif char == ")":
                    balance -= 1
                if balance < 0:  # Closing parentheses before opening
                    return False
            return balance == 0  # Ensure balance is zero for a valid string

        result = []
        visited = set([s])  # To track the strings we've already visited
        queue = deque([s])
        found = False  # Flag to stop after the first level of valid strings

        while queue:
            current_str = queue.popleft()

            # Check if the current string is valid
            if isValid(current_str):
                result.append(current_str)
                found = True

            # If we already found valid strings, stop processing further levels
            if found:
                continue

            # Generate all possible strings by removing one parenthesis at a time
            for i in range(len(current_str)):
                if current_str[i] not in ("(", ")"):
                    continue
                new_str = current_str[:i] + current_str[i + 1 :]
                if new_str not in visited:
                    visited.add(new_str)
                    queue.append(new_str)

        return result