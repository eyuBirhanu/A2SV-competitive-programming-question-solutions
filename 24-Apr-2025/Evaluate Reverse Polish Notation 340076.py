# Problem: Evaluate Reverse Polish Notation - https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        store = []
        for opr in tokens:
            if opr == '+' or opr == '-' or opr == '*' or opr == '/':
                fir = store.pop(-2)
                sec = store.pop(-1)
                if opr == '+':
                    store.append(fir + sec)
                elif opr == '-':
                    store.append(fir - sec)
                elif opr == '*':
                    store.append(fir * sec)
                elif opr == '/':
                    res = fir / sec
                    if res < 0:
                        store.append(math.ceil(res))
                    else:
                        store.append(math.floor(res))
            else:
                store.append(int(opr))
        return store[0]
                

