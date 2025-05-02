# Problem: Design browser history  - https://leetcode.com/problems/design-browser-history/

class Node:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class BrowserHistory:

    def __init__(self, homepage: str):
        self.currPage = Node(homepage)

    def visit(self, url: str) -> None:
        newNode = Node(url)
        self.currPage.next = newNode
        newNode.prev = self.currPage
        self.currPage = newNode


    def back(self, steps: int) -> str:
        while steps > 0 and self.currPage.prev != None:
            self.currPage = self.currPage.prev
            steps -= 1
        return self.currPage.val

    def forward(self, steps: int) -> str:
        while steps > 0 and self.currPage.next != None:
            self.currPage = self.currPage.next
            steps -= 1
        return self.currPage.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
