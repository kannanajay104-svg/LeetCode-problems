class Solution:
    def basicCalculatorIV(self, expression: str, evalvars: List[str], evalints: List[int]) -> List[str]:
        class Poly(defaultdict):
            def __init__(self, d=None):
                super().__init__(int)
                if d:
                    for k, v in d.items():
                        self[k] = v

            def __add__(self, other):
                res = Poly(self)
                for k, v in other.items():
                    res[k] += v
                return res

            def __sub__(self, other):
                res = Poly(self)
                for k, v in other.items():
                    res[k] -= v
                return res

            def __mul__(self, other):
                res = Poly()
                for k1, v1 in self.items():
                    for k2, v2 in other.items():
                        # Multiply coefficients and combine/sort variables lexicographically
                        res[tuple(sorted(k1 + k2))] += v1 * v2
                return res

        # Map known variables to their integer values
        vals = dict(zip(evalvars, evalints))
        
        def make_poly(token: str) -> Poly:
            if token.isdigit():
                return Poly({(): int(token)})
            if token in vals:
                return Poly({(): vals[token]})
            return Poly({(token,): 1})

        # --- Stack-based Evaluation (Shunting-yard) ---
        ops = []
        vals_stack = []
        precedence = {'+': 1, '-': 1, '*': 2}
        
        def apply_op():
            op = ops.pop()
            r = vals_stack.pop()
            l = vals_stack.pop()
            if op == '+': vals_stack.append(l + r)
            elif op == '-': vals_stack.append(l - r)
            elif op == '*': vals_stack.append(l * r)

        i = 0
        while i < len(expression):
            if expression[i] == ' ':
                i += 1
            elif expression[i].isalnum():
                j = i
                while j < len(expression) and expression[j].isalnum():
                    j += 1
                vals_stack.append(make_poly(expression[i:j]))
                i = j
            elif expression[i] == '(':
                ops.append('(')
                i += 1
            elif expression[i] == ')':
                while ops[-1] != '(':
                    apply_op()
                ops.pop()  # Pop the '('
                i += 1
            else: # Operators +, -, *
                while ops and ops[-1] != '(' and precedence[ops[-1]] >= precedence[expression[i]]:
                    apply_op()
                ops.append(expression[i])
                i += 1
                
        # Drain remaining operations
        while ops:
            apply_op()
            
        final_poly = vals_stack[0]
        
        # --- Formatting the Output ---
        terms = []
        for vars_tuple, coeff in final_poly.items():
            if coeff != 0:
                terms.append((vars_tuple, coeff))
                
        # Sort by highest degree first (-len(vars_tuple))
        # Then lexicographically by variable names
        terms.sort(key=lambda x: (-len(x[0]), x[0]))
        
        ans = []
        for vars_tuple, coeff in terms:
            if not vars_tuple:
                ans.append(str(coeff))
            else:
                ans.append(str(coeff) + '*' + '*'.join(vars_tuple))
                
        return ans