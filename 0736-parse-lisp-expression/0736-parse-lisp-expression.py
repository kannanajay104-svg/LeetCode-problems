class Solution:
    def evaluate(self, expression: str) -> int:
        def parse(s):
            """Splits the expression string into top-level tokens."""
            tokens = []
            i = 0
            while i < len(s):
                if s[i] == '(':
                    # Find the matching closing parenthesis
                    bal = 1
                    j = i + 1
                    while bal > 0:
                        if s[j] == '(': bal += 1
                        elif s[j] == ')': bal -= 1
                        j += 1
                    tokens.append(s[i:j])
                    i = j + 1
                elif s[i] != ' ':
                    # Read a continuous block of characters (variable or number)
                    j = i
                    while j < len(s) and s[j] != ' ':
                        j += 1
                    tokens.append(s[i:j])
                    i = j + 1
                else:
                    i += 1
            return tokens

        def evaluate_inner(expr, scope):
            # Base Case 1 & 2: Integer or Variable
            if not expr.startswith('('):
                if expr[0].isdigit() or expr[0] == '-':
                    return int(expr)
                return scope[expr]
            
            # Remove the outer parentheses and split into logical parts
            expr = expr[1:-1]
            tokens = parse(expr)
            
            # Recursive Evaluation based on command
            if tokens[0] == 'add':
                return evaluate_inner(tokens[1], scope) + evaluate_inner(tokens[2], scope)
            
            elif tokens[0] == 'mult':
                return evaluate_inner(tokens[1], scope) * evaluate_inner(tokens[2], scope)
            
            else: # 'let'
                # Create a new scope dict that copies the outer scope
                new_scope = scope.copy()
                # Process variable assignments in pairs
                for i in range(1, len(tokens) - 1, 2):
                    new_scope[tokens[i]] = evaluate_inner(tokens[i+1], new_scope)
                # Evaluate the final expression in the let block
                return evaluate_inner(tokens[-1], new_scope)
        
        return evaluate_inner(expression, {})